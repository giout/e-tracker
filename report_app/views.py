from django.shortcuts import render
from .services import get_dates, report_data

def spreadsheet(request):
    if request.method == 'POST':
        begin = request.POST['begin-date']
        end = request.POST['end-date']

        if begin=='0':
            begin = get_dates().first()['date']
        if end=='0':
            end = get_dates().last()['date'].strftime('%Y-%m-%d')

        ctx = { 
            'dataset': report_data(begin, end), 
            'transaction_dates': get_dates(),
            'begin': begin,
            'end': end,
        }
        return render(request, 'spreadsheet.html', ctx)
    else:
        # by default, spreadsheet prints data from every date
        ctx = { 
            'dataset': report_data(), 
            'transaction_dates': get_dates(),
            'begin': '...',
            'end': '...',
        }
        return render(request, 'spreadsheet.html', ctx)


def  chart(request):
    return render(request, 'chart.html')