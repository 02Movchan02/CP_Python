import pygame as pg

pg.init()

WIDTH = 500
HEIGHT = 400


#f1 = pg.font.Font(None, 70)
#text1 = f1.render('Добро пожаловать!', True, (64, 128,255))
clock = pg.time.Clock()


sc = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption("Добро пожаловать")
i=0
running = True
while running:
    #for event in pg.event.get():
        #if event.type==pg.QUIT:
            #exit()

    house1 = pg.image.load('hotel_photo1.png')
    house_rect1 = house1.get_rect(topright=(WIDTH, 0))
    sc.blit(house1, house_rect1)
    pg.time.delay(200)
    pg.display.update()
    
    house2 = pg.image.load('hotel_photo2.png')
    house_rect2 = house2.get_rect(topright=(WIDTH, 0))
    sc.blit(house2, house_rect2)
    pg.time.delay(200)
    pg.display.update()

    house3 = pg.image.load('hotel_photo3.png')
    house_rect3 = house3.get_rect(topright=(WIDTH, 0))
    sc.blit(house3, house_rect3)
    pg.time.delay(200)
    pg.display.update()

    house4 = pg.image.load('hotel_photo4.png')
    house_rect4 = house4.get_rect(topright=(WIDTH, 0))
    sc.blit(house4, house_rect4)
    pg.time.delay(200)
    pg.display.update()

    house5 = pg.image.load('hotel_photo5.png')
    house_rect5 = house5.get_rect(topright=(WIDTH, 0))
    sc.blit(house5, house_rect5)
    pg.time.delay(200)
    pg.display.update()

    house6 = pg.image.load('hotel_photo6.png')
    house_rect6 = house6.get_rect(topright=(WIDTH, 0))
    sc.blit(house6, house_rect6)
    pg.time.delay(200)
    pg.display.update()
    i+=1
    if (i==5):
        running = False
        #pg.display.quit()     
        import Authorization
        i=0
pg.quit()
        
    

        
