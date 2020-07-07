from .models import Customer, Type

#处理首页按列别展示客户案例

def show_customers_index():
    customers = Customer.objects.all()
    types = Type.objects.all()

    #遍历所有分类实例
    for type in types:
      pass