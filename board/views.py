from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.forms import Form, ModelForm, Textarea
from django import forms

from .models import *

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'board/index.django.html', {})

class ChooseLanguageForm(Form):
    from_lang = forms.ModelChoiceField(queryset=Language.objects.all(), empty_label=None)
    to_lang = forms.ModelChoiceField(queryset=Language.objects.all(), empty_label=None)

class ChooseLanguage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'board/choose.django.html', { 'form' : ChooseLanguageForm() })

class TranslatorRequestForm(ModelForm):
    class Meta:
        model = TranslatorRequest
        fields = [
          'from_lang',
          'to_lang',
          'organization_name',
          'message',
          'email',
          'facebook',
          'phone_number',
          'skype_handle',
          ]
        widgets = {
            'message': Textarea(attrs={'cols': 40, 'rows': 6}),
        }


class TranslatorRequestCreate(CreateView):
    success_url = '/list'
    form_class = TranslatorRequestForm
    model = TranslatorRequest

class TranslatorRequestList(ListView):
    model = TranslatorRequest

    def get_queryset(self):
        qs = TranslatorRequest.objects.all()
        if 'from_lang' in self.request.GET:
            from_lang = self.request.GET['from_lang']
            qs = qs.filter(from_lang=from_lang)

        if 'to_lang' in self.request.GET:
            to_lang = self.request.GET['to_lang']
            qs = qs.filter(to_lang=to_lang)

        return qs.order_by('-created')
