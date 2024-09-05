import csv
import time
import os
# Defining the three main tasks
def prompt_ready():
    input("STARTING? Press the enter to start the timer...")

def wait_for_stop():
    input("FINISHING? Press the enter to stop the timer...")

def main():
    participant_id = input("Enter participant ID: ")

    # Directory to save the CSV file
    save_directory = "YOUR PATH"

    # Ensure the directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    durations = []
    trial_number = 1

    while True:
        print(f"Trial {trial_number}")
        prompt_ready()
        start_time = time.time()
        wait_for_stop()
        end_time = time.time()
        duration = end_time - start_time
        print(f"Duration for trial {trial_number}: {duration:.2f} seconds")
        durations.append((trial_number, duration))
        trial_number += 1

        # Finishing one session and requesting for CSV file generation
        if input("The of the task? (Type STOP for having the results, otherwise press enter): ").lower() == 'stop':
            break

    # Save the durations to a CSV file
    csv_filename = os.path.join(save_directory, f"{participant_id}_task_durations.csv")
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Trial", "Duration (seconds)"])
        for trial, duration in durations:
            writer.writerow([trial, duration])

    print(f"Durations saved to {csv_filename}")

if __name__ == "__main__":
    main()
