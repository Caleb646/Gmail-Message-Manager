# Generated by Django 3.2.5 on 2022-05-17 14:40

from django.conf import settings
from django.db import migrations, models
import rfis.models


class Migration(migrations.Migration):

    dependencies = [
        ('rfis', '0004_auto_20220510_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='fromm',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='to',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='thread',
            name='accepted_answer',
            field=models.TextField(blank=True, default='', verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='gmail_thread_id',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='job_id',
            field=models.ForeignKey(on_delete=models.SET(rfis.models.Job.get_job_sentinel_id), to='rfis.job', verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='message_thread_initiator',
            field=models.ForeignKey(on_delete=models.SET(rfis.models.MyUser.get_user_sentinel_id), to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='original_initiator',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='thread',
            name='subject',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='thread',
            name='thread_status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN', max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='thread_type',
            field=models.ForeignKey(default=rfis.models.ThreadType.get_message_type_sentinel_id, on_delete=models.SET(rfis.models.ThreadType.get_message_type_sentinel_id), to='rfis.threadtype', verbose_name='Type'),
        ),
    ]