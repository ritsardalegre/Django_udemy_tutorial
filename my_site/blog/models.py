from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify



# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"
    


class Tag(models.Model):

    caption = models.CharField(max_length=50)
    

    class Meta:
        # verbose_name = _("")
        # verbose_name_plural = ("")
        pass

    def __str__(self):
        return self.caption

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

    

class Post(models.Model):
    title = models.CharField(max_length=120)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default="", blank=True, null=False)                   
    content = models.TextField(validators=[MinLengthValidator(10)])

    Author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    caption = models.ManyToManyField(Tag)
    

    
