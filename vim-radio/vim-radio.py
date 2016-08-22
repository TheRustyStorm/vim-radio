import os                                                                                                                                                                       
import argparse
from subprocess import call
streamlist=[
#paste stream address here
]
parser = argparse.ArgumentParser()
parser.add_argument("n")
args=parser.parse_args()
number=int(args.n)
call(["/Applications/VLC.app/Contents/MacOS/VLC", "-I", "rc",streamlist[number]])
