import datetime
import os
from django.conf import settings
from django.shortcuts import render


def file_list(request, date: datetime = None):
    template_name = 'index.html'
    path = settings.FILES_PATH
    files = os.listdir(path=path)
    files_list = map(lambda name: {'name': name,
                              'ctime': datetime.date.fromtimestamp(os.stat(os.path.join(path, name)).st_ctime),
                              'mtime': datetime.date.fromtimestamp(os.stat(os.path.join(path, name)).st_mtime)}, files)
    context = {
        'files': list(files_list),
        'date': date
    }
    return render(request, template_name, context)


def file_content(request, name):
    with open(f'files/{name}') as file_name:
        file_content = file_name.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

