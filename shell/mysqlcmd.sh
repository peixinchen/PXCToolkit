#! /bin/bash

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
        arg=`sed 's/"/\\\"/g' <<< ${!i}`
        cmdline="$cmdline $arg"
    done

    eval "$cmdline"
}

### 下面这部分放在不同的命令里 ###

export HOST="mysql host"
export PORT="mysql port"
export USER="mysql user"
export PASSWORD="mysql password" # "" if no password

mysqlcmd "$@"
