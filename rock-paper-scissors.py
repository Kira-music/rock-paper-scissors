from pygame import*

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))    
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
display.set_caption('rock-paper-scissors')

rock = GameSprite('rock.png', 100, 350, 90, 100)
scissors = GameSprite('scissors.png', 300, 350, 90, 100)
paper = GameSprite('paper.png', 500, 350, 90, 100)

clock = time.Clock()
FPS = 60

wait = 0

font1 = font.SysFont('Arial', 36)

game = True

finish = False
while game:
    if not finish:
        text_rock = font1.render('Вы выбрали камень', 1, (0, 0, 0))
        text_scissors = font1.render('Вы выбрали ножницы', 1, (0, 0, 0))
        text_paper = font1.render('Вы выбрали бумагу', 1, (0, 0, 0))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_KP1]:
            window.blit(text_rock, (200, 250))
        if keys_pressed[K_KP2]:
            window.blit(text_scissors, (200, 250))
        if keys_pressed[K_KP3]:
            window.blit(text_paper, (200, 250))
        if wait == 0:
            wait = 80
            window.fill((255, 255, 255))

            paper.reset()

            rock.reset()

            scissors.reset()

            

            
        else:
            wait -= 1

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()
