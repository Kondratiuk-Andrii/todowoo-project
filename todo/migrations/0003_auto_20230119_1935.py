# Generated by Django 3.2.16 on 2023-01-19 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_auto_20230119_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created'], 'verbose_name': 'To Do Task', 'verbose_name_plural': 'To Do Tasks'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time Created'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time Completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False, verbose_name='Important'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True, verbose_name='Memo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner Name'),
        ),
    ]
