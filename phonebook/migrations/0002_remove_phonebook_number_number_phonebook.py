# Generated by Django 4.1.4 on 2022-12-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebook',
            name='number',
        ),
        migrations.AddField(
            model_name='number',
            name='phonebook',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='phonebook.phonebook'),
            preserve_default=False,
        ),
    ]
