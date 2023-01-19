from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', signup_user, name='signupuser'),
    path('login/', login_user, name='loginuser'),
    path('logout/', logout_user, name='logoutuser'),

    # Todos
    path('', home, name='home'),
    path('create/', create_todo, name='createtodo'),
    path('current/', current_todos, name='currenttodos'),
    path('completed/', completed_todos, name='completedtodos'),
    path('todo/<int:todo_pk>', view_todo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', complete_todo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', delete_todo, name='deletetodo'),
]
