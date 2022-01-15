#Commonly used bash commands
##ls
lists files in specified directory. __defaults to current directory with no arguments__
-lah arguments for long form, all files including hidden, human readable byte size
##man
Built in manual for whatever command you are interested in. See also `info`
##mv
moves the file to the destination

#Linux File Permissions
##chmod
this command changes access permissions on the file(s) specified 

#Environment Variables
variables cannot have spaces
##env
prints the details of your current environment including all variables
##PATH
this variable tells the terminal what directories to look for programs to execute them in.
###add current directory to path
export PATH=$(pwd):PATH

#Redirection
##Pipes
Looks like `|` and redirects the output of one command to the next
