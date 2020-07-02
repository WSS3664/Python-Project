import pygame  # 실제 라이브러리 로딩
import sys  # 창을 종료하는 시스템 관련 라이브러리
import time  # 게임 속 시간 관련 라이브러리
import random  # 게임 속 랜덤 요소를 위한 라이브러리
import pygame.mixer as sounds # 게임 속 사운드를 위한 라이브러리


from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGTH = 800
# 게임 화면 크기 지정
GRID_SIZE = 20  # 뱀을 나누는 단위, 한 칸당 20
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGTH = WINDOW_HEIGTH / GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 50, 0)
ORANGE = (250, 150, 0)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 10

sounds.init()
gameover_s = sounds.Sound("sound/game over.wav")
coin_s = sounds.Sound("sound/coin.wav")
Swipe_s = sounds.Sound("sound/Swipe.wav")
level_s = sounds.Sound("sound/level.wav")
level_s.play(-1)





class Python(object):  # 뱀 객체 생성
    def __init__(self):
        self.create()
        self.color = GREEN # 색깔 설정

    def create(self):
        self.length = 2  # 초기 크기 설정
        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGTH / 2))]  # 처음에 뱀 위치 설정
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 초기 뱀 방향

    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return

        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0]  # 뱀의 머리
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGTH)  # 뱀의 몸통부분

        if new in self.positions[2:]: #뱀의 머리와 다른 몸통이 만났을 떄
            self.create() #죽고 새 머리 생성
            feed.create() #먹이 위치 재생성
            obstacle.create()
            obstacle2.create()
            obstacle3.create()
            obstacle4.create()
            obstacle5.create()
            obstacle6.create()
            obstacle7.create()
            obstacle8.create()
            obstacle9.create()
            obstacle10.create()
            gameover_s.play()

        else:
            self.positions.insert(0, new)  # 새로 만든 몸통들 계속 추가
            if len(self.positions) > self.length:
                self.positions.pop()




    def eat(self):  # 먹이를 먹었을 경우 길이 1 증가
        self.length += 1
        coin_s.play()


    def eat_obstacle(self): #장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create() # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()

    def eat_obstacle2(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()

    def eat_obstacle3(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle4(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle5(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create() # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle6(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle7(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle8(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle9(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create() # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()


    def eat_obstacle10(self):  # 장애물과 부딪칠 경우 뱀 다시생성
        python.create()
        feed.create()  # 먹이 위치도 재생성
        obstacle.create()  # 장애물 위치 재생성
        obstacle2.create()  # 장애물 위치 재생성
        obstacle3.create()  # 장애물 위치 재생성
        obstacle4.create()  # 장애물 위치 재생성
        obstacle5.create()  # 장애물 위치 재생성
        obstacle6.create()  # 장애물 위치 재생성
        obstacle7.create()  # 장애물 위치 재생성
        obstacle8.create()  # 장애물 위치 재생성
        obstacle9.create()  # 장애물 위치 재생성
        obstacle10.create()  # 장애물 위치 재생성
        gameover_s.play()



    def draw(self, surface):
        for p in self.positions:
            draw_object(surface, self.color, p)





class Feed(object):  # 먹이 객체 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.create()

    def create(self):  # 먹이 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)







class Obstacle(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle2(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle3(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle4(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle5(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)


class Obstacle6(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle7(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle8(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle9(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)



class Obstacle10(object): #장애물 오브젝트 생성
    def __init__(self):
        self.position = (0, 0)
        self.color = BLACK
        self.create()

    def create(self): #장애물 오브젝트 위치
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)





def draw_object(surface, color, pos):  # 뱀과 먹이, 색깔 그리기
    r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, r)


def check_eat(python, feed): #뱀의 머리가 먹이를 먹을 경우
    if python.positions[0] == feed.position:
        python.eat()
        feed.create()

def check_eat_obstacle(python, obstacle): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle.position:
        python.eat_obstacle()


def check_eat_obstacle2(python, obstacle2): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle2.position:
        python.eat_obstacle2()


def check_eat_obstacle3(python, obstacle3): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle3.position:
        python.eat_obstacle3()


def check_eat_obstacle4(python, obstacle4): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle4.position:
        python.eat_obstacle4()


def check_eat_obstacle5(python, obstacle5): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle5.position:
        python.eat_obstacle5()


def check_eat_obstacle6(python, obstacle6): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle6.position:
        python.eat_obstacle6()


def check_eat_obstacle7(python, obstacle7): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle7.position:
        python.eat_obstacle7()


def check_eat_obstacle8(python, obstacle8): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle8.position:
        python.eat_obstacle8()


def check_eat_obstacle9(python, obstacle9): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle9.position:
        python.eat_obstacle9()


def check_eat_obstacle10(python, obstacle10): #뱀의 머리가 장애물과 부딪힐 경우
    if python.positions[0] == obstacle10.position:
        python.eat_obstacle10()




def show_info(length, speed, surface): #위에 꼬리 길이 등 정보 표시
    font = pygame.font.Font(None, 34)
    text = font.render("Length: " + str(length) + "  Speed:" + str(round(speed, 2)), 1, BLACK)
    pos = text.get_rect()
    pos.centerx = 150
    surface.blit(text, pos)



if __name__ == '__main__':
    
    python = Python()
    feed = Feed()
    obstacle = Obstacle()
    obstacle2 = Obstacle2()
    obstacle3 = Obstacle3()
    obstacle4 = Obstacle4()
    obstacle5 = Obstacle5()
    obstacle6 = Obstacle6()
    obstacle7 = Obstacle7()
    obstacle8 = Obstacle8()
    obstacle9 = Obstacle9()
    obstacle10 = Obstacle10()

    pygame.init()  # pygame 초기화
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)  # 게임 화면 설정
    pygame.display.set_caption('2020810044 심우성 - Snake Game')  # 게임 이름 설정
    surface = pygame.Surface(window.get_size())  # 게임 내 서페이스 설정
    surface = surface.convert()
    surface.fill(BLUE)  # 서페이스 색 설정
    clock = pygame.time.Clock()  # 게임 내 시간 설정
    pygame.key.set_repeat(1, 40)
    window.blit(surface, (0, 0))  # 실제 비트연산을 통한 게임 구현

    while True:  # 뱀 조작 반복문

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # 게임 및 창 종료

            elif event.type == pygame.KEYDOWN:  # 뱀 키 조작
                if event.key == pygame.K_UP:
                    python.control(UP)
                    Swipe_s.play()

                elif event.key == pygame.K_DOWN:
                    python.control(DOWN)
                    Swipe_s.play()

                elif event.key == pygame.K_LEFT:
                    python.control(LEFT)
                    Swipe_s.play()

                elif event.key == pygame.K_RIGHT:
                    python.control(RIGHT)
                    Swipe_s.play()



        surface.fill(BLUE)
        python.move()
        check_eat(python, feed)
        check_eat_obstacle(python, obstacle)
        check_eat_obstacle2(python, obstacle2)
        check_eat_obstacle3(python, obstacle3)
        check_eat_obstacle4(python, obstacle4)
        check_eat_obstacle5(python, obstacle5)
        check_eat_obstacle6(python, obstacle6)
        check_eat_obstacle7(python, obstacle7)
        check_eat_obstacle8(python, obstacle8)
        check_eat_obstacle9(python, obstacle9)
        check_eat_obstacle10(python, obstacle10)

        speed = (FPS + python.length) / 2  # 뱀의 길이와 속도를 비례
        show_info(python.length, speed, surface)
        python.draw(surface)
        feed.draw(surface)
        obstacle.draw(surface)
        obstacle2.draw(surface)
        obstacle3.draw(surface)
        obstacle4.draw(surface)
        obstacle5.draw(surface)
        obstacle6.draw(surface)
        obstacle7.draw(surface)
        obstacle8.draw(surface)
        obstacle9.draw(surface)
        obstacle10.draw(surface)
        window.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(speed)




