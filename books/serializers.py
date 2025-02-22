from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields  = '__all__'

    def validate_publication_date(self, value):
        from django.utils.timezone import now
        if value > now() . date():
            raise serializers.ValidationError("Pubication date cannot be in the future")
        return value
    
    def validate_isbn(self, value):
        import re
        if not re.match(r'^\d{10}(\d{3})?$', value):
            raise serializers.ValidationError("ISBN Must be 10 or 13 digits. ")
        return value
    