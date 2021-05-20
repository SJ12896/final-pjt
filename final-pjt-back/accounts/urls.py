from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import UserCDView, UserView


urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('user/', UserCDView.as_view()),
    path('<username>/detail/', UserView.as_view()),
]
