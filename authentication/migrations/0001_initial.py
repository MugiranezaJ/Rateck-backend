# Generated by Django 4.0.6 on 2022-07-07 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('resident_city', models.CharField(blank=True, max_length=225)),
                ('resident_country', models.CharField(blank=True, max_length=225)),
                ('phone', models.CharField(blank=True, max_length=225)),
                ('profile_image', models.TextField(blank=True, default='')),
                ('is_verified', models.BooleanField(blank=True, default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('seller', 'Seller'), ('editor', 'Editor')], max_length=255)),
                ('gender', models.CharField(blank=True, max_length=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_user_model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]