from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **kwargs):
        # kwargs.setdefault('is_staff', False)
        # kwargs.setdefault('is_superuser', False)
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password=None, **kwargs):
        # kwargs.setdefault('is_staff', True)
        # kwargs.setdefault('is_superuser', True)
        #
        # if kwargs.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if kwargs.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **kwargs)


class User(AbstractBaseUser):

    username = models.CharField(help_text="用户名", max_length=150, unique=True)
    phone = models.CharField(help_text="电话号码", max_length=11, blank=True, null=True)
    email = models.EmailField(help_text="邮箱", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    object = UserManager()

    class Meta:
        db_table = 'user_pro'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.phone

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
