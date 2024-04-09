# Generated by Django 5.0.4 on 2024-04-08 18:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dbapp', '0002_alter_allusers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='allusers',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='allusers',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='allusers',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='allusers',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='allusers',
            name='isadmin',
            field=models.BooleanField(db_column='IsAdmin', default=False),
        ),
        migrations.AlterField(
            model_name='allusers',
            name='username',
            field=models.CharField(db_column='Username', max_length=255, unique=True),
        ),
    ]
