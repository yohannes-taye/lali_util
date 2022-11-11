python /home/tmc/project/lali_util/merge_pictures_h.py \
    -i1 /home/tmc/Documents/Demo/DPT/rgb \
    -i2 /home/tmc/Documents/Demo/DPT/depth \
    -o /home/tmc/Documents/Demo/DPT/combined && \

python /home/tmc/project/lali_util/picture_to_video.py \
    -i /home/tmc/Documents/Demo/DPT/combined \
    -o /home/tmc/Documents/Demo/DPT/ \
    -f 15 && \

ffmpeg -i /home/tmc/Documents/Demo/DPT/video.mp4 -r 15 -vf scale=512:-1 -ss 00:00:01 -to 00:00:20 /home/tmc/Documents/Demo/DPT/demo.gif 
