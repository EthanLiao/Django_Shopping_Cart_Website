# -*- coding: UTF-8 -*-
from django.urls import reverse
from django.db import models
from django.db.models import Q
from uuslug import slugify

class Navbar(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True,
                            null=True,
                            blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'navbar'
        verbose_name_plural = 'navbars'

    # def __str__(self):
    #     return self.name.encode("utf-8")

    def get_absolute_url(self):
        return reverse('shop:category_list_by_navbars',
                        args=[self.slug])
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Navbar,self).save(*args,**kwargs)
'''
    def get_search_url(self):
        return reverse('shop:product_list_by_search',
                        args=[self.slug])
'''

class Category(models.Model):
    navbar = models.ForeignKey(Navbar,related_name='categories',on_delete=models.CASCADE)
    name = models.CharField(u'名稱',max_length=200,
                            db_index=True)
    slug = models.SlugField(u'描述',max_length=200,
                            db_index=True,
                            unique=True,
                            null=True,
                            blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def __str__(self):
    #     return self.name.encode("utf-8")   #return the CharField defined in this class

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)
'''
    def __unicode__(self):
        return self.name
'''



'''
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug,self.id])

'''
class AvailableQuerySet(models.QuerySet):
    def available_product(self):
        return self.filter(available=True)
    def general_search(self,query):
        #return self.filter(name__icontains=query)
        lookup = (
                    Q(description__icontains=query)|
                    Q(name__icontains=query)
                 )
        return self.filter(lookup)

class AvailableManager(models.Manager):
    def get_queryset(self):
        return AvailableQuerySet(self.model,using = self._db)
    def available_product(self):
        return self.get_queryset().available_product()
    def general_search(self,query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().available_product().general_search(query)

PRODUCT_KILOMETERS_CHOICES = [(i, str(i)) for i in range(1, 21)]
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,null=True,blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    #image = models.ImageField(upload_to='products/',blank=True)
    method_URL = models.CharField(max_length=200,default="html/general_transportation_method.html")
    video_URL = models.CharField(max_length=200,default="https://www.youtube.com/embed/hR4DiU8wcVk")
    transcript_URL = models.CharField(max_length=200,default="https://hackmd.io/QPCmFC-6Rkmlv7NWkS76ug")
    description = models.TextField(blank=True)
    kilometers = models.IntegerField(choices=PRODUCT_KILOMETERS_CHOICES,default=1)
    # 台灣價錢都是整數，所以可以設定 decimal_places=0
    price = models.DecimalField(max_digits=10, decimal_places=0,default=9999)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    available_product = AvailableManager()
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    # def __str__(self):
    #     return self.name.encode("utf-8")

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.category.slug,self.category.navbar.slug,self.id, self.slug,self.price,self.kilometers])
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

class IOT_data(models.Model):
    SensorID = models.CharField(max_length=20,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    Temperature = models.CharField(max_length=20,null=True,blank=True)
    Humidity = models.CharField(max_length=20,null=True,blank=True)
    class Meta:
        app_label = 'iot'
