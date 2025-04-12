#!/usr/bin/env bash
#
# Builds all .acs files using ACC, and compares against the compiled versions
# found in the Hexen IWAD file.

set -eu

SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy dosbox -conf build.cfg

success=true

for compiled in compiled/map??acs.lmp; do
    ofile=$(basename $compiled)
    ofile=${ofile/acs.lmp/.O}
    ofile=${ofile/map/MAP}
    if ! diff -u $compiled $ofile; then
        success=false
    fi
done

$success
