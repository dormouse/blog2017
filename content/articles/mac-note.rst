Mac Note
***********


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
