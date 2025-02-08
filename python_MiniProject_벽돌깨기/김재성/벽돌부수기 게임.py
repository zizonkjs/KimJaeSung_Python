import pygame # pygame 모듈 불러오기
import random # 랜덤 모듈 불러오기
import time # 타임 모듈 불러오기

pygame.init() # pygame 모듈내에 함수 사용

BLACK = (0, 0, 0) # 모듈내 색깔 좌표
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
screen_width = 800 # 프로그램 창 가로길이
screen_height = 900 # 프로그램 창 세로길이
screen = pygame.display.set_mode((screen_width, screen_height)) # 설정한 값 적용

clock = pygame.time.Clock() # 모듈에 있는 프레임 설정 값

def runGame():
   
    score = 0 # 블록 몇개 깨드렷는지
    missed = 0 # 공을 몇번 놓쳤는지
    SUCCESS = 1 # 게임 이겼을 시 사용 할 값
    FAILURE = 2 # 게임 졌을 시 사용 할 값
    game_over = 0 # 값이 0 이상이 되면 Game over

    bricks = [] 
    COLUMN_COUNT = 10 # 얘는 블록의 가로 갯수
    ROW_COUNT = 10 # 얘는 블록의 세로 갯수
    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            brick = pygame.Rect(column_index * (60 + 10) + 35, row_index * (16 + 5) + 35, 60, 16) # 만약 (105, 56, 60, 16) 105와 56값은 블럭의 위치, 60과 16은 블럭의 넓이
            bricks.append(brick) # 어팬드 함수를 통해 빈리스트에추가     

    ball = pygame.Rect(screen_width // 2 - 16 // 2, screen_height // 2 - 16 // 2, 16, 16) # (공의 가로위치, 세로위치, 공의 가로 길이, 공의 세로길이 )
    ball_dx = 12 # 공이 x축 방향으로 얼마나 이동할지
    ball_dy = -12 # 공이 y축 방향으로 얼마나 이동할지

    paddle = pygame.Rect(screen_width // 2 - 80 // 2, screen_height - 16, 150, 16) # 공바쳐주는 바 (가로위치, 세로위치, 가로길이, 세로길이) 
    paddle_dx = 0 # BAR 값을 0으로 해서 가운데자리 위치하게    

    while True: 
        clock.tick(60) # 게임의 프레임 속도 FPS 난이도를 올리고싶다면 매개 변수를 높이면됨.
        screen.fill(BLACK) # 원하는 색깔 넣을 수 있음

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 게임창 말고 다른창에 있을 시에 멈춤
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # BAR 이동속도 조절
                    paddle_dx = -25
                elif event.key == pygame.K_RIGHT:
                    paddle_dx = 25
            elif event.type == pygame.KEYUP: # 만약 키보드로 눌리지 않을 시에 Bar 작동
                if event.key == pygame.K_LEFT:
                    paddle_dx = 0 # 움직이지 않게 설정
                elif event.key == pygame.K_RIGHT:
                    paddle_dx = 0        

        paddle.left += paddle_dx # 매 프레임 마다 이동속도를 저장해서 값에 따라 BAR 가 이동할 수 있게함.

        ball.left += ball_dx # 이동 값을 공위치로 저장 (좌우)
        ball.top  += ball_dy # 이동 값을 공위치로 저장 (위아래)

        if ball.left <= 0: # 공이 왼쪽 벽에 충돌했을 때
            ball.left = 0 # 충돌했을 때
            ball_dx = -ball_dx # 이동 방향을 반대로 바꾸는 역할
        elif ball.left >= screen_width - ball.width: # 공의 위치가 (게임창 가로길이 - 공의 가로길이) 값보다 작거나 클때
            ball.left = screen_width - ball.width # 공이 오른쪽 벽에 충돌했을 때
            ball_dx = -ball_dx # 반대로 튕기게
        if ball.top < 0: # 공의 상단위치가 0 이면 맨위쪽
            ball.top = 0 # 맨위쪽이다.
            ball_dy = -ball_dy # 이동 방향 반대로
        elif ball.top >= screen_height: # 공 하단위치가 게임창 높이보다 크거나 같을 때 (공을 놓쳤을 때)
            missed += 1 # 위에 missed 값에 놓친수만큼 값저장
            ball.left = screen_width // 2 - ball.width // 2 # 창의 가로 중앙-공의 길이 = 위치로 저장
            ball.top = screen_height // 2 - ball.width // 2 # 창의 세로 중앙-공의 길이 = 위치로 저장
            ball_dy = -ball_dy # 이동방향 반대로 (처음에 떨어지는 값 -12가 적용되서 저장 값은 12가 됨.)

        if missed >= 5: 
            game_over = FAILURE # 목숨 갯수 설정 난이도 올리고싶으면 값을 낮추면 됨.

        if paddle.left < 0: # 패들이 맨 왼쪽에 있을 때
            paddle.left = 0 # 값을 0으로 지정
        elif paddle.left > screen_width - paddle.width: # 게임창 가로 길이 - BAR 길이 = BAR 위치
            paddle.left = screen_width - paddle.width # 맨 오른쪽 위치

        for brick in bricks: # 벽돌 목록 반복문
            if ball.colliderect(brick): # colliderect 파이썬 sys 모듈에 있는 메서드. ball과 brick이 겹치는 경우를 검사해줌.
                # 겹칠땐 True, 그렇지 않으면 False를 반환 -> 조건문에 의해 True 일시
                bricks.remove(brick) # 우리가 배운 remove로 벽돌 값 제거 
                ball_dy = -ball_dy 
                score += 1 # 점수추가
                break # 벽돌 제거 중단

        if ball.colliderect(paddle): # 공이 패들과 부딪혔을 때
            ball_dy = -ball_dy 
            if ball.centerx <= paddle.left or ball.centerx > paddle.right: #centerx는 pygame 모듈에 있는 속성.
                # 공의 중심좌표 <= 패들 왼쪽 끝 부분 이거나 오른쪽 끝부분보다 크면
                ball_dx = ball_dx * -1 # 공의 값을 반대로 변경

        if len(bricks) == 0: # 벽돌의 값이 0 이라면
            print('success')
            game_over = SUCCESS # 파이썬 TERMINAL에 SUCCESS 출력

        #화면 그리기

        for brick in bricks:
            pygame.draw.rect(screen, GREEN, brick) # (화면, 색깔 설정, 벽돌값)

        if game_over == 0: # 게임오버가 아닐 때
            pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2) # (화면에 중앙에 흰색깔공을 표시, x좌표, y좌표, 공길이)

        pygame.draw.rect(screen, BLUE, paddle) # 파란색 패들 그려줌

        score_image = small_font.render('Point {}'.format(score), True, YELLOW) # 스코어 점수를 노란색으로 설정
        screen.blit(score_image, (10, 10)) # 좌표 10,10(왼쪽위)위치에 스코어 점수 표시

        missed_image = small_font.render('Missed {}'.format(missed), True, YELLOW) 
        screen.blit(missed_image, missed_image.get_rect(right=screen_width - 10, top=10)) # 놓진 횟수를 (창 가로 길이)-10,10 오른쪽위에 missed 출력. 

        if game_over > 0: 
            if game_over == SUCCESS: 
                success_image = large_font.render('SUCCEES, go to pyton (Ctrl+C)', True, RED) 
                screen.blit(success_image, success_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2)) # 게임에 이겼 을때 빨간색으로 성공 메시지를 출력.
            elif game_over == FAILURE:
                failure_image = large_font.render('FAILD, go to pyton (Ctrl+C)', True, RED)
                screen.blit(failure_image, failure_image.get_rect(centerx=screen_width // 2, centery=screen_height // 2))# 게임에 졌을때 빨간색으로 실패 메시지를 출력.

        pygame.display.update() # 설정한 그림 요소들을 화면에 업데이트 시킴

runGame() # 게임실행
pygame.quit() # 게임종료 

 
