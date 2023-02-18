"""stripe_buy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from stripe_buy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>', views.ItemView.as_view(), name='get_item'),
    path('buy/<int:pk>', views.BuyItemView.as_view(), name='buy_item'),
    path('order/<int:pk>', views.OrderView.as_view(), name='get_order'),
    path('buy-order/<int:pk>', views.OrderBuyView.as_view(), name='buy_order')
]
