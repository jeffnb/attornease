from django.contrib import admin
from attorney.models import Attorney, License, FirmAddress, LawCategory


class LicenseInline(admin.StackedInline):
    model = License
    extra = 1


class FirmAddressInLine(admin.StackedInline):
    model = FirmAddress
    extra = 1


class AttorneyAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'is_complete', )
    inlines = [LicenseInline, FirmAddressInLine]

admin.site.register(Attorney, AttorneyAdmin)
admin.site.register(LawCategory)