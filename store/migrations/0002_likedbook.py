# Generated by Django 3.2.10 on 2022-04-17 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.books')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
