# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email,ruc, password, is_staff,is_admin,
                is_superuser, **extra_fields):
        username = email    
        email = self.normalize_email(email)
        if not email:
            raise ValueError('el email debe ser obligatorio')
        
        if not ruc:
            raise ValueError('el ruc debe ser obligatorio')
        
        user = self.model(username = username,email= email,ruc=ruc,is_active = True,
            is_staff = is_staff,is_admin = is_admin, is_superuser= is_superuser, **extra_fields)
        user.set_password(password)
        user.save( using = self._db)
        return user

    def create_user(self, username, email,ruc, password= None, **extra_fields):
        return self._create_user(username,email,ruc,password, False,False, False, **extra_fields)

    def create_superuser(self, username, email,ruc, password= None, **extra_fields):
        return self._create_user(username,email,ruc,password, True,True, True, **extra_fields)   
   
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    ruc = models.CharField(max_length=11)
    razonsocial= models.CharField(max_length=150) 
    first_name = models.CharField(max_length=100)#apellido paterno
    last_name = models.CharField(max_length=100)#apellido materno
    names = models.CharField(max_length=100)#nombres
    telefono = models.CharField(max_length=100)#telefono
    avatar = models.ImageField(upload_to = 'users')

    objects = UserManager()

    is_active = models.BooleanField(default = True)  
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)    
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['ruc','email']

    def get_short_name(self):
        return self.username

