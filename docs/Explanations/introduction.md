Introduction
=============
<!-- Describe the project and its purpose
The goal of this project is to build/create/provide…[the what]… for …[the who]… so that she/he/they can …[the why]. We aim to accomplish this with …[the how]…[the where]… by/on/before …[the when].
-->
This project is an attempt at describing the main parts of an AI/ML agent, whether it's just a simple reflex agent, model-based reflex agent, goal-based agent, or a utility agent. It is intented to make it easier to automate a wide variety of tasks by allowing developers to focus more on improving and optimizing the agent's main components rather than having to worry about how those components fit together to form the whole agent, and by breaking the process into smaller steps that build upon each other as the agent's capabilities are expanded and iterated upon.

This complexity progression for AI/ML agents is defined as follows:

1. "Agent" always performs the same **Action** and the output is always the same regardless of the input
    - i.e. An "agent" that always prints out "Hello, World!"
2. "Agent" always performs the same Action, but the output changes based on the input **Parameters**
    - i.e. An "agent" that always doubles the input
3. Agent uses the input and some **Conditional Logic** to decide which action to perform
    - i.e. An agent that can either add, subtract, multiply, or divide a number depending on the command you provide
4. Agent can keep track of previous **States** so it doesn't have to depend completely upon the current precept
    - i.e. An robotic lawnmower agent that remembers where it has already mowed so that it doesn't try to mow grass that has already been mowed
5. Agent can update its mental "snapshots" according to some **System Dynamics** (Understanding about how the relevant environment changes over time assuming no action from the agent)
6. Agent can update its mental "snapshots" according to some **Control Dynamics** (Understanding about how the relevant environment changes as a result of the agent's actions)
7. Agent can use the System and Control Dynamics to **Speculate** about possible future states caused by taking performing certain actions
8. Agent can determine the usefulness of possible future states using a **Utility Function**
9. Agent uses a **Critic** to measure its performance
10. Agent uses the Critic to compare its performance to some **Performance Standard** (which can be either internal or, perhaps more likely, external)
11. Agent uses a **Learning Element** to adjust the performance parameters of the performance element based on feedback from the Critic
12. Agent uses a **Problem Generator** to create practice problems to challenge itself to learn concepts it doesn't understand very well
13. Agent continues to improve its Speculator by actively trying to learn and anticipate the actions of **Other Agents** and how they could affect the environment as well as the agent's own decision-making process
14. Agent focuses on **Competition** with other agents
15. Agent focuses on **Communication, Negotiation, and Other Collaborative Efforts** with other agents so that it no longer has to compete for resources
