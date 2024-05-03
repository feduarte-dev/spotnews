from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        max_length=200,
                        validators=[
                            news.validators.validate_empty_data,
                            news.validators.validate_max_length,
                        ],
                    ),
                ),
            ],
        ),
    ]
