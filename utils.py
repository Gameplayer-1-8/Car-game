import pygame
def loadImageSized(filename, width, height):
    imgFromFile = pygame.image.load(filename)
    imgToReturn = pygame.transform.scale(imgFromFile,(width,height))
    return imgToReturn

def loadImageScaled(filename, scale):
    imgFromFile = pygame.image.load(filename)
    width = int(imgFromFile.get_width())
    height = int(imgFromFile.get_height())
    imgToReturn = pygame.transform.scale(imgFromFile,(width * scale,height * scale))
    return imgToReturn

def rotateImage(img, angle):
    return pygame.transform.rotate(img, angle)


