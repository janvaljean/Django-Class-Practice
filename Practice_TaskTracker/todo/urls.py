
from django.urls import path,include
from .views import welcome, todo_list_create, todo_update_delete

urlpatterns = [
   
    path('', welcome),
    #functions base view
    path('todos/', todo_list_create),
    
    
]
