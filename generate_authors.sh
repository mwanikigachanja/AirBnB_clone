#!/bin/bash

# Set the GitHub repository owner and name
OWNER="Babuhatarii"
REPO="AirBnB_clone"

# Fetch contributors from the GitHub API
CONTRIBUTORS=$(curl -s "https://api.github.com/repos/$OWNER/$REPO/contributors" | jq -r '.[].login')

# Create or overwrite AUTHORS file
echo "# Authors of $REPO" > AUTHORS
echo >> AUTHORS

# Loop through contributors and fetch their contributions
for CONTRIBUTOR in $CONTRIBUTORS; do
    CONTRIBUTIONS=$(curl -s "https://api.github.com/repos/$OWNER/$REPO/contributors/$CONTRIBUTOR" | jq -r '.contributions')
    echo "$CONTRIBUTOR - $CONTRIBUTIONS contributions" >> AUTHORS
done

echo "Authors list generated and saved to AUTHORS file."

