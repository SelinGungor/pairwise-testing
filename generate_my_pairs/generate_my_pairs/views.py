from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, request
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, reverse
import csv
from generate_my_pairs.forms import UploadFileForm
import codecs
import pandas as pd
import sys
import io

User = get_user_model()

class HomeView(View):
    def get(self, request):
        form = UploadFileForm()

        args = {'form': form}
        return render(request, 'home.html', args)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            parameters = populate_file('data.csv')
            print(type(parameters))
            print(parameters)
            return render(request, "charts.html", {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})


def populate_file(my_file):
    my_parameter_list = []
    with open(my_file, encoding='utf-8', errors='ignore') as my_csv_file:
        file = csv.reader(my_csv_file, delimiter=',')
        for row in file:
            my_parameter_list.append(row)
    return my_parameter_list

def handle_uploaded_file(f):
    with open(f, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# def upload_csv(request):
#     if request.POST and request.FILES:
#         csv_file = request.FILES['csv_file']
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, 'File is not CSV type')
#             return HttpResponseRedirect(reverse("home"))
#         #look
#         with open(csv_file, 'r') as f:
#             reader = csv.reader(f)
#             your_list = list(reader)
#
#         print(your_list)
#         # my_csv = pd.read_csv(csv_file, header=None, sep=" ", error_bad_lines=False)
#     return render(request, "charts.html", locals())

# def techniques(request):
#   if request.method == 'POST':
#     form = YourForm(request.POST)
#
#     if form.is_valid():
#       answer = form.cleaned_data['value']

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

