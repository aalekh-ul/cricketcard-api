# Generated by Django 3.1.2 on 2021-04-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crick', '0005_auto_20210404_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='p_image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]