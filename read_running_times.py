# This program the values in the video_times.txt file 
# and calculates the total running time of the videos.

def main():
    # Open the video_times.txt file for reading.
    video_file = open('running_times.txt', 'r')
    
    # Initialize an accumulator to 0.0.
    total = 0.0
    
    # Initialize a variable to keep count of the videos.
    count = 0
    
    print('Here are the running times for each video:')
    
    # Get the values from the file and total them.
    for line in video_file:
        # Convert a line to a float.
        run_time = float(line)
        
        # Add the run_time to total.
        total += run_time
        
        # Add 1 to the count variable.
        count += 1
        
    # Close the file.
    video_file.close()
        
    # Display the running time.
    print(f"The total running time for video {total:.2f} seconds.")
        
# Call the main function.
if __name__ == "__main__":
    main()