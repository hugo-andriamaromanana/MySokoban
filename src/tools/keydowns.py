import pygame
from pygame.locals import *

def ESC(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True


def SPACEBAR(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return True


def BACKSPACE(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        return True


def RETURN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return True


def STAR(event):
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK):
        return True


def TAB(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
        return True