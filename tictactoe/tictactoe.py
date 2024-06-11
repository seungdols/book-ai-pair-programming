# pygame 이용해서 tic-tac-toe 게임을 만들어 보자.

import pygame
import sys
import numpy as np

# 초기화
pygame.init()

# 화면 크기 설정
width, height = 600, 600

# 화면 설정
screen = pygame.display.set_mode((width, height))

# 선 색깔 설정
white = (255, 255, 255)
line_color = (0, 0, 0)

# 선의 두께 설정
line_width = 15

# 게임 변수 설정
board_rows = 3
board_cols = 3
square_size = 200

# 원 색깔 설정
circle_color = (239, 231, 200)
circle_width = 70

cross_color = (66, 66, 66)
cross_width = 15

# 게임 변수 설정
board = np.zeros((board_rows, board_cols))

# 게임 끝내기 변수 설정
game_over = False
current_player = 1  # 현재 플레이어 추적 변수 추가
# 메인 루프
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 현재 플레이어 확인
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row = pos[1] // square_size
                col = pos[0] // square_size
                # 빈 공간인 경우에만 마크
                if board[row][col] == 0:
                    board[row][col] = current_player
                    # 플레이어 변경
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                    # 게임 종료 조건 확인
                    if np.any(np.all(board == 1, axis=0)) or np.any(np.all(board == 1, axis=1)) or np.all(np.diag(board) == 1) or np.all(np.diag(np.fliplr(board)) == 1):
                        print("Player 1 wins!")
                        game_over = True
                    elif np.any(np.all(board == 2, axis=0)) or np.any(np.all(board == 2, axis=1)) or np.all(np.diag(board) == 2) or np.all(np.diag(np.fliplr(board)) == 2):
                        print("Player 2 wins!")
                        game_over = True
                    elif np.all(board != 0):
                        print("It's a tie!")
                        game_over = True
    # 화면 초기화
    screen.fill(white)
    # 게임 보드 그리기
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (col * square_size + square_size // 2, row * square_size + square_size // 2), circle_width, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * square_size + square_size // 4, row * square_size + square_size // 4), (col * square_size + square_size * 3 // 4, row * square_size + square_size * 3 // 4), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + square_size * 3 // 4, row * square_size + square_size // 4), (col * square_size + square_size // 4, row * square_size + square_size * 3 // 4), cross_width)
    # 화면 업데이트
    pygame.display.flip()
