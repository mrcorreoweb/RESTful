from rest_framework import serializers
from .models import Writer, Book

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    writer = serializers.CharField()  # Accept writer name as a string

    class Meta:
        model = Book
        fields = ['id', 'title', 'writer']

    def create(self, validated_data):
        # Extract writer name from validated data
        writer_name = validated_data.pop('writer')
        
        # Try to fetch the writer by name, or create if it doesn't exist
        writer, created = Writer.objects.get_or_create(name=writer_name)
        
        # Create the book with the associated writer
        book = Book.objects.create(writer=writer, **validated_data)
        
        return book
    
    def update(self, instance, validated_data):
        # Update title and writer
        instance.title = validated_data.get('title', instance.title)
        
        # Get or create writer by name
        writer_name = validated_data.get('writer')
        writer, created = Writer.objects.get_or_create(name=writer_name)
        
        instance.writer = writer
        instance.save()
        return instance
