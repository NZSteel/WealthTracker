from django.contrib import admin

# Register your models here.

from investmentrecorder.models import \
    Investment, \
    InvestmentTransaction, \
    InvestmentValuation, \
    ExternalUpdater,  \
    Currency


class InvestmentTransactionInline(admin.TabularInline):
    model = InvestmentTransaction
    extra = 1


class InvestmentValuationInline(admin.TabularInline):
    model = InvestmentValuation
    extra = 1


class InvestmentAdmin(admin.ModelAdmin):
    list_filter = ('short_name', 'investment_type', 'currency', 'description')
    list_display = ('short_name', 'investment_type', 'currency', 'description')
    inlines = [InvestmentTransactionInline, InvestmentValuationInline]


class InvestmentTransactionAdmin(admin.ModelAdmin):
    list_filter = ('investment', 'type', 'date', 'amount')
    list_display = ('investment', 'type', 'description', 'date', 'amount')


class ExternalUpdaterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Investment, InvestmentAdmin)
admin.site.register(InvestmentTransaction, InvestmentTransactionAdmin)
admin.site.register(InvestmentValuation)
admin.site.register(ExternalUpdater, ExternalUpdaterAdmin)
admin.site.register(Currency)


