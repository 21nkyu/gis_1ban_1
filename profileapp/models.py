from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model): # Model이라는 클래스를 상속받아 사용한다.
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')  #related_name //detail.html에서 호출하는 이름이 된다.

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True)
    message = models.CharField(max_length=200, null=True)

    # (연결시켜줄 클래스 User, on_delete= 연결된 유저객체가 사라졌을때 어떤 정책을 사용할것이냐, )
    # 이미지 이미지필드upload_to 어디로 업로드 할것이냐 profile라는 별도의 폴더에 저장할 것이다. null : 이미지가 없어도 괜찮다.
    # 닉네임 캐릭터 필드 unique 고유한 닉네임이어야 한다.
    # null 대화명을 적지 않아도 된다.

    #db에 반영 마이그레이션해줘야한다 models.py에서 변화를 찾는다
    #pip install pillow
    #python manage.py makemigrations 변화점을 찾는다
    #python manage.py migrate 적용한다