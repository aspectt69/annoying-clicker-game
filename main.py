import pgzrun
import os
import random

WIDTH = 800
HEIGHT = 600
# Centers the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

clicks = 0
floating_scores = []

button = Actor("redbutton")
button.pos = (WIDTH // 2, (3/4) * HEIGHT)
button.multiplier = 1

redarrow = Actor("redarrow")
redarrow.x = (WIDTH // 2)
redarrow.y = (HEIGHT // 2.5)

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
    if button.collidepoint(pos):
        if random.randint(1, 15) != 15:
            print("Clicked button")
            clicks += 1 * button.multiplier
            floating_scores.append(Floating_score(f"+{1 * button.multiplier}", pos[0], pos[1], 1))
        else:
            print("Click missed")
            floating_scores.append(Floating_score("Oops", pos[0], pos[1], 2, (255, 0, 0), 45, 7))

def draw():
    screen.clear()
    screen.fill((255,255,255))
    screen.draw.text("Clicks: " + str(clicks), (20, 20), color = (0,0,0), fontsize = 50)
    screen.draw.text("Click here by the way", (redarrow.x - redarrow.width // 2 - 55, redarrow.y - redarrow.height // 2 - 25), color = (0,0,0,), fontsize = 30)
    redarrow.draw()
    button.draw()

    for score in floating_scores[:]:
        score.draw()
        if score.update():
            floating_scores.remove(score)

def update():
    pass

pgzrun.go()