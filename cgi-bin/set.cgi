#!/bin/sh
echo "Content-Type: audio/wav"
echo
freq=$QUERY_STRING
if [ x$freq = x ]; then
  freq="4526000"
fi

sudo rigctl -r /dev/ttyAMA0 -m117 -s4800 F $freq
