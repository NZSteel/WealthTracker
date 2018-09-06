from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse

# Create your models here.


class Investment(models.Model):
    # Fields
    short_name = models.CharField(max_length=200, help_text='Enter memorable short name')
    description = models.CharField(max_length=1000)
    purchase_date = models.DateField(help_text='Enter the earliest date money was invested')
    liquidate_date = models.DateField(
        null=True,
        blank=True,
        help_text='Enter the date the Asset was liquidated')

    INVESTMENT_TYPE = (
        ('Prop', 'Real Estate'),
        ('Cash', 'Cash Investment/Term Deposit'),
        ('Stck', 'Stocks or Shares'),
        ('Bond', 'Bonds'),
        ('Fund', 'Funds'),
        ('Comp', 'Direct company shareholding'),
        ('Othr', 'Other'),
    )

    investment_type = models.CharField(
        max_length=4,
        choices=INVESTMENT_TYPE,
        help_text='Enter the broad category of investment'
    )
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.PROTECT)
    external_updater = models.ForeignKey(
        'ExternalUpdater',
        on_delete=models.SET_NULL,
        null=True, blank=True)
    external_identifier = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    total_invested = MoneyField(
        max_digits=19,
        decimal_places=4,
        null=True,
        blank=True,
        default_currency='GBP',
    )
    total_returned = MoneyField(
        max_digits=19,
        decimal_places=4,
        null=True,
        blank=True,
        default_currency='GBP',
    )
    total_number_of_units = models.DecimalField(
        max_digits=17,
        decimal_places=8,
        null=True,
        blank=True)

    class Meta:
        ordering = ['investment_type', 'short_name']

    def get_absolute_url(self):
        return reverse('investment-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.short_name}'


class InvestmentTransaction(models.Model):
    # Fields
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    TRANSTYPE = (
        ('b', 'Bought'),
        ('s', 'Sold'),
        ('r', 'Revenue'),
        ('e', 'Expense')
    )
    type = models.CharField(
        max_length=1,
        choices=TRANSTYPE,
    )
    description = models.CharField(
        max_length=500,
        help_text='Please enter a useful description',
        blank=True,
    )
    date = models.DateField(
        null=True,
        blank=True,
        help_text='Enter the date this transaction was made')
    number_of_units = models.DecimalField(
        max_digits=17,
        decimal_places=8,
        null=True,
        blank=True)
    price_per_unit = models.DecimalField(
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=True)
    amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        null=True,
        blank=True,
        default_currency='GBP',
    )
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} ({self.investment.short_name})'


class InvestmentValuation(models.Model):
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter the date the revenue was received')
    amount = MoneyField(
        max_digits=19,
        decimal_places=4,
        default_currency='GBP',
    )
    price_per_unit = models.DecimalField(
        max_digits=19,
        decimal_places=10,
        null=True,
        blank=True)
    INVESTMENT_STATUS = (
        ('actual', 'Actual'),
        ('derived', 'Derived'),
    )
    status = models.CharField(
        max_length=10,
        default='actual',
        help_text='Actual or derived interim value'
    )
    latest = models.CharField(max_length=1, default='y')

    def __str__(self):
        return f'{self.id} ({self.investment.short_name})'


class ExternalUpdater(models.Model):
    name = models.CharField(max_length=100)
    webservice_uri = models.CharField(max_length=400, null=True, blank=True)
    webservice_login = models.CharField(max_length=100, null=True, blank=True)
    webservice_password_plaintext = models.CharField(max_length=100, null=True, blank=True)
    webservice_token = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Currency(models.Model):
    short_code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=1)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.short_code} {self.name}'
