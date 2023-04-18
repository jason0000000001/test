from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import User
from base.models import Data
from base.models import Medicine
from .serializers import UserSerializer
from .serializers import DataSerializer
from .serializers import MedicineSerializer
from .serializers import DataweightSerializer
from .serializers import DatatemperatureSerializer
from .serializers import DatapressuredSerializer
from .serializers import DatapressuresSerializer
from .serializers import DataheartbeatSerializer
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from datetime import timezone
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly
from plotly.graph_objs import Scatter,Layout,Figure
import plotly.graph_objs as go
from django.db.models import Q
from datetime import timedelta
from plotly.subplots import make_subplots


@api_view(['GET'])
def gethistory(request, pk):
    #user = User6.objects.get(name=pk)
    #serializer1 = UserSerializer(user, many=False)
    #id = serializer1.data["id"]
    rooms = Data.objects.filter(userid=pk)
    serializer = DataSerializer(rooms, many=True)
    num=len(rooms)
    c_data=[]
    x_data=[]
    y_data=[]
    t_data=[]
    ps_data=[]
    pd_data=[]
    h_data=[]
    i = 0
    while i < num:
        c_data+=[rooms[i].createtime]#日期寫入[]
        x_data+=[rooms[i].createtime + timedelta(hours = 8)]#日期+8寫入[]
        y_data+=[rooms[i].weight]#體重寫入[]
        t_data+=[rooms[i].temperature]#溫度寫入[]
        ps_data+=[rooms[i].pressures]#收縮壓寫入[]
        pd_data+=[rooms[i].pressured]#舒張壓寫入[]
        h_data+=[rooms[i].heartbeat]#心跳寫入[]
        i=i+1
    print(c_data)
    print(x_data)
    print(y_data)
    print(t_data)
    print(ps_data) 
    print(pd_data) 
    print(h_data) 
    '''
    plt.plot( y_date, color='red', marker="o")
    plt.xlabel('rooms') # 設定 x 軸標題
    plt.ylabel('weight') # 設定 y 軸標題
    plt.show()
    '''

    trace1 = Scatter(
    x=x_data , y=y_data , mode='markers+lines',
    name='體重' , marker_color = 'black'
    )
    trace2 = Scatter(
    x=x_data , y=t_data , mode='markers+lines',
    name='體溫' , marker_color = 'blue'
    )
    trace3 = Scatter(
    x=x_data , y=ps_data , mode='markers+lines',
    name='收縮壓' , marker_color = 'red'
    )
    trace4 = Scatter(
    x=x_data , y=pd_data , mode='markers+lines',
    name='舒張壓' , marker_color = 'green'
    )
    trace5 = Scatter(
    x=x_data , y=h_data , mode='markers+lines',
    name='心跳' , marker_color = 'yellow'
    )
    '''
    trace3 = go.Bar(
        x=x_date, y=ps_date , name='收縮壓'
    )

    trace4 = go.Bar(
        x=x_date, y=pd_date , name='舒張壓'
    )
    '''
    data=[trace1]
    data1=[trace2]
    data2=[trace3,trace4]
    data3=[trace5]
    data_all=[trace1,trace2,trace3,trace4,trace5]
    #體重折線圖
    layout = Layout(title='歷史體重', xaxis_title='創建時間')
    fig = Figure(data = data, layout = layout)
    plot_graph_weight=plot(fig,validate=False,output_type='div',image_width=200,image_height=400)
    #體溫折線圖
    layout = Layout(title='歷史體溫', xaxis_title='創建時間')
    fig = Figure(data = data1, layout = layout)
    plot_graph_temperature=plot(fig,validate=False,output_type='div',image_width=200,image_height=400)
    #血壓折線圖
    layout = Layout( title='歷史血壓', xaxis_title='創建時間' )
    fig = Figure(data = data2, layout=layout)
    plot_graph_pressure=plot(fig,validate=False,output_type='div',image_width=200,image_height=400)
    #心跳折線圖
    layout = Layout( title='歷史心跳', xaxis_title='創建時間' )
    fig = Figure(data = data3, layout=layout)
    plot_graph_heartbeat=plot(fig,validate=False,output_type='div',image_width=200,image_height=400)
    #全部
    layout = Layout( title='全部歷史記錄', xaxis_title='創建時間' )
    fig = Figure(data = data_all, layout=layout)
    plot_graph_all=plot(fig,validate=False,output_type='div',image_width=200,image_height=400)
    if rooms:
        return render(request,'history.html',context={'plot_graph_weight' : plot_graph_weight,'plot_graph_temperature' : plot_graph_temperature,'plot_graph_pressure' : plot_graph_pressure,'plot_graph_heartbeat' : plot_graph_heartbeat,'plot_graph_all' : plot_graph_all,'rooms':rooms})
    else:
        return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET,POST /api/users/',
        'GET,POST,DELETE /api/users/:id/',
        'GET,POST /api/datas/',
        'GET,POST,DELETE /api/datas/:id/',
        'GET,POST /api/:userid/medicine/',
        'GET /api/datasid/:userid/',
        'GET /api/:userid/weight/',
        'GET /api/:userid/temperature/',
        'GET /api/:userid/pressures/',
        'GET /api/:userid/pressured/',
        'GET /api/:userid/heartbeat/',
        'GET /api/datastime/:userid/:start_time/:end_time/',
        'start_time,end_time格式:YYYY-MM-DD或YYYY-MM-DDTHH-MM-SS',
        'GET /api/history/:id/',
    ]
    return Response(routes)


