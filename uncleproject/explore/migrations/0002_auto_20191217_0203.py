# Generated by Django 2.2.1 on 2019-12-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='imgUrl',
        ),
        migrations.AddField(
            model_name='group',
            name='liked_books',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_building',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_celebrate',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_delicious',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_depressed',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_firework',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_hiking',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_infant',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_lonely',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_nightclub',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_selfie',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_sports',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='liked_studying',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='total_user',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='big5_agreeableness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='big5_conscientiousness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='big5_extraversion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='big5_neuroticism',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='big5_openness',
            field=models.IntegerField(),
        ),
    ]
