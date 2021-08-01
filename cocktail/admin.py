from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CocktailProduct, OurUser


class OurUserAdmin(UserAdmin):
    list_display = ('email', 'username','date_joined','last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register( OurUser, OurUserAdmin)
admin.site.register(CocktailProduct)

# Register your models here.
