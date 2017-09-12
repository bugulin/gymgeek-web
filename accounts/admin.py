from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import Group as DjangoGroup
from .models import Account, Group

admin.site.unregister(DjangoGroup)


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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_count')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)
    fieldsets = (
        (None, {'fields': ('name', 'code')}),
        (_('Permissions'), {'fields': ('permissions',)})
    )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'permissions':
            qs = kwargs.get('queryset', db_field.remote_field.model.objects)
            kwargs['queryset'] = qs.select_related('content_type')

        return super(GroupAdmin, self).formfield_for_manytomany(db_field, request=request, **kwargs)

    def account_count(self, group):
        return len(group.account_set.all())

    account_count.short_description = _('account count')
