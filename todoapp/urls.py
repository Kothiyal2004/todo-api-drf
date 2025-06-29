from django.urls import path
from .views import get_all_todos, add_todo, update_todo,delete_todo, patch_todo
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', get_all_todos),
    path('add/', add_todo),
    path('update_todo/<int:id>/',update_todo, name='update_todo'),   # PUT
    path('delete_todo/<int:id>/',delete_todo, name='delete_todo'),   # DELETE
    path('patch_todo/<int:id>/', patch_todo, name='patch_todo'),      # PATCH
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
    path('todos/', get_all_todos),  # your protected API

]


