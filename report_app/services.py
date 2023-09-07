from django.db.models import Sum
from transaction_app.models import Transaction
from category_app.models import Category
from .utils import get_random_colors

def get_dates():
    # obtaining all registered dates
    dataset = Transaction.objects.values('date').distinct().order_by('date')

    for data in dataset:
        data['date'] = data['date'].strftime('%Y-%m-%d')

    return dataset


def report_data(begin_date='0', end_date='0'):
    transactions = Transaction.objects

    if begin_date=='0' and end_date=='0':
        data = transactions
    elif begin_date=='0': 
        data = transactions.filter(date__lte=end_date)
    elif end_date=='0':
        data = transactions.filter(date__gte=begin_date) 
    else:
        data = transactions.filter(date__range=[begin_date, end_date])

    dataset = data.values('category__description').annotate(total_amount=Sum('amount')).order_by('category__description')

    # filtering all transactions by date, grouping by category, displaying total amount and percentage
    total = 0
    for data in dataset:
        total = total + data['total_amount']
    
    # every element of the dataset will contain a unique color
    length = len(dataset) 
    colors = get_random_colors(length)
    for i in range(length): 
        percentage = (dataset[i]['total_amount'] * 100)/total
        dataset[i]['percentage'] = round(percentage, 2)
        dataset[i]['color'] = colors[i]

    return dataset