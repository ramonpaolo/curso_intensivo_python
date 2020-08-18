# Generated by Django 3.0.8 on 2020-07-18 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizzas.Topicos')),
            ],
        ),
    ]
