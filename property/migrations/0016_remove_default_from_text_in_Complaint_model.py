# Generated by Django 2.2.24 on 2022-10-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_add_related_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
    ]