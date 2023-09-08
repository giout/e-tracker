from django.shortcuts import render, redirect
from .services import get_dates, report_data
from django.http import HttpResponse
import csv as csv_module

def report_context(request):
    if request.method == 'POST':
        begin = request.POST['begin-date']
        end = request.POST['end-date']

        if begin=='0':
            begin = get_dates(request).first()['date']
        if end=='0':
            end = get_dates(request).last()['date'].strftime('%Y-%m-%d')

        return {
            'dataset': report_data(request, begin, end), 
            'transaction_dates': get_dates(request),
            'begin': begin,
            'end': end
        }

    else:
        # by default, any report prints data from every date
        begin = get_dates(request).first()['date']
        end = get_dates(request).last()['date'].strftime('%Y-%m-%d')
        return { 
            'dataset': report_data(request), 
            'transaction_dates': get_dates(request),
            'begin': begin,
            'end': end
        }


def export_csv(begin_date, end_date):
    csv_data = [
        ['Category', 'Total Amount', 'Percentage']
    ]
    # obtaining filtered data 
    dataset = report_data(request, begin_date, end_date)
    for data in dataset:
        csv_data.append(
            [
                data['category__description'], 
                data['total_amount'], 
                data['percentage']
            ]
        )
    return csv_data


def spreadsheet(request):
    if request.user.is_authenticated:
        ctx = report_context(request)
        return render(request, 'spreadsheet.html', ctx)
    else:
        return redirect('login_view')

def chart(request):
    if request.user.is_authenticated:
        ctx = report_context(request)
        return render(request, 'chart.html', ctx)
    else:
        return redirect('login_view')

def csv(request, begin, end):
    data = export_csv(begin, end)
    # exporting csv 
    filename = f'EXPENSES_{begin}_{end}.csv'
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )
    # writing data in csv response
    writer = csv_module.writer(response)
    for row in data:
        writer.writerow(row)
    
    return response