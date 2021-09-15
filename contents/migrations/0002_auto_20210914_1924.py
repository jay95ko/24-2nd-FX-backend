# Generated by Django 3.2.7 on 2021-09-14 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.content')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.genre')),
            ],
            options={
                'db_table': 'content_genre_relations',
            },
        ),
        migrations.RemoveField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='contents', to='contents.Genre'),
        ),
        migrations.AddField(
            model_name='content',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='contents', through='contents.ContentGenre', to='contents.Genre'),
        ),
    ]
