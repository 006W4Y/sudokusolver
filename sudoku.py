import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 1000))
pygame.display.set_caption("Sudoku Solver A. Freudenberg")
base_font = pygame.font.Font(None, 50)

# functions:

n = 9

field = [[[1 for k in range(n)] for j in range(n)] for i in range(n)]
counter = 0
ergebnis = 0

user_text = [["" for g in range(n)] for h in range(n)]
text = "Submit"



input_rect = pygame.Rect(10, 10, 80, 80)  # 1
input_rect1 = pygame.Rect(105, 10, 80, 80)  # 2
input_rect2 = pygame.Rect(200, 10, 80, 80)  # 3
input_rect3 = pygame.Rect(315, 10, 80, 80)  # 4
input_rect4 = pygame.Rect(410, 10, 80, 80)  # 5
input_rect5 = pygame.Rect(505, 10, 80, 80)  # 6
input_rect6 = pygame.Rect(620, 10, 80, 80)  # 7
input_rect7 = pygame.Rect(715, 10, 80, 80)  # 8
input_rect8 = pygame.Rect(810, 10, 80, 80)  # 9

input_rect9 = pygame.Rect(10, 105, 80, 80)
input_rect10 = pygame.Rect(105, 105, 80, 80)
input_rect11 = pygame.Rect(200, 105, 80, 80)
input_rect12 = pygame.Rect(315, 105, 80, 80)
input_rect13 = pygame.Rect(410, 105, 80, 80)
input_rect14 = pygame.Rect(505, 105, 80, 80)
input_rect15 = pygame.Rect(620, 105, 80, 80)
input_rect16 = pygame.Rect(715, 105, 80, 80)
input_rect17 = pygame.Rect(810, 105, 80, 80)

input_rect18 = pygame.Rect(10, 200, 80, 80)
input_rect19 = pygame.Rect(105, 200, 80, 80)
input_rect20 = pygame.Rect(200, 200, 80, 80)
input_rect21 = pygame.Rect(315, 200, 80, 80)
input_rect22 = pygame.Rect(410, 200, 80, 80)
input_rect23 = pygame.Rect(505, 200, 80, 80)
input_rect24 = pygame.Rect(620, 200, 80, 80)
input_rect25 = pygame.Rect(715, 200, 80, 80)
input_rect26 = pygame.Rect(810, 200, 80, 80)

input_rect27 = pygame.Rect(10, 315, 80, 80)
input_rect28 = pygame.Rect(105, 315, 80, 80)
input_rect29 = pygame.Rect(200, 315, 80, 80)
input_rect30 = pygame.Rect(315, 315, 80, 80)
input_rect31 = pygame.Rect(410, 315, 80, 80)
input_rect32 = pygame.Rect(505, 315, 80, 80)
input_rect33 = pygame.Rect(620, 315, 80, 80)
input_rect34 = pygame.Rect(715, 315, 80, 80)
input_rect35 = pygame.Rect(810, 315, 80, 80)

input_rect36 = pygame.Rect(10, 410, 80, 80)
input_rect37 = pygame.Rect(105, 410, 80, 80)
input_rect38 = pygame.Rect(200, 410, 80, 80)
input_rect39 = pygame.Rect(315, 410, 80, 80)
input_rect40 = pygame.Rect(410, 410, 80, 80)
input_rect41 = pygame.Rect(505, 410, 80, 80)
input_rect42 = pygame.Rect(620, 410, 80, 80)
input_rect43 = pygame.Rect(715, 410, 80, 80)
input_rect44 = pygame.Rect(810, 410, 80, 80)

input_rect45 = pygame.Rect(10, 505, 80, 80)
input_rect46 = pygame.Rect(105, 505, 80, 80)
input_rect47 = pygame.Rect(200, 505, 80, 80)
input_rect48 = pygame.Rect(315, 505, 80, 80)
input_rect49 = pygame.Rect(410, 505, 80, 80)
input_rect50 = pygame.Rect(505, 505, 80, 80)
input_rect51 = pygame.Rect(620, 505, 80, 80)
input_rect52 = pygame.Rect(715, 505, 80, 80)
input_rect53 = pygame.Rect(810, 505, 80, 80)

input_rect54 = pygame.Rect(10, 620, 80, 80)
input_rect55 = pygame.Rect(105, 620, 80, 80)
input_rect56 = pygame.Rect(200, 620, 80, 80)
input_rect57 = pygame.Rect(315, 620, 80, 80)
input_rect58 = pygame.Rect(410, 620, 80, 80)
input_rect59 = pygame.Rect(505, 620, 80, 80)
input_rect60 = pygame.Rect(620, 620, 80, 80)
input_rect61 = pygame.Rect(715, 620, 80, 80)
input_rect62 = pygame.Rect(810, 620, 80, 80)

input_rect63 = pygame.Rect(10, 715, 80, 80)
input_rect64 = pygame.Rect(105, 715, 80, 80)
input_rect65 = pygame.Rect(200, 715, 80, 80)
input_rect66 = pygame.Rect(315, 715, 80, 80)
input_rect67 = pygame.Rect(410, 715, 80, 80)
input_rect68 = pygame.Rect(505, 715, 80, 80)
input_rect69 = pygame.Rect(620, 715, 80, 80)
input_rect70 = pygame.Rect(715, 715, 80, 80)
input_rect71 = pygame.Rect(810, 715, 80, 80)

input_rect72 = pygame.Rect(10, 810, 80, 80)
input_rect73 = pygame.Rect(105, 810, 80, 80)
input_rect74 = pygame.Rect(200, 810, 80, 80)
input_rect75 = pygame.Rect(315, 810, 80, 80)
input_rect76 = pygame.Rect(410, 810, 80, 80)
input_rect77 = pygame.Rect(505, 810, 80, 80)
input_rect78 = pygame.Rect(620, 810, 80, 80)
input_rect79 = pygame.Rect(715, 810, 80, 80)
input_rect80 = pygame.Rect(810, 810, 80, 80)
submit_rect = pygame.Rect(10, 910, 880, 80)

color_active = (153, 0, 0)

color_passive = (255, 255, 255)
color_submit = (153, 0, 0)

color = color_passive
color1 = color_passive
color2 = color_passive
color3 = color_passive
color4 = color_passive
color5 = color_passive
color6 = color_passive
color7 = color_passive
color8 = color_passive
color9 = color_passive
color10 = color_passive
color11 = color_passive
color12 = color_passive
color13 = color_passive
color14 = color_passive
color15 = color_passive
color16 = color_passive
color17 = color_passive
color18 = color_passive
color19 = color_passive
color20 = color_passive
color21 = color_passive
color22 = color_passive
color23 = color_passive
color24 = color_passive
color25 = color_passive
color26 = color_passive
color27 = color_passive
color28 = color_passive
color29 = color_passive
color30 = color_passive
color31 = color_passive
color32 = color_passive
color33 = color_passive
color34 = color_passive
color35 = color_passive
color36 = color_passive
color37 = color_passive
color38 = color_passive
color39 = color_passive
color40 = color_passive
color41 = color_passive
color42 = color_passive
color43 = color_passive
color44 = color_passive
color45 = color_passive
color46 = color_passive
color47 = color_passive
color48 = color_passive
color49 = color_passive
color50 = color_passive
color51 = color_passive
color52 = color_passive
color53 = color_passive
color54 = color_passive
color55 = color_passive
color56 = color_passive
color57 = color_passive
color58 = color_passive
color59 = color_passive
color60 = color_passive
color61 = color_passive
color62 = color_passive
color63 = color_passive
color64 = color_passive
color65 = color_passive
color66 = color_passive
color67 = color_passive
color68 = color_passive
color69 = color_passive
color70 = color_passive
color71 = color_passive
color72 = color_passive
color73 = color_passive
color74 = color_passive
color75 = color_passive
color76 = color_passive
color77 = color_passive
color78 = color_passive
color79 = color_passive
color80 = color_passive

