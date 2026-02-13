from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
]

# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
