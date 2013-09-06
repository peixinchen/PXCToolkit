#! /bin/sh

function usage()
{
    echo "usage: $0 {s|l} <process name> <strace out>" >&2
    echo "" >&2
    echo "Batch trace process by pid." >&2
    echo "  s means strace" >&2
    echo "  l means ltrace" >&2
    exit 255
}

if test $# -lt 2
then
    usage
fi

case $1 in
    s)
        trace="strace"
        ;;
    l)
        trace="ltrace"
        ;;
    *)
        usage
esac

mkdir -p `dirname $3`

ps aux | awk 'BEGIN {print "-f -o '$3' "} $11 ~ /'$2'/ {print "-p"$2}' | xargs $trace
