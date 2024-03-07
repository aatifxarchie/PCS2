#!/bin/bash

# Define the necessary data structures
declare -a available    #array
declare -A max          #matrix for maximum resources
declare -A allocation   #matrix for number of resources of each type
declare -A need         #matrix for remaining number of resources


available=(10 5 7)     #initialize the available array with the total number of available resources of each type
max=(
    [P1]="7 5 3"
    [P2]="3 2 2"
    [P3]="9 0 2"
    [P4]="2 2 2"
    [P5]="4 3 3"
)                       #initialize the max matrix with the maximum number of resources of each type that each process can request
allocation=(
    [P1]="0 1 0"
    [P2]="2 0 0"
    [P3]="3 0 2"
    [P4]="2 1 1"
    [P5]="0 0 2"
)                       #initialize the allocation matrix with the number of resources of each type currently allocated to each process

# Calculate the need matrix
for process in "${!max[@]}"; do
    need[$process]=""
    max_resources=(${max[$process]})
    allocated_resources=(${allocation[$process]})
    for ((i=0; i<${#max_resources[@]}; i++)); do
        need[$process]+="$((max_resources[$i] - allocated_resources[$i])) "
    done
done

# Implement the Banker's algorithm
completed=""
while [[ "${#completed}" -lt "${#max[@]}" ]]; do
    found=false
    for process in "${!max[@]}"; do
        max_resources=(${max[$process]})
        allocated_resources=(${allocation[$process]})
        need_resources=(${need[$process]})
        can_allocate=true

        for ((i=0; i<${#max_resources[@]}; i++)); do
            if [[ ${need_resources[$i]} -gt ${available[$i]} ]]; then
                can_allocate=false
                break
            fi
        done

        if [[ "$can_allocate" == true ]]; then
            completed+="$process "
            available=("${available[@]}")
            for ((i=0; i<${#max_resources[@]}; i++)); do
                available[$i]=$((available[$i] + allocated_resources[$i]))
            done
            found=true
        fi
    done

    if [[ "$found" == false ]]; then
        echo "Deadlock detected! Preempting a process..."
        break
    fi
done

if [[ "${#completed}" -eq "${#max[@]}" ]]; then
    echo "Safe sequence found: $completed"
else
    echo "Deadlock resolved!"
fi
