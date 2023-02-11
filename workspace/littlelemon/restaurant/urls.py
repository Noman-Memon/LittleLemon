#define URL route for index() view
from django.urls import path
from . import views
# from rest_framework import routers

# routers.DefaultRouter.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingViewSet.as_view()),
    ]
