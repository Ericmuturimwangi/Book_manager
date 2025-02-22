from django.db import models
from django.core import validators
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import re

# validation of the publication date
def validate_publication_date(value):
     if value> now().date():
          raise ValidationError("Publicaion date cannot be in the future")
     
# valifate the isbn
def valiate_isbn(value):
     if not re.match(r'^\d{10}(\d{3})?$', value):
        raise ValidationError("ISBN Must be 10 or 13 digits.")

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(validators=[validate_publication_date])
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField()

    def __str__(self):
        return self.title
