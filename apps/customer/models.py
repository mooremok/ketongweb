from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=100, verbose_name='客户类型')

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = verbose_name_plural = '客户类型'


class Customer(models.Model):
    title = models.CharField(max_length=100, verbose_name='客户名称')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='客户类型')
    description = models.TextField(verbose_name='客户描述')
    customer_logo = models.FileField(verbose_name='客户logo', upload_to='customer_logo/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '客户案例'