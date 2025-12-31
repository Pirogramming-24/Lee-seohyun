
from django.contrib import admin #admin기본관리자기능 을 쓰기위해 가져옴
from django.urls import path,include #path->이 주소로 오면 여기로 보내라. #include:다른urls.py에 넘겨라
from django.shortcuts import redirect

def home(request):
    return redirect("/movies")

urlpatterns = [ #url규칙
    path('admin/', admin.site.urls),
    path("",home),
    path("movies/",include("movies.urls") ), #나머지 모든주소처리->mocies앱에게 맡기ㅣ
]
