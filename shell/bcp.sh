#! /bin/sh

if test $# -lt 4
then
    echo "copy directory to ssh://<user>@<dst_host>:dst_root/" >&2
    echo "usage: $0 <directory> <user> <dst_host> <dst_root>" >&2
    exit 255
fi

directory=$1
user=$2
dst_host=$3
dst_root=$4

cd `dirname $directory`
tar cf - `basename $directory` | ssh $user@$dst_host tar xf - -C $dst_root --same-owner
cd - > /dev/null
