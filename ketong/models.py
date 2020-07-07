from django.db import models
from DjangoUeditor.models import UEditorField

#KetongCmsBase抽象成系统所有涉及图文展示的公共部分

class KetongCmsBase(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    content = UEditorField(verbose_name='内容', width=960, height=600, imagePath='editor_uploads/')

    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True