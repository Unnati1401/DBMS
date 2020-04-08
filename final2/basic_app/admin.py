from django.contrib import admin
from .models import Bloodbank,UserProfileInfo,Stock,BloodCamps

admin.site.register(Bloodbank)
admin.site.register(UserProfileInfo)
admin.site.register(Stock)
admin.site.register(BloodCamps)

# Register your models here.
