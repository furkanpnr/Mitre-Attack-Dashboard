# Generated by Django 5.0.6 on 2024-06-02 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackresult',
            name='result_type',
            field=models.CharField(choices=[('screen_capture', 'Screen Capture'), ('system_info', 'System Info'), ('clipboard_data', 'Clipboard Data')], default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attackresult',
            name='attack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_results', to='api.attack'),
        ),
        migrations.AlterField(
            model_name='attackresult',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_results', to='api.machine'),
        ),
    ]
