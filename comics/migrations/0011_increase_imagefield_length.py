# Generated by Django 2.0.2 on 2018-02-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0010_change_filefield_to_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arc',
            name='image',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/arcs/'),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/characters/'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='image',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/creators/'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='cover',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/issues/', verbose_name='Cover Image'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='logo',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/publishers/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, max_length=150, upload_to='images/teams/'),
        ),
    ]
