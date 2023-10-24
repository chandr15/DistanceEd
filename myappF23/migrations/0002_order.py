# Generated by Django 4.2.6 on 2023-10-23 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myappF23', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(0, 'Order Confirmed'), (1, 'Order Cancelled')], default=1)),
                ('order_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappF23.student')),
            ],
        ),
    ]
