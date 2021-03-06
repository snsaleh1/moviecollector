# Generated by Django 2.2.3 on 2019-09-12 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('snack', models.CharField(choices=[('p', 'Popcorn'), ('c', 'Candy'), ('i', 'Ice Cream'), ('c', 'Chips'), ('s', 'Steak')], default='p', max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Movie')),
            ],
        ),
    ]
