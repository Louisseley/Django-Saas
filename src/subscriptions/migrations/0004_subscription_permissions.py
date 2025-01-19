# Generated by Django 5.0.10 on 2025-01-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0003_subscription_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='permissions',
            field=models.ManyToManyField(to='auth.permission'),
        ),
    ]