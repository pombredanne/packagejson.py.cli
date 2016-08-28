<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

![python](https://img.shields.io/badge/language-python-blue.svg)
[![PyPI](https://img.shields.io/pypi/pyversions/packagejson.svg)](https://pypi.python.org/pypi/packagejson)[![PyPI](https://img.shields.io/pypi/v/packagejson.svg)](https://pypi.python.org/pypi/packagejson)
[![npm](https://img.shields.io/npm/v/packagejson-generator.svg)](https://www.npmjs.com/package/packagejson-generator)

[![codacy.com](https://api.codacy.com/project/badge/Grade/a1f724468e3e425092e648c787d2855b)](https://www.codacy.com/app/russianidiot-github/packagejson-py-cli/dashboard)
[![landscape.io](https://landscape.io/github/russianidiot/packagejson.py.cli/master/landscape.svg?style=flat)](https://landscape.io/github/russianidiot/packagejson.py.cli)
[![codeclimate.com](https://codeclimate.com/github/russianidiot/packagejson.py.cli/badges/gpa.svg)](https://codeclimate.com/github/russianidiot/packagejson.py.cli)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/)

[![drone.io](https://drone.io/github.com/russianidiot/packagejson.py.cli/status.png)](https://drone.io/github.com/russianidiot/packagejson.py.cli)
[![scrutinizer-ci.com](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/badges/build.png?b=master)](https://scrutinizer-ci.com/g/russianidiot/packagejson.py.cli/)
[![semaphoreci.com](https://semaphoreci.com/api/v1/russianidiot/packagejson-py-cli/branches/master/shields_badge.svg)](https://semaphoreci.com/russianidiot/packagejson-py-cli)
[![shippable.com](https://api.shippable.com/projects/576b4fc2b548c8557e5816ca/badge?branch=master)](https://app.shippable.com/projects/576b4fc2b548c8557e5816ca/status/)
[![travis-ci.org](https://api.travis-ci.org/russianidiot/packagejson.py.cli.svg)](https://travis-ci.org/russianidiot/packagejson.py.cli)
[![wercker.com](None)](https://app.wercker.com/russianidiot/packagejson.py.cli/)

<p align="center">
    <b>generate package.json</b>
</p>

#### Install

`[sudo] pip install packagejson`

`[sudo] sudo npm install -g packagejson-generator`

#### Features
*	auto-generated keys
*	enviroment variables

#### Usage

```bash
usage: python -m packagejson
```

#### Example

```bash
$ python -m packagejson # stdout
$ python -m packagejson > package.json # write to file

# export variables
$ export URL="https://github.com/owner/repo/issues"
$ python -m packagejson | grep "$URL"
```

[Examples/](https://github.com/russianidiot/packagejson.py.cli/tree/master/Examples)

Feedback
[![GitHub issues](https://img.shields.io/github/issues/russianidiot/packagejson.py.cli.svg)](https://github.com/russianidiot/packagejson.py.cli/issues)
[![Join the chat at https://gitter.im/russianidiot/packagejson.py.cli](https://badges.gitter.im/russianidiot/packagejson.py.cli.svg)](https://gitter.im/russianidiot/packagejson.py.cli)
[![GitHub followers](https://img.shields.io/github/followers/russianidiot.svg?style=social&label=Follow)](https://github.com/russianidiot)
