
# 모듈(.py) 가 아닌 패키지(디렉토리)를 import 하면
# __init__.py 에 정의된 것만 참조할 수 있다.


import pygame.sound
pygame.sound.echo.echo()
