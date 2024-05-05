#!/bin/bash

# Step 1: Delete a directory and all its contents
rm -rf ./build/deployments

# Step 2: Run a bash command and extract a string
output=$(brownie run scripts/deploy.py --network globalGanache)
extracted_strings=$(echo "$output" | grep -o '0x[[:alnum:]]\+')

# Find the longer string
longest_string=""
for extracted_string in $extracted_strings
do
    if [ ${#extracted_string} -gt ${#longest_string} ]
    then
        longest_string=$extracted_string
    fi
done

# Step 3: Write extracted string to the file
echo "$longest_string" > deployment.txt
