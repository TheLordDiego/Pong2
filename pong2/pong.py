import pygame
import random

pygame.init()

"""Colors used in the game"""
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

"""Maximum Score Set"""
SCORE_MAX = 2

"""Game Variables"""
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MyPong - PyGame Edition')

"""Score text"""
score_font = pygame.font.Font('assets/press_start_font.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

"""Victory text"""
victory_font = pygame.font.Font('assets/press_start_font.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

"""Sound effects"""
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/arcade_bleep_sound.wav')

"""Player 1 Controls and Assets"""
player_1 = pygame.image.load('assets/player.png')
player_1_y = 300
player_1_x = 50
player_1_move_up = False
player_1_move_down = False

"""CPU Controls and Assets"""
player_2 = pygame.image.load('assets/player.png')
player_2_y = 300
player_2_x = 1180
player_2_move_up = False
player_2_move_down = False

"""Game's Ball"""
ball = pygame.image.load('assets/ball.png')
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 0

"""Game's score"""
score_1 = 0
score_2 = 0

"""Game loop"""
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        """Keystroke events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    """Victory condition"""
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        """Clear screen"""
        screen.fill(COLOR_BLACK)

        """Ball collision with the wall"""
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        """Ball collision with the player 1's paddle"""
        if 75 < ball_x < 100:
            if player_1_y < ball_y + 25:
                if player_1_y + 150 > ball_y:
                    ball_dx *= - 1
                    ball_dx += 1
                    ball_dy = random.choice([0, 1, 2, 3, 4, 5, ball_dx])
                    bounce_sound_effect.play()

        """Ball collision with the CPU's paddle"""
        if 1185 > ball_x > 1160:
            if player_2_y < ball_y + 25:
                if player_2_y + 150 > ball_y:
                    ball_dx *= - 1
                    ball_dx -= 1
                    ball_dy = random.choice([0, 1, 2, 3, 4, 5, ball_dx])
                    bounce_sound_effect.play()

        """Scoring points"""
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dy = 0
            ball_dx = - 5
            player_1_x = 50
            player_2_x = 1180
            score_2 += 1
            scoring_sound_effect.play()

        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dy = 0
            ball_dx = 5
            player_1_x = 50
            player_2_x = 1180
            score_1 += 1
            scoring_sound_effect.play()

        """Ball movement"""
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        """Player 1 up movement"""
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        """Player 1 down movement"""
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        """CPU up movement"""
        if player_2_move_up:
            player_2_y -= 5
        else:
            player_2_y += 0

        """CPU down movement"""
        if player_1_move_down:
            player_2_y += 5
        else:
            player_2_y += 0

        """Player 1 collides with upper wall"""
        if player_1_y <= 0:
            player_1_y = 0

        # Player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        """CPU Artificial Intelligence"""
        if player_2_y > ball_y:
            player_2_move_up = True
            player_2_move_down = False
        if player_2_y < ball_y:
            player_2_move_up = False
            player_2_move_down = True
        if player_2_y == ball_y:
            player_2_move_up = False
            player_2_move_down = False

        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        """Update score hud"""
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        """Drawing objects"""
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        """Drawing victory"""
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    """Update screen"""
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
