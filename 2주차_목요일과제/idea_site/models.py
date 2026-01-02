from django.db import models
from django.conf import settings
from django.db.models import Q

class DevTool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.TextField(blank = True)

    def __str__(self):
        return self.name
    
class Idea(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField(upload_to="ideas/", blank=True,null=True)
    #아이디어 등록시 ->이미지업로드
    content = models.TextField()
    interest=models.IntegerField(default=0)
    devtool = models.ForeignKey(
        DevTool,
        on_delete=models.PROTECT,
        related_name="ideas"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title #이 객체를 글자로 보여줄 때 어떤 이름으로 보이게 할것인지?(데이터를 대표하는 이름표를 정해주는 함수)
    
class IdeaStar(models.Model):
     # 찜한 사용자
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=True,
            blank=True,
        )
    
    # 찜한 아이디어
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="stars")
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            # 비로그인
            models.UniqueConstraint(
                fields=["idea", "session_key"],
                condition=Q(session_key__isnull=False),
                name="uniq_star_idea_session",
            ),
            # 로그인 -> 로그인/비로그인으로 짤라서 생성하기..
            models.UniqueConstraint(
                fields=["idea", "user"],
                condition=Q(user__isnull=False),
                name="uniq_star_idea_user",
            ),
        ]

    def __str__(self):
         return f"{self.idea_id}"
# Create your models here.
