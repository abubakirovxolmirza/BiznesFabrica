from rest_framework import serializers
from .models import Tasks, HistoryBalls, Buyum, Auktsion, Balls

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
    

class HistoryBallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryBalls
        fields = '__all__'


# class HistoryTasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HistoryTasks
#         fields = '__all__'


class BuyumTaskssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyum
        fields = '__all__'


class AuktsionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auktsion
        fields = '__all__'
        
        
class BallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balls
        fields = '__all__'
        

# class HtasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Htasks
#         fields = '__all__'