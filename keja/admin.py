from django.contrib import admin
from .models import Profile
from .models import Houselocation,Category
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
@admin.register(Houselocation)
class HouseLocationAdmin(LeafletGeoAdmin):
    list_display =('name','maxprice','minprice',)


admin.site.register(Profile)
# admin.site.register(Houselocation, LeafletGeoAdmin)
admin.site.register(Category)
