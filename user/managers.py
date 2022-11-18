from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, gender, birth_date, phone,
                     id_number, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date,
            phone=phone,
            id_number=id_number,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, True, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)
