#!/bin/bash


#Root directory of dataset
root_dir="/run/user/1000/gvfs/smb-share:server=tmc_datamanage.local,share=datasets/depth train data/test2"

destination_folder="./test2"
#Path to the directory containing the depth images
depth_dir=depth 

#Path to the directory containing the rgb images
rgb_dir=rgb_WithNoise

#Get list of folders in the root directory
folders=$(ls "$root_dir")

#Array of folders to ignore
ignore_folders=("depths" "depths_gray")





#If destination_folder doesnt exist create 
if [ ! -d "$destination_folder" ]; then
    mkdir "$destination_folder"
fi

if [ ! -d "$destination_folder/rgbs/" ]; then
    mkdir "$destination_folder/rgbs/"
fi

if [ ! -d "$destination_folder/depths/" ]; then
    mkdir "$destination_folder/depths/"
fi



#Loop through each folder
for folder in $folders
do
    #Check if folder is in ignore list
    if [[ " ${ignore_folders[@]} " =~ " ${folder} " ]]; then
        echo "Ignoring folder $folder"
        continue
    fi

    echo "Processing folder: $folder"
    mkdir "$destination_folder/rgbs/$folder"
    cp "$root_dir/$folder/$rgb_dir/"/* "$destination_folder/rgbs/$folder"
    mkdir "$destination_folder/depths/$folder"
    cp "$root_dir/$folder/$depth_dir/"* "$destination_folder/depths/$folder"

done



