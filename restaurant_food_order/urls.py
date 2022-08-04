from django.urls import path
from . import views

app_name = 'restaurant_food_order'

urlpatterns = [
    # start view
    path('', views.make_order, name='make_order'),
    path('order_list', views.order_list, name='order_list'),
    path('report', views.report_display, name='report')
]
