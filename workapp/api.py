from workapp.models import HouseInfo,Area
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseInfo
        fields = '__all__'
        depth = 1

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

@api_view(['GET'])
def indexHouseList(request):

    area_list = Area.objects.all()
    areaSerializer = AreaSerializer(area_list,many=True)

    recommendList = HouseInfo.objects.order_by('rent')[:3]
    recommendSerializer = HouseSerializer(recommendList, many=True)

    house_list = HouseInfo.objects.order_by('distance')
    near_area_list = []
    nearby_area_count = 0
    for house in house_list:
        nearby_area = house.area_to.all()
        for area in nearby_area:
            if area not in near_area_list:
                near_area_list.append(area)
                nearby_area_count += 1
            if nearby_area_count >= 3:
                break
        if nearby_area_count >= 3:
            break
    nearHouseSerializer = AreaSerializer(near_area_list, many=True)


    resultDict = {
        'area_list': areaSerializer.data,
        'excellent_house_list': recommendSerializer.data,
        'near_area_list': nearHouseSerializer.data,
    }

    return Response(resultDict)

@api_view(['GET'])
def searchHouselist(request, area_id):
    print("area_id = " + area_id)
    # note: area_to is an object
    a = Area.objects.get(id=area_id)
    house_list = HouseInfo.objects.filter(area_to=a).order_by('-rent')

    if request.method == 'GET': #注：到这里已经能成功访问../api/searchhouselist/?
        #开始：对data进行序列化，返回序列化后的对象
        serializer = HouseSerializer(house_list, many=True)

        #结束：对data进行序列化，返回序列化后的对象
        
        #开始：对序列化后的对象进行处理（校验，加工，返回等）
        return Response(serializer.data)

        #结束：对序列化后的对象进行处理
