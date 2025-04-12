#!/usr/bin/env python3

from omg import *
import sys

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
            vx_a, vx_b = ed.vertexes[line.vx_a], ed.vertexes[line.vx_b]
            x = (vx_a.x + vx_b.x) // 2
            y = (vx_a.y + vx_b.y) // 2
            addendum = " (locked)" if line.action == 83 else ""
            print("\t\tStarted%s by line %d at (%d, %d)" % (
                addendum, line_idx, x, y,
            ))
    print()
