from django.contrib import admin
from django.urls import path

from . import views

app_name = "bank_detail_finder_app"
urlpatterns = [
    path('',views.AppHome.as_view(),name="appHome"),
    path('branch/<str:ifsc_code>', views.BranchView.as_view(), name="branch"),
    path('branches/', views.BranchListView.as_view(), name="branches"),
    path('getbanks/', views.getbanks, name="getbanks"),
    # path('docs/api_spec(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('docs/redoc/',  schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
