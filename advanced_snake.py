# Advanced snake
# developed by Hancheng Yang, Jiaoyang Xu. University of Waterloo

import pygame
import sys
from food import Food
from drink import Drink
from snake import Snake



#size of the map
SCREEN_X = 700
SCREEN_Y = 700


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
        isdead = snake.isdead(SCREEN_X, SCREEN_Y)
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

        food.set(SCREEN_X)
        drink.set(SCREEN_X)
        pygame.draw.rect(screen,(0,0,255),food.rect,0)
        pygame.draw.rect(screen,(136,0,21),drink.rect,0)
        # Display text
        show_text(screen,(50,500),'Scores: '+str(scores),(223,223,223))
        
        pygame.display.update()
        clock.tick(5)
    
    
if __name__ == '__main__':
    main()
