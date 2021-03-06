# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.CharField(help_text='app id, same as the folder name', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='Rendered app name for users', max_length=128, verbose_name='Name')),
                ('description', models.TextField(help_text='Will be rendered as Markdown', verbose_name='Description')),
                ('user_docs', models.URLField(blank=True, max_length=256, verbose_name='User documentation url')),
                ('admin_docs', models.URLField(blank=True, max_length=256, verbose_name='Admin documentation url')),
                ('developer_docs', models.URLField(blank=True, max_length=256, verbose_name='Developer documentation url')),
                ('issue_tracker', models.URLField(blank=True, max_length=256, verbose_name='Issue tracker url')),
                ('website', models.URLField(blank=True, max_length=256, verbose_name='Homepage')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name_plural': 'Apps',
                'verbose_name': 'App',
            },
        ),
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(help_text='Version follows Semantic Versioning', max_length=128, verbose_name='Version')),
                ('php_min', models.CharField(max_length=32, verbose_name='PHP minimum version')),
                ('php_max', models.CharField(blank=True, max_length=32, verbose_name='PHP maximum version')),
                ('platform_min', models.CharField(max_length=32, verbose_name='Platform minimum version')),
                ('platform_max', models.CharField(blank=True, max_length=32, verbose_name='Platform maximum version')),
                ('int_size_min', models.IntegerField(blank=True, default=0, help_text='e.g. 32 for 32bit Integers', verbose_name='Minimum Integer Bits')),
                ('download', models.URLField(blank=True, max_length=256, verbose_name='Archive download Url')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'App Releases',
                'verbose_name': 'App Release',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Full name')),
                ('mail', models.EmailField(blank=True, max_length=256, verbose_name='Mail address')),
                ('homepage', models.URLField(blank=True, max_length=256, verbose_name='Homepage')),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(help_text='Category id which is used to identify a category. Used to identify categories when uploading an app', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='Category name which will be presented to the user', max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.CharField(help_text='Key which is used to identify a database', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='Database name which will be presented to the user', max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Databases',
                'verbose_name': 'Database',
            },
        ),
        migrations.CreateModel(
            name='DatabaseDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_min', models.CharField(max_length=32, verbose_name='Database minimum version')),
                ('version_max', models.CharField(blank=True, max_length=32, verbose_name='Database maximum version')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AppRelease', verbose_name='App release')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Database', verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'Database Dependencies',
                'verbose_name': 'Database Dependency',
            },
        ),
        migrations.CreateModel(
            name='PhpExtension',
            fields=[
                ('id', models.CharField(help_text='e.g. libxml', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='PHP extension')),
            ],
            options={
                'verbose_name_plural': 'PHP Extensions',
                'verbose_name': 'PHP Extension',
            },
        ),
        migrations.CreateModel(
            name='PhpExtensionDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_min', models.CharField(max_length=32, verbose_name='Extension minimum version')),
                ('version_max', models.CharField(blank=True, max_length=32, verbose_name='Extension maximum version')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AppRelease', verbose_name='App Release')),
                ('php_extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PhpExtension', verbose_name='PHP Extension')),
            ],
            options={
                'verbose_name_plural': 'PHP Extension Dependencies',
                'verbose_name': 'PHP Extension Dependency',
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256, verbose_name='Image url')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'Screenshots',
                'verbose_name': 'Screenshot',
            },
        ),
        migrations.CreateModel(
            name='ShellCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of a required shell command, e.g. grep', max_length=128, unique=True, verbose_name='Shell Command')),
            ],
            options={
                'verbose_name_plural': 'Shell Commands',
                'verbose_name': 'Shell Command',
            },
        ),
        migrations.AddField(
            model_name='apprelease',
            name='databases',
            field=models.ManyToManyField(through='core.DatabaseDependency', to='core.Database', verbose_name='Database dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='libs',
            field=models.ManyToManyField(through='core.PhpExtensionDependency', to='core.PhpExtension', verbose_name='PHP extension dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='shell_commands',
            field=models.ManyToManyField(to='core.ShellCommand', verbose_name='Shell command dependency'),
        ),
        migrations.AddField(
            model_name='app',
            name='authors',
            field=models.ManyToManyField(to='core.Author', verbose_name='Authors'),
        ),
        migrations.AddField(
            model_name='app',
            name='categories',
            field=models.ManyToManyField(to='core.Category', verbose_name='Category'),
        ),
    ]
