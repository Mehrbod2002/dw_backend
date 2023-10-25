# Generated by Django 4.2.5 on 2023-09-22 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('markets', '0018_remove_wallets_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockFee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is_Deleted')),
                ('currency', models.CharField(choices=[('USDT', 'Usdt'), ('USD', 'Usd'), ('EURO', 'Euro')], max_length=10, verbose_name='currency')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Amount')),
                ('status', models.CharField(choices=[('COMPLETED', 'Completed'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], default='PENDING', max_length=10, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
