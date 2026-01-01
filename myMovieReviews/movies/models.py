from django.db import models #djang의db기능쓰기위한 도구상자 가져오기

class Movie(models.Model): #db테이블 만들때 필요한 부품들 불러오기(movie라는 이름의 설계도 만들기)
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(null=True, blank=True)   # 개봉년도(blank=True : 폼에서 입력안해도 통과가능/ null->DB레벨에서~..)
    score = models.FloatField(default=0)  # 점수
    review = models.TextField(blank=True)   # 후기
    genre = models.CharField(max_length=20)
    runtime = models.PositiveSmallIntegerField()
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    def __str__(self): #movie데이터가 화면에 어떻게 ㅍ표시될지 정하는
        return self.title
