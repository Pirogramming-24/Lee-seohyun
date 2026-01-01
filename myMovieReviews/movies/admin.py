from django.contrib import admin #admin기능 가져오기
from .models import Movie #movies->models.py에 있는 movie모델 가져오기
admin.site.register(Movie) #movie관리자 사이트에 등록