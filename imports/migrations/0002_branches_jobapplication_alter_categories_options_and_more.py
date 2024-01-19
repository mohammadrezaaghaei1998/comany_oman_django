# Generated by Django 5.0 on 2024-01-13 03:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='email')),
                ('number', models.CharField(default='', max_length=15, verbose_name='number')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='name')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='email')),
                ('whatsapp_number', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='whatsapp number')),
                ('country', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='country')),
                ('city', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='city')),
                ('cv', models.FileField(blank=True, default=None, null=True, upload_to='cv/', verbose_name='cv')),
            ],
            options={
                'verbose_name': ' JobApplication',
                'verbose_name_plural': ' JobApplications',
            },
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='collaborationimage',
            options={'verbose_name': ' CollaborationImage', 'verbose_name_plural': ' CollaborationImages'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Cntact', 'verbose_name_plural': 'Contacs'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': ' UserInfo', 'verbose_name_plural': ' UserInfos'},
        ),
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
        migrations.AddField(
            model_name='categories',
            name='name_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='categories',
            name='name_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='categories',
            name='name_fa',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='categories',
            name='name_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='categories',
            name='name_tr',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collaboration',
            name='whatsapp',
            field=models.CharField(default=None, max_length=15, verbose_name='whatsapp'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='description',
            field=models.TextField(default=None, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='origin',
            field=models.CharField(default=None, max_length=255, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='product_name',
            field=models.CharField(default=None, max_length=255, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='quality',
            field=models.CharField(default=None, max_length=255, verbose_name='quality'),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='collaborationimage',
            name='image',
            field=models.ImageField(upload_to='collaboration_images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='color',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='amount_invested',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True, verbose_name='amount invested'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='duration_staying_money',
            field=models.IntegerField(default=None, help_text='Duration in months', verbose_name='duration_staying_money'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='investment_product/img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='name',
            field=models.CharField(default=None, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='origin',
            field=models.CharField(default=None, max_length=50, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='profitability_percentage',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='profitability_percentage'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='start_date',
            field=models.DateField(default=None, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.categories', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='discount_price '),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='information'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='quality'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subfield',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.subfield', verbose_name='Subfield'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subfield_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.subfield_item', verbose_name='Subfield Item'),
        ),
        migrations.AlterField(
            model_name='subfield',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='subfield_item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(default=None, max_length=255, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(default=None, max_length=255, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=None, max_length=255, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='surname',
            field=models.CharField(default=None, max_length=255, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='whatsapp',
            field=models.CharField(default=None, max_length=15, verbose_name='whatsapp'),
        ),
        migrations.CreateModel(
            name='OrderInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='name')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='email')),
                ('address', models.TextField(default=None, verbose_name='address')),
                ('phone_number', models.CharField(default=None, max_length=20, verbose_name='phone number')),
                ('investment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='imports.investment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, verbose_name='name')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='email')),
                ('address', models.TextField(default=None, verbose_name='address')),
                ('phone_number', models.CharField(default=None, max_length=20, verbose_name='phone number')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imports.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=None, max_length=255, verbose_name='product name')),
                ('quantity', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='quantity')),
                ('quality', models.CharField(default=None, max_length=255, verbose_name='quality')),
                ('origin', models.CharField(default=None, max_length=255, verbose_name='origin')),
                ('description', models.TextField(default=None, verbose_name='description')),
                ('product_images', models.ImageField(default='default_image.jpg', upload_to='product_assistance_images/', verbose_name='product image')),
                ('whatsapp', models.CharField(default=None, max_length=15, verbose_name='whatsapp')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ' Product_Assistance',
                'verbose_name_plural': ' Product_Assistances',
            },
        ),
        migrations.CreateModel(
            name='Product_AssistanceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_assistance_images/', verbose_name='image')),
                ('product_assistance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_assistance_images', to='imports.product_assistance')),
            ],
            options={
                'verbose_name': ' Product_AssistanceImage',
                'verbose_name_plural': ' Product_AssistanceImages',
            },
        ),
    ]