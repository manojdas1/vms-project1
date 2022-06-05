from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'Aadhaar_Number', 'Name', 'Age', 'Gender', 'Mobile_Number', 'Dose', 'Vaccine_Name')