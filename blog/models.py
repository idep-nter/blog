from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="author", null=True)
    email = models.EmailField()
    about_me = models.TextField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(null=True)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")