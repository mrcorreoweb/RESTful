from django.db import models

# Create classes for two entities: 📚 **Books** and ✍️ **Writers**


class Writer(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return str(self.title)
