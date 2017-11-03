import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

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
