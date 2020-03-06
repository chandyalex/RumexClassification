import cv2
import time
import os

def video_to_frames(input_loc, output_loc, jump_between_saving_frames=5):
    """
    https://stackoverflow.com/a/49011190/7910473
    Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        if count % jump_between_saving_frames == 0:
            # Extract the frame
            ret, frame = cap.read()
            # Write the results back to output location.
            cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
            
            # If there are no more frames left
            if (count > (video_length-1)):
                # Log the time again
                time_end = time.time()
                # Release the feed
                cap.release()
                # Print stats
                print ("Done extracting frames.\n%d frames extracted" % count)
                print ("It took %d seconds forconversion." % (time_end-time_start))
                break
        elif count == video_length-1:
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

        count = count + 1

input_loc = './data/rumex.mp4'
output_loc = './data/images/'
video_to_frames(input_loc, output_loc)