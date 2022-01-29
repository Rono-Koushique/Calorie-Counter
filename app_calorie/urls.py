from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='calorie-index'),
    path('delete/<int:id>/', views.delete_consume, name='calorie-delete'),
    path('account-reset/', views.account_reset, name='calorie-account-reset'),
    path('food-data/', views.food_data, name='calorie-food-data')
]