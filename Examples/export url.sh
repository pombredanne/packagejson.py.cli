#!/usr/bin/env bash
{ set +x; } 2>/dev/null

url="https://github.com/owner/repo"
export url="$url"
( set -x; packagejson-generator.py )
