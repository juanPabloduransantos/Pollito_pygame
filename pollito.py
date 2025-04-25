import pygame
import sys

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
gris = (127, 127, 127)
amarillo = (255, 255, 0)
blanco = (255, 255, 255)
negro = (0, 0, 0)

pygame.init()
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pollito")
clock = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36) 

cuadrito_size = 20
cuadrito_x = 240  
cuadrito_y = 480
cuadrito_speed = 5

vidas = 3  

cuadros_rojos = [
    pygame.Rect(480, 213, 20, 20),  
    pygame.Rect(400, 213, 20, 20),  
    pygame.Rect(0, 340, 20, 20),    
    pygame.Rect(100, 340, 20, 20),  
]

cuadros_rojos_velocidad = [-2, -3, 2, 3] 

def mover_cuadrito():
    global cuadrito_x, cuadrito_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cuadrito_x > 0:
        cuadrito_x -= cuadrito_speed
    if keys[pygame.K_RIGHT] and cuadrito_x < 480:
        cuadrito_x += cuadrito_speed
    if keys[pygame.K_UP] and cuadrito_y > 0:
        cuadrito_y -= cuadrito_speed
    if keys[pygame.K_DOWN] and cuadrito_y < 480:
        cuadrito_y += cuadrito_speed

def mover_cuadros_rojos():
    for i, cuadro in enumerate(cuadros_rojos):
        cuadro.x += cuadros_rojos_velocidad[i]

        if cuadro.x > 500:
            cuadro.x = -20
        elif cuadro.x < -20:
            cuadro.x = 500

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    pygame.draw.rect(ventana, verde, (0, 0, 500, 500))
    pygame.draw.rect(ventana, azul, (300, 50, 50, 0))
    pygame.draw.rect(ventana, amarillo, (80, 50, 80, 80))
    pygame.draw.rect(ventana, amarillo, (200, 50, 80, 80))
    pygame.draw.rect(ventana, amarillo, (320, 50, 80, 80))
    pygame.draw.rect(ventana, azul, (70, 30, 100, 20))
    pygame.draw.rect(ventana, azul, (190, 30, 100, 20))
    pygame.draw.rect(ventana, azul, (310, 30, 100, 20))
    pygame.draw.rect(ventana, azul, (500, 50, 50, 0))
    pygame.draw.rect(ventana, gris, (0, 144, 500, 300))
    pygame.draw.line(ventana, amarillo, (0, 223), (70, 223), 5)
    pygame.draw.line(ventana, amarillo, (100, 223), (200, 223), 5)
    pygame.draw.line(ventana, amarillo, (223, 223), (310, 223), 5)
    pygame.draw.line(ventana, amarillo, (340, 223), (400, 223), 5)
    pygame.draw.line(ventana, amarillo, (440, 223), (500, 223), 5)
    pygame.draw.line(ventana, amarillo, (0, 350), (70, 350), 5)
    pygame.draw.line(ventana, amarillo, (100, 350), (200, 350), 5)
    pygame.draw.line(ventana, amarillo, (223, 350), (310, 350), 5)
    pygame.draw.line(ventana, amarillo, (340, 350), (400, 350), 5)
    pygame.draw.line(ventana, amarillo, (440, 350), (500, 350), 5)

    texto_vidas = fuente.render(f"Vidas: {vidas}", True, negro)
    ventana.blit(texto_vidas, (10, 10))

    pygame.draw.rect(ventana, blanco, (cuadrito_x, cuadrito_y, cuadrito_size, cuadrito_size))

    mover_cuadrito()
    mover_cuadros_rojos() 

    if cuadrito_y <= 0:
        cuadrito_x = 240  
        cuadrito_y = 480

    cuadrito_rect = pygame.Rect(cuadrito_x, cuadrito_y, cuadrito_size, cuadrito_size)
    for cuadro in cuadros_rojos:
        if cuadrito_rect.colliderect(cuadro):
            vidas -= 1 
            cuadrito_x = 240  
            cuadrito_y = 480
            break

    if vidas <= 0:
        print("¡Perdiste todas tus vidas!")
        pygame.quit()
        sys.exit()

    for cuadro in cuadros_rojos:
        pygame.draw.rect(ventana, rojo, cuadro)

    pygame.display.flip()
