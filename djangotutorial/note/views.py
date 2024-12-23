from datetime import datetime
import pytz
import os
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

def index(request, path=''):
    base_directory = os.path.expanduser("~/")
    current_path = os.path.join(base_directory, path)

    if not os.path.exists(current_path):
        raise Http404("Directory not found")

    arr = os.listdir(current_path)

    bangkok_tz = pytz.timezone('Asia/Bangkok')
    now = datetime.now(bangkok_tz)
    formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")

    items = []
    parent_path = os.path.dirname(path) 

    for item in arr:
        item_path = os.path.join(path, item)
        is_directory = os.path.isdir(os.path.join(current_path, item))
        items.append({'name': item, 'path': item_path, 'is_directory': is_directory})

    context = {
        'formatted_date': formatted_date,
        'items': items,
        'path': path,
        'parent_path': parent_path,
    }

    return render(request, 'note/index.html', context)
