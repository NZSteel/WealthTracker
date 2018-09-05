from django.shortcuts import render
from django.db.models import Count, Sum

# Create your views here.
from investmentrecorder.models import Investment, InvestmentValuation, InvestmentTransaction, ExternalUpdater, Currency


def index(request):
    """Primary homepage view"""

    num_investments = Investment.objects.all().count()
    total_gbp = InvestmentValuation.objects.filter(
         investment__currency__short_code__startswith='GBP', latest__exact='y').aggregate(Sum('amount'))
    total_usd = InvestmentValuation.objects.filter(
         investment__currency__short_code__startswith='USD', latest__exact='y').aggregate(Sum('amount'))


    context = {
        'num_investments': num_investments,
        'total_gbp': total_gbp.get('amount__sum', 0),
        'total_usd': total_usd.get('amount__sum', 0),
    }

    return render(request, 'index.html', context=context)
