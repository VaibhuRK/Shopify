from django.urls import path
from seller import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard),
    path('add/', views.add_product),
    path('delete/<product_id>', views.delete_product),
    path('update/<product_id>', views.update_product),
    path('products/', views.view_products),
    
    

    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)