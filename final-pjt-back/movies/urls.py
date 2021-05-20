from django.urls import path
from .views import CollectionView, CollectionListView

urlpatterns = [
    path('collection/<int:collection_id>/', CollectionView.as_view()),
    path('collection_list/', CollectionListView.as_view()),
]
