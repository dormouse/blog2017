Mac Note
********


:date: 2017-02-10
:modified: 2017-02-10
:slug: mac-note
:tags: mac, note
:category: software
:author: Dormouse Young
:summary: Note of how to use mac

bash
====

When login, mac will execute ``.bash_profile`` ，but not ``.bashrc``.
So we can add following to ``.bash_profile`` to run ``.bashrc`` ::

    if [ -f ~/.bashrc ]; then
       source ~/.bashrc
    fi


Install wxpython
================

::

    brew install wxmac
    brew install wxpython


Install cTags
=============

If you use the cTags directly on Mac will result following errors::

    ctags: illegal option -- R
    usage: ctags [-BFadtuwvx] [-f tagsfile] file ...错误。

Beacuse the Mac's own cTags does not support the ``-R`` parameter.
So we should install cTags by ourself::

    brew install ctags

After install cTags, if still have errors, we should check ``$PATH``::

    $ $PATH

We can find ``/usr/local/bin`` is not in the ``$PATH``. We have way to add
it.

Way one:

Delete Mac's ctags::

    sudo rm /usr/bin/ctags

Create a soft link::

    sudo ln -s /usr/local/Cellar/ctags/5.8_1/bin/ctags /usr/bin/ctags

Way two:

Edit ``~/.bash_profile``, add following line::

    export PATH=/usr/local/bin:$PATH

I recommend the second way for most of brew intalled software are in the
``/usr/local``.