@api_view(['POST', 'GET'])
def Users(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User succsesfully create!')
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET', 'DELETE'])
def updateUser(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User succsesfully update!')
    elif request.method == 'DELETE':
        user = User.objects.get(id=pk)
        user.delete()
        return Response('User succsesfully delete!')
    else:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def createmedicine(request,pk):
    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Medicine succsesfully create!')
    else:
        medicine = Medicine.objects.filter(userid=pk)
        serializer = MedicineSerializer(medicine, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getDataid(request, pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DataSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getweight(request,pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DataweightSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def gettemperature(request,pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DatatemperatureSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getpressures(request,pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DatapressuresSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getpressured(request,pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DatapressuredSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getheartbeat(request,pk):
    rooms = Data.objects.filter(userid=pk)
    serializer = DataheartbeatSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoomtime(request, pk, sk, ek):
    rooms = Data.objects.filter(userid=pk)
    serializer = DataSerializer(rooms, many=True)
    times = Data.objects.filter(Q(createtime__gte=sk) & Q(createtime__lte=ek), userid=id )
    serializer2 = DataSerializer(times, many=True)
    return Response(serializer2.data)


@api_view(['POST', 'GET'])
def createData(request):
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            userid = serializer.validated_data['userid']
            weight = serializer.validated_data['weight']
            temperature = serializer.validated_data['temperature']
            pressures = serializer.validated_data['pressures']
            pressured = serializer.validated_data['pressured']
            heartbeat = serializer.validated_data['heartbeat']
            bmi = serializer.validated_data['bmi']
            bmr = serializer.validated_data['bmr']
            result1 = serializer.validated_data['result1']
            result2 = serializer.validated_data['result2']
            result3 = serializer.validated_data['result3']
            result4 = serializer.validated_data['result4']
            updatetime = datetime.datetime.now()
            year_now = updatetime.year
            print(updatetime)
            print(year_now)
            user = User.objects.get(name=userid)
            serializer1 = UserSerializer(user, many=False)
            height = serializer1.data['height']
            sex = serializer1.data['sex']
            birthday = serializer1.data['birthday']
            birthday1 = birthday.split('/')
            year = int(birthday1[0])
            month = int(birthday1[1])
            day = int(birthday1[2])
            age = year_now - year
            print(sex)
            print(age)
            print(temperature)
            print(height)
            print(weight)
            print(pressures)
            print(pressured)
            print(heartbeat)
            #BMI計算
            bmi = weight / (height/100.0) ** 2.0
            bmi = round(bmi, 1)
            serializer.validated_data['bmi'] = bmi
            print(bmi)
            #BMR計算
            if sex == "男"or"male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            print(bmr)
            #血壓建議
            if pressures>140.0:
                if pressured>90.0:
                    result1 = ('收縮血壓、擴張血壓數據偏高，勞煩您近期多注意自己的身體，有需要能前往醫院進行更精密的檢查')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('目前舒張壓正常但是收縮壓偏高喔，少吃油炸、精緻食物能幫住您減低血管硬化的風險喔')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮偏高、舒張偏低,請養成運動習慣,每次20到30分鐘,能幫助您降低血壓')
                    serializer.validated_data['result1'] = result1
            elif pressures>100.0:
                if pressured>90.0:
                    result1 = ('收縮血壓正常、舒張壓數據偏高，勞煩您近期多注意自己的身體，有需要能前往醫院進行更精密的檢查')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('恭喜你非常健康，請保持目前的生活作息，能使你更有活力喔')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮壓正常、舒張壓偏低，若有頭暈現象可能是低血壓前兆喔。')
                    serializer.validated_data['result1'] = result1
            else:
                if pressured>90.0:
                    result1 = ('收縮血壓偏低、舒張壓數據偏高，最近工作很勞累喔，請多多活動身體，讓自己喘口氣吧')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('收縮壓偏低、舒張正常，請規律生活及運動')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮壓偏低、舒張壓偏低小心有休克、低血壓的危機喔，請密切觀察盡早處理。')
                    serializer.validated_data['result1'] = result1
            #體溫建議
            if temperature >38.0:
                result2 = ('體溫過高，請盡速前往醫院做盡一步檢查')
                serializer.validated_data['result2'] = result2
            elif temperature >37.0:
                result2 = ('體溫稍微偏高喔，多注意身體狀況')
                serializer.validated_data['result2'] = result2
            else:
                result2 = ("體溫在正常範圍內，但請不要忘記戴口罩防範Covid-19喔")
                serializer.validated_data['result2'] = result2
            #心跳建議
            if heartbeat > 80:
                result3 = ('心跳過快')
                serializer.validated_data['result3'] = result3
            elif heartbeat < 60:
                result3 = ('心跳過慢')
                serializer.validated_data['result3'] = result3
            else:
                result3 = ('正常心跳')
                serializer.validated_data['result3'] = result3
            #BMI建議
            if bmi >= 35.0:
                result4 = ('重度肥胖')
                serializer.validated_data['result4'] = result4
            elif 35.0 > bmi >= 30.0:
                result4 = ('中度肥胖')
                serializer.validated_data['result4'] = result4
            elif 30.0 > bmi >= 27.0:
                result4 = ('輕度肥胖')
                serializer.validated_data['result4'] = result4
            elif 27.0 > bmi >= 24.0:
                result4 = ('過重')
                serializer.validated_data['result4'] = result4
            elif 24.0 > bmi >= 18.5:
                result4 = ('健康體重')
                serializer.validated_data['result4'] = result4
            else:
                result4 = ("體重過輕")
                serializer.validated_data['result4'] = result4
            print(result1)
            print(result2)
            print(result3)
            print(result4)
            serializer.save()
            return Response('Item succsesfully create!')
    else:
        rooms = Data.objects.all()
        serializer = DataSerializer(rooms, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET', 'DELETE'])
def updateData(request, pk):
    if request.method == 'POST':
        room = Data.objects.get(id=pk)
        serializer = DataSerializer(instance=room, data=request.data)
        if serializer.is_valid():
            userid = serializer.validated_data['userid']
            weight = serializer.validated_data['weight']
            temperature = serializer.validated_data['temperature']
            pressures = serializer.validated_data['pressures']
            pressured = serializer.validated_data['pressured']
            heartbeat = serializer.validated_data['heartbeat']
            bmi = serializer.validated_data['bmi']
            bmr = serializer.validated_data['bmr']
            result1 = serializer.validated_data['result1']
            result2 = serializer.validated_data['result2']
            result3 = serializer.validated_data['result3']
            result4 = serializer.validated_data['result4']
            updatetime = datetime.datetime.now()
            year_now = updatetime.year
            print(updatetime)
            print(year_now)
            user = User.objects.get(name=userid)
            serializer1 = UserSerializer(user, many=False)
            height = serializer1.data['height']
            sex = serializer1.data['sex']
            birthday = serializer1.data['birthday']
            birthday1 = birthday.split('/')
            year = int(birthday1[0])
            month = int(birthday1[1])
            day = int(birthday1[2])
            age = year_now - year
            print(sex)
            print(age)
            print(height)
            print(weight)
            #BMI計算
            bmi = weight / (height/100.0) ** 2.0
            bmi = round(bmi, 1)
            serializer.validated_data['bmi'] = bmi
            print(bmi)
            #BMR計算
            if sex == "男"or"male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            print(bmr)
            #血壓建議
            if pressures>140.0:
                if pressured>90.0:
                    result1 = ('收縮血壓、擴張血壓數據偏高，勞煩您近期多注意自己的身體，有需要能前往醫院進行更精密的檢查')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('目前舒張壓正常但是收縮壓偏高喔，少吃油炸、精緻食物能幫住您減低血管硬化的風險喔')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮偏高、舒張偏低,請養成運動習慣,每次20到30分鐘,能幫助您降低血壓')
                    serializer.validated_data['result1'] = result1
            elif pressures>100.0:
                if pressured>90.0:
                    result1 = ('收縮血壓正常、舒張壓數據偏高，勞煩您近期多注意自己的身體，有需要能前往醫院進行更精密的檢查')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('恭喜你非常健康，請保持目前的生活作息，能使你更有活力喔')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮壓正常、舒張壓偏低，若有頭暈現象可能是低血壓前兆喔。')
                    serializer.validated_data['result1'] = result1
            else:
                if pressured>90.0:
                    result1 = ('收縮血壓偏低、舒張壓數據偏高，最近工作很勞累喔，請多多活動身體，讓自己喘口氣吧')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('收縮壓偏低、舒張正常，請規律生活及運動')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('收縮壓偏低、舒張壓偏低小心有休克、低血壓的危機喔，請密切觀察盡早處理。')
                    serializer.validated_data['result1'] = result1
            #體溫建議
            if temperature >38.0:
                result2 = ('體溫過高，請盡速前往醫院做盡一步檢查')
                serializer.validated_data['result2'] = result2
            elif temperature >37.0:
                result2 = ('體溫稍微偏高喔，多注意身體狀況')
                serializer.validated_data['result2'] = result2
            else:
                result2 = ("體溫在正常範圍內，但請不要忘記戴口罩防範Covid-19喔")
                serializer.validated_data['result2'] = result2
            #心跳建議
            if heartbeat > 80:
                result3 = ('心跳過快')
                serializer.validated_data['result3'] = result3
            elif heartbeat < 60:
                result3 = ('心跳過慢')
                serializer.validated_data['result3'] = result3
            else:
                result3 = ('正常心跳')
                serializer.validated_data['result3'] = result3
            #BMI建議
            if bmi >= 35.0:
                result4 = ('重度肥胖')
                serializer.validated_data['result4'] = result4
            elif 35.0 > bmi >= 30.0:
                result4 = ('中度肥胖')
                serializer.validated_data['result4'] = result4
            elif 30.0 > bmi >= 27.0:
                result4 = ('輕度肥胖')
                serializer.validated_data['result4'] = result4
            elif 27.0 > bmi >= 24.0:
                result4 = ('過重')
                serializer.validated_data['result4'] = result4
            elif 24.0 > bmi >= 18.5:
                result4 = ('健康體重')
                serializer.validated_data['result4'] = result4
            else:
                result4 = ("體重過輕")
                serializer.validated_data['result4'] = result4
            print(result1)
            print(result2)
            print(result3)
            print(result4)
            serializer.save()
            return Response('Item succsesfully update!')
    elif request.method == 'DELETE':
        room = Data.objects.get(id=pk)
        room.delete()
        return Response('Item succsesfully delete!')
    else:
        room = Data.objects.get(id=pk)
        serializer = DataSerializer(room, many=False)
        return Response(serializer.data)

