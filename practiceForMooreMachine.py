class MooreMachine:
    def __init__(self):
        # Define states
        self.states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
        self.current_state = 'S0'

        # Define inputs
        self.inputs_EM = ['EM[0]', 'EM[1]', 'EM[2]', 'EM[3]']
        self.inputs_HighestCount = ['HighestCount[0]', 'HighestCount[1]', 'HighestCount[2]', 'HighestCount[3]']

        # Define outputs
        self.outputs = {'S0': 2, 'S1': 5, 'S2': 3, 'S3': 5, 'S4': 3, 'S5': 5, 'S6': 3, 'S7': 5, 'S8': 3}

        # Define transitions
        self.transitions = {
            'S0': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S7'},
            'S1': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S2', 'HighestCount[2]': 'S2', 'HighestCount[3]': 'S2', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S2': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S3': {'HighestCount[0]': 'S4', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S4', 'HighestCount[3]': 'S4', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S4': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S5': {'HighestCount[0]': 'S6', 'HighestCount[1]': 'S6', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S6', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S6': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S7': {'HighestCount[0]': 'S8', 'HighestCount[1]': 'S8', 'HighestCount[2]': 'S8', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'},
            'S8': {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S6', 'NULL': 'S0',
                   'EM[0]': 'S0', 'EM[1]': 'S1', 'EM[2]': 'S2', 'EM[3]': 'S3'}
        }

    def transition(self, input_val):
        if input_val in self.transitions[self.current_state]:
            self.current_state = self.transitions[self.current_state][input_val]
            return self.outputs[self.current_state]
        else:
            return None

# Example usage:
moore_machine = MooreMachine()
directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'}
vehicleCounter = {'right': 5, 'down': 7, 'left': 0,  'up':0 }

if vehicleCounter[directionNumbers[0]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[0]] > vehicleCounter[directionNumbers[2]] and vehicleCounter[directionNumbers[0]]> vehicleCounter[directionNumbers[3]]:
    input_value = 'HighestCount[0]'
elif vehicleCounter[directionNumbers[1]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[1]] > vehicleCounter[directionNumbers[2]] and vehicleCounter[directionNumbers[1]]> vehicleCounter[directionNumbers[3]]:
    input_value = 'HighestCount[1]'
elif vehicleCounter[directionNumbers[2]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[2]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[2]]> vehicleCounter[directionNumbers[3]]:
    input_value = 'HighestCount[2]'
elif vehicleCounter[directionNumbers[3]] > vehicleCounter[directionNumbers[0]] and vehicleCounter[directionNumbers[3]] > vehicleCounter[directionNumbers[1]] and vehicleCounter[directionNumbers[3]]> vehicleCounter[directionNumbers[2]]:
    input_value = 'HighestCount[3]'


output_value = moore_machine.transition(input_value)

print(f"Current State: {moore_machine.current_state}")
print(f"Output Value: {output_value}")