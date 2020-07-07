from django.db import models


class IndexBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.FileField(verbose_name='图片', upload_to='indexbanner/')
    url = models.URLField(max_length=255, verbose_name='点击跳转', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '主页banner'
        ordering = ['-created_time']
    

class SubPageBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.FileField(verbose_name='图片', upload_to='indexbanner/')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '二级页面banner'
        ordering = ['-created_time']