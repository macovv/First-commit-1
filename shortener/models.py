# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import code_generator, create_shortcode
from django.db import models

# Create your models here.


class KirrURL(models.Model):
    url = models.CharField(max_length=200,)
    shortcode = models.CharField(max_length=60, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self,*args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = code_generator()
        super(KirrURL,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)

    def __unicovde__(self):
        return str(self.url)
