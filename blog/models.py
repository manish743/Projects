from django.db import models

# Create your models here.
class BlogPost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()