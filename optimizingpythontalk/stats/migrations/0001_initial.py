# Generated by Django 2.0.6 on 2018-06-17 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('commit_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_url', models.CharField(max_length=30)),
                ('repo_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='commitcounts',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Repository', verbose_name='the related repository'),
        ),
    ]
