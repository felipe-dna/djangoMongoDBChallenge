from django.urls import path
from .views import (
    HomeView,
    WatchVideoView,
    ThemeDetailView,
    ThemeListView,
    thumbUp,
    thumbDown,
    uploadView,
    createThemeView
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('watch/<uuid:pk>/', WatchVideoView.as_view(), name='watch'),
    path('themes/', ThemeListView.as_view(), name='themes'),
    path('themes/<uuid:pk>/', ThemeDetailView.as_view(), name='theme'),
    # View functions.
    path('upload/', uploadView, name='upload' ),
    path('create-theme/', createThemeView, name='create-theme' ),
    path('thumb-up/<uuid:pk>/', thumbUp, name='thumbUp'),
    path('thumb-down/<uuid:pk>/', thumbDown, name='thumbDown'),
]
