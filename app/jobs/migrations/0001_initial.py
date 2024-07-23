# Generated by Django 4.2.4 on 2024-07-23 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('company_type', models.CharField(blank=True, choices=[('agency/freelance', 'agency/freelance'), ('product', 'product'), ('outsource/outstaff', 'outsource/outstaff'), ('other', 'other')], default='', max_length=20, null=True)),
                ('country_code', models.CharField(blank=True, db_index=True, default='', max_length=3, null=True)),
                ('is_international', models.BooleanField(default=False)),
                ('dou_link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('shortcode', models.CharField(db_index=True, default='', max_length=10, unique=True)),
                ('logo_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('name', models.CharField(default='', max_length=250)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='', max_length=250)),
                ('primary_keyword', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('secondary_keyword', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('long_description', models.TextField(blank=True, default='')),
                ('domain', models.CharField(blank=True, choices=[('adult', 'Adult'), ('advertising', 'Advertising / Marketing'), ('automotive', 'Automotive'), ('crypto', 'Blockchain / Crypto'), ('dating', 'Dating'), ('ecommerce', 'E-commerce / Marketplace'), ('edutech', 'Education'), ('fintech', 'Fintech'), ('gambling', 'Gambling'), ('gamedev', 'Gamedev'), ('hardware', 'Hardware / IoT'), ('healthcare', 'Healthcare / MedTech'), ('manufacturing', 'Manufacturing'), ('ml', 'Machine Learning / Big Data'), ('media', 'Media'), ('miltech', 'MilTech'), ('mobile', 'Mobile'), ('saas', 'SaaS'), ('security', 'Security'), ('telecom', 'Telecom / Communications'), ('travel', 'Travel / Tourism'), ('other', 'Other')], default='', max_length=20, null=True)),
                ('company_type', models.CharField(blank=True, choices=[('agency/freelance', 'agency/freelance'), ('product', 'product'), ('outsource/outstaff', 'outsource/outstaff'), ('other', 'other')], default='', max_length=20, null=True)),
                ('salary_min', models.IntegerField(blank=True, default=0, null=True)),
                ('salary_max', models.IntegerField(blank=True, default=0, null=True)),
                ('public_salary_min', models.IntegerField(blank=True, default=0, null=True)),
                ('public_salary_max', models.IntegerField(blank=True, default=0, null=True)),
                ('extra_keywords', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('experience_years', models.FloatField(default=0)),
                ('english_level', models.CharField(blank=True, choices=[('no_english', 'No English'), ('basic', 'Beginner/Elementary'), ('pre', 'Pre-Intermediate'), ('intermediate', 'Intermediate'), ('upper', 'Upper-Intermediate'), ('fluent', 'Advanced/Fluent')], default='', max_length=15, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('accept_region', models.CharField(blank=True, choices=[('office_locations', 'Office locations'), ('', 'Worldwide'), ('ukraine', 'Only Ukraine'), ('europe_only', 'Only Europe'), ('europe', 'Ukraine + Europe'), ('custom_selection', 'Custom selection')], default='', max_length=20, null=True)),
                ('remote_type', models.CharField(blank=True, choices=[('office', 'Office Work'), ('partly_remote', 'Hybrid Remote'), ('full_remote', 'Full Remote'), ('candidate_choice', 'Office/Remote of your choice')], default='', max_length=20, null=True)),
                ('is_parttime', models.BooleanField(db_index=True, default=False)),
                ('has_test', models.BooleanField(db_index=True, default=False)),
                ('requires_cover_letter', models.BooleanField(db_index=True, default=False)),
                ('is_ukraine_only', models.BooleanField(db_index=True, default=False)),
                ('is_reserving_from_mobilisation', models.BooleanField(default=False)),
                ('unread_count', models.IntegerField(default=0)),
                ('search_count', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
                ('applications_count', models.IntegerField(default=0)),
                ('sent_count', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published'), ('closed', 'Closed'), ('archived', 'Archived'), ('failed', 'Failed')], db_index=True, default='draft', max_length=10)),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('published', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.company')),
                ('recruiter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.recruiter')),
            ],
        ),
    ]
