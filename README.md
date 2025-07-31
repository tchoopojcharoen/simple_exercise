Exercise: Go-To-Goal Controller
Objective
To become familiar with the concept of interface design using composition over inheritance in the context of ROS 2.

Requirements
ROS 2 Humble

Installed packages:

turtlesim

geometry_msgs

Instructions
Clone the repository and move the interface_exercise ROS package into the src folder of your ROS 2 workspace.

Implement the interface:
Open the go2goal_node_exercise.py script inside the scripts folder. Complete the Interface class definition. You may also modify other parts of the script as needed. Renaming the script is allowed.

Update the build system:
Modify the CMakeLists.txt file so that it correctly installs or registers your updated script.

Test your implementation:
Use ROS 2 CLI tools to launch the turtlesim node, run your script, and publish goal positions to evaluate the behavior.
