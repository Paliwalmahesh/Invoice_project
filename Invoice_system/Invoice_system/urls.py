"""Invoice_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from posts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_invoice,name='addinvoice'),
    path('Add_Item/<str:Invoice_Id>',views.Add_Item,name="Add_Item"),
    path('update_Items/<str:pk>/', views.updateItems, name="update_Items"),
    path('delete_Items/<str:pk>/', views.deleteItems, name="delete_Items"),
    path('render_pdf_view/<str:Invoice_Id>',views.render_pdf_view,name="render_pdf_view"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
