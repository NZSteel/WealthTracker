from django.shortcuts import render
from django.db.models import Count, Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from money import Money

# Create your views here.
from investmentrecorder.models import Investment, InvestmentValuation, InvestmentTransaction, ExternalUpdater, Currency


class InvestmentValuationListView(generic.ListView):
    model = InvestmentValuation

    def get_queryset(self):
        return InvestmentValuation.objects.filter(
            latest__exact='y',
            investment__user=self.request.user)

@login_required
def index(request):
    """Primary homepage view"""

    num_investments = Investment.objects.filter(user=request.user).count()
    gbp_total = InvestmentValuation.objects.filter(
        investment__currency__short_code__startswith='GBP',
        latest__exact='y',
        investment__user=request.user
    ).aggregate(Sum('amount'))
    usd_total = InvestmentValuation.objects.filter(
        investment__currency__short_code__startswith='USD',
        latest__exact='y',
        investment__user=request.user
    ).aggregate(Sum('amount'))
    ###total_gbp = my_investment_valuations_in_gbp.aggregate(Sum('amount'))
    ###total_usd = my_investment_valuations_in_usd.aggregate(Sum('amount'))
    ###total_gbp = total_gbp or 0
    ###total_usd = total_usd or 0
    try:
        gbp_total = Money(gbp_total.get('amount__sum', 0), 'GBP')
    except TypeError:
        gbp_total = Money(0, 'GBP')
    try:
        usd_total = Money(usd_total.get('amount__sum', 0), 'USD')
    except TypeError:
        usd_total = Money(0, 'USD')
    context = {
        'num_investments': num_investments,
        'total_gbp': gbp_total,
        'total_usd': usd_total,
    }

    return render(request, 'index.html', context=context)


