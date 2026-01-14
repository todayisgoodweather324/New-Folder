import time
from rich.console import Console
from rich.panel import Panel
import pygame
import os


class M:
    def play_music(self):
        os.chdir("c://Users/hatak/Music_Folder/")
        pygame.mixer.init()
        pygame.mixer.music.load("background-music-381788 (1).mp3")
        pygame.mixer.music.play(1)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()


user_input = Console().input(
    Panel("Please type the seconds", style="black on green", padding=1))
user_input = int(user_input)
for x in range(user_input, 1, -1):
    seconds = x % 60
    minutes = x // 60 % 60
    hour = x // 60 // 60 % 24
    Console().print(Panel(f"{hour} {minutes} {seconds}",
                          style="black on green", padding=1))
    time.sleep(1)
print("Time's up!")
M().play_music()
