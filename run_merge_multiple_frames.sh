output_path=/home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/merged_video

rm -rf $output_path/*

python ./merge_multiple_frames.py \
    -i /home/tmc/project/AdelaiDepth/LeReS/Train/scripts/output/depth_test \
    -f depth \
    -o $output_path \
    # -d \

python ./picture_to_video.py \
    -i $output_path \
    -o $output_path \
    -n depth \
    -f 30 \

    