from django.db import models
from django.utils.translation import gettext_lazy as _

# - user appointments - name, action, date and time
class Appointment(models.Model):
    name = models.CharField(_('Full Name'), max_length=100, default='')
    action = models.TextField(_('What do you want?'), default='')
    date = models.DateField(_('Appointment Date'), null=True, blank=True)
    time = models.TimeField(_('Appointment Time'), null=True, blank=True)

    def __str__(self):
        return self.name
