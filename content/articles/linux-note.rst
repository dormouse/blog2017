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


adb
===

2014年 10月 23日 星期四 21:13:09 CST

安装 adb 后，手机联上电脑后可以看见 SD 卡::

    sudo apt-get install android-tools-adb


brickset
========

2014年 10月 23日 星期四 22:20:58 CST

Write to brickset.com ,and my project name is LM_LEGO.


ReText
======

2015年 03月 18日 星期三 10:02:54 CST

安装 ReText::
    sudo apt-get install retext
    sudo apt-get install python3-docutils python3-markdown python3-pygments python3-enchant

ReText 是一个使用python qt 写的 Markdown 编辑器。

ReText 依赖： python3-markups python3-pyqt4 python3-sip+

终端命令技巧
===================================

查找目录中所有文件的内容::

    grep some_tag -rl *.rst

替换目录中所有文件的内容::

    sed -i "s/old_str/new_str/g" `grep old_str -rl *.rst`
