# Generated by Django 4.2 on 2023-05-03 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('tel_number', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=20)),
                ('worker_tip', models.CharField(max_length=20)),
                ('today_money', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_worker', to='service.worker')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_for_worker', to='service.worker')),
            ],
        ),
        migrations.CreateModel(
            name='OrderForUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('img_link', models.CharField(blank=True, max_length=500, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_user', to='service.user')),
            ],
        ),
    ]