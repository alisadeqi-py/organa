# Generated by Django 3.2 on 2022-11-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images')),
                ('Properties', models.TextField()),
                ('M_taking', models.TextField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('special', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('Update_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.BigIntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
        ),
    ]
