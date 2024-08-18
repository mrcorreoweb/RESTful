""" Create classes for two entities: 📚 **Books** and ✍️ **Writers**"""

from django.db import models


class Writer(models.Model):
    """Represents a writer in the library."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    """Represents a book in the library."""

    title = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return str(self.title)
