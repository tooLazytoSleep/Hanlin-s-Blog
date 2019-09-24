from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Category',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField('Tag', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog Tag'
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField('Article Title',max_length=128)
    author = models.ForeignKey(User,verbose_name='Author',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_img',null=True,blank=True,verbose_name='Blog Image')
    body = models.TextField('Body',)
    abstract = models.TextField('Abstract',max_length=256,null=True,blank=True)
    visiting = models.PositiveIntegerField('Visiting',default=0)
    category = models.ManyToManyField('Category',verbose_name='Blog Category')
    tags = models.ManyToManyField('Tag',verbose_name='Tag')
    created_time = models.DateTimeField('Created Time',auto_now_add=True)
    modified_time = models.DateTimeField('Modified Time',auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = 'Blog Body'
        verbose_name_plural = verbose_name