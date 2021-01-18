import pygame


class Snake(object):
    # intialize all properties (the default direction towards right/the default size is 2)
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(2):
            self.addnode()

    # Add cell in front of the snake
    def addnode(self):
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0, node)

    # Delete all cell
    def delnode(self):
        self.body.pop()

    # how to die
    def isdead(self, size_x, size_y):
        # when to hit the wall
        if self.body[0].x not in range(size_x):
            return True
        if self.body[0].y not in range(size_y):
            return True
        # when the snake hits itself
        if self.body[0] in self.body[1:]:
            return True
        return False

    # Move!
    def move(self):
        self.addnode()
        self.delnode()

    # change direction
    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.dirction in LR):
                return
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey