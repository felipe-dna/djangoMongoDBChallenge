from django.urls import path
from .views import (
    HomeView,
    WatchVideoView,
    uploadView,
    ThemeDetailView,
    thumbUp,
    thumbDown
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('watch/<uuid:pk>/', WatchVideoView.as_view(), name='watch'),
    path('theme/<uuid:pk>/', ThemeDetailView.as_view(), name='theme'),
    path('upload/', uploadView, name='upload' ),

    # thumb up and thumb down views
    path('thumb-up/<uuid:pk>/', thumbUp, name='thumbUp'),
    path('thumb-down/<uuid:pk>/', thumbDown, name='thumbDown'),

]
