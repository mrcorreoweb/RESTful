from rest_framework import serializers
from .models import Writer, Book

class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ['url', 'id', 'name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    # Use HyperlinkedRelatedField to link to the Writer model
    writer = serializers.HyperlinkedRelatedField(view_name='writer-detail', queryset=Writer.objects.all())
    # Additional field to return the writer name
    writer_name = serializers.CharField(source='writer.name', read_only=True)

    class Meta:
        model = Book
        # Include both the writer's url and his name
        fields = ['url', 'id', 'title', 'writer', 'writer_name']

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
        writer_name = validated_data.get('writer')
        writer, created = Writer.objects.get_or_create(name=writer_name)
        instance.writer = writer
        instance.save()
        return instance
