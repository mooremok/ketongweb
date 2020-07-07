from django.db import models
from ketong.models import KetongCmsBase


class CompanyInfo(KetongCmsBase):
    image = models.FileField(upload_to='images_uploads/', verbose_name='图片上传',
                             help_text='该图片用于样式设置，无特别说明时，勿自行上传', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = '公司简介'


class CompanyShow(KetongCmsBase):
    image = models.FileField(upload_to='images_uploads/', verbose_name='图片上传',
                             help_text='该图片用于样式设置，无特别说明时，勿自行上传', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = '可通风采'


class CompanyCulture(KetongCmsBase):
    image = models.FileField(upload_to='images_uploads/', verbose_name='图片上传',
                             help_text='该图片用于样式设置，无特别说明时，勿自行上传', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = '企业文化'


class Honor(KetongCmsBase):
    image = models.FileField(upload_to='images_uploads/', verbose_name='图片上传',
                             help_text='该图片用于样式设置，无特别说明时，勿自行上传', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '企业荣誉'


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述', blank=True, null=True)
    video = models.FileField(verbose_name='视频上传', upload_to='video/')
    upload_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '视频中心'
        ordering = ['-upload_time']
