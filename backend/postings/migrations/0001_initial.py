# Generated by Django 2.1.1 on 2018-09-27 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateableEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewHelpfulVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpful', models.BooleanField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postings.Review')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=200)),
                ('date_published', models.DateField(verbose_name='date published')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('rateableentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='postings.RateableEntity')),
            ],
            bases=('postings.rateableentity',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('rateableentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='postings.RateableEntity')),
            ],
            bases=('postings.rateableentity',),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('rateableentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='postings.RateableEntity')),
            ],
            bases=('postings.rateableentity',),
        ),
        migrations.AddField(
            model_name='review',
            name='rateable_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postings.RateableEntity'),
        ),
        migrations.AddField(
            model_name='professor',
            name='universities',
            field=models.ManyToManyField(to='postings.University'),
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(to='postings.Professor'),
        ),
        migrations.AddField(
            model_name='course',
            name='taught_at_university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postings.University'),
        ),
    ]
