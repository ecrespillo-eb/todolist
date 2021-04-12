from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListTodoView.as_view(), name='list_todo'),
    path('create/', views.CreateTodoView.as_view(), name='create_todo'),
    path('<pk>/update/', views.UpdateTodoView.as_view(), name='update_todo'),
    path('<pk>/update-user/', views.UpdateAssignedUser.as_view(), name='update_user'),
    path('<pk>/delete/', views.DeleteTodoView.as_view(), name='delete_todo'),
]
