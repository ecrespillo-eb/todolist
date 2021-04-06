"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist_app import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', todo_views.CreateTodoView.as_view(), name='create_todo'),
    path('create-priority/', todo_views.CreatePriorityView.as_view(), name='create_priority'),
    path('<pk>/update/', todo_views.UpdateTodoView.as_view(), name='update_todo'),
    path('<pk>/update-user/', todo_views.UpdateAssignedUser.as_view(), name='update_user'),
    path('<pk>/delete/', todo_views.DeleteTodoView.as_view(), name='delete_todo'),
    path('', todo_views.ListTodoView.as_view(), name='list_todo'),
]