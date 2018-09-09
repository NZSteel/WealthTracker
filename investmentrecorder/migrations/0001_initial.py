# Generated by Django 2.1.1 on 2018-09-08 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(max_length=3)),
                ('symbol', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalUpdater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('webservice_uri', models.CharField(blank=True, max_length=400, null=True)),
                ('webservice_login', models.CharField(blank=True, max_length=100, null=True)),
                ('webservice_password_plaintext', models.CharField(blank=True, max_length=100, null=True)),
                ('webservice_token', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Enter memorable short name', max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('purchase_date', models.DateField(help_text='Enter the earliest date money was invested')),
                ('liquidate_date', models.DateField(blank=True, help_text='Enter the date the Asset was liquidated', null=True)),
                ('investment_type', models.CharField(choices=[('Prop', 'Real Estate'), ('Cash', 'Cash Investment/Term Deposit'), ('Stck', 'Stocks or Shares'), ('Bond', 'Bonds'), ('Fund', 'Funds'), ('Comp', 'Direct company shareholding'), ('Othr', 'Other')], help_text='Enter the broad category of investment', max_length=4)),
                ('external_identifier', models.CharField(blank=True, max_length=100, null=True)),
                ('total_invested', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('total_returned', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('total_number_of_units', models.DecimalField(blank=True, decimal_places=8, max_digits=17, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investmentrecorder.Currency')),
                ('external_updater', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='investmentrecorder.ExternalUpdater')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['investment_type', 'short_name'],
            },
        ),
        migrations.CreateModel(
            name='InvestmentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('b', 'Bought'), ('s', 'Sold'), ('r', 'Revenue'), ('e', 'Expense')], max_length=1)),
                ('description', models.CharField(blank=True, help_text='Please enter a useful description', max_length=500)),
                ('date', models.DateField(blank=True, help_text='Enter the date this transaction was made', null=True)),
                ('number_of_units', models.DecimalField(blank=True, decimal_places=8, max_digits=17, null=True)),
                ('price_per_unit', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investmentrecorder.Currency')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investmentrecorder.Investment')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentValuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Enter the date the revenue was received')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('price_per_unit', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('status', models.CharField(default='actual', help_text='Actual or derived interim value', max_length=10)),
                ('latest', models.CharField(default='y', max_length=1)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investmentrecorder.Currency')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investmentrecorder.Investment')),
            ],
        ),
    ]
