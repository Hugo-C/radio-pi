#!/usr/bin/env bash

echo "Starting radio-pi auto_start.sh"
pulseaudio --start
echo "connecting ..."
while true
do
  bluetoothctl connect $RADIO_PI_MAC_ADDRESS
  if [ $? -eq 0 ]; then
    break;
  else
    echo "retrying bluetooth connection ..."
    sleep 10
  fi
done
echo "connected !"
sleep 2
which python
python radio_pi.py
echo "done !"
