from django.db import models


# Model used to store the excel File uploaded by the users.
class uploadfolder(models.Model):
    File_to_upload = models.FileField(upload_to='')
    synth_index_array = models.JSONField(default=dict, null=True, blank=True) # Stored calculation result

    def __str__(self) -> str:
        return self.File_to_upload.name