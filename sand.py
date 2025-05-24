import pygame

class Grid:
    def __init__(self, width, height):
        self.width = height
        self.height = width
        self.grid = [[0 for _ in range(height)] for _ in range(width)]

    def clear(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def set(self, x, y, color):
        self.grid[x][y] = color

    def swap(self, x1, y1, x2, y2):
        temp = self.grid[x1][y1]
        self.grid[x1][y1] = self.grid[x2][y2]
        self.grid[x2][y2] = temp

    def is_empty(self, x, y):
        return self.grid[x][y] == 0

    def get_color(self, x, y):
        return self.grid[x][y]


WIDTH = 200
HEIGHT = 160

grid = Grid(WIDTH, HEIGHT)

def update_pixel(x, y):
    if grid.is_empty(x, y+1):
        grid.swap(x, y, x, y+1)
    elif  x - 1 >= 0 and grid.is_empty(x-1, y+1):
        grid.swap(x, y, x-1, y+1)
    elif x + 1 <= WIDTH - 1 and grid.is_empty(x+1, y+1):
        grid.swap(x, y, x+1, y+1)

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sand")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH > event.pos[0] >= 0 and HEIGHT > event.pos[1] >= 0:
                grid.set(event.pos[0], event.pos[1], pygame.Color("white"))

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        (x, y) = pygame.mouse.get_pos()
        if WIDTH > x >= 0 and HEIGHT > y >= 0:
            grid.set(x, y, pygame.Color("white"))

    for col in range(grid.width - 2, -1, -1):
        for row in range(grid.height - 1, -1, -1):
            update_pixel(row, col)

    for col in range(grid.width):
        for row in range(grid.height):
            screen.set_at((row, col), grid.get_color(row, col))

    pygame.display.flip()
    clock.tick(120)


pygame.quit()
