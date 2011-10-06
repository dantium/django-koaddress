from django.contrib import admin

from koaddress.models import Address

class AddressAdmin(admin.ModelAdmin):
    model = Address
    search_fields = ['code','city','area']

admin.site.register(Address, AddressAdmin)