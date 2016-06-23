#!/usr/bin/env bash
{ set +x; } 2>/dev/null

bugs="https://github.com/owner/repo/issues"
export BUGS="$BUGS"
( set -x; python -m packagejson )
