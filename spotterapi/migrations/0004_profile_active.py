# Generated by Django 4.1.3 on 2023-01-09 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotterapi', '0003_remove_profile_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
    ]
