import pgzrun
import pygame
import os
import random

WIDTH = 800
HEIGHT = 600
# Centers the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

clicks = 0
upgrade1cost = 1
secondsplaying = 0
minutesplaying = 0
hoursplaying = 0
floating_scores = []

button = Actor("redbutton")
button.pos = (WIDTH // 2, (3/4) * HEIGHT)
button.multiplier = 1

redarrow = Actor("redarrow")
redarrow.x = (WIDTH // 2)
redarrow.y = (HEIGHT // 2.5)

upgradebutton1 = Actor("upgradebutton1")
upgradebutton1.x = 95
upgradebutton1.y = 85

class Floating_score():
    def __init__(self, text, x, y, size, color=(0,0,0), duration=30, offset=5):
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.alpha = 255
        self.duration = duration
        self.offset = offset
        self.timer = 0
        self.color = color

    def update(self):
        self.y -= self.offset / 2
        self.alpha -= 255 / (self.duration * 1.5)
        self.timer += 1
        self.offset = self.offset - 0.1
        if self.offset <= 0:
            self.offset += 0.1

        if self.alpha <= 0:
            return True
        return False
    
    def draw(self):
        screen.draw.text(self.text, (self.x - len(self.text), self.y), color=self.color, fontsize=50, alpha=self.alpha, owidth=0.5, ocolor="white")




def on_mouse_down(pos):
    global clicks
    global upgrade1cost
    if button.collidepoint(pos):
        if random.randint(1, 15) != 15:
            print("Clicked button")
            clicks += 1 * button.multiplier
            floating_scores.append(Floating_score(f"+{round(1 * button.multiplier, 1)}", pos[0], pos[1], 1))
        else:
            print("Click missed")
            floating_scores.append(Floating_score("Oops", pos[0], pos[1], 2, (255, 0, 0), 45, 7))
    if upgradebutton1.collidepoint(pos):
        if clicks >= upgrade1cost:
            if random.randint(1, 10) != 10:
                print("Upgraded")
                button.multiplier = button.multiplier + button.multiplier * 0.15
                clicks = clicks - upgrade1cost
                upgrade1cost = upgrade1cost * 1.25
            else:
                print("Upgrade Moved")
                upgradebutton1.x = random.randint(95, 595)
                upgradebutton1.y = random.randint(85, 110)
        else:
            print("Not enough to upgrade")

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.draw.text("Clicks: " + str(round(clicks)), (20, 20), color = (0,0,0), fontsize = 50)
    screen.draw.text("Click here by the way", (redarrow.x - redarrow.width // 2 - 55, redarrow.y - redarrow.height // 2 - 25), color=(0,0,0,), fontsize=30)
    screen.draw.text("Random events happen", (20, 470), color=(0,0,0), fontsize=25)
    screen.draw.text("every 30 seconds!", (20, 490), color=(0,0,0), fontsize=25)
    screen.draw.text("Time spent playing:", (20, 520), color=(0,0,0), fontsize=20)
    screen.draw.text("Hours: " + str(hoursplaying), (20, 540), color=(0,0,0), fontsize=20)
    screen.draw.text("Minutes: " + str(minutesplaying), (20, 560), color=(0,0,0), fontsize=20)
    screen.draw.text("Seconds: " + str(round(secondsplaying)), (20, 580), color=(0,0,0), fontsize=20)

    upgradebutton1.draw()
    upgrade1_text = f"Upgrade: {round(upgrade1cost)}"
    font = pygame.font.Font(None, 30)
    text_width, text_height = font.size(upgrade1_text)
    text_x = upgradebutton1.x - (text_width // 2)
    text_y = upgradebutton1.y - (text_height // 2)
    screen.draw.text(upgrade1_text, (text_x, text_y), color=(0, 0, 0), fontsize=30, ocolor="white", owidth=0.5)

    redarrow.draw()
    button.draw()

    for score in floating_scores[:]:
        score.draw()
        if score.update():
            floating_scores.remove(score)

def update():
    global secondsplaying, minutesplaying, hoursplaying
    secondsplaying += 1 / 60
    if secondsplaying == 60:
        secondsplaying = 0
        minutesplaying += 1
    elif minutesplaying == 60:
        minutesplaying = 0
        hoursplaying += 1

pgzrun.go()