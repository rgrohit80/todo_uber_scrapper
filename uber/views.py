from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Cab, Rider, Trip
from .serializers import CabSerializer, RiderSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics

"""
List all the cabs
Register a new cabs
"""


class ListCreateCab(APIView):
    def get(self, request):
        cabs = Cab.objects.all()
        serializer = CabSerializer(cabs, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = CabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


"""
- get a particular cab
- update that cab information
- delete the cab 
"""


class RetrieveUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            cab = Cab.objects.get(pk=pk)
            return cab
        except Cab.DoesNotExist:
            return Http404

    def get(self, request, pk):
        cab = self.get_object(pk)
        serializer = CabSerializer(cab)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request, pk):
        cab = self.get_object(pk)
        serializer = CabSerializer(cab, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cab = self.get_object(pk)
        cab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
List the rider
create the rider
"""


class ListCreateRider(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


"""
- get a particular rider
- update that rider information
- delete the rider 
"""


class RetrieveUpdateDeleteRider(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
