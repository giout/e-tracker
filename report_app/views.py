from django.shortcuts import render


def spreadsheet(request):
    return render(request, 'spreadsheet.html')


def  chart(request):
    return render(request, 'chart.html')