from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseAttornEaseUser(AbstractUser):
    pass

class StaffUser(BaseAttornEaseUser):
    is_staff = True
    is_superuser = True

    class Meta:
        verbose_name = "Staff User"


