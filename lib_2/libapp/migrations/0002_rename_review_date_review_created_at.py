# Generated by Django 3.2.23 on 2023-12-06 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_date',
            new_name='created_at',
        ),
    ]
