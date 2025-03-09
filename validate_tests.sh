#!/bin/bash

# Move to the 'tests' folder
cd tests || exit

# Ensure 'expected' and 'outputs' directories exist
EXPECTED_DIR="Expected_Outputs"
OUTPUTS_DIR="Outputs"

# Check if the 'expected' and 'outputs' directories exist
if [[ ! -d "$EXPECTED_DIR" || ! -d "$OUTPUTS_DIR" ]]; then
  echo "Error: Expected or Outputs directory is missing!"
  exit 1
fi

# Validate daily transaction files (.atf) and terminal output files (.out)
for test_dir in */; do
    if [[ -d "$test_dir" ]]; then
        # Get the test name (remove trailing slash)
        test_name=$(basename "$test_dir")

        echo "Checking test: $test_name"

        # Compare .atf files (transaction files)
        if [[ -f "$OUTPUTS_DIR/$test_name.atf" && -f "$EXPECTED_DIR/$test_name.etf" ]]; then
            echo "Checking transaction file for test $test_name..."
            if diff "$OUTPUTS_DIR/$test_name.atf" "$EXPECTED_DIR/$test_name.etf" > /dev/null; then
                echo "$test_name.atf - PASS"
            else
                echo "$test_name.atf - FAIL"
            fi
        else
            echo "Missing files for transaction: $test_name"
        fi

        # Compare .out files (terminal output files)
        if [[ -f "$OUTPUTS_DIR/$test_name.out" && -f "$EXPECTED_DIR/$test_name.out" ]]; then
            echo "Checking terminal output for test $test_name..."
            if diff "$OUTPUTS_DIR/$test_name.out" "$EXPECTED_DIR/$test_name.out" > /dev/null; then
                echo "$test_name.out - PASS"
            else
                echo "$test_name.out - FAIL"
            fi
        else
            echo "Missing terminal output file: $test_name"
        fi

        echo "-----------------------------"
    fi
done
