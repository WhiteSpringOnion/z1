echo '[julien note]:  ==>  from bash_profile (login shell )'

# Julien learn dart add [stagehand]'s path
export PATH="$PATH":"$HOME/.pub-cache/bin"

# julien add Git branch in prompt.
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# export PS1="\[\033[31m\]\$(parse_git_branch)\[\033[00m\] \w $ \[\033[33m\]"
export PS1="\[\033[31m\]\$(parse_git_branch)\[\033[00m\] \w $ \[\033[32m\]"
# 33 yellow 32 green 94 dark blue


darkmode="\[\033[31m\]\$(parse_git_branch)\[\033[00m\] \w $ \[\033[35m\]"

 #Julien add raspberry pi ip address
pi_ip="172.20.10.12"   # from iphone
export pi_ip  #export到每一個 non-login shell 的child shell 裡
pi_ip2="192.168.1.3"  # from home ip
export home_ip

gcp=$'gcloud config list
gcloud info
gsutil list
-------------------------------------------------
glcoud auth login
datalab connect
------------------------------------------------
gcloud compute ssh davidliao900@mydatalab
-----------------------------------------------
datalab stop mydatalab
datalab list
gcloud compute --project "<-->" ssh --zone "<-->" "<INSTANCE NAME> 
-----------------------------------------------
gcloud alpha cloud-shell ssh
'





# added by Anaconda3 5.1.0 installer
export PATH="/anaconda3/bin:$PATH"



# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/julienjazz/Julien/gcp/google-cloud-sdk/path.bash.inc' ]; then . '/Users/julienjazz/Julien/gcp/google-cloud-sdk/path.bash.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/julienjazz/Julien/gcp/google-cloud-sdk/completion.bash.inc' ]; then . '/Users/julienjazz/Julien/gcp/google-cloud-sdk/completion.bash.inc'; fi
