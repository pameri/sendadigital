# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
    

class Producto(models.Model):
    fregistro = models.DateTimeField(auto_now_add=True, blank=True)
    codigo = models.CharField(max_length=5)    
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=18, decimal_places=2, default =0)
    estado = models.CharField(max_length=1)
    moneda = models.CharField(max_length=3, default='PEN')
    #foto =   models.CharField(max_length=1)
      
    def __str__(self):             
        return self.descripcion

class Perfil(models.Model):
    
    fregistro = models.DateTimeField(auto_now_add=True, blank=True)
    tipopersona =models.CharField(max_length=1) 
    tipodoi =models.CharField(max_length=1) 
    nrodoi = models.CharField(max_length=11,blank=True, null=True)    
    razonsocial= models.CharField(max_length=250,blank=True, null=True)
    direfiscal = models.CharField(max_length=250,blank=True, null=True)
    pais = models.CharField(max_length=2, default = 'PE')
    departamento=models.CharField(max_length=250,blank=True, null=True)
    provincia=models.CharField(max_length=250,blank=True, null=True)
    distrito=models.CharField(max_length=250,blank=True, null=True)
    telefono = models.CharField(max_length=100)#telefono
    email = models.EmailField()    
    informacion = models.TextField(blank=True, null=True)#informacion

    def __str__(self):             
        return self.razonsocial    

class Entidad(models.Model):
    
    fregistro = models.DateTimeField(auto_now_add=True, blank=True) 
    tipodoi = models.EmailField()    
    nrodoi = models.CharField(max_length=11,blank=True, null=True)    
    razonsocial= models.CharField(max_length=150,blank=True, null=True)
    direfiscal = models.CharField(max_length=250,blank=True, null=True)
    pais = models.CharField(max_length=2, default = 'PE')
    email = models.EmailField()
        
    def __str__(self):             
        return self.razonsocial
        
class Pedido(models.Model):
    
    fregistro = models.DateTimeField(auto_now_add=True, blank=True)
    pedido = models.CharField(max_length=250)             
    contacto = models.CharField(max_length=250)
    telefono = models.CharField(max_length=100)
    informacion = models.TextField(blank=True, null=True)
    estado_contrato = models.CharField(max_length=1)
    estado = models.CharField(max_length=1)  
    url_factura = models.CharField(max_length=250)
    producto = models.OneToOneField(Producto)
    perfil = models.OneToOneField(Perfil)   
    entidad = models.OneToOneField(Entidad)
    user = models.OneToOneField(User)

    def __str__(self):             
        return self.razonsocial  
    
