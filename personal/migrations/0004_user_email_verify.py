# Generated by Django 3.2.6 on 2022-04-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
