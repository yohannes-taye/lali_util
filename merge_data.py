import argparse
import debugpy
import os 
import cv2 


def main(): 
    #Process arguments
    parser = argparse.ArgumentParser(description='Merge multiple frames into one')
    parser.add_argument('--input_folder', help='Input folder', required=True) 
    parser.add_argument('--output_folder', help='Output folder', required=True)
    parser.add_argument('--frame_path', help='Path to frame', required=True)
    parser.add_argument('--debug', help='Debug mode', action='store_true', default=False)
    parser.add_argument('--resolution', help='Resolution', required=True)
    parser.add_argument('--duration', help="Duration",  default="10")
    parser.add_argument('--extension', help="Extension",  default="jpeg")
    parser.add_argument('--ignore_folders', nargs='+', help="List of folders to ignore")
    args = parser.parse_args()
    
    if args.debug:
        debugpy.listen(5678)
        print("Press play!")
        debugpy.wait_for_client()

    #Create output folder if it doesn't exist
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    #Get all folders in input folder
    folders = [f for f in os.listdir(args.input_folder) if os.path.isdir(os.path.join(args.input_folder, f))]

    duration = int(args.duration) 
    num_read_frames = 30 * duration
    global_counter = 0 

    width = int(args.resolution.split("x")[0])
    height = int(args.resolution.split("x")[1])
    
    for folder in folders: 
        #Get all images in folder
        path = os.path.join(args.input_folder, folder, args.frame_path)
        images = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]   
        images.sort() 

        if args.ignore_folders and folder in args.ignore_folders:
            print(f"Ignoring folder {folder}")
            continue

        for i in range(num_read_frames):
            print(f"Processing image {images[i]}")
            img = cv2.imread(images[i])
            #Resize image
            img = cv2.resize(img, (width, height))
            cv2.imwrite(os.path.join(args.output_folder, f'{global_counter}.{args.extension}'), img)
            global_counter += 1
    


if __name__ == "__main__":
    main()