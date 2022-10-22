from curses.ascii import US
from rest_framework import viewsets,  status
from rest_framework.decorators import action
from .models import User
from . import serializers
from rest_framework.response import Response
from .mlFunctions import showData


# Create your views here.

class MlView(viewsets.ModelViewSet):
    serializer_class = serializers.MonitorSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'])
    def saveLog(self, request):
        try:
            return Response(showData(request), status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
