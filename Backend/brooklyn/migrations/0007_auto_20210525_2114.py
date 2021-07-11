# Generated by Django 3.1.1 on 2021-05-25 21:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brooklyn', '0006_auto_20210524_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectobject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectobject',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 25, 21, 14, 18, 906674, tzinfo=utc)),
        ),
    ]