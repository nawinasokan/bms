from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def test_view(request):
    return HttpResponse("DJANGO ROUTING WORKS")
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('dashboard.urls')),
#     path('accounts/', include('accounts.urls')),
#     path('customers/', include('customers.urls')),
#     path('products/', include('products.urls')),
#     path('orders/', include('orders.urls')),

# ]
