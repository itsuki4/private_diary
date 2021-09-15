import logging
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from . forms import InquiryForm
# Create your views here.


def index(request):
    return render(request, 'diary/index.html')


class IndexView(generic.TemplateView):
    template_name = "diary/index.html"


class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm

def form_valid(self,form):
    form.send_email()
    messages.success(self.request,'メッセージを送信しました。')
    return super().form_valid(form)