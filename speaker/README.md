This script is meant to be run on your speaker side. It will open a listening network socket
with `netcat`, and pipe any received bytes to the `sox` command `play`. Therefore, you must
install:

`apt update && apt install -y netcat sox`

Ideally, you'd run this in a tmux session, or better yet, a service supervisor (like `supervisord`)
to bring it back up if it crashes.
