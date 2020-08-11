from rest_framework.views import APIView
from .models import Task, Step
from .serializers import TaskSerializer, StepSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# class TaskListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()


class TaskListCreateAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.session.set_test_cookie()
        # print(request.session)
        # print(request.COOKIES)

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TaskGetUpdateDelete(APIView):

    def get_objects(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            return Http404

    def get(self, request, pk):
        task = self.get_objects(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self.get_objects(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_objects(pk)
        task.delete()
        return Response(status.HTTP_204_NO_CONTENT)
