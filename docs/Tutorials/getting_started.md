Getting Started
================
1. Import the agent component types you need for your project
    ```python
    from agents import Agent, Action, Speculator, PerformanceElement
    ```
2. Import your agent component definitions
    ```python
    import my_agent
    ```
3. Import your action modules
    ```python
    import my_action_module
    ```
4. Initialize and run the agent
    ```python
    def main():
        # Define actions the agent can take
        actions = [
            Action("Agent Main Loop", my_action_module.main, input_types="PreviousState", output_types="NextState")
        ]

        # Initialize the agent
        agent = Agent(
            PerformanceElement(
                actions,
                my_agent.conditionalLogic,
                Speculator(
                    my_agent.systemDynamics,
                    my_agent.controlDynamics
                ),
                my_agent.utilityFunction
            )
        )

        # Define the starting state
        initial_state = {}

        # Run the agent
        agent.run(initial_state)

    if __name__ == '__main__':
        main()
    ```
5. Run your agent with
    ```terminal
    $ python agent.py
    ```
