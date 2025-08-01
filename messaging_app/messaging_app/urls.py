# messaging_app/urls.py

from django.contrib import admin
from django.urls import path, include
from messaging_app.chats import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', auth.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', auth.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/chats/', include('messaging_app.chats.urls')),  # if your chats app has its own URLs
]
