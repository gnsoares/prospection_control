#
# IMPORTS
#
# Django
from django.contrib import admin

# Project
from .models import Company
from .models import Prospector


#
# CODE
#
admin.site.register(Company)
admin.site.register(Prospector)