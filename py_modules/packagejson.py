#!/usr/bin/env python
import copy
import json
import os
import sys

if __name__ != "__main__":
    sys.exit(0)

USAGE = "usage: %s" % os.path.basename(__file__)

if len(sys.argv) == 2 and sys.argv[1] == "--help":
    print(USAGE)
    sys.exit(0)


def read(path, default=None):
    if os.path.exists(path) and os.path.isfile(path):
        return open(path).read()  # .decode("utf-8")
    return default

package = dict(
    name=None,  # required
    version='0.0.0',  # required
    description=os.environ.get("DESCRIPTION", None),
    keywords=os.environ.get("KEYWORDS", None),
    licence=os.environ.get("LICENCE", None),
    readme=None,  # README.md
    repository=dict(),
    scripts=dict(),
    bin=[],
    bugs=[],

    # not editable
    private=None,
    preferGlobal=[],
)

# name
# pkgname.py -> pkgname
# pkgname.sh.cli -> pkgname
# CASE SENSITIVE!!!1
package["name"] = os.path.basename(os.getcwd()).split(".")[0].lower()
if "NAME" in os.environ and os.environ["NAME"]:
    package["name"] = os.environ["NAME"]

# version
for path in ["version", "version.txt"]:
    if os.path.exists(path) and os.path.isfile(path):
        version = read(path)
        if version:
            package["version"] = version.rstrip()

# description
for path in ["description", "description.txt"]:
    if os.path.exists(path) and os.path.isfile(path):
        package["description"] = read(path)

# keywords
for path in ["keywords", "keywords.txt"]:
    if os.path.exists(path) and os.path.isfile(path):
        package["keywords"] = read(path).split(' ')

# bin
if os.path.exists("bin") and os.path.isdir("bin"):
    listdir = os.listdir("bin")
    for l in listdir:
        fullname = os.path.join("bin", l)
        if os.path.isfile(fullname):
            package["bin"] += ["./%s" % fullname]

# bugs
if "BUGS" in os.environ and os.environ["BUGS"]:
    package["repository"]["bugs"] = [os.environ["BUGS"]]

# repository
# repository.type
if os.path.exists(".git"):
    package["repository"]["type"] = "git"
# repository.url
if "URL" in os.environ and os.environ["URL"]:
    package["repository"]["url"] = os.environ["URL"]

# readme
if "README" in os.environ and os.environ["README"]:
    readme = os.environ["README"]
    if os.path.exists(readme):
        if os.path.isfile(readme):
            package["readme"] = read(readme)
        else:
            raise OSError("%s NOT EXISTS" % readme)
else:
    if os.path.exists("README.md") and os.path.isfile("README.md"):
        package["readme"] = read("README.md")

# https://docs.npmjs.com/misc/scripts
for script in [
        "prepublish",
        "publish",
        "postpublish",
        "install",
        "preinstall",
        "preuninstall"
        "uninstall"
        "postuninstall",
        "preversion",
        "version",
        "postversion",
        "test",
        "stop",
        "start",
        "restart"
]:
    folder = "npm-scripts"
    relpath = "%s/%s.sh" % (folder, script)
    path = os.path.join(os.getcwd(), relpath)
    if os.path.exists(path) and os.path.isfile(path):
        package["scripts"][script] = "bash ./%s" % relpath

# delete empty keys
for key, value in copy.copy(package).items():
    if not value:
        del package[key]

for key, value in package.items():
    if isinstance(value, str):
        package[key] = value.rstrip()

# echo "$json" | python -mjson.tool
text = json.dumps(package, sort_keys=True, indent=4)
print(text)
