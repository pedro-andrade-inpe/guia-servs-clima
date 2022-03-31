# coding: utf-8
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('O email é obrigatório')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)

    name = models.CharField('Nome', max_length=100)

    is_active = models.BooleanField('Ativo', default=True,)
    is_staff = models.BooleanField('Administrador', default=False,)
    date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(" ")[0]

    def get_username(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('usuario_list')
