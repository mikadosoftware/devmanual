======================
Managing Configuration
======================

Let's keep things simple (it is one of our goals).
We shall utilise a wide spread and deep computing thing - `environment variables`.

Every process is started off with a certain *context* - this context is stored in a key/value
store called "environment variables". The actual store is an in memory byte string in each process
- you can see it in /proc/<pid>/environ - the string is delimited by zero byte - so we can see my current emacs process is on pid 2753 (using `ps`) and 

  cat /proc/2753/environ | tr '\0' '\n'

  This repalces the \0 delimiter with \n for easy reading but it is pretty simple.
  (ps tr is 'text replace' and just does what it says on the tin.  Its like a less complex sed)

  GDMSESSION=gnome-classic
  GNOME_DESKTOP_SESSION_ID=this-is-deprecated
  LOGNAME=pbrian
  DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
  XDG_RUNTIME_DIR=/run/user/1000
  XAUTHORITY=/run/user/1000/gdm/Xauthority
  VIRTUALENVWRAPPER_PROJECT_FILENAME=.project
  MODULESHOME=/usr/share/Modules
  HISTSIZE=1000
  SESSION_MANAGER=local/unix:@/tmp/.ICE-unix/1692,unix/unix:/tmp/.ICE-unix/1692
  LESSOPEN=||/usr/bin/lesspipe.sh %s
  BASH_FUNC_module%%=() {  eval `/usr/bin/modulecmd bash $*`
  }
  BASH_FUNC_scl%%=() {  local CMD=$1;
  if [ "$CMD" = "load" -o "$CMD" = "unload" ]; then
  eval "module $@";
  else
  /usr/bin/scl "$@";
  fi
  }
  OLDPWD=/home/pbrian
  _=/usr/bin/emacs


So we have a key value store "builtin"

Now lets grab a simple python program

mikadolib.common.config


How to use it


from mikadolib.common import config

confd = config.get_confd()

