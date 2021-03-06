# Generated by Django 2.2.13 on 2020-09-18 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0126_update_history_after_directing_dept_remove'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutingExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.Department')), # noqa
                ('_expression', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='routing_department', to='signals.Expression')), # noqa
            ],
        ),
    ]
