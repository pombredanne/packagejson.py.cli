![python](https://img.shields.io/badge/language-python-blue.svg)

[![PyPI](https://img.shields.io/pypi/pyversions/packagejson.svg)](https://pypi.python.org/pypi/packagejson)[![PyPI](https://img.shields.io/pypi/v/packagejson.svg)](https://pypi.python.org/pypi/packagejson)
[![npm](https://img.shields.io/npm/v/packagejson.svg)](https://www.npmjs.com/package/packagejson)

[![codacy.com](https://api.codacy.com/project/badge/Grade/a1f724468e3e425092e648c787d2855b)](https://www.codacy.com/app/russianidiot-github/packagejson-py-cli/dashboard)
[![landscape.io](https://landscape.io/github/russianidiot/packagejson.py.cli/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/packagejson.py.cli)
[![codeclimate.com](https://codeclimate.com/github/russianidiot/packagejson.py.cli/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/packagejson.py.cli)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/)

[![codecov.io](https://codecov.io/github/russianidiot/packagejson.py.cli/coverage.svg?branch=master)](https://codecov.io/github/russianidiot/packagejson.py.cli?branch=master)
[![drone.io](https://drone.io/github.com/russianidiot/packagejson.py.cli/status.png)](https://drone.io/github.com/russianidiot/packagejson.py.cli)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/)
[![semaphoreci.com](https://semaphoreci.com/api/v1/russianidiot/packagejson-py-cli/branches/master/shields_badge.svg)](https://semaphoreci.com/russianidiot/packagejson-py-cli)
[![shippable.com](https://api.shippable.com/projects/576b4fc2b548c8557e5816ca/badge?branch=master)](https://app.shippable.com/projects/576b4fc2b548c8557e5816ca)
[![travis-ci.org](https://travis-ci.org/russianidiot/packagejson.py.cli.svg)](https://travis-ci.org/russianidiot/packagejson.py.cli)
[![wercker.com](None)](None)

<h1 color="red">Integrations</h1>
*	drone.io:
[open](https://drone.io/github.com/russianidiot/packagejson.py.cli)
[add](https://drone.io/new#/github?fullname=russianidiot/packagejson.py.cli)
[badge](https://drone.io/github.com/russianidiot/packagejson.py.cli/status.png)
*	scrutinizer-ci.com:
[badge_score](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/quality-score.png?b=master)
[add](https://scrutinizer-ci.com/g/new?name=russianidiot/packagejson.py.cli)
[config](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/settings/build-config)
[open](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/)
[badge_build](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/build.png?b=master)
*	codacy.com:
[new](https://www.codacy.com/project/new/github?add=packagejson.py.cli)
[badge](https://api.codacy.com/project/badge/Grade/a1f724468e3e425092e648c787d2855b)
[integrations](https://www.codacy.com/app/russianidiot-github/packagejson-py-cli/settings/integrations)
[open](https://www.codacy.com/app/russianidiot-github/packagejson-py-cli/dashboard)
*	shippable.com:
[open](https://app.shippable.com/projects/576b4fc2b548c8557e5816ca)
[add](https://app.shippable.com/subscriptions/57068cba2a8192902e1bbb7e?add=russianidiot/packagejson.py.cli)
[badge](https://api.shippable.com/projects/576b4fc2b548c8557e5816ca/badge?branch=master)
*	semaphoreci.com:
[open](https://semaphoreci.com/russianidiot/packagejson-py-cli)
[add](https://semaphoreci.com/projects/new?repo_host=github&add=russianidiot/packagejson.py.cli)
[badge](https://semaphoreci.com/api/v1/russianidiot/packagejson-py-cli/branches/master/shields_badge.svg)
*	codeclimate.com:
[open](https://codeclimate.com/github/russianidiot/packagejson.py.cli)
[add](https://codeclimate.com/github/signup?name=russianidiot/packagejson.py.cli)
[badge](https://codeclimate.com/github/russianidiot/packagejson.py.cli/badges/gpa.svg)
*	landscape.io:
[open](https://landscape.io/github/russianidiot/packagejson.py.cli)
[add](https://landscape.io/repository/add?name=russianidiot/packagejson.py.cli)
[badge](https://landscape.io/github/russianidiot/packagejson.py.cli/master/landscape.svg?style=flat)
[sync](https://landscape.io/dashboard?click=sync)

<p align="center">
    <b>generate package.json</b>
</p>

#### Install

pip: 
`[sudo] pip install packagejson`

npm: 
`npm install -g packagejson`

#### Features
*	auto-generated keys
*	enviroment variables

#### Usage

```shell
usage: python -m packagejson.py
```

#### Example

```shell
$ python -m packagejson.py # stdout
$ python -m packagejson.py > package.json # write to file

# export variables
$ export URL="https://github.com/owner/repo/issues"
$ python -m packagejson.py | grep "$URL"
```

[Examples/](https://github.com/russianidiot/packagejson.py.cli/tree/master/Examples)

Sources:
*	[py_modules/packagejson.py](https://github.com/russianidiot/packagejson.py.cli/blob/master/py_modules/packagejson.py)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/packagejson.py.cli.svg)](https://github.com/russianidiot/packagejson.py.cli/issues)
[![Join the chat at https://gitter.im/russianidiot/packagejson.py.cli](https://badges.gitter.im/russianidiot/packagejson.py.cli.svg)](https://gitter.im/russianidiot/packagejson.py.cli)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)

* * *

<p align="center">
	Python packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/python/</a>
	<img src="http://russianidiot.github.io/images/python/16.png" />
</p>
<p align="center">
	cli packages <a href="http://russianidiot.github.io/python/">russianidiot.github.io/cli/</a>
<img src="http://russianidiot.github.io/images/cli/16.png" />
</p>

<p align="center">
	repos list <a href="http://russianidiot.github.io/">russianidiot.github.io</a> <img src="http://russianidiot.github.io/images/star/16.png" />
</p>

<p align="center">
	<a href="https://raw.githubusercontent.com/russianidiot/packagejson.py.cli/master/README.md">README.md</a> generated with <a href="https://github.com/russianidiot/readme-mako.py">readmemako.py</a> (python+<a href="http://www.makotemplates.org/">mako</a> templates) and <a href="https://github.com/russianidiot-dotfiles/.README">.README</a> dotfiles 
<img src="http://russianidiot.github.io/images/book/16.png">
</p>
