# Generated by Django 2.2 on 2019-05-18 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0013_build_take_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='take_from',
            field=models.ForeignKey(blank=True, help_text='Select location to take stock from for this build (leave blank to take from any stock location)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sourcing_builds', to='stock.StockLocation'),
        ),
    ]
