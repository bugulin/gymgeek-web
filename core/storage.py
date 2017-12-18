from django.contrib.auth.models import Permission
from django.db.models import Q
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

from accounts.models import Account


class Storage(GoogleDriveStorage):

    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            self.delete(name)
        return name

    def _save(self, *args, **kwargs):
        permission = Permission.objects.get(codename='change_lesson')
        accounts = Account.objects.filter(Q(groups__permissions=permission) | Q(user_permissions=permission)).distinct().exclude(email=None)
        self._permissions = [GoogleDriveFilePermission(GoogleDrivePermissionRole.WRITER, GoogleDrivePermissionType.USER, account.email) for account in accounts]

        return super()._save(*args, **kwargs)
