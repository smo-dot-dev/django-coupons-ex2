# Generated by Django 4.2.5 on 2023-09-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponstats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='promotion_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='value',
            field=models.PositiveIntegerField(null=True),
        ),
    ]