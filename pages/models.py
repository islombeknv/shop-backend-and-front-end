from django.db import models
from django.utils.translation import ugettext_lazy as _

from pages.validators import clean_picture


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class TeamModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    image = models.ImageField(upload_to='team', validators=[clean_picture],  verbose_name=_('image'))
    position = models.CharField(max_length=100, verbose_name=_('position'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = 'teams'


class PartnerModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    image = models.ImageField(upload_to='partner', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
