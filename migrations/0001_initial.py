# Generated by Django 2.0.2 on 2018-03-01 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_date', models.DateField(auto_now=True)),
                ('closing_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contract_type', models.CharField(choices=[('PT', 'Part-Time'), ('FT', 'Full-Time'), ('CN', 'Contract')], max_length=10)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('street_address', models.TextField(max_length=500)),
                ('district', models.CharField(choices=[('AM', 'Ampara'), ('AN', 'Anuradhapura'), ('BD', 'Badulla'), ('BT', 'Batticaloa'), ('CO', 'Colombo'), ('GL', 'Galle'), ('GP', 'Gampaha'), ('HT', 'Hambantota'), ('JF', 'Jaffna'), ('KT', 'Kalutara'), ('KY', 'Kandy'), ('KG', 'Kegalle'), ('KL', 'Kilinochchi'), ('KR', 'Kurunegala'), ('MN', 'Mannar'), ('ME', 'Matale'), ('MT', 'Matara'), ('MO', 'Monaragala'), ('ML', 'Mullaitivu'), ('NE', 'Nuwara Eliya'), ('PN', 'Polonnaruwa'), ('PT', 'Puttalam'), ('RT', 'Ratnapura'), ('TR', 'Trincomalee'), ('VW', 'Vavuniya')], max_length=50)),
                ('town', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Advertisement')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('industry', models.CharField(choices=[('IT', 'Information Technology'), ('FN', 'Finance'), ('MC', 'Management Consultants'), ('CN', 'Constructions')], max_length=25)),
                ('street_address', models.TextField(max_length=500)),
                ('district', models.CharField(choices=[('AM', 'Ampara'), ('AN', 'Anuradhapura'), ('BD', 'Badulla'), ('BT', 'Batticaloa'), ('CO', 'Colombo'), ('GL', 'Galle'), ('GP', 'Gampaha'), ('HT', 'Hambantota'), ('JF', 'Jaffna'), ('KT', 'Kalutara'), ('KY', 'Kandy'), ('KG', 'Kegalle'), ('KL', 'Kilinochchi'), ('KR', 'Kurunegala'), ('MN', 'Mannar'), ('ME', 'Matale'), ('MT', 'Matara'), ('MO', 'Monaragala'), ('ML', 'Mullaitivu'), ('NE', 'Nuwara Eliya'), ('PN', 'Polonnaruwa'), ('PT', 'Puttalam'), ('RT', 'Ratnapura'), ('TR', 'Trincomalee'), ('VW', 'Vavuniya')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher')),
            ],
        ),
        migrations.AddField(
            model_name='following',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher'),
        ),
    ]
