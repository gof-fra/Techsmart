# Generated by Django 2.2 on 2019-04-28 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='images_pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images_pics'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('titre', 'slug')},
        ),
    ]