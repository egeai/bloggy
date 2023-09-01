from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    # Note: Index ordering is not supported on MySQL. If you use MySQL for the database,
    # a descending index will be created as a normal index.
    # you can also specify a custom database name for your model in the
    # Meta class of the model using the db_table attribute.
    class Meta:
        ordering = ['-publish']  # descending order on the "publish" column
        indexes = [  # this will improve performance for queries filtering or ordering results by this field
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
