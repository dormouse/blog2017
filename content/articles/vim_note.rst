Vim Note
********


:date: 2017-02-10
:modified: 2017-02-10
:slug: vim-note
:tags: vim, note
:category: software
:author: Dormouse Young
:summary: Note for vim.

Edit more than one file
=======================

open file
---------

Out vim
^^^^^^^

- vim file1 file2 : open multiple files
- vim  -o file1 file2 : open multiple files with horizontal windows 
- vim  -O file1 file2 : open multiple files with vertical windows 

in vim
^^^^^^

- :e file : open new file
- :sp file : open new file in hroizontal window
- :vsp file : open new file in vertical window


close file
----------

:bd close current buffer

:bd2 close buffer No.2

switch file
-----------

:ls show files list

:n next file

:N previous file


Split Window
============

- ``:sp`` split horizontally
- ``:vs`` split vertically

Shell
=====

date

- ``:shell``: open shell window. Use ``exit`` to quit shell window
- ``:!command``: run command in shell
- ``:r !command``: run command in shell, insert result to next line
  (ie: ``:r !date``: insert date to nex line)

Reference
=========

- Vim Doc: http://www.vim.org/docs.php
- Vim Cheat Sheet: https://vim.rtorr.com/
