'''
 * Nombre: raytracer.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: Finalizado el 29.09.2023
              Modificado el 12.10.2023
 '''

import pygame
from pygame.locals import *

from figures import *
from lights import *
from materials import *
from rt import *

width = 600
height = 600

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = Raytracer(screen)
rayTracer.rtClearColor(0.5, 0.9, 0.9)
#rayTracer.rtClearColor(0.2, 0.8, 0.8)
rayTracer.rtColor(1, 1, 1)

#Suelo
rayTracer.scene.append(Plane(position=(0, -4, 0), normal=(0, 1, -0.2), material=floor()))

#Esferas
rayTracer.scene.append(Sphere(position = (-0.5, -0.3, -4.5), radius = 0.35, material = diamond()))

# Cilindros
rayTracer.scene.append(Cylinder(position=(0, -1, -5), size=(1.2, 0.4), material=pink()))
rayTracer.scene.append(Cylinder(position=(0.7, -0.7, -5), size=(0.4, 0.8), material=pink()))
rayTracer.scene.append(Cylinder(position=(0.85, -0.7, -2.8), size=(0.15, 0.17), material=white()))
rayTracer.scene.append(Cylinder(position=(0.85, -0.5, -2.8), size=(0.09, 0.12), material=mirror()))

#Piramides
rayTracer.scene.append(Pyramid(position=(-0.9, -0.8, -3.6), size=(0.7, 0.7, 0.7), material=paint()))

#AABBs
rayTracer.scene.append(AABB(position=(2.2, -0.5, -7), size=(1.5, 1.8, 1), material=paint()))
rayTracer.scene.append(AABB(position=(-2.5, 0, -7), size=(0.8, 3, 1), material=yellow()))
rayTracer.scene.append(AABB(position=(-1.8, -0.65, -7), size=(0.7, 1.7, 1), material=yellow()))
rayTracer.scene.append(AABB(position=(-1.2, -0.9, -7), size=(0.7, 1, 1), material=yellow()))


#Discos
rayTracer.scene.append(Disk(position=(0.5, 1.5, -6), normal=(0, 0, 1), radius=0.9, material=yellow()))
rayTracer.scene.append(Disk(position=(0.42, 1.32, -5), normal=(0, 0, 1), radius=0.4, material=white()))
rayTracer.scene.append(Disk(position=(-0.9, 1.7, -5), normal=(0, 0, 1), radius=0.3, material=white()))
rayTracer.scene.append(Disk(position=(2, 1.5, -5), normal=(0, 0, 1), radius=0.5, material=white()))


#Ilumniacion
rayTracer.lights.append(AmbientLight(intensity=0.9))
rayTracer.lights.append(DirectionalLight(direction=(-0.5, -0.5, 1), intensity=0.7, color=(1, 1, 1)))
rayTracer.lights.append(DirectionalLight(direction=(2, -0.5, 1), intensity=0.7, color=(1, 1, 1)))
rayTracer.lights.append(DirectionalLight(direction=(1, 2, 1), intensity=0.7, color=(1, 1, 1)))
rayTracer.lights.append(PointLight(position=(0.25, 1, -3), intensity=1))

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

rect = pygame. Rect(0, 0, width, height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "scene.jpg")

pygame.quit()
