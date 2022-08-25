from django.urls import path

from upload.views import file_upload

app_name = 'file_upload'

urlpatterns = [
    path('', file_upload, name='upload')
]
