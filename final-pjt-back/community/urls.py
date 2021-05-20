from django.urls import path
from .views import ReviewView, MovieReview, CommentView, ReviewComment


urlpatterns = [
    path('movie/<int:movie_id>/', MovieReview.as_view()),
    path('review/<int:review_id>/', ReviewView.as_view()),
    path('comment/<int:comment_id>/', CommentView.as_view()),
    path('review/<int:review_id>/comment', ReviewComment.as_view()),
]
