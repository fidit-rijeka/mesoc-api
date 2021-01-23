import uuid


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import BooleanField, EmailField, UUIDField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, password=None):
        return self.create_user(email, password)


class User(AbstractBaseUser):
    objects = UserManager()
    id = UUIDField(default=uuid.uuid4, primary_key=True)
    email = EmailField(unique=True)
    verified = BooleanField(blank=True, default=False)
    USERNAME_FIELD = 'email'
