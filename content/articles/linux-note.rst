Linux Note
***********


:date: 2016-05-27
:modified: 2017-02-10
:slug: linux-note
:tags: linux, note
:category: software
:author: Dormouse Young
:summary: Note of how to use linux

Install chrome
==============

date: 2016-05-27

::

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo gdebi google-chrome-stable_current_amd64.deb

Install new font
================

date: 2015-04-29

How-to
------

For system wide installation, copy the fonts to /usr/share/fonts and run sudo fc-cache to rebuild the font cache, or for user local installation, make sure ~/.fonts exists, copy them into there, then rebuild the font cache.

Example
-------

Install `adobe-fonts/source-code-pro
<https://github.com/adobe-fonts/source-code-pro>`_ in Ubuntu 14.04::

    [ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
    sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
    sudo fc-cache -f -v
