from django import forms

from .models import uploadfolder

# uploading file form
class uploadfileform(forms.ModelForm):
	class Meta:
		model=uploadfolder
		fields=('File_to_upload',)