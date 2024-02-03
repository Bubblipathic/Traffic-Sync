class MooreMachine:
    def __init__(self):
        # List of States
        self.states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']

        # Starting State
        self.current_state = 'S0'

        # List of inputs
        self.inputs_EM = ['EM[0]', 'EM[1]', 'EM[2]', 'EM[3]']
        self.inputs_HighestCount = ['HighestCount[0]', 'HighestCount[1]', 'HighestCount[2]', 'HighestCount[3]']

        # Dictionary of outputs
        self.outputs = {'S0': 3, 'S1': 8, 'S2': 4, 'S3': 8, 'S4': 4, 'S5': 8, 'S6': 4, 'S7': 8, 'S8': 4}

        # A Dictionary of Transitions for each state
        self.transitions = {
            self.states[0]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S7'},
            self.states[1]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S2', 'HighestCount[2]': 'S2', 'HighestCount[3]': 'S2', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S2', 'EM[2]': 'S2', 'EM[3]': 'S2'},
            self.states[2]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S7'},
            self.states[3]: {'HighestCount[0]': 'S4', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S4', 'HighestCount[3]': 'S4', 'NULL': 'S0',
                   'EM[0]': 'S4', 'EM[1]': 'S3', 'EM[2]': 'S4', 'EM[3]': 'S4'},
            self.states[4]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S7'},
            self.states[5]: {'HighestCount[0]': 'S6', 'HighestCount[1]': 'S6', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S6', 'NULL': 'S0',
                   'EM[0]': 'S6', 'EM[1]': 'S6', 'EM[2]': 'S5', 'EM[3]': 'S6'},
            self.states[6]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S7'},
            self.states[7]: {'HighestCount[0]': 'S8', 'HighestCount[1]': 'S8', 'HighestCount[2]': 'S8', 'HighestCount[3]': 'S7', 'NULL': 'S0',
                   'EM[0]': 'S8', 'EM[1]': 'S8', 'EM[2]': 'S8', 'EM[3]': 'S7'},
            self.states[8]: {'HighestCount[0]': 'S1', 'HighestCount[1]': 'S3', 'HighestCount[2]': 'S5', 'HighestCount[3]': 'S6', 'NULL': 'S0',
                   'EM[0]': 'S1', 'EM[1]': 'S3', 'EM[2]': 'S5', 'EM[3]': 'S6'}
        }

        # A Dictionary of signal states for each state
        self.definition = {
            self.states[0]: {'currentGreen': 5, 'currentYellow': 5},
            self.states[1]: {'currentGreen': 0, 'currentYellow': 0},
            self.states[2]: {'currentGreen': 0, 'currentYellow': 1},
            self.states[3]: {'currentGreen': 1, 'currentYellow': 0},
            self.states[4]: {'currentGreen': 1, 'currentYellow': 1},
            self.states[5]: {'currentGreen': 2, 'currentYellow': 0},
            self.states[6]: {'currentGreen': 2, 'currentYellow': 1},
            self.states[7]: {'currentGreen': 3, 'currentYellow': 0},
            self.states[8]: {'currentGreen': 3, 'currentYellow': 1},
        }