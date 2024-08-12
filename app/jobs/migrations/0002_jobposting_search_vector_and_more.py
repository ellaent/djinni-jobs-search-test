# Generated by Django 4.2.4 on 2024-08-11 19:49

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='jobposting',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='jobs_jobpos_search__a9892e_gin'),
        ),
    ]
