from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Auktsion, Buyum, Tasks, HistoryBalls, Balls
from .serializers import AuktsionSerializer, BuyumTaskssSerializer, TasksSerializer, HistoryBallsSerializer, BallsSerializer
from rest_framework import permissions

# Create your views here.


class AuktsionCreateListView(ListCreateAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# class HtasksCreateListView(ListCreateAPIView):
#     queryset = Htasks.objects.all()
#     serializer_class = HtasksSerializer
    
    
class BuyumCreateListView(ListCreateAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class TasksCreateListView(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class HistoryBallsCreateListView(ListCreateAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# class HistoryTasksCreateListView(ListCreateAPIView):
#     queryset = HistoryTasks.objects.all()
#     serializer_class = HistoryTasksSerializer
    
    
class BallsTasksCreateListView(ListCreateAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    

class AuktsionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BuyumDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Buyum.objects.all()
    serializer_class = BuyumTaskssSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class HistoryBallsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HistoryBalls.objects.all()
    serializer_class = HistoryBallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# class HistoryTasksDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = HistoryTasks.objects.all()
#     serializer_class = HistoryTasksSerializer
    
    
class BallsTasksDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
# class HtasksDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Htasks.objects.all()
#     serializer_class = HtasksSerializer
    
class DoneTasksListView(ListAPIView):
    serializer_class = TasksSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tasks.objects.filter(status='Done')
    