import pygame 

#settings
#-----------------------------------------------
canvas_size = (1000,1000)
pixel_size = 10   
#-----------------------------------------------

pygame.init()

screen = pygame.display.set_mode((canvas_size[0],canvas_size[1]))   
clock = pygame.time.Clock()

colors = ['gray','green','blue','yellow','red','pink','orange','purple','white','gold','black','white']
color = 0
clicked = False

text_font = pygame.font.SysFont('monospace',20)

while True:
    # exiting program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #blits text
    for i in zip(['place : left-mouse-button','change : right-mouse-button','remove : middle-mouse-button'],[(10,10),(10,30),(10,50)]):
        text = text_font.render(i[0],1,(255,255,255))
        screen.blit(text,i[1])

    #placing collor 
    if pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(screen,colors[color],pygame.Rect((int(pygame.mouse.get_pos()[0]/pixel_size))*pixel_size,(int(pygame.mouse.get_pos()[1]/pixel_size))*pixel_size, pixel_size, pixel_size))

    #changing collors
    if pygame.mouse.get_pressed()[2] and clicked == False:
        color += 1
        if color >= len(colors):
            color = 0
        clicked = True
    elif pygame.mouse.get_pressed()[2] == False:
        clicked = False

    #reseting screen
    if pygame.mouse.get_pressed()[1]:
        screen.fill('black')

    pygame.display.set_caption(f"simple-pixel-art   color:{colors[color]}")
    pygame.display.update()
    clock.tick(60)