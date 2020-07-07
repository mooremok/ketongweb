from ketong.models import KetongCmsBase

class Service(KetongCmsBase):
    class Meta:
        verbose_name = verbose_name_plural = '服务设置'

class SpecialService(KetongCmsBase):
    class Meta:
        verbose_name = verbose_name_plural = '特色服务'

class KeeperService(KetongCmsBase):
    class Meta:
        verbose_name = verbose_name_plural = '管家服务'