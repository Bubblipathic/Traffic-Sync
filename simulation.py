import threading
import pygame
import sys
import time
import random

from button import Button
from constants import *
from moore import MooreMachine

moore_machine = MooreMachine()

pygame.init()
simulation = pygame.sprite.Group()

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicleClass, direction_number, direction):
        pygame.sprite.Sprite.__init__(self)
        self.lane = lane
        self.vehicleClass = vehicleClass
        self.speed = speeds[vehicleClass]
        self.direction_number = direction_number
        self.direction = direction

        self.x = x[direction][lane]
        self.y = y[direction][lane]
        self.crossed = 0
        vehicles[direction][lane].append(self)
        self.index = len(vehicles[direction][lane]) - 1
        path = "images/" + direction + "/" + vehicleClass + ".png"
        self.image = pygame.image.load(path)

        if self.vehicleClass in {'ambulance', 'police', 'firetruck'}:
            emergencyVehicleDetector[self.direction] += 1

        vehicleCounter[direction] += 1

        if(len(vehicles[direction][lane])>1 and vehicles[direction][lane][self.index-1].crossed==0):    # if more than 1 vehicle in the lane of vehicle before it has crossed stop line
            if(direction=='right'):
                self.stop = vehicles[direction][lane][self.index-1].stop - vehicles[direction][lane][self.index-1].image.get_rect().width - stoppingGap         # setting stop coordinate as: stop coordinate of next vehicle - width of next vehicle - gap
            elif(direction=='left'):
                self.stop = vehicles[direction][lane][self.index-1].stop + vehicles[direction][lane][self.index-1].image.get_rect().width + stoppingGap
            elif(direction=='down'):
                self.stop = vehicles[direction][lane][self.index-1].stop - vehicles[direction][lane][self.index-1].image.get_rect().height - stoppingGap
            elif(direction=='up'):
                self.stop = vehicles[direction][lane][self.index-1].stop + vehicles[direction][lane][self.index-1].image.get_rect().height + stoppingGap
        else:
            self.stop = defaultStop[direction]
            
        # Set new starting and stopping coordinate
        if(direction=='right'):
            temp = self.image.get_rect().width + stoppingGap    
            x[direction][lane] -= temp
        elif(direction=='left'):
            temp = self.image.get_rect().width + stoppingGap
            x[direction][lane] += temp
        elif(direction=='down'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] -= temp
        elif(direction=='up'):
            temp = self.image.get_rect().height + stoppingGap
            y[direction][lane] += temp

        simulation.add(self)

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if(self.direction=='right'):
            if(self.crossed==0 and self.x+self.image.get_rect().width>stopLines[self.direction]):   # if the image has crossed stop line now
                self.crossed = 1
                vehicleCounter[self.direction] -= 1
                if self.vehicleClass in {'ambulance', 'police', 'firetruck'}:
                    emergencyVehicleDetector[self.direction] -= 1
            if((self.x+self.image.get_rect().width<=self.stop or self.crossed == 1 or (currentGreen==0 and currentYellow==0)) and (self.index==0 or self.x+self.image.get_rect().width<(vehicles[self.direction][self.lane][self.index-1].x - movingGap))):                
            # (if the image has not reached its stop coordinate or has crossed stop line or has green signal) and (it is either the first vehicle in that lane or it is has enough gap to the next vehicle in that lane)
                self.x += self.speed  # move the vehicle
        elif(self.direction=='down'):
            if(self.crossed==0 and self.y+self.image.get_rect().height>stopLines[self.direction]):
                self.crossed = 1
                vehicleCounter[self.direction] -= 1
                if self.vehicleClass in {'ambulance', 'police', 'firetruck'}:
                    emergencyVehicleDetector[self.direction] -= 1
            if((self.y+self.image.get_rect().height<=self.stop or self.crossed == 1 or (currentGreen==1 and currentYellow==0)) and (self.index==0 or self.y+self.image.get_rect().height<(vehicles[self.direction][self.lane][self.index-1].y - movingGap))):                
                self.y += self.speed
        elif(self.direction=='left'):
            if(self.crossed==0 and self.x<stopLines[self.direction]):
                self.crossed = 1
                vehicleCounter[self.direction] -= 1
                if self.vehicleClass in {'ambulance', 'police', 'firetruck'}:
                    emergencyVehicleDetector[self.direction] -= 1
            if((self.x>=self.stop or self.crossed == 1 or (currentGreen==2 and currentYellow==0)) and (self.index==0 or self.x>(vehicles[self.direction][self.lane][self.index-1].x + vehicles[self.direction][self.lane][self.index-1].image.get_rect().width + movingGap))):                
                self.x -= self.speed   
        elif(self.direction=='up'):
            if(self.crossed==0 and self.y<stopLines[self.direction]):
                self.crossed = 1
                vehicleCounter[self.direction] -= 1
                if self.vehicleClass in {'ambulance', 'police', 'firetruck'}:
                    emergencyVehicleDetector[self.direction] -= 1
            if((self.y>=self.stop or self.crossed == 1 or (currentGreen==3 and currentYellow==0)) and (self.index==0 or self.y>(vehicles[self.direction][self.lane][self.index-1].y + vehicles[self.direction][self.lane][self.index-1].image.get_rect().height + movingGap))):                
                self.y -= self.speed

