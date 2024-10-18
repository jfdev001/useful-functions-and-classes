#!/usr/bin/bash
# Purpose: Generic bash CLI with options, positions, flags and documentation.
# References:
# https://web.archive.org/web/20130927000512/http://www.devhands.com/2010/01/handling-positional-and-non-positional-command-line-arguments-from-a-shell-script/
# https://stackoverflow.com/questions/11742996/is-mixing-getopts-with-positional-parameters-possible
# man grep
#  https://gitlab.dkrz.de/icon/icon-model/-/blob/a1324166fa60ec5bda5e838fdbfef4c19ae67899/scripts/preprocessing/mars4icon_smi 
# argparse output from mars -h
# https://github.com/petsc/petsc/blob/0f6b61ebcc3e6537ba558a641cd0ae0acf185194/lib/petsc/bin/petscdiff#L35

# Setup CLI
name=$(basename $0)
length_name=${#name}

# Print a number of spaces to pad and therefore align parameters in heredoc  
function pad {
    printf "%*s" $length_name ""
} 

heredoc=$(cat << HELP_EOF
usage: $name [-h] [-H HOSTNAME] [-u USERNAME] [-p PASSWORD] [-d DATABASE] 
       $(pad) ARG1 ARG2
       $(pad) ARG3

Example bash script with flags, optional, and positional arguments. 

positional arguments:
    ARG1         First positional argument.
    ARG2         Second positional argument.
    ARG3         Third positional argument.
    
options:
    -h           Output a usage message and exit.
    -H HOSTNAME  Name of host.
    -u USERNAME  Name of user for login. 
    -p PASSWORD  Password for login. 
    -d DATABASE  Name of database.
HELP_EOF
)

while getopts "hH:u:p:d:" flag; do
case "$flag" in
    H) HOSTNAME=$OPTARG;;
    u) USERNAME=$OPTARG;;
    p) PASSWORD=$OPTARG;;
    d) DATABASE=$OPTARG;;
    h) echo "$heredoc"
       exit 0
       ;;
    *) echo "ERROR: unrecognized flags!"
       echo "Try '$name -h' for more information."
       exit 1
       ;;
esac
done

shift $(($OPTIND - 1))

# Capture positional arguments 
n_positional_args=3 # TODO: Change this if you add/remove positional args
ARG1=$1
ARG2=$2
ARG3=$3

# Check if all positional arguments were provided 
if [ $# -lt $n_positional_args ]
then
    echo "ERROR: Missing positional arguments!"
    echo "Try '$name -h' for more information."
    exit 1
fi
