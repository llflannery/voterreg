# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Invite(models.Model):
         voterid = models.CharField(max_length=500)
         county = models.CharField(max_length=500)
         firstname = models.CharField(max_length=500)
         middlename = models.CharField(max_length=500)
         lastname = models.CharField(max_length=500)
         suffix = models.CharField(max_length=500)
         birthdate = models.CharField(max_length=500)
         regdate = models.CharField(max_length=500)
         address1 = models.CharField(max_length=500)
         address2 = models.CharField(max_length=500)
         city = models.CharField(max_length=500)
         state = models.CharField(max_length=500)
         zip = models.CharField(max_length=500)
         phone = models.CharField(max_length=500)
         party = models.CharField(max_length=500)
         condistrict = models.CharField(max_length=500)
         senatedistrict = models.CharField(max_length=500)
         assemblydistrict = models.CharField(max_length=500)
         edudistrict = models.CharField(max_length=500)
         regentdistrict = models.CharField(max_length=500)
         regprecinct = models.CharField(max_length=500)
         countystatus = models.CharField(max_length=500)
         countyvoterid = models.CharField(max_length=500)
         idrequired = models.CharField(max_length=500)
         notes = models.TextField(blank=True)
