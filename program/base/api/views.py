from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from django.http import HttpResponse


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/createrooms',
        'POST /api/updaterooms/:id',
        'DELETE /api/deleterooms/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def createRoom(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Item succsesfully create!')
    return Response({
        "image_id": 1,
        "name": "tom",
        "birthday": "2000/01/01",
        "sex": "m",
        "temperature": 36.0,
        "weight": 55.0,
        "height": 180.0,
        "pressures": 55,
        "pressured": 55
    })
	#serializer = RoomSerializer(data=request.data)

	#if serializer.is_valid():
		#serializer.save()

	#return Response(serializer.data)


@api_view(['POST', 'GET'])
def updateRoom(request, pk):
	#room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(instance=room, data=request.data)
        #serializer = RoomSerializer(room, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response('Item succsesfully update!')
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
	#serializer = RoomSerializer(instance=room, data=request.data)

	#if serializer.is_valid():
		#serializer.save()

	#return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def deleteRoom(request, pk):
	#room = Room.objects.get(id=pk)
	#room.delete()
    if request.method == 'DELETE':
        room = Room.objects.get(id=pk)
        room.delete()
        return Response('Item succsesfully delete!')
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

	#return Response('Item succsesfully delete!')
