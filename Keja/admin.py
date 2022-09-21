from django.contrib import admin
from .models import Profile
from .models import Houselocation,Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(Houselocation)
admin.site.register(Category)
