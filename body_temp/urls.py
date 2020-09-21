from django.urls import path

from .views import (
    BodyTempDayArchiveView,
    BodyTempTodayArchiveView,
    BodyTempCreateView,
    BodyTempUpdateView,
    BodyTempDeleteView,
)

app_name = 'body_temp'

urlpatterns = [
    path('body_temp/<int:pk>/delete',
         BodyTempDeleteView.as_view(),
         name='delete'),
    path('body_temp/<int:pk>/edit/',
         BodyTempUpdateView.as_view(),
         name='edit'),
    path('body_temp/new',
         BodyTempCreateView.as_view(),
         name='new'),
    path('<int:year>/<int:month>/<int:day>',
         BodyTempDayArchiveView.as_view(),
         name='day'),
    path('',
         BodyTempTodayArchiveView.as_view(),
         name='today'),
]