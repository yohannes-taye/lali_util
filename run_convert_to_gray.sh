#!/bin/bash


#Root directory of dataset
root_dir=/home/tmc/Documents/virtual_scene_training_data

#Path to the directory containing the depth images
depth_dir=$root_dir/depths


#Get list of folders in the root directory
folders=$(ls $depth_dir)

#Array of folders to ignore
ignore_folders=("depths" "depths_gray")

#Loop through each folder
for folder in $folders
do
    #Check if folder is in ignore list
    if [[ " ${ignore_folders[@]} " =~ " ${folder} " ]]; then
        echo "Ignoring folder $folder"
        continue
    fi
    
    echo "Processing folder: $depth_dir/$folder"
    
    python ./convert_to_gray.py \
        -i $depth_dir/$folder \
        -o $depth_dir/$folder 
    
    rm $depth_dir/$folder/*.jpeg 

done