# Generating vehicles in the simulation
def generateVehiclesWest():
    vehicle_type = random.randint(0,3)
    lane_number = random.randint(1,2)
    direction_number = 0
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateVehiclesNorth():
    vehicle_type = random.randint(0,3)
    lane_number = random.randint(1,2)
    direction_number = 1
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateVehiclesEast():
    vehicle_type = random.randint(0,3)
    lane_number = random.randint(1,2)
    direction_number = 2
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateVehiclesSouth():
    vehicle_type = random.randint(0,3)
    lane_number = random.randint(1,2)
    direction_number = 3
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateEmergencyVehiclesWest():
    vehicle_type = random.randint(4,6)
    lane_number = random.randint(1,2)
    direction_number = 0
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateEmergencyVehiclesNorth():
    vehicle_type = random.randint(4,6)
    lane_number = random.randint(1,2)
    direction_number = 1
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateEmergencyVehiclesEast():
    vehicle_type = random.randint(4,6)
    lane_number = random.randint(1,2)
    direction_number = 2
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

def generateEmergencyVehiclesSouth():
    vehicle_type = random.randint(4,6)
    lane_number = random.randint(1,2)
    direction_number = 3
    Vehicle(lane_number, vehicleTypes[vehicle_type], direction_number, directionNumbers[direction_number])

#Looping Functions
def timer():
    global timerText
    while True:
        if timerText == 0:
            timerText = moore_machine.outputs[moore_machine.current_state]
        if timerText > 0:
            timerText -= 1
        time.sleep(1)
def repeat():
    global currentGreen, currentYellow, input_value

    while True:
        # Set the input based on which lane has the Highest number of Emergency Vehicle
        if emergencyVehicleDetector[directionNumbers[0]] > emergencyVehicleDetector[directionNumbers[1]] and emergencyVehicleDetector[directionNumbers[0]] > emergencyVehicleDetector[directionNumbers[2]] and emergencyVehicleDetector[directionNumbers[0]]> emergencyVehicleDetector[directionNumbers[3]]:
            input_value = moore_machine.inputs_EM[0]
        elif emergencyVehicleDetector[directionNumbers[1]] > emergencyVehicleDetector[directionNumbers[0]] and emergencyVehicleDetector[directionNumbers[1]] > emergencyVehicleDetector[directionNumbers[2]] and emergencyVehicleDetector[directionNumbers[1]]> emergencyVehicleDetector[directionNumbers[3]]:
            input_value = moore_machine.inputs_EM[1]
        elif emergencyVehicleDetector[directionNumbers[2]] > emergencyVehicleDetector[directionNumbers[0]] and emergencyVehicleDetector[directionNumbers[2]] > emergencyVehicleDetector[directionNumbers[1]] and emergencyVehicleDetector[directionNumbers[2]]> emergencyVehicleDetector[directionNumbers[3]]:
            input_value = moore_machine.inputs_EM[2]
        elif emergencyVehicleDetector[directionNumbers[3]] > emergencyVehicleDetector[directionNumbers[0]] and emergencyVehicleDetector[directionNumbers[3]] > emergencyVehicleDetector[directionNumbers[1]] and emergencyVehicleDetector[directionNumbers[3]]> emergencyVehicleDetector[directionNumbers[2]]:
            input_value = moore_machine.inputs_EM[3]
        else:
            # Set the input based on which lane has the Highest number of Vehicles
            if vehicleCounter[directionNumbers[0]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[0]] > vehicleCounter[directionNumbers[2]] and vehicleCounter[directionNumbers[0]]> vehicleCounter[directionNumbers[3]]:
                input_value = moore_machine.inputs_HighestCount[0]
            elif vehicleCounter[directionNumbers[1]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[1]] > vehicleCounter[directionNumbers[2]] and vehicleCounter[directionNumbers[1]]> vehicleCounter[directionNumbers[3]]:
                input_value = moore_machine.inputs_HighestCount[1]
            elif vehicleCounter[directionNumbers[2]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[2]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[2]]> vehicleCounter[directionNumbers[3]]:
                input_value = moore_machine.inputs_HighestCount[2]
            elif vehicleCounter[directionNumbers[3]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[3]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[3]]> vehicleCounter[directionNumbers[2]]:
                input_value = moore_machine.inputs_HighestCount[3]
            elif vehicleCounter[directionNumbers[0]] == 0 and vehicleCounter[directionNumbers[1]] == 0  and vehicleCounter[directionNumbers[2]] == 0 and vehicleCounter[directionNumbers[3]] == 0 :
                input_value = 'NULL'

            #If two lanes have the same number of vehicles, proceed in order of North, South, East, West
            else:
                     if vehicleCounter[directionNumbers[0]] > 0:
                         input_value = moore_machine.inputs_HighestCount[0]
                     elif vehicleCounter[directionNumbers[1]] > 0:
                         input_value = moore_machine.inputs_HighestCount[1]
                     elif vehicleCounter[directionNumbers[2]] > 0:
                         input_value = moore_machine.inputs_HighestCount[2]
                     elif vehicleCounter[directionNumbers[3]] > 0:
                         input_value = moore_machine.inputs_HighestCount[3]

        moore_machine.current_state = moore_machine.transitions[moore_machine.current_state][input_value]
        # Update global signal states based on current Moore machine state
        signal_states = moore_machine.definition[moore_machine.current_state]
        currentGreen =  signal_states['currentGreen']
        currentYellow = signal_states['currentYellow']

        time.sleep(moore_machine.outputs[moore_machine.current_state]) 

