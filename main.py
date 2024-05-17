import argparse
from pathlib import Path
from copy import copy


# Parse argument from sys arg
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-d',
    '--dataset',
    nargs='+',
    type=str,
    choices=['train', 'val'],
    help="Dataset to download."
)

parser.add_argument(
    '-a',
    '--annotation',
    type=str,
    help="Path to annotation file. Ignored if --dataset is set."
)

parser.add_argument(
    '-c',
    '--classes',
    nargs='+',
    type=str,
    help="Classes to download. Used when only certain classes are needed. Default to None, which downloads all classes."
)

parser.add_argument(
    '-ac',
    '--all-classes',
    action='store_true',
    help="Whether to download only images that contains all classes. Default to False. Ignored if --classes is None."
)

parser.add_argument(
    '-s',
    '--save',
    type=str,
    help="Path to destination directory for saving"
)

parser.add_argument(
    '-sa',
    '--save-annotation',
    type=str,
    choices=['yolo', 'coco'],
    default='coco',
    help="Annotation style to save data as. Default to COCO style."
)

args = parser.parse_args()

if __name__ == '__main__':
    print(args.dataset)