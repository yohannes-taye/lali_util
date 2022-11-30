#!/bin/bash

python /home/tmc/project/lali_util/merge_data.py \
    --input_folder /home/tmc/Documents/virtual_scene_training_data/rgbs \
    --output_folder ./test \
    --frame_path "" \
    --resolution 1920x1080 \
    --duration 10 \
    --extension jpeg \
    --debug 
