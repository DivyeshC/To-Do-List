# Generated by Django 3.1.4 on 2021-01-11 04:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100)),
                ('priority', models.CharField(choices=[('1-High', 'High'), ('2-Medium', 'Medium'), ('3-Low', 'Low')], max_length=100)),
                ('last_date', models.DateField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
