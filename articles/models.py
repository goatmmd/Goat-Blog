from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=32, verbose_name=_('name'))
    parent_id = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True,
        blank=True, related_name='parents', verbose_name=_('parent id ')
    )

    created_time = models.DateTimeField(auto_now=True, verbose_name=_('created time'))
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name=_('modified time'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category-post', args=str(self.pk))


class Post(models.Model):
    DRAFT = _("Draft")
    PUBLISHED = _('Published')

    Article_Status = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    title = models.CharField(
        max_length=50, verbose_name=_('title')
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', verbose_name=_('author')
    )

    status = models.CharField(
        choices=Article_Status, max_length=20, verbose_name=_('status')
    )

    body = RichTextField(
        blank=True, null=True, verbose_name=_('body')
    )

    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, related_name='categories', verbose_name=_('category')
    )

    likes = models.ManyToManyField(
        User, related_name='likes', blank=True, verbose_name=_('likes')
    )

    created_time = models.DateTimeField(auto_now=True, verbose_name=_('created time'))
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name=_('modified time'))

    class Meta:
        ordering = ('-created_time',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-detail', args=[self.pk])


class Comment(models.Model):
    class Meta:
        ordering = ('-created_time', )
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()

    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} comment on {self.post}"
