from django.shortcuts import render
from .services import get_dates, report_data
from django.http import HttpResponse
import csv as csv_module

def report_context(request):
    if request.method == 'POST':
        begin = request.POST['begin-date']
        end = request.POST['end-date']

        if begin=='0':
            begin = get_dates().first()['date']
        if end=='0':
            end = get_dates().last()['date'].strftime('%Y-%m-%d')

        return {
            'dataset': report_data(begin, end), 
            'transaction_dates': get_dates(),
            'begin': begin,
            'end': end
        }

    else:
        # by default, any report prints data from every date
        return { 
            'dataset': report_data(), 
            'transaction_dates': get_dates(),
            'begin': '...',
            'end': '...'
        }


def export_csv(begin_date, end_date):
    csv_data = [
        ['Category', 'Total Amount', 'Percentage']
    ]
    # obtaining filtered data 
    dataset = report_data(begin_date, end_date)
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
    ctx = report_context(request)
    return render(request, 'spreadsheet.html', ctx)


def chart(request):
    ctx = report_context(request)
    return render(request, 'chart.html', ctx)

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