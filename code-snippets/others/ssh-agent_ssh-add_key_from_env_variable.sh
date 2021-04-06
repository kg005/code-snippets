eval `ssh-agent` > /dev/null && echo "$GIT_SSH_KEY" | tr  '_' '\n' | ssh-add - > /dev/null && ssh

