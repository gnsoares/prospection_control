#
# IMPORTS
#
# Django
from django.shortcuts import render
from django.views import View


#
# CODE
#
class Update(View):

    def get(self, request, *args, **kwargs):
        return render(request, '', {})

    def post(self, request, *args, **kwargs):
        return render(request, '', {})
