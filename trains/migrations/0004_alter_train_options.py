# Generated by Django 4.1.3 on 2022-12-15 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_rename_form_city_train_from_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='train',
            options={'ordering': ['name'], 'verbose_name': 'Train', 'verbose_name_plural': 'Trains'},
        ),
    ]
