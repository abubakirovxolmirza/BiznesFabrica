from django.urls import path
from .views import VABListView, TranCreateListView, TranDetailView,  BuyumUsersCreateListView,  ShRCreateListView, YangiliklarCreateListView, TalablarCreateListView, VABCreateListView, VABDetailView, PriceCreateListView, PriceDetailView, TaskUsersDetailView, TaskUsersListView, DoneTasksListView, BallsTasksCreateListView, BallsTasksDetailView, AuktsionCreateListView, AuktsionDetailView, TasksCreateListView, TasksDetailView, HistoryBallsCreateListView, HistoryBallsDetailView, BuyumCreateListView, BuyumDetailView, ShRDetailView, YangiliklarDetailView, TalablarDetailView, BuyumUsersDetailView

urlpatterns = [
    path('vabkey', VABListView.as_view()),
    path('auktsion', AuktsionCreateListView.as_view()),
    path('balls', BallsTasksCreateListView.as_view()),
    path('tasks', TasksCreateListView.as_view()),
    path('hballs', HistoryBallsCreateListView.as_view()),
    # path('htasks', HistoryTasksCreateListView.as_view()),
    path('buyum', BuyumCreateListView.as_view()),
    path('auktsion/<int:pk>', AuktsionDetailView.as_view()),
    path('tasks/<int:pk>', TasksDetailView.as_view()),
    path('hballs/<int:pk>', HistoryBallsDetailView.as_view()),
    # path('htasks/<int:pk>', HistoryTasksDetailView.as_view()),
    path('buyum/<int:pk>', BuyumDetailView.as_view()),
    path('balls/<int:pk>', BallsTasksDetailView.as_view()),
    path('task-dones', DoneTasksListView.as_view()),
    path('taskusers', TaskUsersListView.as_view()),
    path('taskusers/<int:pk>', TaskUsersDetailView.as_view()),
    path('price', PriceCreateListView.as_view()),
    path('price/<int:pk>', PriceDetailView.as_view()),
    path('vab', VABCreateListView.as_view()),
    path('vab/<int:pk>', VABDetailView.as_view()),
    path('ShRivoj',ShRCreateListView .as_view()),
    path('yangiliklar', YangiliklarCreateListView.as_view()),
    path('talablar', TalablarCreateListView.as_view()),
    path('Shrivoj/<int:pk>', ShRDetailView.as_view()),
    path('yangiliklar/<int:pk>', YangiliklarDetailView.as_view()),
    path('talablar/<int:pk>', TalablarDetailView.as_view()),
    path('buyumusers', BuyumUsersCreateListView.as_view()),
    path('buyumusers/<int:pk>', BuyumUsersDetailView.as_view()),
    path('tranzaksiya', TranCreateListView.as_view()),
    path('tranzaksiya/<int:pk>', TranDetailView.as_view()),   
 ]
