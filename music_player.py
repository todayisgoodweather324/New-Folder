import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pygame")
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import time
import pygame


1
clock = pygame.time.Clock()
pygame.mixer.init()
music = True
def play_music(song):
    os.chdir(folder)
    
    global music
    while music:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        if pygame.mixer.music.get_busy():
            print("Playing...")
            command = input("Please type 'pause', 'unpause', 'stop', or 'q'.\n").lower()
            
            if command == "pause":
                pygame.mixer.music.pause()
                print("Music paused")
                command = input("Please type 'pause', 'unpause', 'stop', or 'q'.\n")

            elif command == "unpause":
                pygame.mixer.music.unpause()
                print("Music resumed")
                command = input("Please type 'pause', 'unpause', 'stop', or 'q'.\n")

            elif command == "stop":
                pygame.mixer.music.stop()
                print("Music stopped.")
                command = input("Please type 'pause', 'unpause', 'stop', or 'q'.\n")
                os.system("cls")
            elif command == "play":
                continue
            elif command == "q":
                pygame.mixer.music.stop()
                music = False
                print("Exiting")

            else:
                print("Unknown command")
                command = input("Please type 'pause', 'unpause', 'stop', or 'q'.\n")
        else:
            print("Music finished playing.")
            music = False

    pygame.mixer.music.stop()


UI = """1. Listen music
2. Play 'Dodge-Obstacles' game
3. Quit"""
folder = "michael-jackson-dangerous_202403"
songs = [x for x in os.listdir(folder) if x.endswith(".mp3")]
def list1():
    for song in songs:
        print(song)

if __name__ == "__main__":
    while True:
        try:
            print(UI)
            user_input = input("Please type '1' or '2' or '3':\n")
            if user_input == "1":
                list1()
                time.sleep(1)
                user_input = (input("Please select your song:\n"))
                if not user_input.isdigit():
                    while True:
                        print("Please type only digits.")
                        time.sleep(1)
                        user_input = input("Please select your song:\n")
                        if bool(user_input) == user_input.isdigit():
                            break
                        else:
                            print("Please type only digits.1")
                        continue
                user_input = int(user_input) - 1
                if user_input == 0:
                    play_music(songs[user_input])
                elif user_input == 1:
                    play_music(songs[user_input])
                elif user_input == 2:
                    play_music(songs[user_input])
                elif user_input == 3:
                    play_music(songs[user_input])
                elif user_input == 4:
                    play_music(songs[user_input])
                elif user_input == 5:
                    play_music(songs[user_input])
                elif user_input == 6:
                    play_music(songs[user_input])
                elif user_input == 7:
                    play_music(songs[user_input])
                elif user_input == 8:
                    play_music(songs[user_input])
                elif user_input == 9:
                    play_music(songs[user_input])
                elif user_input == 10:
                    play_music(songs[user_input])
                elif user_input == 11:
                    play_music(songs[user_input])
                elif user_input == 11+1:
                    play_music(songs[user_input])
                elif user_input == 1+12:
                    play_music(songs[user_input])
                elif (user_input) == "q":
                    print("Goodbye!👋")
                    import sys
                    sys.exit()
            elif user_input == "2":
                import random
                pygame.init()
                screen = pygame.display.set_mode((400, 400))
                pygame.display.set_caption("Dodge-Obstacles")
                player = pygame.Rect(40, 40, 40, 40)
                enemy = pygame.Rect(random.randint(0, 350), random.randint(0, 350), 40, 40)
                player_speed = 5
                enemy_speed = 2
                running = True
                game_over = False
                font = pygame.font.Font(None, 48)
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    if not game_over:

                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_RIGHT]:
                            player.x += player_speed
                        if keys[pygame.K_LEFT]:
                            player.x -= player_speed
                        if keys[pygame.K_UP]:
                            player.y -= player_speed
                        if keys[pygame.K_DOWN]:
                            player.y += player_speed
                        player.clamp_ip(screen.get_rect())
                        if enemy.x < player.x:
                            enemy.x += enemy_speed
                        if enemy.x > player.x:
                            enemy.x -= enemy_speed
                        if enemy.y < player.y:
                            enemy.y += enemy_speed
                        if enemy.y > player.y:
                            enemy.y -= enemy_speed

                        if player.colliderect(enemy):
                            game_over = True

                        screen.fill((0, 0, 0))
                        pygame.draw.rect(screen, (255, 0, 0), enemy)                
                        pygame.draw.rect(screen, (0, 0, 255), player)


                    else:
                        screen.fill((177, 0, 255))
                        text = font.render("Game Over~", True, (255, 255, 255))
                        text_rect = text.get_rect(center=(200, 200))
                        screen.blit(text, text_rect)
                    pygame.display.flip()
                    pygame.time.Clock().tick(60)
                pygame.quit()
            elif user_input == "3":
                break
            else:
                print("Please type only '1' or '2' or 'q'.")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Press 'q' to quit.")