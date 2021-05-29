#!/bin/sh

# Eg
# $ BITRATE=48000 DTYPE=f32 ./play_net_sound.sh 8001

# Use the bitrate you send with your client
# Use 'play -h | grep "AUDIO FILE FORMATS"' to see available values for DTYPE

BITRATE=${BITRATE:-48000}
DTYPE=${DTYPE:-f32}
PORT=${1:-8000}

nc -lk ${PORT} | play -r ${BITRATE} -t ${DTYPE}  -