active = False
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False
active7 = False
active8 = False
active9 = False
active10 = False
active11 = False
active12 = False
active13 = False
active14 = False
active15 = False
active16 = False
active17 = False
active18 = False
active19 = False
active20 = False
active21 = False
active22 = False
active23 = False
active24 = False
active25 = False
active26 = False
active27 = False
active28 = False
active29 = False
active30 = False
active31 = False
active32 = False
active33 = False
active34 = False
active35 = False
active36 = False
active37 = False
active38 = False
active39 = False
active40 = False
active41 = False
active42 = False
active43 = False
active44 = False
active45 = False
active46 = False
active47 = False
active48 = False
active49 = False
active50 = False
active51 = False
active52 = False
active53 = False
active54 = False
active55 = False
active56 = False
active57 = False
active58 = False
active59 = False
active60 = False
active61 = False
active62 = False
active63 = False
active64 = False
active65 = False
active66 = False
active67 = False
active68 = False
active69 = False
active70 = False
active71 = False
active72 = False
active73 = False
active74 = False
active75 = False
active76 = False
active77 = False
active78 = False
active79 = False
active80 = False

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            if input_rect1.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False
            if input_rect2.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False
            if input_rect3.collidepoint(event.pos):
                active3 = True
            else:
                active3 = False
            if input_rect4.collidepoint(event.pos):
                active4 = True
            else:
                active4 = False
            if input_rect5.collidepoint(event.pos):
                active5 = True
            else:
                active5 = False
            if input_rect6.collidepoint(event.pos):
                active6 = True
            else:
                active6 = False
            if input_rect7.collidepoint(event.pos):
                active7 = True
            else:
                active7 = False
            if input_rect8.collidepoint(event.pos):
                active8 = True
            else:
                active8 = False
            if input_rect9.collidepoint(event.pos):
                active9 = True
            else:
                active9 = False
            if input_rect10.collidepoint(event.pos):
                active10 = True
            else:
                active10 = False
            if input_rect11.collidepoint(event.pos):
                active11 = True
            else:
                active11 = False
            if input_rect12.collidepoint(event.pos):
                active12 = True
            else:
                active12 = False
            if input_rect13.collidepoint(event.pos):
                active13 = True
            else:
                active13 = False
            if input_rect14.collidepoint(event.pos):
                active14 = True
            else:
                active14 = False
            if input_rect15.collidepoint(event.pos):
                active15 = True
            else:
                active15 = False
            if input_rect16.collidepoint(event.pos):
                active16 = True
            else:
                active16 = False
            if input_rect17.collidepoint(event.pos):
                active17 = True
            else:
                active17 = False
            if input_rect18.collidepoint(event.pos):
                active18 = True
            else:
                active18 = False
            if input_rect19.collidepoint(event.pos):
                active19 = True
            else:
                active19 = False
            if input_rect20.collidepoint(event.pos):
                active20 = True
            else:
                active20 = False
            if input_rect21.collidepoint(event.pos):
                active21 = True
            else:
                active21 = False
            if input_rect22.collidepoint(event.pos):
                active22 = True
            else:
                active22 = False
            if input_rect23.collidepoint(event.pos):
                active23 = True
            else:
                active23 = False
            if input_rect24.collidepoint(event.pos):
                active24 = True
            else:
                active24 = False
            if input_rect25.collidepoint(event.pos):
                active25 = True
            else:
                active25 = False
            if input_rect26.collidepoint(event.pos):
                active26 = True
            else:
                active26 = False
            if input_rect27.collidepoint(event.pos):
                active27 = True
            else:
                active27 = False
            if input_rect28.collidepoint(event.pos):
                active28 = True
            else:
                active28 = False
            if input_rect29.collidepoint(event.pos):
                active29 = True
            else:
                active29 = False
            if input_rect30.collidepoint(event.pos):
                active30 = True
            else:
                active30 = False
            if input_rect31.collidepoint(event.pos):
                active31 = True
            else:
                active31 = False
            if input_rect32.collidepoint(event.pos):
                active32 = True
            else:
                active32 = False
            if input_rect33.collidepoint(event.pos):
                active33 = True
            else:
                active33 = False
            if input_rect34.collidepoint(event.pos):
                active34 = True
            else:
                active34 = False
            if input_rect35.collidepoint(event.pos):
                active35 = True
            else:
                active35 = False
            if input_rect36.collidepoint(event.pos):
                active36 = True
            else:
                active36 = False
            if input_rect37.collidepoint(event.pos):
                active37 = True
            else:
                active37 = False
            if input_rect38.collidepoint(event.pos):
                active38 = True
            else:
                active38 = False
            if input_rect39.collidepoint(event.pos):
                active39 = True
            else:
                active39 = False
            if input_rect40.collidepoint(event.pos):
                active40 = True
            else:
                active40 = False
            if input_rect41.collidepoint(event.pos):
                active41 = True
            else:
                active41 = False
            if input_rect42.collidepoint(event.pos):
                active42 = True
            else:
                active42 = False
            if input_rect43.collidepoint(event.pos):
                active43 = True
            else:
                active43 = False
            if input_rect44.collidepoint(event.pos):
                active44 = True
            else:
                active44 = False
            if input_rect45.collidepoint(event.pos):
                active45 = True
            else:
                active45 = False
            if input_rect46.collidepoint(event.pos):
                active46 = True
            else:
                active46 = False
            if input_rect47.collidepoint(event.pos):
                active47 = True
            else:
                active47 = False
            if input_rect48.collidepoint(event.pos):
                active48 = True
            else:
                active48 = False
            if input_rect49.collidepoint(event.pos):
                active49 = True
            else:
                active49 = False
            if input_rect50.collidepoint(event.pos):
                active50 = True
            else:
                active50 = False
            if input_rect51.collidepoint(event.pos):
                active51 = True
            else:
                active51 = False
            if input_rect52.collidepoint(event.pos):
                active52 = True
            else:
                active52 = False
            if input_rect53.collidepoint(event.pos):
                active53 = True
            else:
                active53 = False
            if input_rect54.collidepoint(event.pos):
                active54 = True
            else:
                active54 = False
            if input_rect55.collidepoint(event.pos):
                active55 = True
            else:
                active55 = False
            if input_rect56.collidepoint(event.pos):
                active56 = True
            else:
                active56 = False
            if input_rect57.collidepoint(event.pos):
                active57 = True
            else:
                active57 = False
            if input_rect58.collidepoint(event.pos):
                active58 = True
            else:
                active58 = False
            if input_rect59.collidepoint(event.pos):
                active59 = True
            else:
                active59 = False
            if input_rect60.collidepoint(event.pos):
                active60 = True
            else:
                active60 = False
            if input_rect61.collidepoint(event.pos):
                active61 = True
            else:
                active61 = False
            if input_rect62.collidepoint(event.pos):
                active62 = True
            else:
                active62 = False
            if input_rect63.collidepoint(event.pos):
                active63 = True
            else:
                active63 = False
            if input_rect64.collidepoint(event.pos):
                active64 = True
            else:
                active64 = False
            if input_rect65.collidepoint(event.pos):
                active65 = True
            else:
                active65 = False
            if input_rect66.collidepoint(event.pos):
                active66 = True
            else:
                active66 = False
            if input_rect67.collidepoint(event.pos):
                active67 = True
            else:
                active67 = False
            if input_rect68.collidepoint(event.pos):
                active68 = True
            else:
                active68 = False
            if input_rect69.collidepoint(event.pos):
                active69 = True
            else:
                active69 = False
            if input_rect70.collidepoint(event.pos):
                active70 = True
            else:
                active70 = False
            if input_rect71.collidepoint(event.pos):
                active71 = True
            else:
                active71 = False
            if input_rect72.collidepoint(event.pos):
                active72 = True
            else:
                active72 = False
            if input_rect73.collidepoint(event.pos):
                active73 = True
            else:
                active73 = False
            if input_rect74.collidepoint(event.pos):
                active74 = True
            else:
                active74 = False
            if input_rect75.collidepoint(event.pos):
                active75 = True
            else:
                active75 = False
            if input_rect76.collidepoint(event.pos):
                active76 = True
            else:
                active76 = False
            if input_rect77.collidepoint(event.pos):
                active77 = True
            else:
                active77 = False
            if input_rect78.collidepoint(event.pos):
                active78 = True
            else:
                active78 = False
            if input_rect79.collidepoint(event.pos):
                active79 = True
            else:
                active79 = False
            if input_rect80.collidepoint(event.pos):
                active80 = True
            else:
                active80 = False
            if submit_rect.collidepoint(event.pos):
                print("Logic")
                print(field)
                print(user_text)

                while True:
                    for i in range(0, 9):
                        for j in range(0, 9):
                            for k in range(0, 9):
                                if field[i][j][k] == 1:
                                    counter += counter
                                    ergebnis = k
                            if counter == 1:
                                print("Answer found!")
                                user_text[i][j] = ergebnis

        # Text Input

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][0] = user_text[0][0][:-1]
                else:
                    user_text[0][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][0]) - 1] = 0
                        field[0][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][0]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[0][0]) - 1] = 0
                    field[0][0][int(user_text[0][0]) - 1] = 1
            if active1:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][1] = user_text[0][1][:-1]
                else:
                    user_text[0][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][1]) - 1] = 0
                        field[0][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][1]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[0][1]) - 1] = 0
                    field[0][1][int(user_text[0][1]) - 1] = 1
            if active2:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][2] = user_text[0][2][:-1]
                else:
                    user_text[0][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][2]) - 1] = 0
                        field[0][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][2]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[0][2]) - 1] = 0
                    field[0][2][int(user_text[0][2]) - 1] = 1

            if active3:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][3] = user_text[0][3][:-1]
                else:
                    user_text[0][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][3]) - 1] = 0
                        field[0][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][3]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[0][3]) - 1] = 0
                    field[0][3][int(user_text[0][3]) - 1] = 1
            if active4:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][4] = user_text[0][4][:-1]
                else:
                    user_text[0][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][4]) - 1] = 0
                        field[0][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][4]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[0][4]) - 1] = 0
                    field[0][4][int(user_text[0][4]) - 1] = 1
            if active5:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][5] = user_text[0][5][:-1]
                else:
                    user_text[0][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][5]) - 1] = 0
                        field[0][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][5]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[0][5]) - 1] = 0
                    field[0][5][int(user_text[0][5]) - 1] = 1

            if active6:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][6] = user_text[0][6][:-1]
                else:
                    user_text[0][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][6]) - 1] = 0
                        field[0][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][6]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[0][6]) - 1] = 0
                    field[0][6][int(user_text[0][6]) - 1] = 1
            if active7:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][7] = user_text[0][7][:-1]
                else:
                    user_text[0][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][7]) - 1] = 0
                        field[0][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][7]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[0][7]) - 1] = 0
                    field[0][7][int(user_text[0][7]) - 1] = 1
            if active8:
                if event.key == pygame.K_BACKSPACE:
                    user_text[0][8] = user_text[0][8][:-1]
                else:
                    user_text[0][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[0][8]) - 1] = 0
                        field[0][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[0][8]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[0][8]) - 1] = 0
                    field[0][8][int(user_text[0][8]) - 1] = 1

            # 2. Zeile

            if active9:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][0] = user_text[1][0][:-1]
                else:
                    user_text[1][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][0]) - 1] = 0
                        field[1][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][0]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[1][0]) - 1] = 0
                    field[1][0][int(user_text[1][0]) - 1] = 1
            if active10:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][1] = user_text[1][1][:-1]
                else:
                    user_text[1][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][1]) - 1] = 0
                        field[1][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][1]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[1][1]) - 1] = 0
                    field[1][1][int(user_text[1][1]) - 1] = 1
            if active11:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][2] = user_text[1][2][:-1]
                else:
                    user_text[1][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][2]) - 1] = 0
                        field[1][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][2]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[1][2]) - 1] = 0
                    field[1][2][int(user_text[1][2]) - 1] = 1

            if active12:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][3] = user_text[1][3][:-1]
                else:
                    user_text[1][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][3]) - 1] = 0
                        field[1][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][3]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[1][3]) - 1] = 0
                    field[1][3][int(user_text[1][3]) - 1] = 1
            if active13:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][4] = user_text[1][4][:-1]
                else:
                    user_text[1][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][4]) - 1] = 0
                        field[1][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][4]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[1][4]) - 1] = 0
                    field[1][4][int(user_text[1][4]) - 1] = 1
            if active14:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][5] = user_text[1][5][:-1]
                else:
                    user_text[1][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][5]) - 1] = 0
                        field[1][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][5]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[1][5]) - 1] = 0
                    field[1][5][int(user_text[1][5]) - 1] = 1

            if active15:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][6] = user_text[1][6][:-1]
                else:
                    user_text[1][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][6]) - 1] = 0
                        field[1][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][6]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[1][6]) - 1] = 0
                    field[1][6][int(user_text[1][6]) - 1] = 1
            if active16:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][7] = user_text[1][7][:-1]
                else:
                    user_text[1][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][7]) - 1] = 0
                        field[1][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][7]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[1][7]) - 1] = 0
                    field[1][7][int(user_text[1][7]) - 1] = 1
            if active17:
                if event.key == pygame.K_BACKSPACE:
                    user_text[1][8] = user_text[1][8][:-1]
                else:
                    user_text[1][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[1][8]) - 1] = 0
                        field[1][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[1][8]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[1][8]) - 1] = 0
                    field[1][8][int(user_text[1][8]) - 1] = 1

            if active18:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][0] = user_text[2][0][:-1]
                else:
                    user_text[2][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][0]) - 1] = 0
                        field[2][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][0]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[2][0]) - 1] = 0
                    field[2][0][int(user_text[2][0]) - 1] = 1
            if active19:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][1] = user_text[2][1][:-1]
                else:
                    user_text19 = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][1]) - 1] = 0
                        field[2][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][1]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[2][1]) - 1] = 0
                    field[2][1][int(user_text[2][1]) - 1] = 1
            if active20:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][2] = user_text[2][2][:-1]
                else:
                    user_text[2][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][2]) - 1] = 0
                        field[2][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][2]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(0, 3):
                            field[i][j][int(user_text[2][2]) - 1] = 0
                    field[2][2][int(user_text[2][2]) - 1] = 1

            if active21:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][3] = user_text[2][3][:-1]
                else:
                    user_text[2][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][3]) - 1] = 0
                        field[2][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][3]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[2][3]) - 1] = 0
                    field[2][3][int(user_text[2][3]) - 1] = 1
            if active22:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][4] = user_text[2][4][:-1]
                else:
                    user_text[2][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][4]) - 1] = 0
                        field[2][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][4]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[2][4]) - 1] = 0
                    field[2][4][int(user_text[2][4]) - 1] = 1
            if active23:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][5] = user_text[2][5][:-1]
                else:
                    user_text[2][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][5]) - 1] = 0
                        field[2][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][5]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(3, 6):
                            field[i][j][int(user_text[2][5]) - 1] = 0
                    field[2][5][int(user_text[2][5]) - 1] = 1

            if active24:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][6] = user_text[2][6][:-1]
                else:
                    user_text[2][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][6]) - 1] = 0
                        field[2][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][6]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[2][6]) - 1] = 0
                    field[2][6][int(user_text[2][6]) - 1] = 1
            if active25:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][7] = user_text[2][7][:-1]
                else:
                    user_text[2][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][7]) - 1] = 0
                        field[2][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][7]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[2][7]) - 1] = 0
                    field[2][7][int(user_text[2][7]) - 1] = 1
            if active26:
                if event.key == pygame.K_BACKSPACE:
                    user_text[2][8] = user_text[2][8][:-1]
                else:
                    user_text[2][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[2][8]) - 1] = 0
                        field[2][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[2][8]) - 1] = 0
                    for i in range(0, 3):
                        for j in range(6, 9):
                            field[i][j][int(user_text[2][8]) - 1] = 0
                    field[2][8][int(user_text[2][8]) - 1] = 1

            if active27:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][0] = user_text[3][0][:-1]
                else:
                    user_text[3][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][0]) - 1] = 0
                        field[3][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][0]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[3][0]) - 1] = 0
                    field[3][0][int(user_text[3][0]) - 1] = 1
            if active28:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][1] = user_text[3][1][:-1]
                else:
                    user_text[3][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][1]) - 1] = 0
                        field[3][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][1]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[3][1]) - 1] = 0
                    field[3][1][int(user_text[3][1]) - 1] = 1
            if active29:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][2] = user_text[3][2][:-1]
                else:
                    user_text[3][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][2]) - 1] = 0
                        field[3][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][2]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[3][2]) - 1] = 0
                    field[3][2][int(user_text[3][2]) - 1] = 1

            if active30:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][3] = user_text[3][3][:-1]
                else:
                    user_text[3][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][3]) - 1] = 0
                        field[3][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][3]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[3][3]) - 1] = 0
                    field[3][3][int(user_text[3][3]) - 1] = 1
            if active31:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][4] = user_text[3][4][:-1]
                else:
                    user_text[3][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][4]) - 1] = 0
                        field[3][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][4]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[3][4]) - 1] = 0
                    field[3][4][int(user_text[3][4]) - 1] = 1
            if active32:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][5] = user_text[3][5][:-1]
                else:
                    user_text[3][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][5]) - 1] = 0
                        field[3][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][5]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[3][5]) - 1] = 0
                    field[3][5][int(user_text[3][5]) - 1] = 1

            if active33:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][6] = user_text[3][6][:-1]
                else:
                    user_text[3][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][6]) - 1] = 0
                        field[3][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][6]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[3][6]) - 1] = 0
                    field[3][6][int(user_text[3][6]) - 1] = 1
            if active34:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][7] = user_text[3][7][:-1]
                else:
                    user_text[3][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][7]) - 1] = 0
                        field[3][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][7]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[3][7]) - 1] = 0
                    field[3][7][int(user_text[3][7]) - 1] = 1
            if active35:
                if event.key == pygame.K_BACKSPACE:
                    user_text[3][8] = user_text[3][8][:-1]
                else:
                    user_text[3][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[3][8]) - 1] = 0
                        field[3][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[3][8]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[3][8]) - 1] = 0
                    field[3][8][int(user_text[3][8]) - 1] = 1

            if active36:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][0] = user_text[4][0][:-1]
                else:
                    user_text[4][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][0]) - 1] = 0
                        field[4][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][0]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[4][0]) - 1] = 0
                    field[4][0][int(user_text[4][0]) - 1] = 1
            if active37:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][1] = user_text[4][1][:-1]
                else:
                    user_text[4][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][1]) - 1] = 0
                        field[4][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][1]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[4][1]) - 1] = 0
                    field[4][1][int(user_text[4][1]) - 1] = 1
            if active38:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][2] = user_text[4][2][:-1]
                else:
                    user_text[4][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][2]) - 1] = 0
                        field[4][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][2]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[4][2]) - 1] = 0
                    field[4][2][int(user_text[4][2]) - 1] = 1

            if active39:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][3] = user_text[4][3][:-1]
                else:
                    user_text[4][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][3]) - 1] = 0
                        field[4][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][3]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[4][3]) - 1] = 0
                    field[4][3][int(user_text[4][3]) - 1] = 1
            if active40:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][4] = user_text[4][4][:-1]
                else:
                    user_text[4][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][4]) - 1] = 0
                        field[4][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][4]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[4][4]) - 1] = 0
                    field[4][4][int(user_text[4][4]) - 1] = 1
            if active41:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][5] = user_text[4][5][:-1]
                else:
                    user_text[4][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][5]) - 1] = 0
                        field[4][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][5]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[4][5]) - 1] = 0
                    field[4][5][int(user_text[4][5]) - 1] = 1

            if active42:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][6] = user_text[4][6][:-1]
                else:
                    user_text[4][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][6]) - 1] = 0
                        field[4][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][6]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 9):
                            field[i][j][int(user_text[4][6]) - 1] = 0
                    field[4][6][int(user_text[4][6]) - 1] = 1
            if active43:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][7] = user_text[4][7][:-1]
                else:
                    user_text[4][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][7]) - 1] = 0
                        field[4][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][7]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[4][7]) - 1] = 0
                    field[4][7][int(user_text[4][7]) - 1] = 1
            if active44:
                if event.key == pygame.K_BACKSPACE:
                    user_text[4][8] = user_text[4][8][:-1]
                else:
                    user_text[4][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[4][8]) - 1] = 0
                        field[4][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[4][8]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[4][8]) - 1] = 0
                    field[4][8][int(user_text[4][8]) - 1] = 1

            if active45:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][0] = user_text[5][0][:-1]
                else:
                    user_text[5][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][0]) - 1] = 0
                        field[5][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][0]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[5][0]) - 1] = 0
                    field[5][0][int(user_text[5][0]) - 1] = 1
            if active46:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][1] = user_text[5][1][:-1]
                else:
                    user_text[5][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][1]) - 1] = 0
                        field[5][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][1]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[5][1]) - 1] = 0
                    field[5][1][int(user_text[5][1]) - 1] = 1
            if active47:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][2] = user_text[5][2][:-1]
                else:
                    user_text[5][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][2]) - 1] = 0
                        field[5][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][2]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(0, 3):
                            field[i][j][int(user_text[5][2]) - 1] = 0
                    field[5][2][int(user_text[5][2]) - 1] = 1

            if active48:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][3] = user_text[5][3][:-1]
                else:
                    user_text[5][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][3]) - 1] = 0
                        field[5][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][3]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[5][3]) - 1] = 0
                    field[5][3][int(user_text[5][3]) - 1] = 1
            if active49:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][4] = user_text[5][4][:-1]
                else:
                    user_text[5][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][4]) - 1] = 0
                        field[5][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][4]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[5][4]) - 1] = 0
                    field[5][4][int(user_text[5][4]) - 1] = 1
            if active50:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][5] = user_text[5][5][:-1]
                else:
                    user_text[5][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][5]) - 1] = 0
                        field[5][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][5]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(3, 6):
                            field[i][j][int(user_text[5][5]) - 1] = 0
                    field[5][5][int(user_text[5][5]) - 1] = 1

            if active51:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][6] = user_text[5][6][:-1]
                else:
                    user_text[5][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][6]) - 1] = 0
                        field[5][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][6]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[5][6]) - 1] = 0
                    field[5][6][int(user_text[5][6]) - 1] = 1
            if active52:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][7] = user_text[5][7][:-1]
                else:
                    user_text[5][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][7]) - 1] = 0
                        field[5][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][7]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[5][7]) - 1] = 0
                    field[5][7][int(user_text[5][7]) - 1] = 1
            if active53:
                if event.key == pygame.K_BACKSPACE:
                    user_text[5][8] = user_text[5][8][:-1]
                else:
                    user_text[5][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[5][8]) - 1] = 0
                        field[5][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[5][8]) - 1] = 0
                    for i in range(3, 6):
                        for j in range(6, 9):
                            field[i][j][int(user_text[5][8]) - 1] = 0
                    field[5][8][int(user_text[5][8]) - 1] = 1

            if active54:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][0] = user_text[6][0][:-1]
                else:
                    user_text[6][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][0]) - 1] = 0
                        field[6][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][0]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[6][0]) - 1] = 0
                    field[6][0][int(user_text[6][0]) - 1] = 1
            if active55:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][1] = user_text[6][1][:-1]
                else:
                    user_text[6][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][1]) - 1] = 0
                        field[6][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][1]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[6][1]) - 1] = 0
                    field[6][1][int(user_text[6][1]) - 1] = 1
            if active56:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][2] = user_text[6][2][:-1]
                else:
                    user_text[6][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][2]) - 1] = 0
                        field[6][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][2]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[6][2]) - 1] = 0
                    field[6][2][int(user_text[6][2]) - 1] = 1

            if active57:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][3] = user_text[6][3][:-1]
                else:
                    user_text[6][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][3]) - 1] = 0
                        field[6][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][3]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[6][3]) - 1] = 0
                    field[6][3][int(user_text[6][3]) - 1] = 1
            if active58:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][4] = user_text[6][4][:-1]
                else:
                    user_text[6][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][4]) - 1] = 0
                        field[6][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][4]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[6][4]) - 1] = 0
                    field[6][4][int(user_text[6][4]) - 1] = 1
            if active59:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][5] = user_text[6][5][:-1]
                else:
                    user_text[6][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][5]) - 1] = 0
                        field[6][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][5]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[6][5]) - 1] = 0
                    field[6][5][int(user_text[6][5]) - 1] = 1

            if active60:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][6] = user_text[6][6][:-1]
                else:
                    user_text[6][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][6]) - 1] = 0
                        field[6][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][6]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[6][6]) - 1] = 0
                    field[6][6][int(user_text[6][6]) - 1] = 1
            if active61:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][7] = user_text[6][7][:-1]
                else:
                    user_text[6][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][7]) - 1] = 0
                        field[6][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][7]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[6][7]) - 1] = 0
                    field[6][7][int(user_text[6][7]) - 1] = 1
            if active62:
                if event.key == pygame.K_BACKSPACE:
                    user_text[6][8] = user_text[6][8][:-1]
                else:
                    user_text[6][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[6][8]) - 1] = 0
                        field[6][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[6][8]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[6][8]) - 1] = 0
                    field[6][8][int(user_text[6][8]) - 1] = 1

            if active63:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][0] = user_text[7][0][:-1]
                else:
                    user_text[7][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][0]) - 1] = 0
                        field[7][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][0]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[7][0]) - 1] = 0
                    field[7][0][int(user_text[7][0]) - 1] = 1
            if active64:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][1] = user_text[7][1][:-1]
                else:
                    user_text[7][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][1]) - 1] = 0
                        field[7][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][1]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[7][1]) - 1] = 0
                    field[7][1][int(user_text[7][1]) - 1] = 1
            if active65:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][2] = user_text[7][2][:-1]
                else:
                    user_text[7][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][2]) - 1] = 0
                        field[7][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][2]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[7][2]) - 1] = 0
                    field[7][2][int(user_text[7][2]) - 1] = 1

            if active66:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][3] = user_text[7][3][:-1]
                else:
                    user_text[7][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][3]) - 1] = 0
                        field[7][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][3]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[7][3]) - 1] = 0
                    field[7][3][int(user_text[7][3]) - 1] = 1
            if active67:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][4] = user_text[7][4][:-1]
                else:
                    user_text[7][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][4]) - 1] = 0
                        field[7][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][4]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[7][4]) - 1] = 0
                    field[7][4][int(user_text[7][4]) - 1] = 1
            if active68:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][5] = user_text[7][5][:-1]
                else:
                    user_text[7][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][5]) - 1] = 0
                        field[7][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][5]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[7][5]) - 1] = 0
                    field[7][5][int(user_text[7][5]) - 1] = 1

            if active69:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][6] = user_text[7][6][:-1]
                else:
                    user_text[7][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][6]) - 1] = 0
                        field[7][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][6]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[7][6]) - 1] = 0
                    field[7][6][int(user_text[7][6]) - 1] = 1
            if active70:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][7] = user_text[7][7][:-1]
                else:
                    user_text[7][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][7]) - 1] = 0
                        field[7][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][7]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[7][7]) - 1] = 0
                    field[7][7][int(user_text[7][7]) - 1] = 1
            if active71:
                if event.key == pygame.K_BACKSPACE:
                    user_text[7][8] = user_text[7][8][:-1]
                else:
                    user_text[7][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[7][8]) - 1] = 0
                        field[7][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[7][8]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[7][8]) - 1] = 0
                    field[7][8][int(user_text[7][8]) - 1] = 1

            if active72:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][0] = user_text[8][0][:-1]
                else:
                    user_text[8][0] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][0]) - 1] = 0
                        field[8][0][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][0]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[8][0]) - 1] = 0
                    field[8][0][int(user_text[8][0]) - 1] = 1
            if active73:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][1] = user_text[8][1][:-1]
                else:
                    user_text[8][1] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][1]) - 1] = 0
                        field[8][1][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][1]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[8][1]) - 1] = 0
                    field[8][1][int(user_text[8][1]) - 1] = 1
            if active74:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][2] = user_text[8][2][:-1]
                else:
                    user_text[8][2] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][2]) - 1] = 0
                        field[8][2][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][2]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(0, 3):
                            field[i][j][int(user_text[8][2]) - 1] = 0
                    field[8][2][int(user_text[8][2]) - 1] = 1

            if active75:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][3] = user_text[8][3][:-1]
                else:
                    user_text[8][3] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][3]) - 1] = 0
                        field[8][3][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][3]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[8][3]) - 1] = 0
                    field[8][3][int(user_text[8][3]) - 1] = 1
            if active76:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][4] = user_text[8][4][:-1]
                else:
                    user_text[8][4] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][4]) - 1] = 0
                        field[8][4][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][4]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[8][4]) - 1] = 0
                    field[8][4][int(user_text[8][4]) - 1] = 1
            if active77:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][5] = user_text[8][5][:-1]
                else:
                    user_text[8][5] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][5]) - 1] = 0
                        field[8][5][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][5]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(3, 6):
                            field[i][j][int(user_text[8][5]) - 1] = 0
                    field[8][5][int(user_text[8][5]) - 1] = 1

            if active78:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][6] = user_text[8][6][:-1]
                else:
                    user_text[8][6] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][6]) - 1] = 0
                        field[8][6][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][6]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[8][6]) - 1] = 0
                    field[8][6][int(user_text[8][6]) - 1] = 1
            if active79:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][7] = user_text[8][7][:-1]
                else:
                    user_text[8][7] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][7]) - 1] = 0
                        field[8][7][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][7]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[8][7]) - 1] = 0
                    field[8][7][int(user_text[8][7]) - 1] = 1
            if active80:
                if event.key == pygame.K_BACKSPACE:
                    user_text[8][8] = user_text[8][8][:-1]
                else:
                    user_text[8][8] = event.unicode
                    for i in range(0, 9):
                        field[0][i][int(user_text[8][8]) - 1] = 0
                        field[8][8][i] = 0
                    for j in range(0, 9):
                        field[j][0][int(user_text[8][8]) - 1] = 0
                    for i in range(6, 9):
                        for j in range(6, 9):
                            field[i][j][int(user_text[8][8]) - 1] = 0
                    field[8][8][int(user_text[8][8]) - 1] = 1

    screen.fill((30, 30, 30))
    #    pygame.draw.line(screen, (255, 255, 255), (299, 10), (299, 890), 10)
    #    pygame.draw.line(screen, (255, 255, 255), (599, 10), (599, 890), 10)
    #    pygame.draw.line(screen, (255, 255, 255), (10, 599), (890, 599), 10)
    #    pygame.draw.line(screen, (255, 255, 255), (10, 299), (890, 299), 10)

    # set color
    if active:
        color = color_active
    else:
        color = color_passive
    if active1:
        color1 = color_active
    else:
        color1 = color_passive
    if active2:
        color2 = color_active
    else:
        color2 = color_passive
    if active3:
        color3 = color_active
    else:
        color3 = color_passive
    if active4:
        color4 = color_active
    else:
        color4 = color_passive
    if active5:
        color5 = color_active
    else:
        color5 = color_passive
    if active6:
        color6 = color_active
    else:
        color6 = color_passive
    if active7:
        color7 = color_active
    else:
        color7 = color_passive
    if active8:
        color8 = color_active
    else:
        color8 = color_passive
    if active9:
        color9 = color_active
    else:
        color9 = color_passive
    if active10:
        color10 = color_active
    else:
        color10 = color_passive
    if active11:
        color11 = color_active
    else:
        color11 = color_passive
    if active12:
        color12 = color_active
    else:
        color12 = color_passive
    if active13:
        color13 = color_active
    else:
        color13 = color_passive
    if active14:
        color14 = color_active
    else:
        color14 = color_passive
    if active15:
        color15 = color_active
    else:
        color15 = color_passive
    if active16:
        color16 = color_active
    else:
        color16 = color_passive
    if active17:
        color17 = color_active
    else:
        color17 = color_passive
    if active18:
        color18 = color_active
    else:
        color18 = color_passive
    if active19:
        color19 = color_active
    else:
        color19 = color_passive
    if active20:
        color20 = color_active
    else:
        color20 = color_passive
    if active21:
        color21 = color_active
    else:
        color21 = color_passive
    if active22:
        color22 = color_active
    else:
        color22 = color_passive
    if active23:
        color23 = color_active
    else:
        color23 = color_passive
    if active24:
        color24 = color_active
    else:
        color24 = color_passive
    if active25:
        color25 = color_active
    else:
        color25 = color_passive
    if active26:
        color26 = color_active
    else:
        color26 = color_passive
    if active27:
        color27 = color_active
    else:
        color27 = color_passive
    if active28:
        color28 = color_active
    else:
        color28 = color_passive
    if active29:
        color29 = color_active
    else:
        color29 = color_passive
    if active30:
        color30 = color_active
    else:
        color30 = color_passive
    if active31:
        color31 = color_active
    else:
        color31 = color_passive
    if active32:
        color32 = color_active
    else:
        color32 = color_passive
    if active33:
        color33 = color_active
    else:
        color33 = color_passive
    if active34:
        color34 = color_active
    else:
        color34 = color_passive
    if active35:
        color35 = color_active
    else:
        color35 = color_passive
    if active36:
        color36 = color_active
    else:
        color36 = color_passive
    if active37:
        color37 = color_active
    else:
        color37 = color_passive
    if active38:
        color38 = color_active
    else:
        color38 = color_passive
    if active39:
        color39 = color_active
    else:
        color39 = color_passive
    if active40:
        color40 = color_active
    else:
        color40 = color_passive
    if active41:
        color41 = color_active
    else:
        color41 = color_passive
    if active42:
        color42 = color_active
    else:
        color42 = color_passive
    if active43:
        color43 = color_active
    else:
        color43 = color_passive
    if active44:
        color44 = color_active
    else:
        color44 = color_passive
    if active45:
        color45 = color_active
    else:
        color45 = color_passive
    if active46:
        color46 = color_active
    else:
        color46 = color_passive
    if active47:
        color47 = color_active
    else:
        color47 = color_passive
    if active48:
        color48 = color_active
    else:
        color48 = color_passive
    if active49:
        color49 = color_active
    else:
        color49 = color_passive
    if active50:
        color50 = color_active
    else:
        color50 = color_passive
    if active51:
        color51 = color_active
    else:
        color51 = color_passive
    if active52:
        color52 = color_active
    else:
        color52 = color_passive
    if active53:
        color53 = color_active
    else:
        color53 = color_passive
    if active54:
        color54 = color_active
    else:
        color54 = color_passive
    if active55:
        color55 = color_active
    else:
        color55 = color_passive
    if active56:
        color56 = color_active
    else:
        color56 = color_passive
    if active57:
        color57 = color_active
    else:
        color57 = color_passive
    if active58:
        color58 = color_active
    else:
        color58 = color_passive
    if active59:
        color59 = color_active
    else:
        color59 = color_passive
    if active60:
        color60 = color_active
    else:
        color60 = color_passive
    if active61:
        color61 = color_active
    else:
        color61 = color_passive
    if active62:
        color62 = color_active
    else:
        color62 = color_passive
    if active63:
        color63 = color_active
    else:
        color63 = color_passive
    if active64:
        color64 = color_active
    else:
        color64 = color_passive
    if active65:
        color65 = color_active
    else:
        color65 = color_passive
    if active66:
        color66 = color_active
    else:
        color66 = color_passive
    if active67:
        color67 = color_active
    else:
        color67 = color_passive
    if active68:
        color68 = color_active
    else:
        color68 = color_passive
    if active69:
        color69 = color_active
    else:
        color69 = color_passive
    if active70:
        color70 = color_active
    else:
        color70 = color_passive
    if active71:
        color71 = color_active
    else:
        color71 = color_passive
    if active72:
        color72 = color_active
    else:
        color72 = color_passive
    if active73:
        color73 = color_active
    else:
        color73 = color_passive
    if active74:
        color74 = color_active
    else:
        color74 = color_passive
    if active75:
        color75 = color_active
    else:
        color75 = color_passive
    if active76:
        color76 = color_active
    else:
        color76 = color_passive
    if active77:
        color77 = color_active
    else:
        color77 = color_passive
    if active78:
        color78 = color_active
    else:
        color78 = color_passive
    if active79:
        color79 = color_active
    else:
        color79 = color_passive
    if active80:
        color80 = color_active
    else:
        color80 = color_passive

    pygame.draw.rect(screen, color, input_rect, 5)
    pygame.draw.rect(screen, color1, input_rect1, 5)
    pygame.draw.rect(screen, color2, input_rect2, 5)
    pygame.draw.rect(screen, color3, input_rect3, 5)
    pygame.draw.rect(screen, color4, input_rect4, 5)
    pygame.draw.rect(screen, color5, input_rect5, 5)
    pygame.draw.rect(screen, color6, input_rect6, 5)
    pygame.draw.rect(screen, color7, input_rect7, 5)
    pygame.draw.rect(screen, color8, input_rect8, 5)
    pygame.draw.rect(screen, color9, input_rect9, 5)
    pygame.draw.rect(screen, color10, input_rect10, 5)
    pygame.draw.rect(screen, color11, input_rect11, 5)
    pygame.draw.rect(screen, color12, input_rect12, 5)
    pygame.draw.rect(screen, color13, input_rect13, 5)
    pygame.draw.rect(screen, color14, input_rect14, 5)
    pygame.draw.rect(screen, color15, input_rect15, 5)
    pygame.draw.rect(screen, color16, input_rect16, 5)
    pygame.draw.rect(screen, color17, input_rect17, 5)
    pygame.draw.rect(screen, color18, input_rect18, 5)
    pygame.draw.rect(screen, color19, input_rect19, 5)
    pygame.draw.rect(screen, color20, input_rect20, 5)
    pygame.draw.rect(screen, color21, input_rect21, 5)
    pygame.draw.rect(screen, color22, input_rect22, 5)
    pygame.draw.rect(screen, color23, input_rect23, 5)
    pygame.draw.rect(screen, color24, input_rect24, 5)
    pygame.draw.rect(screen, color25, input_rect25, 5)
    pygame.draw.rect(screen, color26, input_rect26, 5)
    pygame.draw.rect(screen, color27, input_rect27, 5)
    pygame.draw.rect(screen, color28, input_rect28, 5)
    pygame.draw.rect(screen, color29, input_rect29, 5)
    pygame.draw.rect(screen, color30, input_rect30, 5)
    pygame.draw.rect(screen, color31, input_rect31, 5)
    pygame.draw.rect(screen, color32, input_rect32, 5)
    pygame.draw.rect(screen, color33, input_rect33, 5)
    pygame.draw.rect(screen, color34, input_rect34, 5)
    pygame.draw.rect(screen, color35, input_rect35, 5)
    pygame.draw.rect(screen, color36, input_rect36, 5)
    pygame.draw.rect(screen, color37, input_rect37, 5)
    pygame.draw.rect(screen, color38, input_rect38, 5)
    pygame.draw.rect(screen, color39, input_rect39, 5)
    pygame.draw.rect(screen, color40, input_rect40, 5)
    pygame.draw.rect(screen, color41, input_rect41, 5)
    pygame.draw.rect(screen, color42, input_rect42, 5)
    pygame.draw.rect(screen, color43, input_rect43, 5)
    pygame.draw.rect(screen, color44, input_rect44, 5)
    pygame.draw.rect(screen, color45, input_rect45, 5)
    pygame.draw.rect(screen, color46, input_rect46, 5)
    pygame.draw.rect(screen, color47, input_rect47, 5)
    pygame.draw.rect(screen, color48, input_rect48, 5)
    pygame.draw.rect(screen, color49, input_rect49, 5)
    pygame.draw.rect(screen, color50, input_rect50, 5)
    pygame.draw.rect(screen, color51, input_rect51, 5)
    pygame.draw.rect(screen, color52, input_rect52, 5)
    pygame.draw.rect(screen, color53, input_rect53, 5)
    pygame.draw.rect(screen, color54, input_rect54, 5)
    pygame.draw.rect(screen, color55, input_rect55, 5)
    pygame.draw.rect(screen, color56, input_rect56, 5)
    pygame.draw.rect(screen, color57, input_rect57, 5)
    pygame.draw.rect(screen, color58, input_rect58, 5)
    pygame.draw.rect(screen, color59, input_rect59, 5)
    pygame.draw.rect(screen, color60, input_rect60, 5)
    pygame.draw.rect(screen, color61, input_rect61, 5)
    pygame.draw.rect(screen, color62, input_rect62, 5)
    pygame.draw.rect(screen, color63, input_rect63, 5)
    pygame.draw.rect(screen, color64, input_rect64, 5)
    pygame.draw.rect(screen, color65, input_rect65, 5)
    pygame.draw.rect(screen, color66, input_rect66, 5)
    pygame.draw.rect(screen, color67, input_rect67, 5)
    pygame.draw.rect(screen, color68, input_rect68, 5)
    pygame.draw.rect(screen, color69, input_rect69, 5)
    pygame.draw.rect(screen, color70, input_rect70, 5)
    pygame.draw.rect(screen, color71, input_rect71, 5)
    pygame.draw.rect(screen, color72, input_rect72, 5)
    pygame.draw.rect(screen, color73, input_rect73, 5)
    pygame.draw.rect(screen, color74, input_rect74, 5)
    pygame.draw.rect(screen, color75, input_rect75, 5)
    pygame.draw.rect(screen, color76, input_rect76, 5)
    pygame.draw.rect(screen, color77, input_rect77, 5)
    pygame.draw.rect(screen, color78, input_rect78, 5)
    pygame.draw.rect(screen, color79, input_rect79, 5)
    pygame.draw.rect(screen, color80, input_rect80, 5)
    pygame.draw.rect(screen, color_submit, submit_rect, )

    text_surface = base_font.render(user_text[0][0], False, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 30, input_rect.y + 25))
    text_surface1 = base_font.render(user_text[0][1], False, (255, 255, 255))
    screen.blit(text_surface1, (input_rect1.x + 30, input_rect1.y + 25))
    text_surface2 = base_font.render(user_text[0][2], False, (255, 255, 255))
    screen.blit(text_surface2, (input_rect2.x + 30, input_rect2.y + 25))
    text_surface3 = base_font.render(user_text[0][3], False, (255, 255, 255))
    screen.blit(text_surface3, (input_rect3.x + 30, input_rect3.y + 25))
    text_surface4 = base_font.render(user_text[0][4], False, (255, 255, 255))
    screen.blit(text_surface4, (input_rect4.x + 30, input_rect4.y + 25))
    text_surface5 = base_font.render(user_text[0][5], False, (255, 255, 255))
    screen.blit(text_surface5, (input_rect5.x + 30, input_rect5.y + 25))
    text_surface6 = base_font.render(user_text[0][6], False, (255, 255, 255))
    screen.blit(text_surface6, (input_rect6.x + 30, input_rect6.y + 25))
    text_surface7 = base_font.render(user_text[0][7], False, (255, 255, 255))
    screen.blit(text_surface7, (input_rect7.x + 30, input_rect7.y + 25))
    text_surface8 = base_font.render(user_text[0][8], False, (255, 255, 255))
    screen.blit(text_surface8, (input_rect8.x + 30, input_rect8.y + 25))
    text_surface9 = base_font.render(user_text[1][0], False, (255, 255, 255))
    screen.blit(text_surface9, (input_rect9.x + 30, input_rect9.y + 25))
    text_surface10 = base_font.render(user_text[1][1], False, (255, 255, 255))
    screen.blit(text_surface10, (input_rect10.x + 30, input_rect10.y + 25))
    text_surface11 = base_font.render(user_text[1][2], False, (255, 255, 255))
    screen.blit(text_surface11, (input_rect11.x + 30, input_rect11.y + 25))
    text_surface12 = base_font.render(user_text[1][3], False, (255, 255, 255))
    screen.blit(text_surface12, (input_rect12.x + 30, input_rect12.y + 25))
    text_surface13 = base_font.render(user_text[1][4], False, (255, 255, 255))
    screen.blit(text_surface13, (input_rect13.x + 30, input_rect13.y + 25))
    text_surface14 = base_font.render(user_text[1][5], False, (255, 255, 255))
    screen.blit(text_surface14, (input_rect14.x + 30, input_rect14.y + 25))
    text_surface15 = base_font.render(user_text[1][6], False, (255, 255, 255))
    screen.blit(text_surface15, (input_rect15.x + 30, input_rect15.y + 25))
    text_surface16 = base_font.render(user_text[1][7], False, (255, 255, 255))
    screen.blit(text_surface16, (input_rect16.x + 30, input_rect16.y + 25))
    text_surface17 = base_font.render(user_text[1][8], False, (255, 255, 255))
    screen.blit(text_surface17, (input_rect17.x + 30, input_rect17.y + 25))
    text_surface18 = base_font.render(user_text[2][0], False, (255, 255, 255))
    screen.blit(text_surface18, (input_rect18.x + 30, input_rect18.y + 25))
    text_surface19 = base_font.render(user_text[2][1], False, (255, 255, 255))
    screen.blit(text_surface19, (input_rect19.x + 30, input_rect19.y + 25))
    text_surface20 = base_font.render(user_text[2][2], False, (255, 255, 255))
    screen.blit(text_surface20, (input_rect20.x + 30, input_rect20.y + 25))
    text_surface21 = base_font.render(user_text[2][3], False, (255, 255, 255))
    screen.blit(text_surface21, (input_rect21.x + 30, input_rect21.y + 25))
    text_surface22 = base_font.render(user_text[2][4], False, (255, 255, 255))
    screen.blit(text_surface22, (input_rect22.x + 30, input_rect22.y + 25))
    text_surface23 = base_font.render(user_text[2][5], False, (255, 255, 255))
    screen.blit(text_surface23, (input_rect23.x + 30, input_rect23.y + 25))
    text_surface24 = base_font.render(user_text[2][6], False, (255, 255, 255))
    screen.blit(text_surface24, (input_rect24.x + 30, input_rect24.y + 25))
    text_surface25 = base_font.render(user_text[2][7], False, (255, 255, 255))
    screen.blit(text_surface25, (input_rect25.x + 30, input_rect25.y + 25))
    text_surface26 = base_font.render(user_text[2][8], False, (255, 255, 255))
    screen.blit(text_surface26, (input_rect26.x + 30, input_rect26.y + 25))
    text_surface27 = base_font.render(user_text[3][0], False, (255, 255, 255))
    screen.blit(text_surface27, (input_rect27.x + 30, input_rect27.y + 25))
    text_surface28 = base_font.render(user_text[3][1], False, (255, 255, 255))
    screen.blit(text_surface28, (input_rect28.x + 30, input_rect28.y + 25))
    text_surface29 = base_font.render(user_text[3][2], False, (255, 255, 255))
    screen.blit(text_surface29, (input_rect29.x + 30, input_rect29.y + 25))
    text_surface30 = base_font.render(user_text[3][3], False, (255, 255, 255))
    screen.blit(text_surface30, (input_rect30.x + 30, input_rect30.y + 25))
    text_surface31 = base_font.render(user_text[3][4], False, (255, 255, 255))
    screen.blit(text_surface31, (input_rect31.x + 30, input_rect31.y + 25))
    text_surface32 = base_font.render(user_text[3][5], False, (255, 255, 255))
    screen.blit(text_surface32, (input_rect32.x + 30, input_rect32.y + 25))
    text_surface33 = base_font.render(user_text[3][6], False, (255, 255, 255))
    screen.blit(text_surface33, (input_rect33.x + 30, input_rect33.y + 25))
    text_surface34 = base_font.render(user_text[3][7], False, (255, 255, 255))
    screen.blit(text_surface34, (input_rect34.x + 30, input_rect34.y + 25))
    text_surface35 = base_font.render(user_text[3][8], False, (255, 255, 255))
    screen.blit(text_surface35, (input_rect35.x + 30, input_rect35.y + 25))
    text_surface36 = base_font.render(user_text[4][0], False, (255, 255, 255))
    screen.blit(text_surface36, (input_rect36.x + 30, input_rect36.y + 25))
    text_surface37 = base_font.render(user_text[4][1], False, (255, 255, 255))
    screen.blit(text_surface37, (input_rect37.x + 30, input_rect37.y + 25))
    text_surface38 = base_font.render(user_text[4][2], False, (255, 255, 255))
    screen.blit(text_surface38, (input_rect38.x + 30, input_rect38.y + 25))
    text_surface39 = base_font.render(user_text[4][3], False, (255, 255, 255))
    screen.blit(text_surface39, (input_rect39.x + 30, input_rect39.y + 25))
    text_surface40 = base_font.render(user_text[4][4], False, (255, 255, 255))
    screen.blit(text_surface40, (input_rect40.x + 30, input_rect40.y + 25))
    text_surface41 = base_font.render(user_text[4][5], False, (255, 255, 255))
    screen.blit(text_surface41, (input_rect41.x + 30, input_rect41.y + 25))
    text_surface42 = base_font.render(user_text[4][6], False, (255, 255, 255))
    screen.blit(text_surface42, (input_rect42.x + 30, input_rect42.y + 25))
    text_surface43 = base_font.render(user_text[4][7], False, (255, 255, 255))
    screen.blit(text_surface43, (input_rect43.x + 30, input_rect43.y + 25))
    text_surface44 = base_font.render(user_text[4][8], False, (255, 255, 255))
    screen.blit(text_surface44, (input_rect44.x + 30, input_rect44.y + 25))
    text_surface45 = base_font.render(user_text[5][0], False, (255, 255, 255))
    screen.blit(text_surface45, (input_rect45.x + 30, input_rect45.y + 25))
    text_surface46 = base_font.render(user_text[5][1], False, (255, 255, 255))
    screen.blit(text_surface46, (input_rect46.x + 30, input_rect46.y + 25))
    text_surface47 = base_font.render(user_text[5][2], False, (255, 255, 255))
    screen.blit(text_surface47, (input_rect47.x + 30, input_rect47.y + 25))
    text_surface48 = base_font.render(user_text[5][3], False, (255, 255, 255))
    screen.blit(text_surface48, (input_rect48.x + 30, input_rect48.y + 25))
    text_surface49 = base_font.render(user_text[5][4], False, (255, 255, 255))
    screen.blit(text_surface49, (input_rect49.x + 30, input_rect49.y + 25))
    text_surface50 = base_font.render(user_text[5][5], False, (255, 255, 255))
    screen.blit(text_surface50, (input_rect50.x + 30, input_rect50.y + 25))
    text_surface51 = base_font.render(user_text[5][6], False, (255, 255, 255))
    screen.blit(text_surface51, (input_rect51.x + 30, input_rect51.y + 25))
    text_surface52 = base_font.render(user_text[5][7], False, (255, 255, 255))
    screen.blit(text_surface52, (input_rect52.x + 30, input_rect52.y + 25))
    text_surface53 = base_font.render(user_text[5][8], False, (255, 255, 255))
    screen.blit(text_surface53, (input_rect53.x + 30, input_rect53.y + 25))
    text_surface54 = base_font.render(user_text[6][0], False, (255, 255, 255))
    screen.blit(text_surface54, (input_rect54.x + 30, input_rect54.y + 25))
    text_surface55 = base_font.render(user_text[6][1], False, (255, 255, 255))
    screen.blit(text_surface55, (input_rect55.x + 30, input_rect55.y + 25))
    text_surface56 = base_font.render(user_text[6][2], False, (255, 255, 255))
    screen.blit(text_surface56, (input_rect56.x + 30, input_rect56.y + 25))
    text_surface57 = base_font.render(user_text[6][3], False, (255, 255, 255))
    screen.blit(text_surface57, (input_rect57.x + 30, input_rect57.y + 25))
    text_surface58 = base_font.render(user_text[6][4], False, (255, 255, 255))
    screen.blit(text_surface58, (input_rect58.x + 30, input_rect58.y + 25))
    text_surface59 = base_font.render(user_text[6][5], False, (255, 255, 255))
    screen.blit(text_surface59, (input_rect59.x + 30, input_rect59.y + 25))
    text_surface60 = base_font.render(user_text[6][6], False, (255, 255, 255))
    screen.blit(text_surface60, (input_rect60.x + 30, input_rect60.y + 25))
    text_surface61 = base_font.render(user_text[6][7], False, (255, 255, 255))
    screen.blit(text_surface61, (input_rect61.x + 30, input_rect61.y + 25))
    text_surface62 = base_font.render(user_text[6][8], False, (255, 255, 255))
    screen.blit(text_surface62, (input_rect62.x + 30, input_rect62.y + 25))
    text_surface63 = base_font.render(user_text[7][0], False, (255, 255, 255))
    screen.blit(text_surface63, (input_rect63.x + 30, input_rect63.y + 25))
    text_surface64 = base_font.render(user_text[7][1], False, (255, 255, 255))
    screen.blit(text_surface64, (input_rect64.x + 30, input_rect64.y + 25))
    text_surface65 = base_font.render(user_text[7][2], False, (255, 255, 255))
    screen.blit(text_surface65, (input_rect65.x + 30, input_rect65.y + 25))
    text_surface66 = base_font.render(user_text[7][3], False, (255, 255, 255))
    screen.blit(text_surface66, (input_rect66.x + 30, input_rect66.y + 25))
    text_surface67 = base_font.render(user_text[7][4], False, (255, 255, 255))
    screen.blit(text_surface67, (input_rect67.x + 30, input_rect67.y + 25))
    text_surface68 = base_font.render(user_text[7][5], False, (255, 255, 255))
    screen.blit(text_surface68, (input_rect68.x + 30, input_rect68.y + 25))
    text_surface69 = base_font.render(user_text[7][6], False, (255, 255, 255))
    screen.blit(text_surface69, (input_rect69.x + 30, input_rect69.y + 25))
    text_surface70 = base_font.render(user_text[7][7], False, (255, 255, 255))
    screen.blit(text_surface70, (input_rect70.x + 30, input_rect70.y + 25))
    text_surface71 = base_font.render(user_text[7][8], False, (255, 255, 255))
    screen.blit(text_surface71, (input_rect71.x + 30, input_rect71.y + 25))
    text_surface72 = base_font.render(user_text[8][0], False, (255, 255, 255))
    screen.blit(text_surface72, (input_rect72.x + 30, input_rect72.y + 25))
    text_surface73 = base_font.render(user_text[8][1], False, (255, 255, 255))
    screen.blit(text_surface73, (input_rect73.x + 30, input_rect73.y + 25))
    text_surface74 = base_font.render(user_text[8][2], False, (255, 255, 255))
    screen.blit(text_surface74, (input_rect74.x + 30, input_rect74.y + 25))
    text_surface75 = base_font.render(user_text[8][3], False, (255, 255, 255))
    screen.blit(text_surface75, (input_rect75.x + 30, input_rect75.y + 25))
    text_surface76 = base_font.render(user_text[8][4], False, (255, 255, 255))
    screen.blit(text_surface76, (input_rect76.x + 30, input_rect76.y + 25))
    text_surface77 = base_font.render(user_text[8][5], False, (255, 255, 255))
    screen.blit(text_surface77, (input_rect77.x + 30, input_rect77.y + 25))
    text_surface78 = base_font.render(user_text[8][6], False, (255, 255, 255))
    screen.blit(text_surface78, (input_rect78.x + 30, input_rect78.y + 25))
    text_surface79 = base_font.render(user_text[8][7], False, (255, 255, 255))
    screen.blit(text_surface79, (input_rect79.x + 30, input_rect79.y + 25))
    text_surface80 = base_font.render(user_text[8][8], False, (255, 255, 255))
    screen.blit(text_surface80, (input_rect80.x + 30, input_rect80.y + 25))

    submit = base_font.render(text, False, (255, 255, 255))
    screen.blit(submit, (submit_rect.x + 350, submit_rect.y + 25))

    pygame.display.flip()
    clock.tick(60)

