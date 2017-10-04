from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import Account, AuthKey

admin.site.register(AuthKey)

@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('get_full_name', 'email', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'username')
    ordering = ('is_active', 'last_name', 'first_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'url', 'avatar', 'about')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                           'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )

    def get_full_name(self, account):
        return account.get_full_name()

    get_full_name.short_description = _('full name')
