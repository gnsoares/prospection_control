#
# IMPORTS
#
# Django
from django.shortcuts import render
from django.views import View


#
# CODE
#
class ProspectorSelect(View):

    def get(self, request, *args, **kwargs):
        return render(request, '', {})