# Main
class Main:
    thread1 = threading.Thread(name="Repeat",target=repeat, args=())    # initialization
    thread1.daemon = True
    thread1.start()

    # Colours 
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Screensize 
    screenWidth = 1400
    screenHeight = 800
    screenSize = (screenWidth, screenHeight)

    # Setting background image i.e. image of intersection
    background = pygame.image.load('images/intersection.png')

    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("SIMULATION")

    # Loading signal images and font
    redSignal = pygame.image.load('images/signals/red.png')
    yellowSignal = pygame.image.load('images/signals/yellow.png')
    greenSignal = pygame.image.load('images/signals/green.png')
    font = pygame.font.Font(None, 30)

    # Creating Buttons
    buttons = [
        Button(490, 20, 150, 50, (0, 150, 250), "Normal",lambda: generateVehiclesNorth()),
        Button(730, 20, 150, 50, (150, 0, 255), "Emergency",lambda: generateEmergencyVehiclesNorth()),
        Button(30, 300, 150, 50, (0, 150, 250), "Normal",lambda: generateVehiclesWest()),
        Button(30, 520, 150, 50, (150, 0, 255), "Emergency",lambda: generateEmergencyVehiclesWest()),
        Button(490, 720, 150, 50, (0, 150, 250), "Normal",lambda: generateVehiclesSouth()),
        Button(730, 720, 150, 50, (150, 0, 255), "Emergency",lambda: generateEmergencyVehiclesSouth()),
        Button(1220, 300, 150, 50, (0, 150, 250), "Normal",lambda: generateVehiclesEast()),
        Button(1220, 520, 150, 50, (150, 0, 255), "Emergency",lambda: generateEmergencyVehiclesEast()),
    ]

    thread2 = threading.Thread(name="Timer",target=timer, args=())    # Timer
    thread2.daemon = True
    thread2.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
            else:
                for button in buttons:
                    button.handle_event(event)

        screen.blit(background,(0,0))   # display background in simulation
        for i in range(0,noOfSignals):  # display signal and set timer according to current status: green, yello, or red
            if(i==currentGreen):
                if(currentYellow==1):
                    screen.blit(yellowSignal, signalCoods[i])
                else:
                    screen.blit(greenSignal, signalCoods[i])
            else:
                screen.blit(redSignal, signalCoods[i])

        # display signal timer
        timerTexts = font.render("Timer: " + str(timerText), True, white, black)
        screen.blit(timerTexts,TimerCoods)

        # Display counters
        counterTexts = ["", "", "", ""]
        for i in range(0, noOfSignals):
            counterTexts[i] = font.render(str(laneNumbers[i])+ " Count: " + str(vehicleCounter[directionNumbers[i]]), True, white, black)
            screen.blit(counterTexts[i], counterCoods[i])

        # Display Current State
        stateTexts = ""
        stateTexts = font.render("Current State: " + str(moore_machine.current_state), True, white, black)
        screen.blit(stateTexts, stateCoods)

        # display the vehicles
        for vehicle in simulation:  
            screen.blit(vehicle.image, [vehicle.x, vehicle.y])
            vehicle.move()

        # Draw buttons
        for button in buttons:
            button.draw(screen, (255, 255, 255))

        pygame.display.update()


Main()