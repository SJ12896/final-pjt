from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from .views import UserCDView, UserView


urlpatterns = [
    path('user/', UserCDView.as_view()),
    path('<username>/', UserView.as_view()),
    path('api-token-auth/', obtain_jwt_token),
]
