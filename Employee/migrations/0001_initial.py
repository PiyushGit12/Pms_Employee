# Generated by Django 3.0.3 on 2020-02-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDaTa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('job_title', models.CharField(default='NA', max_length=25)),
                ('last_ap_date', models.CharField(max_length=100)),
                ('reporting_mail', models.EmailField(max_length=50)),
                ('doj', models.CharField(max_length=100)),
                ('evalute_by', models.CharField(max_length=100)),
            ],
        ),
    ]