from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email or not username:
            raise ValidationError("User must have email and username")
        email = self.normalize_email(email).lower()

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(first_name, last_name, username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
