**Task duration calculation**

This code is designed for an experimental setting where one participant completes the same task across multiple trials. The focus is on measuring the duration of each trial (i.e., the time it takes to accomplish the task).

**How it works:**

1) The program begins by asking for the participant's ID (e.g., **Sub01**).
2) Once the ID is entered, you will be prompted to start the task.
  - Press `Enter` to start the timer.
  - After completing the task, press `Enter` again to stop the timer.
3) After each trial, you will be asked if this is the end of the experiment:
  - **Type** `STOP` to end the session.
  - Otherwise, press `Enter` to continue and start a new trial.
4) Each trial's duration will be recorded in a CSV file, named based on the participant's ID, and saved in the designated location.

**Output:**

- A CSV file is generated for each participant, capturing the time data for every trial.
- The CSV file contains two columns:
  1) Trial Number: The trial number (e.g., 1, 2, 3, …).
  2) Duration (seconds): The duration of the task in seconds for each trial.
