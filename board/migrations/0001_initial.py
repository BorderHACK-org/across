# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('iso_639_3', models.CharField(max_length=3, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TranslatorRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(help_text=b'Include a message with the purpose and scope of your request', max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('homepage', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('skype_handle', models.CharField(max_length=64, blank=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('from_lang', models.ForeignKey(related_name='from_requests', to='board.Language')),
                ('to_lang', models.ForeignKey(related_name='to_requests', to='board.Language')),
            ],
        ),
    ]
