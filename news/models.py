from django.db import models
from news.validators import validate_class_attributes


class Category(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_class_attributes]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
        max_length=200, validators=[validate_class_attributes]
    )
    email = models.EmailField(
        max_length=200, validators=[validate_class_attributes]
    )
    password = models.CharField(
        max_length=200, validators=[validate_class_attributes]
    )
    role = models.CharField(
        max_length=200, validators=[validate_class_attributes]
    )

    def __str__(self):
        return self.name
