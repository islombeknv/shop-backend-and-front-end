# Generated by Django 3.2 on 2021-05-05 07:13

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productmodel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttagmodel',
            options={'verbose_name': 'product tag', 'verbose_name_plural': 'product tags'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.ProductTagModel'),
        ),
    ]
