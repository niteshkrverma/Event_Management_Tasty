"""Event_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Tasty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashboard),
    path('home/',views.index),
    path('singup/',views.sign_up,name='singup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.User_logout,name='logout'),
    path('menu/',views.menu),
    path('event',views.event),
    path('about',views.about),
    path('aboutus',views.aboutus),
    path('service',views.service),
    path('contact/',views.contact),
    path('booking',views.booking),
    path('bookingstatus',views.booking_status),
    path('delete_booking/<int:pk>', views.delete_booking,name='delete_booking'),
    # admin
    path('admin_dashboard',views.admin_dashboard),
    path('customer_view',views.customer_view),
    path('delete_customer_view/<int:pk>', views.delete_customer_view,name='delete_customer_view'),
    path('contactlist',views.contact_views),
    path('delete_contact_list/<int:pk>', views.delete_contact_list,name='delete_contact_list'),
    path('admin_menu/',views.admin_menu),
    path('admin_event',views.admin_event),
    path('view_booking',views.view_booking),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),
    
    
]
