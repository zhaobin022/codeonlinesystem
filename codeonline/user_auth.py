#-*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an user name')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=64,unique=True)
    alias = models.CharField(max_length=64,unique=True,blank=True,null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    description = models.CharField(max_length=20,  blank=True,null=True,verbose_name=u'人员描述')
    group_admin_tag = models.BooleanField(default=False)
    team_member = models.ManyToManyField('User',blank=True,related_name='team_leader_set')





    objects = UserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.alias

    def get_short_name(self):
        # The user is identified by their email address
        return self.alias

    def __str__(self):              # __unicode__ on Python 2
        # return self.username
        return self.alias

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def __unicode__(self):
        if self.alias:
            return self.alias
        else:
            return self.username
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
