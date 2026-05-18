from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models


class FontType(models.IntegerChoices):
    TITLE = 1
    ABILITY_NAME = 2
    ABILITY_DESC = 3
    STATS = 4
    CREDITS = 5


class FontConfig(models.Model):
    name = models.CharField(max_length=50, default="settings")


# Create your models here.
class Font(models.Model):
    file = models.FileField(
        help_text="The font file", validators=[FileExtensionValidator(allowed_extensions=["ttf", "otf"])]
    )
    role = models.SmallIntegerField(help_text="The type of font", unique=True, choices=FontType)
    size = models.IntegerField(help_text="The font size", validators=[MinValueValidator(1), MaxValueValidator(400)])
    config = models.ForeignKey(FontConfig, on_delete=models.CASCADE)

    def __str__(self):
        return str(FontType(self.role))
