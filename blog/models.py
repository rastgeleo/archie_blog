from django.db import models


class Category(models.Model):
    """Category an entry associated with"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.text


class Post(models.Model):
    """Blog post"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    def get_preview(self):
        return self.text[:200]
