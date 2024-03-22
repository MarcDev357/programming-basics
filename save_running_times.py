#This program saves a sequence of running times to a file
def main():
    # Get the number of videos in the project.
    num_videos = int(input("How many videos are in the project? "))
    
    #Open the file to hold the running times.
    video_file = open('running_times.txt', 'w')
    
    # Get each video's running time and write it to the file.
    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input(f"Video #{count}: "))
        video_file.write(f"{run_time}\n")
        
        #close the file.
    video_file.close()
    print('The running times have been saved to running_times.txt.')
        
        # Call the main function.
if __name__ == "__main__":
    main()