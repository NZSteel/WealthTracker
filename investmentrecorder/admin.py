from django.contrib import admin

# Register your models here.

from  investmentrecorder.models import Investment, InvestmentCapital, InvestmentExpense, InvestmentRevenue, InvestmentValuation, ExternalUpdater

admin.site.register(Investment)
admin.site.register(InvestmentCapital)
admin.site.register(InvestmentExpense)
admin.site.register(InvestmentRevenue)
admin.site.register(InvestmentValuation)
admin.site.register(ExternalUpdater)
