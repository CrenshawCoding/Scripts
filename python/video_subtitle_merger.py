import argparse

# Setting up the arg parser:
parser = argparse.ArgumentParser(description='parse for relevant information')
parser.add_argument('video_format')
parser.add_argument('subtitle_format')
parser.add_argument('--dir', help='Root directory for merging')
args = parser.parse_args()
print(args)