#!/usr/bin/env python3

from omg import *
import re
import sys

SCRIPT_DEF_RE = re.compile("script (\d+) ")

ACS_LINE_TYPES = {
    80: "Started",
    81: "Suspended",
    82: "Stopped",
    83: "Started (locked)"
}

def describe_line(line_idx, line):
    vx_a, vx_b = ed.vertexes[line.vx_a], ed.vertexes[line.vx_b]
    x = (vx_a.x + vx_b.x) // 2
    y = (vx_a.y + vx_b.y) // 2
    return "%s by line %d at (%d, %d)" % (
        ACS_LINE_TYPES[line.action], line_idx, x, y,
    )

def describe_thing(thing_idx, thing):
    return "%s by thing %d at (%d, %d)" % (
        ACS_LINE_TYPES[thing.action], thing_idx, thing.x, thing.y,
    )

def describe_trigger(idx, trigger):
    if isinstance(trigger, ZThing):
        return describe_thing(idx, trigger)
    else:
        return describe_line(idx, trigger)

w = WAD()
w.from_file(sys.argv[1])
for name in w.maps:
    print(name)
    ed = MapEditor(w.maps[name])
    scripts = {}
    for line_idx, line in enumerate(ed.linedefs):
        if line.action in ACS_LINE_TYPES:
            scripts.setdefault(line.arg0, []).append((line_idx, line))

    for thing_idx, thing in enumerate(ed.things):
        if thing.action in ACS_LINE_TYPES:
            scripts.setdefault(thing.arg0, []).append((thing_idx, thing))

    for script, triggers in sorted(scripts.items()):
        print("\tScript %d:" % script)
        for idx, trigger in triggers:
            print("\t\t" + describe_trigger(idx, trigger))

    if True:
        lines = []
        acs_filename = "../%s.acs" % name.lower()
        with open(acs_filename) as f:
            for s in f:
                s = s.rstrip()
                m = SCRIPT_DEF_RE.match(s)
                if m:
                    script = int(m.group(1))
                    for idx, trigger in scripts.get(script, []):
                        lines.append("// " + describe_trigger(idx, trigger))
                lines.append(s)

        with open(acs_filename, "w") as f:
            for s in lines:
                print(s, file=f)

    print()
