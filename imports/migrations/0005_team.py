# Generated by Django 5.0 on 2024-01-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0004_brand_name_ar_categories_name_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('googleplus_url', models.URLField(blank=True, null=True)),
                ('pinterest_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('telegram_url', models.URLField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='team_members/')),
            ],
        ),
    ]