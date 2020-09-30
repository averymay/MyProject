from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'product'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('index', views.ProductIndexView.as_view(), name="index_view"),
    path('registration', views.ProductRegisterView.as_view(), name="registration_view"),
]