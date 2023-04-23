# Generated by Django 4.2 on 2023-04-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_store', '0003_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=20, verbose_name='Название столбца')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимость')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
