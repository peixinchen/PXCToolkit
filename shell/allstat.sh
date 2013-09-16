#! /bin/sh

USAGE="usage: $0 <type> [<args>...]\n
\n
type list:\n
    vm: vmstat\n
    io: iostat\n
    mp: mpstat\n
    net: netstat\n
"

function usage()
{
    echo -e $USAGE >&2
    exit 255
}

CMD=""

case $1 in
    vm) CMD="vmstat";;
    io) CMD="iostat";;
    mp) CMD="mpstat";;
    net) CMD="netstat";;
    *) usage;;
esac

shift

$CMD $@
