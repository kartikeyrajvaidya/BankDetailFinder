from django.contrib import admin
from django.urls import path

from . import views

app_name = "bank_detail_finder_app"
urlpatterns = [
    path('',views.AppHome.as_view(),name="appHome"),
    path('branch/<str:ifsc_code>', views.BranchView.as_view(), name="branch"),
    path('branches/', views.BranchListView.as_view(), name="branches"),
]
