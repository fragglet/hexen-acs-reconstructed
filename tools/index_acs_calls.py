#!/usr/bin/env python3
#
# Generates an index of which ACS scripts execute other scripts

import re
import sys

SCRIPT_RE = re.compile(r"script (\d+)")
COMMENT_RE = re.compile(r"/\*.*\*/")
EXECUTE_CALL_RE = re.compile(r"ACS_Execute\((.*)\s*,\s*(.*),\s*(.*),\s*(.*),\s*(.*)\)")
MAP_NAME_RE = re.compile(r"map(\d+)")

for filename in sys.argv[1:]:
    mapnum = 0
    m = MAP_NAME_RE.match(filename)
    if m:
        mapnum = int(m.group(1))
    with open(filename) as f:
        curr_script = None
        for line in f:
            line = line.replace("const:", "")
            line = COMMENT_RE.sub("", line)
            m = SCRIPT_RE.match(line)
            if m:
                curr_script = int(m.group(1))
            m = EXECUTE_CALL_RE.search(line)
            if m:
                exscript = int(m.group(1))
                exmap = int(m.group(2))
                if exmap == 0:
                    exmap = mapnum
                print("%s %d %d %d" % (filename, curr_script, exmap, exscript))
