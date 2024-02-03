# Countdown for each state
timerText = 0

# Array for each traffic lights [NSEW]
signals = [0,1,2,3]
noOfSignals = 4
currentGreen = 5  # Indicates which signal is green currently
currentYellow = 0   # Indicates whether yellow signal is on or off 
input_value = "NULL"

 # Speed of vehicles
speeds = {'car':2.25, 'bus':1.8, 'truck':1.8, 'bike':2.5, 'ambulance':3,'police':3, 'firetruck':3}

# Assigning definition for each dictionary/list
vehicles = {'right': {0:[], 1:[], 2:[], 'crossed':0}, 'down': {0:[], 1:[], 2:[], 'crossed':0}, 'left': {0:[], 1:[], 2:[], 'crossed':0}, 'up': {0:[], 1:[], 2:[], 'crossed':0}}
vehicleTypes = {0:'car', 1:'bus', 2:'truck', 3:'bike', 4:'ambulance', 5:'police', 6:'firetruck'}
directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'}
laneNumbers = {0:'West', 1:'North', 2:'East', 3:'South'}

# Counter for Total Vehical in each lane
vehicleCounter = {'right': 0, 'down': 0, 'left': 0,  'up':0 }
# Counter for Total Emergency Vehicle in each lane
emergencyVehicleDetector = {'right': 0, 'down': 0, 'left': 0,  'up':0 }

# Coordinates of vehicles' start
x = {'right':[0,0,0], 'down':[755,727,697], 'left':[1400,1400,1400], 'up':[602,627,657]}    
y = {'right':[348,370,398], 'down':[0,0,0], 'left':[498,466,436], 'up':[800,800,800]}
# Coordinates of signal image, timer, and vehicle count
signalCoods = [(530,230),(810,230),(810,570),(530,570)]
TimerCoods = (150,40)
counterCoods = [(440,200), (810,200), (810,540), (440,540)]
stateCoods = (150,70)
# Coordinates of stop lines
stopLines = {'right': 590, 'down': 330, 'left': 800, 'up': 535}
defaultStop = {'right': 580, 'down': 320, 'left': 810, 'up': 545}
# Gap between vehicles
stoppingGap = 15    # stopping gap
movingGap = 15   # moving gap