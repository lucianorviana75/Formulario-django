

from django.contrib import admin
from django.urls import path
from controles_gastos import views
from controles_gastos.views import home1,listagem,nova_transação,update,delete





urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/', home1),
    path('', listagem, name='url_listagem'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/',views.delete, name='url_delete'),
    path('nova/', nova_transação, name='url_nova')

]  
