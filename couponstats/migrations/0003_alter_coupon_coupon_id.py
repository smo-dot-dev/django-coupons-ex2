# Generated by Django 4.2.5 on 2023-09-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponstats', '0002_alter_coupon_promotion_type_alter_coupon_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_id',
            field=models.PositiveIntegerField(),
        ),
    ]