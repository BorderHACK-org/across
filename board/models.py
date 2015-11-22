from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Language(models.Model):
    iso_639_3 = models.CharField(max_length=3, primary_key=True)
    native_name = models.CharField(max_length=64)
    latin_name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.native_name + ' - ' + self.latin_name)

class TranslatorRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    from_lang = models.ForeignKey('Language', related_name='from_requests')
    to_lang = models.ForeignKey('Language', related_name='to_requests')

    organization_name = models.CharField(max_length=64, blank=True)
    message = models.CharField(max_length=500, help_text="Include a message with the purpose and scope of your request")
    email = models.EmailField()
    homepage = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    skype_handle = models.CharField(max_length=64, blank=True)
    phone_number = PhoneNumberField(blank=True)
