from django.db import models


# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=20, null=False)  # charF max_len 받아준다
    description = models.CharField(max_length=200, null=False)  # null=false db에 저장할때 하지 않아도 된다, 폼에 적지 않으려면  black
    image = models.ImageField(upload_to='project/', null=False)  # 프로젝트를 넣어줌으로써 미디어 안에 project 폴더를 만들어 줄것이다
    created_at = models.DateTimeField(auto_now_add=True)  # 서버나 클라이언트한테 할당받지 않아도 자동으로 생성된다

    # models py가 변경 되었기 때문에 변화 추척후 실제 db에 반영해야한다

    class Meta:
        ordering = ['-pk']

    def __str__(self):  # 스페셜메서트 오버라이드드
        return f'{self.name}'
