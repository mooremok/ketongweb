from django.db import models


class IndexSpe(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    image = models.FileField(upload_to='index/')
    target = models.URLField(max_length=255, verbose_name='跳转链接')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '优势线路设置'

class IndexSer(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述', blank=True, null=True, help_text='预留接口，无需填写')
    image = models.FileField(upload_to='index/')
    target = models.URLField(max_length=255, verbose_name='跳转链接')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '服务项目设置'
