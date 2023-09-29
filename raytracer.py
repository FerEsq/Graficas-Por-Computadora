'''
 * Nombre: raytracer.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: Finalizado el 29.09.2023
 '''

import pygame

from figures import *
from lights import *
from rt import *
from materials import *

width = 212
height = 212

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = Raytracer(screen)
rayTracer.environmentMap = pygame.image.load("maps/map.jpg")
rayTracer.rtClearColor(0.25, 0.25, 0.25)
rayTracer.rtColor(1, 1, 1)

'''
rayTracer.scene.append(
    Sphere(position=(0, 0, -7), radius=2, material=soapy())
)
rayTracer.scene.append(
    Sphere(position=(-1.5, -1, -5), radius=0.5, material=earth())
)
'''

rayTracer.scene.append(
    Sphere(position=(-1, 0, -5), radius=1, material=glass())
)
rayTracer.scene.append(
    Sphere(position=(1, 0, -5), radius=1, material=diamond())
)
rayTracer.scene.append(
    Sphere(position=(0, 1, -8), radius=1, material=brick())
)

rayTracer.lights.append(
    AmbientLight(intensity=0.4)
)
rayTracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.7)
)
rayTracer.lights.append(
    PointLight(position=(0, 0, -4.5), intensity=1, color=(1, 0, 1))
)

rayTracer.rtClear()
rayTracer.rtRender()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

pygame.quit()
