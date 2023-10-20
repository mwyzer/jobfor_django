# Generated by Django 4.2.6 on 2023-10-18 08:50

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
            name="CandidateApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("passingYear", models.IntegerField()),
                ("yearOfExp", models.IntegerField(default=0)),
                ("resume", models.FileField(upload_to="resume")),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "pending"), ("selected", "selected")],
                        default="pending",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("companyName", models.CharField(max_length=200)),
                ("salaryLow", models.IntegerField(default=0)),
                ("salaryHigh", models.IntegerField(default=0)),
                ("applyCount", models.IntegerField(default=0)),
                ("lastDateToApply", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SelectCandidateJob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "candidate",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hr.candidateapplication",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hr.jobpost"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hr",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="candidateapplication",
            name="job",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="hr.jobpost"
            ),
        ),
        migrations.AddField(
            model_name="candidateapplication",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]