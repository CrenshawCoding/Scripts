import argparse
import os, sys
import shutil

# Setting up the arg parser:
parser = argparse.ArgumentParser(description='parse for relevant information')
parser.add_argument('video_format', help='File ending of the video files, currently supported: mkv, mp4', choices=['mkv', 'mp4'])
parser.add_argument('subtitle_format', help='File ending of the subtitle files, currently supported: srt', choices=['srt'])
parser.add_argument('subtitle_language', help='language of the subitle, currently supported: ger, en, spa', choices=['en', 'ger', 'spa'])
parser.add_argument('--dir', help='Root directory for merging, default is \'.\'', default='.')
args = parser.parse_args()

#kinda deprecated. I always put files in subdirectories now. Makes it easier
def colliding_files_in_dir(directory):
    return True if count_files_of_type(args.video_format, directory) > 0 else False

def count_files_of_type(file_ext, directory):
    counter = 0
    for f in os.listdir(directory):
        if(f.endswith('.' + file_ext)):
            counter = counter + 1
    return counter
    
def get_all_files_of_type(file_ext, directory):
    file_list = []
    for f in os.listdir(directory):
        if(f.endswith('.' + file_ext)):
            file_list.append(f)
    return file_list
    
    
#Script start:
  
inp = False  
for root, dirs, files in os.walk(args.dir, topdown = False):
    if root == args.dir: #skipping the top level. Checks for this are done seperately later
        continue
    
    for name in files:
        if name.endswith('.' + args.video_format) and os.path.join(root, name).count('/') > 2: #found video files in subsubdirectories of root
            print('The root directory \'' + str(args.dir) + '\' is flawed. It may only contain video or subtitle files in subdirectories of \'' + str(args.dir) + '\' but \'' + str(os.path.join(root, name)) + '\' was found.')
            if not inp:
                inp = input('Do you wish to move all of them to the root dir' + os.path.join(args.dir, name) + ' automatically? Type \'y\' or \'n\'\n')
            if inp == 'y':  #moving the file to the root directory
                shutil.move(os.path.join(root, name), os.path.join(args.dir, name))
                print('Moved', os.path.join(root, name), 'to', os.path.join(args.dir, name))
            elif inp == 'n':
                print('Exiting.')
                sys.exit()
    
    for name in dirs:
        if count_files_of_type(args.video_format, os.path.join(root, name)) > 2: #found multiple video files in a subdirectory
            print('Found multiple video files in \'' + os.path.join(root, name) + '\'')
            print('Exiting.')


#Multiple files of same type in base directory, offer to sort them
if(colliding_files_in_dir(args.dir)):
    inp = input('Multiple files with the same extension in root detected\nDo you wish to sort them into subdirectories automatically? Type \'y\' or \'n\':\n')
    if inp == 'y':
        all_video_files = get_all_files_of_type(args.video_format, args.dir)
        all_subtitle_files = get_all_files_of_type(args.subtitle_format, args.dir)
        for x in range(0, len(all_video_files)):
            try:
                dirName = args.dir + os.sep + str(x + 1)
                print('creating', dirName)
                os.mkdir(dirName)
            except OSError as e:
                if e.errno == errno.EEXist:
                    print('directory', dirName, 'already exists.')
            target = dirName + os.sep + all_video_files[x]
            print('moving', all_video_files[x], 'to', target)
            shutil.move(all_video_files[x], target)
            if x < len(all_subtitle_files):
                target = dirName + os.sep + all_subtitle_files[x]
                print('moving', all_subtitle_files[x], 'to', target)
                shutil.move(all_subtitle_files[x], target)
            
    elif inp == 'n':
        print('Try again after manually sorting the files into subdirectories')
        sys.exit()

for root, dirs, files in os.walk(args.dir, topdown = True):
    for name in dirs:
        if count_files_of_type(args.video_format, os.path.join(root, name)) == 1 and count_files_of_type(args.subtitle_format, os.path.join(root, name)) > 0:
            video_file = get_all_files_of_type(args.video_format, os.path.join(root, name))[0]
            merge_command = 'mkvmerge ' + '-o \"' + os.path.join(args.dir, video_file) + '\" \"' + os.path.join(root, name, video_file) + '\" '
            for subfile in get_all_files_of_type(args.subtitle_format, os.path.join(root, name)):
                merge_command = merge_command + '--language 0:' + args.subtitle_language + ' \"' + os.path.join(root, name, subfile) + '\" '
            if video_file and subfile:
                print(merge_command)
                os.system(merge_command)
