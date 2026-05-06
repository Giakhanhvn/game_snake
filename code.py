import pygame
import random
pygame.init()

#Tiêu đề , icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#kích thước màn hình
screen = pygame.display.set_mode((600, 600))

#nhạc nền
pygame.mixer.music.load('âm-thanh/nhạc-nền.mp3')
pygame.mixer.music.play(-1)  # Phát nhạc nền lặp lại

#Rắn
snake = pygame.image.load('hình-ảnh/snake.png').convert_alpha()
snake = pygame.transform.scale(snake, (30, 30))

#Táo
táo = pygame.image.load('hình-ảnh/táo.png').convert_alpha()
táo = pygame.transform.scale(táo, (30, 30))

#màu
black = (0, 0, 0)

#Danh sách toạ độ của rắn
x_rắn = [0]
y_rắn = [0]

#biến
dx = 1
dy = 0
apple = 0
điểm = 0
tốc_độ = 5

#đồng hồ
clock = pygame.time.Clock()

#Vòng lặp chính
running = True
while running:

    clock.tick(tốc_độ)  # Giới hạn tốc độ khung hình (FPS)

    tốc_độ = 5 + điểm // 5  # Tăng tốc độ

    #Hiện nền
    screen.fill(black)

    #hiện điểm
    if điểm < 10:
        điểm_1 = pygame.image.load(f'hình-ảnh/{điểm}.png').convert_alpha()
        điểm_1 = pygame.transform.scale(điểm_1, (30, 30))
        screen.blit(điểm_1, (20, 10))
    else:
        điểm_1 = pygame.image.load(f'hình-ảnh/{điểm//10}.png').convert_alpha()
        điểm_2 = pygame.image.load(f'hình-ảnh/{điểm%10}.png').convert_alpha()
        điểm_1 = pygame.transform.scale(điểm_1, (30, 30))
        điểm_2 = pygame.transform.scale(điểm_2, (30, 30))
        screen.blit(điểm_1, (20, 10))
        screen.blit(điểm_2, (60, 10))

    #toạ độ của táo
    if apple == 0:
        while True:
            x_táo = random.randint(0, 19) * 30
            y_táo = random.randint(0, 19) * 30
            # Kiểm tra xem táo có trùng với vị trí rắn không
            if (x_táo, y_táo) not in zip(x_rắn, y_rắn):
                break
        apple = 1

    #Hiện rắn
    for i in range(len(x_rắn)):
        screen.blit(snake, (x_rắn[i], y_rắn[i]))

    #Hiện táo
    screen.blit(táo, (x_táo, y_táo))

    if x_rắn[-1] == x_táo and y_rắn[-1] == y_táo:
        apple = 0
        điểm += 1

    new_x = x_rắn[-1] + dx * 30
    new_y = y_rắn[-1] + dy * 30

    if 0 <= new_x < 600 and 0 <= new_y < 600:   
        x_rắn.append(new_x)
        y_rắn.append(new_y)
    else:
        print('Game Over!')
        print('Điểm của bạn là:', điểm)
        running = False
        break

    for i in range(len(x_rắn) - 1):
        if x_rắn[-1] == x_rắn[i] and y_rắn[-1] == y_rắn[i]:
            print('Game Over!')
            print('Điểm của bạn là:', điểm)
            running = False
            break

    if apple == 1:
        x_rắn.pop(0)
        y_rắn.pop(0)

    for event in pygame.event.get():
        #Xử lý sự kiện bàn phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx != 1:  # Ngăn rắn quay ngược lại
                dx = -1
                dy = 0
            elif event.key == pygame.K_RIGHT and dx != -1:  # Ngăn rắn quay ngược lại
                dx = 1
                dy = 0
            elif event.key == pygame.K_UP and dy != 1:  # Ngăn rắn quay ngược lại
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN and dy != -1:  # Ngăn rắn quay ngược lại
                dx = 0
                dy = 1

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()