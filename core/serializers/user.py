from django.contrib import auth
from django.core import exceptions as django_exceptions

from rest_framework.reverse import reverse
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField, ValidationError


class UserSerializer(ModelSerializer):
    password = CharField(max_length=128, required=True, write_only=True)
    documents = SerializerMethodField(read_only=True)

    class Meta:
        model = auth.get_user_model()
        fields = ('id', 'email', 'password', 'verified', 'last_login', 'documents')
        read_only_fields = ('id', 'last_login', 'verified', 'documents')

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
        password = validated_data.pop('password')
        if password:
            instance.set_password(validated_data['password'])

        return self.Meta.model.objects.create_user(validated_data['email'], validated_data['password'])

    def get_documents(self, obj):
        return reverse('user-documents', args=(obj.pk,), request=self.context['request'])
