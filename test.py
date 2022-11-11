

import os 

"""A function to return all files in a directory as a list of strings"""
def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        files.append(filename)
    return files

def main():
    contents = list_files('/run/user/1000/gvfs/smb-share:server=192.168.3.2,share=tmc数据缓冲区/lali/depth2')
    print(contents)




if __name__ == "__main__":
    main()
