# Generated by Django 3.0.6 on 2020-08-07 10:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('symbol', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('lastedit', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('weekday', models.CharField(max_length=3)),
                ('priceopen', models.DecimalField(decimal_places=2, max_digits=6)),
                ('priceclose', models.DecimalField(decimal_places=2, max_digits=6)),
                ('overnight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('intraday', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sum24', models.DecimalField(decimal_places=2, max_digits=6)),
                ('volume', models.PositiveIntegerField()),
                ('high', models.DecimalField(decimal_places=2, max_digits=6)),
                ('low', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historical.Ticker')),
            ],
        ),
    ]
