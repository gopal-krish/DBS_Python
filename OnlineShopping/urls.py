urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder')
]
