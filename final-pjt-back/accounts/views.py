from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


class UserView(APIView):

    def get(self, request, username):
        person = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(person)
        return Response(serializer.data)
    
    def post(self, request, username):
        person = get_object_or_404(get_user_model(), username=username)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
                followed = False
            else:
                person.followers.add(request.user)
                followed = True
            follow_status = {
            'followed' : followed,
            'count' : person.followers.count(),
        }
            return Response(follow_status)
        return Response({'detail': '자신을 팔로우할 수 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)



class UserCDView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')
            
        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def delete(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
