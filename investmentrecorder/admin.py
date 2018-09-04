from django.contrib import admin

# Register your models here.

from investmentrecorder.models import \
    Investment, \
    InvestmentCapital, \
    InvestmentExpense, \
    InvestmentRevenue, \
    InvestmentValuation, \
    ExternalUpdater,  \
    Currency


class InvestmentAdmin(admin.ModelAdmin):
    list_filter = ('short_name', 'investment_type', 'currency', 'description')
    list_display = ('short_name', 'investment_type', 'currency', 'description')


class InvestmentCapitalAdmin(admin.ModelAdmin):
    list_filter = ('investment', 'purchase_date', 'liquidate_date')
    list_display = ('investment', 'purchase_date', 'liquidate_date')


class ExternalUpdaterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Investment, InvestmentAdmin)
admin.site.register(InvestmentCapital, InvestmentCapitalAdmin)
admin.site.register(InvestmentExpense)
admin.site.register(InvestmentRevenue)
admin.site.register(InvestmentValuation)
admin.site.register(ExternalUpdater, ExternalUpdaterAdmin)
admin.site.register(Currency)


