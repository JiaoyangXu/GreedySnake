# Advanced snake
# developed by Hancheng Yang, Jiaoyang Xu. University of Waterloo

import pygame
import sys
import random


#size of the map
SCREEN_X = 700
SCREEN_Y = 700


# Class Snake
class Snake(object):
    # intialize all properties (the default direction towards right/the default size is 2)
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(2):
            self.addnode()
        
    # Add cell in front of the snake    
    def addnode(self):
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25)
        if self.dirction == pygame.K_LEFT:
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)
        
    # Delete all cell
    def delnode(self):
        self.body.pop()
        
    # how to die
    def isdead(self):
        # when to hit the wall 
        if self.body[0].x  not in range(SCREEN_X):
            return True
        if self.body[0].y  not in range(SCREEN_Y):
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
    def changedirection(self,curkey):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if curkey in LR+UD:
            if (curkey in LR) and (self.dirction in LR):
                return
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey
       
       
# Food
# Option Set/Delete
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)
        
    def remove(self):
        self.rect.x=-25
    
    def set(self):
        if self.rect.x == -25:
            allpos = []
            for pos in range(25,SCREEN_X-25,25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top  = random.choice(allpos)
            print(self.rect)
            

# Drink
# Option Set/Delete
class Drink:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)
        
    def remove(self):
        self.rect.x=-25
    
    def set(self):
        if self.rect.x == -25:
            allpos = []
            # range of position between 25 and SCREEN_X-25,25
            for pos in range(25,SCREEN_X-25,25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top  = random.choice(allpos)
            print(self.rect)


def show_text(screen, pos, text, color, font_bold = False, font_size = 60, font_italic = False):   
    #Set the font of the text
    cur_font = pygame.font.SysFont("Times", font_size)  
    #Set the font bold
    cur_font.set_bold(font_bold)  
    #Set if it is italic  
    cur_font.set_italic(font_italic)  
    #Set the content of text  
    text_fmt = cur_font.render(text, 1, color)  
    #Draw text
    screen.blit(text_fmt, pos)

     
def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    scores = 0
    isdead = False
    
    # Snake/Food
    snake = Snake()
    food = Food()
    drink = Drink()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                # restart the game after pressing space
                if event.key == pygame.K_SPACE and isdead:
                    return main()
                
            
        screen.fill((255,255,255))
        
        # Draw the body of snake/add one point every step
        if not isdead:
            scores+=1
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39),rect,0)

        # Display death text   
        isdead = snake.isdead()
        if isdead:
            show_text(screen,(100,200),'YOU DEAD!',(227,29,18),False,100)
            show_text(screen,(150,260),'press space to try again...',(0,0,22),False,30)
            
        # Set food / add 50 points after eating it.
        # When snake touches food, add one node to the snake
        if food.rect == snake.body[0]:
            scores+=50
            food.remove()
            snake.addnode()
        

        # Set food / add 25 points after eating it.
        # When snake touches food, add one node to the snake
        if drink.rect == snake.body[0]:
            scores += 25
            drink.remove()
            snake.addnode()
            snake.addnode()

        food.set()
        drink.set()
        pygame.draw.rect(screen,(0,0,255),food.rect,0)
        pygame.draw.rect(screen,(136,0,21),drink.rect,0)
        # Display text
        show_text(screen,(50,500),'Scores: '+str(scores),(223,223,223))
        
        pygame.display.update()
        clock.tick(5)
    
    
if __name__ == '__main__':
    main()
