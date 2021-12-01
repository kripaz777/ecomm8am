# Generated by Django 3.2.9 on 2021-12-01 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=300)),
                ('mobile_no', models.CharField(max_length=400)),
                ('office_no', models.CharField(max_length=400)),
                ('home_no', models.CharField(max_length=400)),
                ('logo', models.ImageField(upload_to='media')),
            ],
        ),
    ]
