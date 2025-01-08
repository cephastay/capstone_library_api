# Generated by Django 5.1.3 on 2024-12-18 09:40

import accounts.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', accounts.fields.CaseInsensitiveCharField(max_length=70, unique=True)),
                ('author', accounts.fields.CaseInsensitiveCharField(max_length=100)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('book_copies', models.PositiveIntegerField(verbose_name='Number of Book Copies')),
            ],
        ),
    ]
