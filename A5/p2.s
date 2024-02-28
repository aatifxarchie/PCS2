#!/bin/bash

# Initialize the semaphore value
semaphore=3

# Acquiring the semaphore
acquire_semaphore() {
  # Decrementing the value
  semaphore=$((semaphore - 1))
  
  # If the semaphore value is negative, wait until it becomes positive
  while [ $semaphore -lt 0 ]; do
    sleep 1
  done
}

# Releasing the semaphore
release_semaphore() {
  # Increment the semaphore value
  semaphore=$((semaphore + 1))
}

# Critical section to access the shared resource
critical_section() {
  # Acquire the semaphore
  acquire_semaphore
  
  # Access the shared resource
  echo "shared resource is accessed"
  sleep 2
  
  # Release the semaphore
  release_semaphore
}

# Create multiple threads to access the shared resource
for i in {1..5}; do
  critical_section &
done

# Wait for all threads to finish
wait
