#python extract_frame_from_video.py -i /home/tmc/Documents/Data/2d-3d-test/test_stuff/01.mp4 -o /home/tmc/Documents/Data/2d-3d-test/test_stuff/01 & 
#python extract_frame_from_video.py -i /home/tmc/Documents/Data/2d-3d-test/test_stuff/02.mp4 -o /home/tmc/Documents/Data/2d-3d-test/test_stuff/02 & 
#python extract_frame_from_video.py -i /home/tmc/Documents/Data/2d-3d-test/test_stuff/03.mp4 -o /home/tmc/Documents/Data/2d-3d-test/test_stuff/03 & 
python extract_frame_from_video.py -i /home/tmc/Documents/Data/office/VID_20220606_173034.mp4 -o /home/tmc/Documents/Data/office/img & 


python ./scripts/colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 16 --images /home/tmc/Documents/Data/office/img/