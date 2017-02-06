+++
date = "2017-02-05T22:34:28+08:00"
title = "Install Software In OSX"
description = "We always have to install... . Wait, How to?"
tags = ["OSX"]
categories = ["Software"]
slug = "Install-software-in-osx"
+++

# Homebrew-Cask

Homebrew-Cask extends Homebrew and brings its elegance, simplicity, and
speed to the installation and management of GUI macOS applications such as
Google Chrome and Adium.

We do this by providing a friendly Homebrew-style CLI workflow for the administration of macOS applications distributed as binaries.

It’s implemented as a homebrew external command called cask.

To start using Homebrew-Cask, you just need Homebrew installed.

Example:

    $ brew cask install atom
    ==> Satisfying dependencies
    complete
    ==> Downloading https://github.com/atom/atom/releases/download/v1.8.0/atom-mac.zip
    ######################################################################## 100.0%
    ==> Verifying checksum for Cask atom
    ==> Moving App 'Atom.app' to '/Applications/Atom.app'
    ==> Symlinking Binary 'apm' to '/usr/local/bin/apm'
    ==> Symlinking Binary 'atom.sh' to '/usr/local/bin/atom'
    🍺  atom was successfully installed!

And there we have it. Atom installed with one quick command: no clicking, no dragging, no dropping.
