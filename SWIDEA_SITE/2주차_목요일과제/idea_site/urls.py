from django.urls import path
from . import views
#가지사이트들 등록..
app_name = "idea_site"

urlpatterns = [
    path("", views.idea_list, name="idea_list"),  # 메인(아이디어목록)
    path("ideas/new/", views.idea_create, name="idea_create"),
    path("ideas/<int:pk>/", views.idea_detail, name="idea_detail"),
    path("ideas/<int:pk>/edit/", views.idea_update, name="idea_update"),
    path("ideas/<int:pk>/delete/", views.idea_delete, name="idea_delete"),
    # DevTool
    path("devtools/", views.devtool_list, name="devtool_list"),
    path("devtools/new/", views.devtool_create, name="devtool_create"),
    path("devtools/<int:pk>/", views.devtool_detail, name="devtool_detail"),
    path("devtools/<int:pk>/edit/", views.devtool_update, name="devtool_update"),
    path("devtools/<int:pk>/delete/", views.devtool_delete, name="devtool_delete"),
    #찜
    path("ideas/<int:pk>/star/", views.idea_star_toggle, name="idea_star_toggle"),

]
