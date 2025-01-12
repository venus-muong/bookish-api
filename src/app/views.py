from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import VisionBoard
from rest_framework import status
from app.serializers import VisionBoardSerializer


@api_view(['GET', 'POST', 'PUT'])
def view_vision_board(request):
    if request.method == 'GET':
        vb_obj = VisionBoard.objects.last()
        serializer = VisionBoardSerializer(vb_obj)
        return Response({'msg': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = VisionBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        vb_obj = VisionBoard.objects.get(pk=request.data.get('id'))
        serializer = VisionBoardSerializer(vb_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

