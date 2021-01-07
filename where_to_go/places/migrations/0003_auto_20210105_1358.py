# Generated by Django 3.1.4 on 2021-01-05 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20210103_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='imgs',
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.place', verbose_name='Место'),
        ),
    ]