#!/bin/bash

# Move into the inputs directory
cd Tests/Inputs || exit

# Ensure the outputs directory exists (going back to Phase_3 first)
mkdir -p ../Outputs

# Loop over each input file
for input_file in *.inp; do
    # Extract base name (removes .imp extension)
    base_name="${input_file%.inp}"

    # Print message
    echo "Running test for input file: $input_file"

    # Run the program, redirecting outputs
    ../../bank-atm ../../currentaccounts.txt ../Outputs/"$base_name".atf \
        < "$input_file" \
        > ../Outputs/"$base_name".out
done
