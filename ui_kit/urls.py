from django.urls import path
from . import views

urlpatterns = [
    path("", views.ui_kit_index, name="ui_kit_index"),
    path("<int:pk>/", views.ui_kit_detail, name="ui_kit_detail"),
    path("<category>/", views.ui_kit_category, name="ui_kit_category"),
]
