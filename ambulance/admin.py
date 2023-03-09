from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Counties)
admin.site.register(models.Sub_counties)
admin.site.register(models.Hospital)
admin.site.register(models.Ambulance)
admin.site.register(models.EmergencyCartegory)
admin.site.register(models.Emergency)