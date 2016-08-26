<!--
README generated with readmemako.py (github.com/russianidiot/readme-mako.py) and .README dotfiles (github.com/russianidiot-dotfiles/.README)
-->

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
