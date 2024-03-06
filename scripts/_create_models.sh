#!/bin/bash

# Check if two arguments are given
if [ $# -gt 2 ]; then
    echo "Invalid number of arguments supplied. Usage: go.sh [pattern] [action]. Default pattern is '*', default action is 'info'. If the pattern contains spaces or special characters, try \"using quotes\". Supported actions: 'info' and 'exec'"
    exit 1
fi

PATTERN=${1:-*} # If no pattern is provided, default to all files (*)
ACTION=${2:-"info"} # Default action is 'info' if not specified
OLLAMA_COMMAND="_ollama"

for file in *; do
      # Checking if it's a regular file and matches pattern
     if [[ -f "$file" && $(basename -- "$file") == $PATTERN ]]; then
         case "$ACTION" in
             info) 
                 echo "File: $(basename -- "$file")"
                #  cat "$file"
                #  echo ""
                 ;;
             exec)
                # Replace 'command' with your actual command here
                FILENAME=$(basename -- "$file")
                FILENAME_NOEXT="${FILENAME%.*}"
                # echo "File without extension: $FILENAME_NOEXT"
                echo "Processing modelfile: $(basename -- "$file")"
                COMMAND="$OLLAMA_COMMAND create $FILENAME_NOEXT -f $FILENAME"
                echo "Running command: $COMMAND"
                exec $COMMAND
                ;;
             *)
                 echo "Invalid action specified. Choose either 'info' or 'exec'"
                 exit 1
         esac
     fi
done