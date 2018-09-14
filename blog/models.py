from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
        verbose_name=_('Post|author')
    )
    title = models.CharField(max_length=200, verbose_name=_('Post|title'))
    text = models.TextField(verbose_name=_('Post|text'))
    created_date = models.DateTimeField(default=timezone.now,
        verbose_name=_('Post|created date')
    )
    published_date = models.DateTimeField(blank=True, null=True,
        verbose_name=_('Post|published date')
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def publish(self):
        self.published_date = timezone.now()

        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,
        related_name='comments', verbose_name=_('Comment|post')
    )
    author = models.CharField(max_length=200, verbose_name=_('Comment|author'))
    text = models.TextField(verbose_name=_('Comment|text'))
    created_date = models.DateTimeField(default=timezone.now,
        verbose_name=_('Comment|created date')
    )
    approved_comment = models.BooleanField(default=False,
        verbose_name=_('Comment|approved comment')
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def approve(self):
        self.approved_comment = True

        self.save()

    def __str__(self):
        return self.text
