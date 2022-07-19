import json
import base64
from urllib import request, response
from django.shortcuts import render
from rest_framework import status

# Create your views here.
from .models import BikeDetail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bike_app.serializers import BikeDetailSerializer,BikeDetailDataSerializer, decode_bike_number
from drf_yasg.utils import swagger_auto_schema

def index(request):
    return Response("welcome to index page")

class BikeDetailView(APIView):
    serialzer_class = BikeDetailSerializer
    @swagger_auto_schema(responses={200: BikeDetailSerializer(many=True)})
    def get(self,request,format=None):
        try:
            return Response("welcome")
        except Exception as e:
            return Response({'error':str(e)},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=BikeDetailSerializer)
    def post(self, request):
        try:
            serializer = BikeDetailSerializer(data=request.data) #1
            if serializer.is_valid():
                result, bike_num = decode_bike_number(request.data.get('bike_number'))
                obj = BikeDetail.objects.filter(bike_number = bike_num).last()
                ser = BikeDetailDataSerializer(obj) #2
                return Response({'result':True,'message':'success','data':ser.data}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.utils.encoding import smart_text
from rest_framework import renderers
class PlainTextRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    format = 'txt'
    charset = 'iso-8859-1'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data.encode(self.charset)