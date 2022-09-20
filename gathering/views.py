# Django imports
from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.shortcuts import render
from django.conf import settings
# Personal/local imports
from processing.models import uploadfolder
from processing.forms import uploadfileform
# Others
import os
import pandas as pd


def index(request):
    """ 
        Function that initiates the necessary form for the users' to upload files and redirects to the upload page.
    """
    form = uploadfileform()
    return render(request, 'upload.html', {'form': form})


def upload_file(request): 
    """ 
        Function that stores users' uploaded file as requested via AJAX from the front-end. If the file already exists in /media, it is overwritten.
        The file is also stored in the DDBB incase further traking is needed (add commit=False when saving to avoid saving in DDBB).
        parameters: 
            request - needed to retreive the completed formulary.
    """

    if request.method=='POST':
        form = uploadfileform(request.POST,request.FILES)
        if form.is_valid():
            file_name = form.cleaned_data['File_to_upload'].name
            path=os.path.join(settings.MEDIA_ROOT, file_name)
            if default_storage.exists(path):
                default_storage.delete(path)
                try:
                    old_file=uploadfolder.objects.get(File_to_upload=file_name)
                    old_file.delete()
                except uploadfolder.MultipleObjectsReturned:
                    for u in uploadfolder.objects.filter(File_to_upload=file_name):
                        u.delete()
                except uploadfolder.DoesNotExist:
                    pass
                
            form.save()

            context = {
                'message': "File successfully uploaded"
            }

            return JsonResponse(context, status=200)


def gather_data(file_name):
    """
        Function that returns a dataframe gathered from an excel file. Add data corrections if needes to customize the result.
        parameters: 
            file_name - name correspondant to the file where the data is stored
    """
    try:
        data = pd.read_excel('media/'+file_name, sheet_name=None)
    except FileNotFoundError:
        return "{ERROR} The specified file " + file_name + " does not exist"

    return data['data']
