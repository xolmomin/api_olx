from django.urls import path, include

urlpatterns = [
    path('adverts/', include('adverts.urls')),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),

]
