# Generated by Django 3.1.4 on 2021-02-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynewapp', '0002_auto_20210210_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Place',
        ),
        migrations.AlterField(
            model_name='user',
            name='District',
            field=models.CharField(choices=[('kasaragod', 'Kasaragod'), ('kannur', 'Kannur'), ('kozhikkode', 'Kozhikkode'), ('vayanad', 'Vayanad'), ('malappuram', 'Malappuram'), ('thrissure', 'Thrissure'), ('idukki', 'Idukki'), ('palakkad', 'Palakkad'), ('ernakulam', 'Ernakulam'), ('alappuzha', 'Alappuzha'), ('pathanamthitta', 'Pathanamthitta'), ('kottayam', 'Kottayam'), ('kollam', 'Kollam'), ('thiruvananthapuram', 'Thiruvananthapuram')], max_length=100),
        ),
    ]
