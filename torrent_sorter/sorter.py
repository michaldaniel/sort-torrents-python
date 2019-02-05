# -*- coding: utf-8 -*-

import os
import re
import warnings


# Just some terminal beauty helpers
class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARK_CYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


# Helpful regex
ANY_CHARACTER = r"[\w\W]"
ANY_CHARACTERS = ANY_CHARACTER + r"+"
ANY_CHARACTERS_IN_BRACKETS = r"\[" + ANY_CHARACTERS + r"\]"

# Config to match HorribleSubs distributions and most others
# Requires to produce 3 groups in order: name, episode, extension
# \[[\w\W]+\] ([\w\W]+) - ([\d]+) \[[\w\W]+\].([\w]+)
PATTERN = ANY_CHARACTERS_IN_BRACKETS + r" (" + ANY_CHARACTERS + r") - ([\d]+) " \
          + ANY_CHARACTERS_IN_BRACKETS + r".([\w]+)"


def sort(source, destination):
    pattern = re.compile(PATTERN)
    print("Looking for matching files inside \"%s\"." % source)
    source_files = [f for f in os.listdir(source) if
                    os.path.isfile(os.path.join(source, f)) and pattern.fullmatch(f)]
    print("%d files found." % len(source_files))
    if len(source_files) > 0:
        print("Sorting into \"%s\"." % destination)
    torrents_moved = {}
    directories_created = []
    failed_attempts = 0
    for file in source_files:
        groups = pattern.fullmatch(file).groups()
        if len(groups) != 3:
            raise RuntimeError("pattern produced invalid number of groups")
        show = groups[0]
        episode = groups[1]
        extension = groups[2]
        if not os.path.exists(os.path.join(destination, show)):
            directories_created.append(show)
            os.makedirs(os.path.join(destination, show))
        try:
            os.rename(os.path.join(source, file),
                      os.path.join(destination, show, show + " - " + episode + "." + extension))
            torrents_moved[show] = torrents_moved.get(show, 0) + 1
        except OSError:
            warnings.warn("Failed to move file \"%s\", already exists at destination." % file, Warning)
            failed_attempts += 1

    print(os.linesep)
    print(Color.BOLD + "Summary" + Color.END)
    print("Created %d new directories." % len(directories_created))
    print("Sorted %d series and %d episodes." % (len(torrents_moved.keys()), sum(torrents_moved.values())))
    if len(directories_created):
        print("New directories: " + ", ".join(directories_created))
    for key, entry in torrents_moved.items():
        print("Moved %d files into \"%s\" directory." % (entry, key))
    if failed_attempts > 0:
        print("Failed to move %d files" % failed_attempts)
