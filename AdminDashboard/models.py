from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.category


# Blog Post
class BlogPost(models.Model):
    cover_image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', max_length=75, on_delete=models.CASCADE)
    posts = models.Manager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def images(self):
        return "\n".join([
            f'Image: { child.image}' for child in self.image_set.all()
        ])
    images.short_description = "Images"

    def sections(self):
        return "\n".join([
            f'{ child.section }' for child in self.post_set.all()
        ])
    sections.short_description = "Sections"


# Images for blog post
class Image(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='images', verbose_name='Image')

    def __str__(self):
        return self.post.title


# Posts for blog post
class Post(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.SET_DEFAULT)
    section = models.TextField()

    def __str__(self):
        return self.post.title


# Comments for blog post
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=60, default='Anonymous',)
    comment = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    comments = models.Manager()

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-created_on']

