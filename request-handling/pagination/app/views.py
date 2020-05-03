import urllib
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect, render
from django.urls import reverse
from django.conf import settings
import csv

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    data_list = []
    with open(settings.BUS_STATION_CSV, encoding = 'cp1251', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            data_dict = {}
            data_dict["Name"] = line["Name"]
            data_dict["Street"] = line["Street"]
            data_dict["District"] = line["District"]
            data_list.append(data_dict)
    paginator = Paginator(data_list, 10)
    current_page = request.GET.get('page', 1)
    next_page_url = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if next_page_url.has_previous():
        prev_page = f'?page={next_page_url.previous_page_number()}'
    if next_page_url.has_next():
        next_page = f'?page={next_page_url.next_page_number()}'
    return render_to_response('index.html', context={
        'bus_stations': next_page_url,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    })

