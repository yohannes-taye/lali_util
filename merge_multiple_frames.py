import argparse
import debugpy 
import os 
import cv2 
#MAIN 
def main(): 
    parser = argparse.ArgumentParser(description='Merge multiple frames into one')
    parser.add_argument('-i', '--input_folder', help='Input folder', required=True)
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true', default=False)
    parser.add_argument('-f', '--image_folder', help='Image folder', required=True)
    parser.add_argument('-o', '--output_folder', help='Output folder', required=True)
    parser.add_argument('-s', '--show_image', help="Show image before saving",  action='store_true', default=False)
    args = parser.parse_args() 

    if args.debug:
        debugpy.listen(5678)
        print("Press play!")
        debugpy.wait_for_client()

    #Get all folders in input folder
    folders = [f for f in os.listdir(args.input_folder) if os.path.isdir(os.path.join(args.input_folder, f))]
    images = {}
    for folder in folders: 
        path = os.path.join(args.input_folder, folder, args.image_folder)
        images[folder] = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]   
        images[folder].sort() 

    #Get all keys for images dict 
    keys = images.keys()
    #convert to list
    keys = list(keys)
    for i in range(len(images[keys[0]])):
        frame = []
        for key in keys:
            img = cv2.imread(images[key][i])
            #Add big red text to top left corner
            cv2.putText(img, f"Stage {key}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            frame.append(img)
        #Merge all images into one
        merged = cv2.vconcat(frame)


        if(args.show_image):
            cv2.imshow('Depth', merged)
            cv2.waitKey(1)

        #save image
        cv2.imwrite(os.path.join(args.output_folder, f'{i}.png'), merged)
                        
        print(f"Processing image {images[keys[0]][i]}")
        print("pawse")
    print("shit")


if __name__ == "__main__":

    main()