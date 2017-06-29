from django.test import TestCase

# Create your tests here.

# for cloning group HouseInfo.objects only (begin)
from workapp.models import HouseInfo
from workapp.models import Area
import random

def group_delete():

    for i in range(1,25):
        obji = HouseInfo.objects.get(pk=i)
        obji_tbd = HouseInfo.objects.get(pk=i)
        obji_tbd.delete()
        obji.save()
    # obj1 = HouseInfo.objects.get(pk=1)
    # obj2 = HouseInfo.objects.get(pk=2)
    # obj3 = HouseInfo.objects.get(pk=3)
    # obj4 = HouseInfo.objects.get(pk=4)
    #
    # obj_list = HouseInfo.objects.all()
    # for obj in obj_list:
    #     obj.delete()
    #
    # obj1.save()
    # obj2.save()
    # obj3.save()
    # obj4.save()

def group_klone():

    j_list = [1,2,3,4,8]
    random.shuffle(j_list)

    for i in range(1,5): #原体循环
        for j in j_list: #户型循环
            for k in ['整租','合租','月租']: #类型循环
                for m in [
                        '电视 网络 淋浴 空调',
                        '电视 网络 淋浴 空调 厨房',
                        '电视 网络 淋浴 空调 暖气',
                        '电视 网络 淋浴 空调 独立卫生间 独立阳台',
                        '电视 网络 淋浴 空调 独立卫生间 厨房',
                        '电视 网络 淋浴 空调 独立卫生间 厨房'
                        ]: #设施循环
                    for n in range(1,11): #图片循环

                        # 准备
                        HOUSETYPE_DICT = {
                            '1': '一室一厅一卫',
                            '2': '二室一厅一卫',
                            '3': '三室一厅两卫',
                            '4': '四室两厅两卫',
                            '8': '八室八厅八卫'
                        }
                        obj0 = HouseInfo.objects.get(pk=i)

                        #克隆原体
                        obj = HouseInfo.objects.get(pk=i)
                        obj.pk = None
                        obj.save()
                        obj.area_to = obj0.area_to.all()

                        #改变参数 - 户型
                        obj.housetype = HOUSETYPE_DICT[str(j)]
                        if obj.title.find('居'):
                            obj.title_mid = obj.title.replace(obj.title[obj.title.find('居') - 1], str(j))
                        else:
                            obj.title_mid = obj.title

                        #改变参数 - 类型
                        for k_mid_index, k_mid in enumerate(['整租','合租','月租']):
                            if obj.title_mid.find(k_mid):
                                obj.title = obj.title_mid.replace(k_mid, k)
                            elif k_mid_index == 2:
                                obj.title = obj.title_mid
                        obj.type = k

                        # if k == '合租':
                        #     obj.title = obj.title_mid.replace(obj.title[-2:], '单间')
                        # else:
                        #     obj.title = obj.title_mid.replace(obj.title[-2:], k)


                        #改变参数 - 设施
                        obj.installations = m

                        #改变参数 - 价格
                        p = random.sample(range(1,3001),1)[0]
                        obj.rent = p

                        #改变参数 - 图片
                        obj.pic_max.name = 'house_pic/img' + str(n) + '.png'

                        #保存
                        obj.save()

# for cloning group HouseInfo.objects only (ender)

# for cloning one HouseInfo.objects only (begin)
def one_klone():

    i = 1 #原体 - pk = 1
    j = 4 #户型 - 4居
    k = '整租' #类型 - 整租
    m = '电视 网络 淋浴 空调 暖气' #设施 - ...

    # 准备
    obj0 = HouseInfo.objects.get(pk=i)

    #克隆原体
    obj = HouseInfo.objects.get(pk=i)
    obj.pk = 4
    obj.save()
    obj.area_to = obj0.area_to.all()

    #改变参数 - 户型
    obj.title_mid = obj.title.replace(obj.title[obj.title.find('院') + 1], str(j))

    #改变参数 - 类型
    if k == '合租':
        obj.title = obj.title_mid.replace(obj.title[-2:], '单间')
    else:
        obj.title = obj.title_mid.replace(obj.title[-2:], k)
    obj.type = k

    #改变参数 - 设施
    obj.installations = m

    #保存
    obj.save()

# for cloning one HouseInfo.objects only (ender)
