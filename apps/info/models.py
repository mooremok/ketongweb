from django.db import models
from ketong.models import KetongCmsBase

class Info(KetongCmsBase):
    image = models.FileField(verbose_name='封面上传', upload_to='info/')
    created_time = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '企业动态'


class News(KetongCmsBase):
    created_time = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '行业新闻'

class QandA(KetongCmsBase):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '常见问题'
