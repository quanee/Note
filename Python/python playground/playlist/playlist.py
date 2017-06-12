import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


def findCommonTracks(fileNames):
    """
    Find common tracks in given playlist files,
    and save them to common.txt
    """
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set()
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add the track name to a set
                trackNames.add(track['Name'])
            except Exception:
                # ignore
                pass
        # add to list
        trackNameSets.append(trackNames)
        # get the set of common tracks
        commonTracks = set.intersection(*trackNameSets)
        # write to file
        if len(commonTracks) > 0:
            f = open("common.txt", 'w')
            for val in commonTracks:
                s = "%s\n" % val
                f.write(str(s.encode("utf8")))
            f.close()
            print("%d common tracks found."
                  "Track names written to common.txt" % len(commonTracks))