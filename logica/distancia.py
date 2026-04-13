import pygame

def calcular_distancia(pos_j1, pos_j2):
    return pygame.math.Vector2(pos_j1).distance_to(pos_j2)