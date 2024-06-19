# Personal-task-manager

A simple task manager designed to run on a Raspberry Pi within a home network. This project aims to provide users with an efficient tool for organizing and prioritizing tasks, enhancing productivity and effectiveness in managing daily activities.


## Getting Started

Follow these instructions to set up and run the project on your local system.


### Prerequisites

Ensure you have the following software installed on your system:

1. [Python 3] (https://www.python.org/downloads/)
2. [PyCharm IDE] (https://www.jetbrains.com/pycharm/download/?section=windows)
3. Install required Python packages using PyCharm, such as:
 - Flask library: from flask import Flask


### Installation

1. Clone the repository:[GitHub Repository](https://github.com/AbiyuTamirat2/Personal-task-manager)  
2. Navigate to the project directory.

### Running the Application

Initialize the Database

Run the following command to initialize the SQLite database:

python task_manager.py

This will create a tasks.db file with the necessary table.



### Access the Task Manager

Open a web browser and navigate to http://<raspberry-pi-ip>:5000.

Add Tasks: Create new tasks with a title and description.

View Tasks: See a list of all tasks.

Edit Tasks: Modify existing task details.

Delete Tasks: Remove tasks that are no longer needed.


### Files

task_manager.py: Main application file containing Flask routes and database interactions.

templates/home.html: Template for displaying the list of tasks.

templates/add.html: Template for adding a new task.

templates/edit.html: Template for editing an existing task.


## Credits

Special thanks to Professor Kim for providing the initial codebase and allowing us to modify it for our project.

