#!/usr/bin/env python3

from omg import *
import re
import sys

SCRIPT_DEF_RE = re.compile("script (\d+) ")

def describe_line(line_idx, line):
    vx_a, vx_b = ed.vertexes[line.vx_a], ed.vertexes[line.vx_b]
    x = (vx_a.x + vx_b.x) // 2
    y = (vx_a.y + vx_b.y) // 2
    addendum = " (locked)" if line.action == 83 else ""
    return "Started%s by line %d at (%d, %d)" % (
        addendum, line_idx, x, y,
    )

w = WAD()
w.from_file(sys.argv[1])
for name in w.maps:
    print(name)
    ed = MapEditor(w.maps[name])
    scripts = {}
    for line_idx, line in enumerate(ed.linedefs):
        if line.action in (80, 83):
            scripts.setdefault(line.arg0, []).append((line_idx, line))

    for script, lines in sorted(scripts.items()):
        print("\tScript %d:" % script)
        for line_idx, line in lines:
            print("\t\t" + describe_line(line_idx, line))

    if True:
        lines = []
        acs_filename = "../%s.acs" % name.lower()
        with open(acs_filename) as f:
            for s in f:
                s = s.rstrip()
                m = SCRIPT_DEF_RE.match(s)
                if m:
                    script = int(m.group(1))
                    for line_idx, line in scripts.get(script, []):
                        lines.append("// " + describe_line(line_idx, line))
                lines.append(s)

        with open(acs_filename, "w") as f:
            for s in lines:
                print(s, file=f)

    print()
