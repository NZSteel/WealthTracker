from django.db import models


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
    currency = models.CharField(max_length=3)
    external_updater = models.ForeignKey(
        'ExternalUpdater',
        on_delete=models.SET_NULL,
        null=True, blank=True)
    external_identifier = models.CharField(
        max_length=100,
        null=True,
        blank=True)

    class Meta:
        ordering = ['investment_type', 'short_name']


class InvestmentCapital(models.Model):
    # Fields
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    purchase_date = models.DateField(help_text='Enter the date this tranche of investment was made')
    liquidate_date = models.DateField(null=True, help_text='Enter the date this tranche of investment was made')
    purchase_amount = models.DecimalField(max_digits=11, decimal_places=2)
    liquidate_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    currency = models.CharField(max_length=3)


class InvestmentRevenue(models.Model):
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter the date the revenue was received')
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=11, decimal_places=2)


class InvestmentExpense(models.Model):
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter the date the revenue was received')
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=11, decimal_places=2)


class InvestmentValuation(models.Model):
    investment = models.ForeignKey('Investment', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter the date the revenue was received')
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.CharField(max_length=10, help_text='Actual or derived interim value')


class ExternalUpdater(models.Model):
    name = models.CharField(max_length=100)
    webservice_uri = models.CharField(max_length=400, null=True, blank=True)
    webservice_login = models.CharField(max_length=100, null=True, blank=True)
    webservice_password_plaintext = models.CharField(max_length=100, null=True, blank=True)
    webservice_token = models.CharField(max_length=500, null=True, blank=True)
