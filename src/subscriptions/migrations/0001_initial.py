# Generated by Django 5.0.10 on 2025-01-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'permissions': [('advanced', 'Advance Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm')],
            },
        ),
    ]
