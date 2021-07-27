from django.db import models
from django.urls import reverse


class Tag(models.Model):
    TagName = models.CharField(max_length=65)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.TagName

    def get_absolute_url(self):
        return reverse('newsBlog:tag', args=[self.id])


# Модель, внутри которой хранятся ip посетителей
class IP(models.Model):
    IpName = models.CharField(max_length=45)


class News(models.Model):
    header = models.CharField(max_length=165, db_index=True, unique=True)
    slug = models.SlugField(max_length=165, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    tags = models.ManyToManyField('Tag', blank=False, related_name='tags')
    views = models.ManyToManyField(IP, blank=True)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('newsBlog:post',
                       args=[self.slug])

    # функция подсчета просмотров через поле views
    def total_views(self):
        return self.views.count()



