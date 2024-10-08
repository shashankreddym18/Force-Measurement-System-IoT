

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=' Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('address', models.TextField()),
                ('email', models.EmailField(default='', max_length=254)),
                ('pin', models.IntegerField(default=0)),
                ('mob', models.IntegerField(default=0)),
            ],
        ),
    ]

