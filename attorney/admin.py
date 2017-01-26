from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from attorney.models import Attorney, License, FirmAddress, LawCategory, ServiceArea, AttorneyUser


class LicenseInline(admin.StackedInline):
    model = License
    extra = 1

class FirmAddressInLine(admin.StackedInline):
    model = FirmAddress
    extra = 1


class AttorneyAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'is_complete', )
    #inlines = [LicenseInline, FirmAddressInLine]


class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('area', 'state')
    list_filter = ('state',)


class AttorneyUserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email', 'phone', 'is_complete', )

    add_fieldsets = (
        ('Login', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Contact Information', {
            'fields': ('first_name','last_name','phone','website','email'),
        }),
        ('Affiliations', {
            'fields': ('firm','school'),
        }),
        ('Service Details', {
            'fields': ('categories', 'service_areas', 'rate')
        }),
        ('Bio Details', {
            'fields': ('year_started', 'description', 'profile_pic')
        })
    )

    inlines = [LicenseInline, FirmAddressInLine]
    readonly_fields = ('last_login', 'date_joined')
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


admin.site.register(Attorney, AttorneyAdmin)
admin.site.register(LawCategory)
admin.site.register(ServiceArea, ServiceAreaAdmin)
admin.site.register(AttorneyUser, AttorneyUserAdmin)