from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Auktsion, Buyum, Tasks, HistoryBalls, Balls, TaskUsers, VAB, Price, Sh_rivojlanish, Talablar, Yangiliklar
from .serializers import VABSeralizers, PriceSerializers, AuktsionSerializer, BuyumTaskssSerializer, TasksSerializer, HistoryBallsSerializer, BallsSerializer, TaskUsersSerializer, YangiliklarSeralizers, TalablarSeralizers, ShRSeralizers
from rest_framework import permissions
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.response import Response
# Create your views here.


class TalablarCreateListView(ListCreateAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalablarSeralizers
    permission_classes = [permissions.IsAuthenticated]

class YangiliklarCreateListView(ListCreateAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSeralizers
    permission_classes = [permissions.IsAuthenticated]

class ShRCreateListView(ListCreateAPIView):
    queryset =Sh_rivojlanish .objects.all()
    serializer_class = ShRSeralizers
    permission_classes = [permissions.IsAuthenticated]

class AuktsionCreateListView(ListCreateAPIView):
    queryset = Auktsion.objects.all()
    serializer_class = AuktsionSerializer
    permission_classes = [permissions.IsAuthenticated]

class VABCreateListView(ListCreateAPIView):
    queryset = VAB.objects.all()
    serializer_class = VABSeralizers
    permission_classes = [permissions.IsAuthenticated]
    
class PriceCreateListView(ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializers
    permission_classes = [permissions.IsAuthenticated]
    
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import TaskUsers
from .serializers import TaskUsersSerializer
from users.models import CustomUser

class TaskUsersListView(ListAPIView):
    queryset = TaskUsers.objects.all()
    serializer_class = TaskUsersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Modify serializer data to include profile_photo, first_name, last_name
        data = serializer.data
        for item in data:
            # Fetch related CustomUser instances
            users_data = item.get('users', [])
            users = []
            for user_id in users_data:
                user_instance = CustomUser.objects.get(id=user_id)
                user_data = {
                    'id': user_instance.id,
                    'first_name': user_instance.first_name,
                    'profile_photo': user_instance.profile_photo.url if user_instance.profile_photo else None,
                }
                users.append(user_data)

            item['users'] = users

        return Response(data)

    
    
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
    
class TaskUsersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TaskUsers.objects.all()
    serializer_class = TaskUsersSerializer
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

class VABDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Balls.objects.all()
    serializer_class = BallsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PriceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializers
    permission_classes = [permissions.IsAuthenticated]

class YangiliklarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSeralizers
    permission_classes = [permissions.IsAuthenticated]


class TalablarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Talablar.objects.all()
    serializer_class = TalablarSeralizers
    permission_classes = [permissions.IsAuthenticated]


class ShRDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sh_rivojlanish.objects.all()
    serializer_class = ShRSeralizers
    permission_classes = [permissions.IsAuthenticated]
