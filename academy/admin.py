# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
   list_display = ("voterid", "county", "firstname", "middlename", "lastname", "suffix", "birthdate", "regdate", "address1", "address2", "city", "state", "zip", "phone", "party", "condistrict", "senatedistrict", "assemblydistrict", "edudistrict", "regentdistrict", "regprecinct", "countystatus", "countyvoterid", "idrequired")
   list_filter = ("county", "city", "party")
   search_fields = ("firstname", "lastname", )
admin.site.register(Invite, InviteAdmin)
