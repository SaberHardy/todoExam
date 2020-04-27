from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.list_todo_items,name="todo_list"),
    path('signup/',views.signup,name='signup'),
    # path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout'),
    path('insert_into_list/',views.insert_into_list,name='insert_into_list'),
    path('delete_item/<int:todo_id>/',views.delete_item,name="delete_item"),
	path('edit/<int:id>/',views.edit,name="edit"),

    
]