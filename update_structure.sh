#!/bin/bash

# File: update_structure.sh
# Purpose: Automatically regenerate the project_structure.md file

OUTPUT_FILE="project_structure.md"

echo "# 📁 Project Structure – Praevia.AI" > $OUTPUT_FILE
echo "" >> $OUTPUT_FILE
tree -a -I '.git|__pycache__|node_modules' >> $OUTPUT_FILE

echo "Updated $OUTPUT_FILE"

