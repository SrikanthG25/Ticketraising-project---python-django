# Generated by Django 4.2.6 on 2023-12-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket_ID', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Reason', models.TextField()),
                ('Reason_Description', models.TextField()),
                ('Appeared_Time', models.DateTimeField()),
                ('Priority_Scales', models.CharField(choices=[('none', 'None'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default=None, max_length=100)),
                ('Status', models.CharField(choices=[('none', 'None'), ('pending', 'Pending'), ('inprogress', 'In Progress'), ('success', 'Completed')], default=None, max_length=100)),
                ('Reporter', models.TextField(default=None)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
