#! /bin/sh

function mysqlcmd()
{
    mode=$1

    cmd="mysql"
    if test "$mode" == "dump"
    then
        shift
        cmd="mysqldump"
    fi

    cmdline="$cmd -h$HOST -P$PORT -u$USER"

    if test "$PASSWORD" != ""
    then
        cmdline="$cmdline -p$PASSWORD"
    fi

    for((i=1;i<=$#;i++))
    do
        cmdline="$cmdline ${!i}"
    done

    eval $cmdline
}

export HOST="mysql host"
export PORT="mysql port"
export USER="mysql user"
export PASSWORD="mysql password" # "" if no password

mysqlcmd $*
