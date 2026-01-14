from rich.panel import Panel
import time
from rich.console import Console
import pygame
import os
console = Console()
user_input = console.input(Panel("Hello, please type your name here:",
                                 style="black on green", padding=1))


def greet(user_name):
    print("Hello, ", user_name.title())


greet(user_input)
UI = """1. Let's do some mathematics!
2. Let's listen to this music!
"""
if __name__ == "__main__":
    print(UI)
    while True:
        user_input = console.input(
            Panel("Please type your choice here:", style="black on green", padding=1))
        if user_input == "1":
            while True:
                operator = console.input(
                    Panel("Please type your operator here:", style="black on green", padding=1))
                num1 = console.input(
                    Panel("Please type your number here:", style="black on green", padding=1))
                num1 = int(num1)
                num2 = console.input(
                    Panel("Please type another number here:", style="black on green", padding=1))
                num2 = int(num2)
                if operator == "+":
                    total = num1 + num2
                    console.print(
                        Panel(f"The total is {total}", style="black on green", padding=1))
                elif operator == "-":
                    total = num1 - num2
                    console.print(
                        Panel(f"The total is {total}", style="black on green", padding=1))
                elif operator == "*":
                    total = num1 * num2
                    console.print(
                        Panel(f"The total is {total}", style="black on green", padding=1))
                elif operator == "/":
                    total = num1 / num2
                    console.print(
                        Panel(f"The total is {total}", style="black on green", padding=1))
                elif operator == "q" or num1 == "q" or num2 == "q":
                    break

        elif user_input == "2":
            os.chdir("c://Users/hatak/Music_Folder")
            pygame.init()

            pygame.mixer.music.load(
                "happy-kids-background-music-456466.mp3", "Standard recording 11.mp3")
            pygame.mixer.music.play(1)
            console.input(Panel("Playing..."))
            pygame.mixer.music.stop()
        elif user_input == "q":
            break
        elif user_input == "3":
            while True:
                console.print(Panel("Let's play with colors!",
                              style="black on green", padding=1))
                user_input = console.input(
                    Panel("Type something here:", style="black on green", padding=1))
                if user_input == "cls":
                    os.system("cls")
                elif user_input == "green":
                    print("\033[32mType something here.")
                elif user_input == "q":
                    break
