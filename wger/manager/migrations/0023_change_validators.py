# Generated by Django 4.2.20 on 2025-04-05 11:41

import django.core.validators
from django.db import migrations, models
import wger.manager.validators


class Migration(migrations.Migration):
    dependencies = [
        ('manager', '0022_alter_rir_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxrepetitionsconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(3000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='maxrestconfig',
            name='value',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(600),
                ]
            ),
        ),
        migrations.AlterField(
            model_name='maxrirconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    wger.manager.validators.NullMinValueValidator(0),
                    wger.manager.validators.validate_rir,
                ],
            ),
        ),
        migrations.AlterField(
            model_name='maxsetsconfig',
            name='value',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(50),
                ]
            ),
        ),
        migrations.AlterField(
            model_name='maxweightconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(3000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='repetitionsconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(3000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='restconfig',
            name='value',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1800),
                ]
            ),
        ),
        migrations.AlterField(
            model_name='rirconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=1,
                max_digits=2,
                validators=[
                    wger.manager.validators.NullMinValueValidator(0),
                    wger.manager.validators.validate_rir,
                ],
            ),
        ),
        migrations.AlterField(
            model_name='setsconfig',
            name='value',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(50),
                ]
            ),
        ),
        migrations.AlterField(
            model_name='weightconfig',
            name='value',
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(3000),
                ],
            ),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='rir',
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=2,
                null=True,
                validators=[
                    wger.manager.validators.NullMinValueValidator(0),
                    wger.manager.validators.validate_rir,
                ],
            ),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='rir_target',
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=2,
                null=True,
                validators=[
                    wger.manager.validators.NullMinValueValidator(0),
                    wger.manager.validators.validate_rir,
                ],
            ),
        ),
    ]
