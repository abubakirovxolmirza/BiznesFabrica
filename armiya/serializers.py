from rest_framework import serializers
from .models import Tranzaksiya,  Tasks, HistoryBalls, Buyum, Auktsion, Balls, TaskUsers, VAB, Price, Yangiliklar, Talablar, Sh_rivojlanish, BuyumUsers
from users.models import CustomUser

# class UsersTasksSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'profile_photo')
class VABSeralizers(serializers.ModelSerializer):
    class Meta:
        model = VAB
        fields = '__all__'

class TranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranzaksiya
        fields = '__all__'

class YangiliklarSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = '__all__'

class TalablarSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Talablar
        fields = '__all__'

class ShRSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Sh_rivojlanish
        fields = '__all__'

class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
 
class TaskUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUsers
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
        
class BuyumUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyumUsers
        fields = '__all__'
# class HtasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Htasks
#         fields = '__all__'
