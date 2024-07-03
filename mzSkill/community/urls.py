from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('', community, name='community'),

    path('create_post/', create_post, name='create_post'),
    path('create_comment/<int:id>/', create_comment, name='create_comment'),

    path('post_detail/<int:id>/', post_detail, name='post_detail'),

    # 다대다 좋아요 경로
    path('add_like/<int:post_id>/', add_like, name ="add_like"),
    path('remove_like/<int:post_id>/', remove_like, name ="remove_like"),
    #게시글 삭제
    path('delete_post/<int:id>', delete_post, name = 'delete_post'),
    # 댓글 삭제
    path('delete_comment/<int:id>', delete_comment, name = "delete_comment"),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),  # 게시글 수정 URL 패턴 추가
]