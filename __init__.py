class Action:
    def __init__(self, name, action, input_types=['Inputs'], output_types=['Outputs']):
        self.name = name
        self.action = action
        self.input_types = input_types
        self.output_types = output_types

    def __call__(self, input_data):
        return self.action(input_data)

    def __repr__(self):
        return f"'{self.name}'"

    def __str__(self):
        return f"{self.input_types} -{self.name}-> {self.output_types}"

import functools
from functools import total_ordering
@total_ordering
class Option:
    def __init__(self, action_utility, anticipated_result_of_action, action):
        assert not (action_utility < action_utility), "AssertionError: Option.utility must be ordinal"
        self.utility = action_utility
        # TODO: Use predictions with uncertainty
        # assert isinstance(action, Prediction), "AssertionError: Option.action must be of type Prediction"
        self.anticipated_result = anticipated_result_of_action
        assert isinstance(action, Action), "AssertionError: Option.action must be of type Action"
        self.action = action

    def __lt__(self, obj):
        assert isinstance(obj, Option), "AssertionError: Options can only be compared to other Options"
        return ((self.utility) < (obj.utility))

    def __gt__(self, obj):
        assert isinstance(obj, Option), "AssertionError: Options can only be compared to other Options"
        return ((self.utility) > (obj.utility))

    def __le__(self, obj):
        assert isinstance(obj, Option), "AssertionError: Options can only be compared to other Options"
        return ((self.utility) <= (obj.utility))

    def __ge__(self, obj):
        assert isinstance(obj, Option), "AssertionError: Options can only be compared to other Options"
        return ((self.utility) >= (obj.utility))

    def __eq__(self, obj):
        assert isinstance(obj, Option), "AssertionError: Options can only be compared to other Options"
        return (self.utility == obj.utility)

def toOption(action, current_state=None, utility_func=lambda state: 0.0, speculator_func=lambda state, action: state):
    anticipated_result_of_action = speculator_func(current_state, action)
    action_utility = utility_func(anticipated_result_of_action)
    return Option(action_utility, anticipated_result_of_action, action)

class Speculator:
    """Predicts the next state based on the current state and available actions
    """
    def __init__(self, system_dynamics, control_dynamics):
        """Initializes a speculator

        Parameters
        ----------
        system_dynamics : SystemDynamics
            How the environment naturally changes over time
        control_dynamics : ControlDynamics
            How the environment changes as a result of specific actions
        """
        self.system_dynamics = system_dynamics
        self.control_dynamics = control_dynamics

    def __call__(self, state, action):
        """Make a prediction

        Parameters
        ----------
        state : CurrentState
            The current state
        action : Action
            The action being considered

        Returns
        -------
        AnticipatedState
            The anticipated state
        """
        environmental_effects = self.system_dynamics(state)
        control_effects = self.control_dynamics(environmental_effects, action)#(action)
        changes = control_effects#environmental_effects + control_effects
        prediction = changes#state + changes#state.anticipate(changes)
        return prediction

# Learning Dynamics:
#   ResourceLevelHistory (perferrably when not changing stuff) -SystemEquationGenerator-> SystemEquation
#   ResourceLevel -SystemEquation-> SystemBasedPredictedResourceLevel
#   SystemEquations -SystemDynamicsGenerator-> SystemDynamics
#   State -SystemDynamics-> SystemBasedPredictedState
# 
#   ResourceLevelHistory (perferrably when environment not changing) -ControlEquationGenerator-> ControlEquation
#   ResourceLevel -ControlEquation-> ControlBasedPredictedResourceLevel
#   ControlEquations -ControlDynamicsGenerator-> ControlDynamics
#   State, Action -ControlDynamics-> ControlBasedPredictedState

class PerformanceElement:
    def __init__(self, actions=None, conditional_logic=None, speculator=None, utility_function=None):
        """Maps precepts to actions

        Parameters
        ----------
        actions : FunctionList
            The actions the agent can take
        conditional_logic : Options, Actions -> Action
            How the agent decides which action to take based on the options available
        speculator : State, Time, Action -> NextState
            How the environment changes over time and as a result of actions the agent takes
        utility_function : State -> Number
            How the agent determines how useful a given state might be
        """
        default_action = Action("Default Action", lambda msg: print("Warning: No actions defined, press Ctrl+C to quit."))
        # TODO: Make default logic choose random action from actions instead of always choosing the first
        default_conditional_logic = lambda options: list(reversed(sorted(options)))[0].action
        default_speculator = lambda state, action: state
        default_utility_function = lambda state: 0.0

        self.actions = actions if actions != None else [default_action]
        self.conditional_logic = conditional_logic if conditional_logic != None else default_conditional_logic
        self.speculator = speculator if speculator != None else default_speculator
        self.utility_function = utility_function if utility_function != None else default_utility_function

    def __call__(self, prev_state):
        # Generate list of options (possible future states)
        options = map(
            lambda action: toOption(action, prev_state, self.utility_function, self.speculator),
            self.actions
        )

        # Apply conditional logic to choose an action from the options
        action = self.conditional_logic(options)

        # Perform action (Warning: May have side-effects)
        state = action(prev_state)

        # Output results
        return state

class Agent:
    def __init__(self, performance_element, initial_state={}):
        self.state = initial_state
        self.performance_element = performance_element

    def __call__(self, previous_state):
        return self.performance_element(previous_state)

    def run(self, initial_state):
        self.state = initial_state
        while True:
            self.state = self.performance_element(self.state)

'''

Performance Standard
- Some performance goal

Critic
- Compares the performance of the Performance Element to some Performance Standard

Learning Element
- Adjusts the parameters of the Performance Element based on feedback from the Critic in order to get better performance

Problem Generator
- Generates tasks that challenge the Agent to practice skills that need improvement

'''
