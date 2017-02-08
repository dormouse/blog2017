Tmux Note
*********


:date: 2017-02-08 18:35:00
:modified: 2017-02-08 18:35:00
:slug: tmux-note
:tags: tmux, note
:category: software
:author: Dormouse Young
:summary: Note for tmux.

Official site: https://github.com/tmux/tmux

cheat-sheet
===========

tmux use prefix key (default: ``C-b``)

General
-------

=========================== ===========================
Key                         Description
=========================== ===========================
:                           intera ctive dialog (promt)
d                           detach session
tmux restore                restore session
: source -file ~/.tmux.conf reload .tmux.conf
t                           big clock
?                           list bindings
=========================== ===========================

Pane Handling
-------------

=============== ========================================
Key                           Description
=============== ========================================
%               split vertically
"               split horizontally
o               go to next pane (down- pane)
q               show pane number, press number to go to
{               move current pane left
}               move current pane right
x               kill pane
<space>         toggle through layouts
;               last pane
z               resize pane
M-Up            resize pane up 5 row
C-Up            resize pane up 1 row
=============== ========================================

Window Handling
---------------------


=============== ===================================
Key                           Description
=============== ===================================
c               new window
,               rename window
n               next window
p               previous window
l               previously selected window
w               list all windows
[0-9]           move to window number [0-9]
f [window name] find window
:               list-windows list windows
&               kill window
.               move window
=============== ===================================

Session handling
----------------

============================= ===================================
Key                           Description
============================= ===================================
tmux                          start new
tmux new -s myname            start new with name
tmux a -t                     reattach session (or at, or attach)
tmux a -t myname              reattach named session
tmux ls                       list sessions
tmux kill-s ession -t myname  kill named session
:new                          new session
s                             list sessions
$                             name session
tmux kill-s erver             kill server and all sessions
============================= ===================================

customizing tmux
----------------

+------------------------+--------------------------------------+
|Key                     | Description                          |
+========================+======================================+
|set-option -g prefix C-a| rebind the Ctrl-b prefix to Ctrl-a ; |
|                        | -g for global => every window        |
+------------------------+--------------------------------------+
|bind-key C-a last-window|switch to last active window;         |
|                        |To use hit Ctrl-a twice               |
+------------------------+--------------------------------------+
|unbind %                |Remove default split binding          |
+------------------------+--------------------------------------+
|bind | split-window -h  |bind vertical splitting to |          |
+------------------------+--------------------------------------+
|bind - split-window -v  |bind vertical splitting to -          |
+------------------------+--------------------------------------+
|set -g status-bg black  |set status bar bg color to black      |
+------------------------+--------------------------------------+
|set -g status-fg white  |set status bar fg color to white      |
+------------------------+--------------------------------------+
|set -g status-left      |beginning of statusbar hostname in    |
|'#[fg=green]#H'         |green                                 |
+------------------------+--------------------------------------+
|set -g status-right     | number of users and load average for |
|'#[fg=yellow]#( uptime  | computer                             |
|| cut -d "," -f 2-)'    |                                      |
+------------------------+--------------------------------------+
|set-window-o ption -g   |current window shown in red           |
|window-status-current-bg|                                      |
|red                     |                                      |
+------------------------+--------------------------------------+
|setw -g monito r-a      |highlight window with new activity    |
|ctivity on              |                                      |
+------------------------+--------------------------------------+
|set -g visual -ac tivity|show info on new activity             |
|on                      |                                      |
+------------------------+--------------------------------------+
|setw -g automatic       |set window title to current command   |
|-rename on              |                                      |
+------------------------+--------------------------------------+



References
==========

- https://www.cheatography.com/bechtold/cheat-sheets/tmux-the-terminal-multiplexer/
- http://harttle.com/2015/11/06/tmux-startup.html
