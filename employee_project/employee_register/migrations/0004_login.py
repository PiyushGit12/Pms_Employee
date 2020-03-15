# Generated by Django 3.0.3 on 2020-03-15 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_auto_20200315_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=1000)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Employee')),
            ],
        ),
    ]