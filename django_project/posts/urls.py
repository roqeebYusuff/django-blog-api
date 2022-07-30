from operator import imod
from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import PostDetail,PostList,UserDetail,UserList
from .views import PostViewSet, UserViewSet

# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>/", UserDetail.as_view()), 
#     path('<int:pk>/', PostDetail.as_view(), name="post_detail"),
#     path('', PostList.as_view(), name="post_list"),
# ]

# For VIewsets
router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
