#! /usr/bin/env python
import argparse
from Shoutcast.stream_writer import StreamWriter
from pprint import pprint

parser = argparse.ArgumentParser(description='Tool that will record a Shoutcast stream.')

parser.add_argument('url', help="Shoutcast stream URL")
parser.add_argument('length', type=int, help="Length of time to record stream (in seconds)")
parser.add_argument('-d', '--destination', default="./", 
                    help="File destination. Defaults to current directory")
parser.add_argument('-f', '--filename', default="output.mp3", help="File name of saved stream")

args = parser.parse_args()

s = StreamWriter( args.url, args.length, destination=args.destination, filename=args.filename)

s.record()
pprint(s.metadata)
