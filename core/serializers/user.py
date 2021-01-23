from django.contrib import auth
from django.core import exceptions as django_exceptions

from rest_framework.reverse import reverse
from rest_framework.serializers import CharField, HyperlinkedModelSerializer, SerializerMethodField, ValidationError


class UserSerializer(HyperlinkedModelSerializer):
    password = CharField(max_length=128, required=True, write_only=True)
    documents = SerializerMethodField()
    url = SerializerMethodField()

    class Meta:
        model = auth.get_user_model()
        fields = ('email', 'password', 'verified', 'last_login', 'documents', 'url')
        read_only_fields = ('verified', 'last_login',)

    def validate(self, attrs):
        user = self.Meta.model(**attrs)
        password = attrs.get('password')

        if password:
            try:
                auth.password_validation.validate_password(password=password, user=user)
            except django_exceptions.ValidationError as e:
                raise ValidationError({'password': list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance

    def get_documents(self, obj):
        return reverse('document-list', request=self.context['request'])

    def get_url(self, obj):
        return reverse('account', args=(), request=self.context['request'])
