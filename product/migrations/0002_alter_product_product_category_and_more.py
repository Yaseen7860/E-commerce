# Generated by Django 4.0.2 on 2022-02-26 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='product.productcategory'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='product'),
        ),
    ]
