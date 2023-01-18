import pygame # instalar pygame
import randon

# formato das peças:
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

formatos = [S, Z, I, O, J, L, T] # index de 0 a 6
cor_formatos = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

largura_tela = 800
altura_tela = 700
largura_jogo = 300
altura_jogo = 600
tamanho_bloco = 30

topo_esquerdo_x = (largura_tela - largura_jogo) // 2
topo_esquerdo_y = largura_tela - largura_jogo

class Piece(object): 
    def __init__(self, x, y, shapes):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = cor_formatos[formatos.index(shape)]
        self.rotation = 0

def create_grid({}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)] # "x" pode ser substituido por "_"

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format():
    pass

def valid_space():
    pass

def check_lost():
    pass

def get_shape():
    return Piece(5, 0, random.choice(formatos))

def draw_text_middle():
    pass

def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (topo_esquerdo_x + j*tamanho_bloco, topo_esquerdo_y + i*tamanho_bloco, tamanho_bloco, tamanho_bloco), 0)

    pygame.draw.rect(surface, (255,0,0), (topo_esquerdo_x, topo_esquerdo_y, largura_jogo, altura_jogo), 4)

def clear_rows():
    pass

def draw_next_shape():
    pass

def draw_windows(surface, grid):
    surface.fill((0,0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255,255,255))

    surface.blit(label, (topo_esquerdo_x + largura_jogo/2 - (label.get_width()/2), 30))
    draw_grid(surface, grid)
    pygame.display.update()

def main():

    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDWN
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y +=1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece += 1

        draw_window(surface, grid)

def main menu():
    pass

win = pygame.display.set_mode((largura_tela, altura_tela))
main menu()