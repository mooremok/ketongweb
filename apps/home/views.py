from django.shortcuts import render
from ad.models import IndexBanner
from info.models import Info, News, QandA
from about_us.models import Video
from customer.models import Customer, Type
from . models import IndexSer, IndexSpe
from ketong.navs import dynamic_navs

def index(request):
		#banner
		banners = IndexBanner.objects.all()[:3]
		infos = Info.objects.all()[:4]
		news = News.objects.all()[:5]
		qas = QandA.objects.all()[:5]
		videos = Video.objects.all()[:3]
		types = Type.objects.all()
		sers = IndexSer.objects.all()[:4]
		spes = IndexSpe.objects.all()[:3]

		context = {
				'banners': banners,
				'infos': infos,
				'news': news,
				'qas': qas,
				'videos': videos,
				'types': types,
				'sers': sers,
				'spes': spes,
		}
		context.update(dynamic_navs())
		return render(request, 'home/index.html', context)