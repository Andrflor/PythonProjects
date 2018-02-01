# -*- coding: utf-8 -*-

import sys,pygame,os,math,random

#Schéma déffinissant les inputs de base, ici on ne bouge pas
baseScheme = {'up':False,'left':False,'right':False,'down':False}

#Une IA débile ce basant sur le random
class DumbIA:

    def __init__(self):
        self.outputs = baseScheme

#Retourne les outputs de l'ia
    def getOutputs(self):
        self.computeOutputs()
        return self.outputs

#Calcule les outputs
    def computeOutputs(self):
        self.outputs['up'] = bool(random.getrandbits(1))
        self.outputs['down'] = bool(random.getrandbits(1))
        self.outputs['right'] = bool(random.getrandbits(1))
        self.outputs['left'] = bool(random.getrandbits(1))

#Une IA a base de genome
class Genome:

    def __init__(self,genome):
        self.outputs = baseScheme
        if(genome==None):genome = []
        #On enlève 15% du génome afin de le remplacer par du random
        self.genome = genome[0:10*len(genome)//12]
        self.outputsHistory  = []

#Retourne les outputs de l'ia
    def getOutputs(self):
        self.computeOutputs()
        return self.outputs

#Permet de calculer les inputs en fonction du genome
    def computeOutputs(self):
        if (self.genome!=[]):
            self.outputs = self.genome.pop(0)
        else:
            self.randomCompute()
        self.outputsHistory.append(self.outputs)

#Si on a plus rien dans le génome on go random
    def randomCompute(self):
        self.outputs['up'] = bool(random.getrandbits(1))
        self.outputs['down'] = bool(random.getrandbits(1))
        self.outputs['right'] = bool(random.getrandbits(1))
        self.outputs['left'] = bool(random.getrandbits(1))

    def getGenome(self):
        return self.outputsHistory

#La machine qui permet le brassage génomique
class BrassMachine:

    def __init__(self):
        self.generations = []

#FOnction de brassage du génome
    def bass(self):
        pass

#Le sprite de la voiture
class Sprite:

    def __init__(self,name,game):
        self.size = (30,64)
        self.x = 300
        self.y = 70
        self.angle = 90
        self.game = game
        #On load deux image une de base a partir de laquaelle effectuer les rotations
        self.baseimg = pygame.image.load(os.path.join('img',name))
        self.baseimg = pygame.transform.scale(self.baseimg,self.size)
        #Une actuellement display
        self.img = self.baseimg.copy()
        self.update()

#On update le mask pour le pixel perfect collision et le centre pour la rotation centrée
    def update(self):
        self.updateMask()
        self.updateCenter()

    def updateCenter(self):
        self.center = (self.img.get_size()[0]/2+self.x,self.img.get_size()[1]/2+self.y)

    def updateMask(self):
        self.imgMask = pygame.mask.from_surface(self.img)

    def draw(self):
        self.game.screen.blit(self.img,(self.x,self.y))

#On bouge en foncton de la vitesse et de l'angle grâce à la trigo sur x et y
    def move(self,speed):
        self.x += speed*math.sin(math.radians(self.angle))
        self.y += speed*math.cos(math.radians(self.angle))
        self.updateCenter()

#On centre la rotation
    def rotate(self,angle):
        self.angle += angle
        self.img = pygame.transform.rotate(self.baseimg,self.angle)
        self.size = self.img.get_size()
        hSize = [n/2 for n in self.size]
        self.x = self.center[0]-hSize[0]
        self.y = self.center[1]-hSize[1]
        self.update()

#Classe de la voiture
class Car:
    def __init__(self,game):
        self.game = game
        self.direction = 0
        #Distance de course composante principale du fitness qui determine la valeur de l'ia
        self.runDistance = 0
        self.maxSpeed = 10
        self.speed = 0
        self.inputs = baseScheme
        #On load la benz ma gueule et ouais on roule en gros gamos ;)
        self.sprite = Sprite('benz.png',self.game)
        self.setIa()

#Fonction permettant d'affecter l'ia que l'on a choisi
    def setIa(self):
        self.ia = Genome([])

#Fonction principale permettant de gerer les inputs de tourner et bouger la voiture ainsi que de la dessiner
    def run(self):
        self.setInputs(self.ia.getOutputs())
        self.turn()
        self.move()
        self.activate()

#La fonction de fitness permettant de calculer la valeur de l'ia
    def getFitness(self):
        return self.runDistance, self.ia.getGenome()

#On accelere en vonction d'un momentum
    def acceleration(self,momentum):
        self.speed += momentum
        if(self.speed <=0):self.speed = 0
        if(self.speed >= self.maxSpeed):self.speed = self.maxSpeed

    def accelerate(self):
        self.acceleration(1)

    def brake(self):
        self.acceleration(-1)

#On se déplace donc on modifi la runDistance
    def move(self):
        self.sprite.move(self.speed)
        self.runDistance += self.speed

    def turn(self):
        self.sprite.rotate(self.speed*self.direction)

    def activate(self):
        self.sprite.draw()

    def setDirection(self,direction):
        self.direction = direction

#Ici on compute les inputs pour changer la direction et l'acceleration de la voiture
    def setInputs(self,inputs):
        self.inputs = inputs
        if(self.inputs['left'] == False and self.inputs['right'] == True):
            direction = -1
        elif (self.inputs['left'] == True and self.inputs['right'] == False):
            direction = 1
        else :
            direction = 0
        if(self.inputs['down'] == False and self.inputs['up'] == True):
            self.accelerate()
        elif (self.inputs['down'] == True and self.inputs['up'] == False):
            self.brake()
        self.setDirection(direction)

#Classe principale le jeux en lui même
class Game:

    def __init__(self):
        #Permet de mettre la fenêtre en au à gauche
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
        #On cache la souris
        pygame.mouse.set_visible(False)
        self.cars = []
        self.caption = "Un jeu de course pour tester des ia"
        self.size = pygame.display.Info().current_w//2, pygame.display.Info().current_h
        self.display=pygame.display
        self.display.set_caption(self.caption)
        #On load la piste est on l'ajuste a l'écran
        self.track = pygame.image.load(os.path.join('img','track.png'))
        self.track = pygame.transform.scale(self.track, self.size)
        self.trackMask = pygame.mask.from_surface(self.track)
        #Demare l'horloge du jeux
        self.clock = pygame.time.Clock()
        self.launch()

#Lance le jeux ajoute la première voiture, montre l'écren et lance la boucle principale
    def launch(self):
        self.addCar()
        self.screen = self.display.set_mode((self.size))
        self.loop()

#Permet de redessiner le fond
    def setBack(self):
        self.screen.fill([255,255,255])
        self.screen.blit(self.track,(0,-30))

#Permet d'ajouter une nouvelle voiture au jeux
    def addCar(self):
        self.cars.append(Car(self))

#Boucle principale du programme
    def loop(self):
        #Boucle infini du jeux
        while True:
            #Permet de fermer malgrès la boucle infini si on appuis sur la crois ou alt+f4
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            #On redessine le fond
            self.setBack()
            #Pour chaque voiture on regarde si il y a collision avec les masques
            for car in self.cars:
                if (self.trackMask.overlap(car.sprite.imgMask, (int(car.sprite.x), 30+int(car.sprite.y))) != None):
                    #Collision on enlève la voiture
                    self.cars.remove(car)
                else:
                    #Pas de collision on run l'ia a nouveau
                    car.run()
            #Permet de dessiner les changement à l'écran
            self.display.flip()
            #On attend 30ms entre chaque tour de boucle
            pygame.time.wait(30)
            #On ajoute une nouvelle voiture a chaque boucle
            self.addCar()

#Ce lance quand on run le programe
if __name__=='__main__':
    #Initialise Pygame
    pygame.init()
    #Crée le jeux puis le lance
    game = Game()
    game.launch()
