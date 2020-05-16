from django.db import models


class FoodBlogPost(models.Model):
    cover_image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    posts = models.Manager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def images(self):
        return "\n".join([
            f'Image: { child.image}' for child in self.foodimage_set.all()
        ])
    images.short_description = "Images"

    def sections(self):
        return "\n".join([
            f'{ child.section }' for child in self.foodpost_set.all()
        ])
    sections.short_description = "Sections"


class FoodImage(models.Model):
    post = models.ForeignKey(FoodBlogPost, default=None, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='images', verbose_name='Image')

    def __str__(self):
        return self.post.title


class FoodPost(models.Model):
    post = models.ForeignKey(FoodBlogPost, default=None, on_delete=models.SET_DEFAULT)
    section = models.TextField()

    def __str__(self):
        return self.post.title


class FoodComment(models.Model):
    post = models.ForeignKey(FoodBlogPost, on_delete=models.CASCADE)
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





