# Generated by Django 3.1.4 on 2021-02-17 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0003_auto_20210210_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Colour', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='media/')),
            ],
        ),
    ]