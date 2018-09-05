# Generated by Django 2.1.1 on 2018-09-05 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investmentrecorder', '0003_auto_20180904_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boughtsold', models.CharField(choices=[('p', 'Purchased'), ('s', 'Sold')], max_length=1)),
                ('date', models.DateField(blank=True, help_text='Enter the date this transaction was made', null=True)),
                ('number_of_units', models.DecimalField(blank=True, decimal_places=8, max_digits=17, null=True)),
                ('price_per_unit', models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investmentrecorder.Currency')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investmentrecorder.Investment')),
            ],
        ),
        migrations.RemoveField(
            model_name='investmentcapital',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='investmentcapital',
            name='investment',
        ),
        migrations.DeleteModel(
            name='InvestmentCapital',
        ),
    ]