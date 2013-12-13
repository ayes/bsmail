# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ValidationError

class MailDomain(models.Model):
	domain = models.CharField(u'Domain name', max_length = 64, help_text = 'Domain name to serve (example: bsmsite.com)', unique = True)
	notes = models.CharField(u'Notes', max_length = 1024, help_text = 'Anything about this domain')

	def __unicode__(self):
		return self.domain

	class Meta:
		db_table = 'domains'
		verbose_name = 'mail domain'
		verbose_name_plural = 'mail domains'
		ordering = ('domain',)

class MailUser(models.Model):
	QUOTA_CHOICES = (
		(10, '10 megabytes'),
		(50, '50 megabytes'),
		(100, '100 megabytes'),
		(1024, '1 gigabyte'),
		(0, 'unlimited space'),
	)

	def __unicode__(self):
		return self.username

	def mailbox_size(self):
		return self.get_quota_display()

	username = models.CharField('Username', max_length = 64, help_text = 'Left part (before @ sign) of the e-mail address')
	domain = models.ForeignKey(MailDomain, verbose_name = 'Domain')
	password = models.CharField('Password', max_length = 32, help_text = 'Used to connect through POP, IMAP and SMTP')
	quota = models.IntegerField('Mailbox size', choices = QUOTA_CHOICES, help_text = 'How much space should the user have?')
 	active = models.BooleanField('Access', help_text = 'Disabling the user’s access does not destroy his mailbox')

	class Meta:
		db_table = 'users'
		verbose_name = 'mail user'
		verbose_name_plural = 'mail users'
		ordering = ('username',)
