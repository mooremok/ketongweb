from django.db import models
from ketong.models import KetongCmsBase

class Network(KetongCmsBase):

    class Meta:
        verbose_name = verbose_name_plural = '网点'

class WechatQrCode(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    image = models.FileField(verbose_name='二维码', upload_to='wechat/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '二维码管理'

class MessageBoard(models.Model):
    TYPE = (
        (1, '建议'),
        (2, '投诉'),
    )

    title = models.CharField(max_length=100, verbose_name='标题')
    type = models.IntegerField(choices=TYPE, verbose_name='留言类型')
    from_to = models.CharField(max_length=100, verbose_name='联系人')
    tel = models.CharField(max_length=30, verbose_name='联系方式')
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = verbose_name_plural = '投诉与建议'
        ordering = ['-created_time']
