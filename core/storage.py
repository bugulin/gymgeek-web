import os
from django.conf import settings
from django.contrib.auth.models import Permission
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

from accounts.models import Account


class CustomGoogleDriveStorage(GoogleDriveStorage):

    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            self.delete(name)
        return name

    def _save(self, *args, **kwargs):
        permission = Permission.objects.get(codename='change_lesson')
        accounts = Account.objects.filter(Q(groups__permissions=permission) | Q(user_permissions=permission)).distinct().exclude(email=None)
        self._permissions = [GoogleDriveFilePermission(GoogleDrivePermissionRole.WRITER, GoogleDrivePermissionType.USER, account.email) for account in accounts]

        super()._save(*args, **kwargs)


# https://djangosnippets.org/snippets/976/
class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, *args, **kwargs):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """

        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


if settings.DEBUG:
    storage = OverwriteStorage()
else:
    storage = CustomGoogleDriveStorage()
