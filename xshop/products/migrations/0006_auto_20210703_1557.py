# Generated by Django 3.2 on 2021-07-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210330_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='no_picture.png', upload_to='images/products/'),
        ),
    ]
