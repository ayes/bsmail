# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from models import *

class MailDomainAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'notes', 'position')
	list_editable = ('position',)

	class Media:
		js = ['/static/js/admin_list_reorder.js',]

class MailUserAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'domain', 'mailbox_size', 'active')
	list_filter = ('domain',)

admin.site.register(MailDomain, MailDomainAdmin)
admin.site.register(MailUser, MailUserAdmin)

admin.site.unregister(Group)
