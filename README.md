puush for Linux
===============

[![License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/KoffeinFlummi/puush/blob/master/LICENSE)

A Python 3 implementation of Puush for Linux.


### Setup

```
$ python3 setup.py install
```

* In order to take screenshots, you need [scrot](https://github.com/dreamer/scrot) installed and in your PATH.
* In order to use the clipboard option, you need [xclip](http://sourceforge.net/projects/xclip/) (WARNING: sourceforge link) installed and in your PATH.
* If you want to play the beep when the upload is finished, the `play` command has to be available. It is most likely found in the `sox` package of your respective package manager.


### API Key

In order to use Puush, you have to have an API key. To retrieve your API key, log into your [Puush account](http://puush.me/account) and get your API key; to be found under Account > Settings.

You can either pass the key to Puush in the environment variable `PUUSH_API_KEY` or by dumping it into the file `~/.config/puush/key`.


### Usage

```
puush for linux

Usage:
    puush [-cmd] upload <file>...
    puush [-cmd] (window | desktop | area)
    puush -h | --help

Commands:
    upload          Upload the specified file(s)
    window          Take a screenshot of the current window and upload it
    desktop         Take a screenshot of the entire desktop and upload it
    area            Take a screenshot of a certain area and upload it

Options:
    -c --clipboard  Copy the URL to clipboard additionally to STDOUT
    -m --mute       Mute. Don't play beep.
    -d --debug      Show debug messages.
    -h --help       Show this help
```


### Keybindings

If you want to use the same keybindings that you are used to on Windows, you will have to set those in your WM/DE settings. If you use a full DE like KDE, XFCE, Gnome/Cinnamon or Unity, you will find a keybindings option in your system settings.

Below is a sample configuration for the i3 window manager:

```
# Puush keybindings
bindsym Ctrl+Shift+2    exec --no-startup-id puush -c window
bindsym Ctrl+Shift+3    exec --no-startup-id puush -c desktop
bindsym Ctrl+Shift+4    exec --no-startup-id puush -c area
```


### Disclaimers

This is not an official Puush implementation and I'm not affiliated with the creator(s) of Puush.

The method for the upload has been taken from [here](https://github.com/blha303/puush-linux).
