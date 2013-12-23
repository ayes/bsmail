# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ValidationError

class MailDomain(models.Model):
	domain = models.CharField(u'Domain name', max_length = 64, help_text = 'Domain name to serve (example: bsmsite.com)', unique = True)
	notes = models.CharField(u'Notes', max_length = 1024, help_text = 'Anything about this domain')
	position = models.IntegerField(u'Position', help_text = 'Position in the drop-down list in mail.bsmsite.com', blank = True)

	def save(self, *args, **kwargs):
		if self.position is None:
			try:
				last = MailDomain.objects.order_by('-position')[0]
				self.position = last.position + 1
			except:
				self.position = 0

	def __unicode__(self):
		return self.domain

	class Meta:
		db_table = 'domains'
		verbose_name = 'mail domain'
		verbose_name_plural = 'mail domains'
		ordering = ('position',)

class MailQuota(models.Model):
	quota = models.IntegerField('Quota, megabytes', help_text = u'User quota in megabytes, 0 means unlimited')
	title = models.CharField('Quota name', help_text = 'Example: 100 megabytes, for staff', max_length = 255)

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'quotas'
		verbose_name = 'Mail quota'
		verbose_name_plural = 'Mail quotas'

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
	quota = models.ForeignKey(MailQuota, verbose_name = 'Mailbox size')
 	active = models.BooleanField('Access', help_text = 'Disabling the user’s access does not destroy his mailbox')

	class Meta:
		db_table = 'users'
		verbose_name = 'mail user'
		verbose_name_plural = 'mail users'
		ordering = ('username',)
