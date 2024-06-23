# Generated by Django 5.0.2 on 2024-05-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0037_tradesales'),
    ]

    operations = [
        migrations.AddField(
            model_name='channels',
            name='local_inbound_base_fee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channels',
            name='local_inbound_fee_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channels',
            name='remote_inbound_base_fee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channels',
            name='remote_inbound_fee_rate',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forwards',
            name='inbound_fee',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
