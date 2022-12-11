# Generated by Django 4.1.3 on 2022-11-29 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("group", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupmember",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships",
                to="group.group",
            ),
        ),
        migrations.AlterField(
            model_name="groupmember",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups_joined",
                to="user.profile",
            ),
        ),
    ]