# Generated by Django 3.2 on 2021-05-25 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210525_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.postmodel', verbose_name='comments'),
        ),
    ]