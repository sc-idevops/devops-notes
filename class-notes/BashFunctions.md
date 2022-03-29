##Bash Functions
function-name() {
  echo "your commands"

}

just call the function by name when you want to use it

its recommended to echo variables at some point in the script to help with debugging and so the user can follow along with the script's workings

##Passing Values to Bash Functions

values are numerical and positional. $1, $2, just like parameters for the script

### etc
##hidden characters and hating life
sometimes different line endings between windows/unix can cause issues in your script
`:set list` allows you to view hidden characters

##environment variables
environment variables are local to the script/sub-shell its executed from. 
If you want to make use of these variables outside of the shell, you'll need to source the script
you can also source variables between scripts using source

##automation with variables
often times you can check or act upon the results of a command by assigning it to a variable and then using test commands on that variable
