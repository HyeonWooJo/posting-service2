# Generated by Django 4.1.1 on 2022-09-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('context', models.CharField(max_length=200)),
                ('psword', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'postings',
            },
        ),
    ]
