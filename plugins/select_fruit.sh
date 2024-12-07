#!/bin/bash
FRUIT=$1
if [ $FRUIT == APPLE ]; then
	echo "You selected Apple!"
elif [ $FRUIT == ORANGE ] ; then
	echo "You selected Orange!"
else
	echo "you selected other fruit!"
fi
