import pygame
import sys
import random

# Inicialize o Pygame
pygame.init()

# Defina as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Defina o tamanho da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Esquiva")

# Defina a classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Limita o movimento do jogador dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Defina a classe do obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Crie grupos de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Crie o jogador
player = Player()
all_sprites.add(player)

# Crie os obstáculos
for _ in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Crie um relógio para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    # Mantenha o loop na taxa de atualização desejada
    clock.tick(60)

    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar
    all_sprites.update()

    # Verificar colisões entre jogador e obstáculos
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        running = False  # Fim do jogo se houver colisão

    # Limpar a tela
    screen.fill(BLACK)

    # Desenhar todos os sprites
    all_sprites.draw(screen)

    # Atualizar a tela
    pygame.display.flip()

# Fim do jogo
pygame.quit()
sys.exit()
