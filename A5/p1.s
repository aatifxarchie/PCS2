#!/bin/bash

# Variables
turn=0
flag1=0
flag2=0

# Process 1
(
    flag1=1
    turn=2
    while [ $flag2 -eq 1 ] && [ $turn -eq 2 ]; do
        :
    done

    # Critical Section
    echo "Process 1 is in critical section"

    flag1=0
) &

# Process 2
(
    flag2=1
    turn=1
    while [ $flag1 -eq 1 ] && [ $turn -eq 1 ]; do
        :
    done

    # Critical Section
    echo "Process 2 is in critical section"

    flag2=0
) &

wait
