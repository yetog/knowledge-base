#!/bin/bash

# Script to systematically fix HTML files in the knowledge base
# Fixes broken script references, preload patterns, and navigation

echo "Starting HTML standardization process..."

# Function to fix root-level files
fix_root_level_files() {
    echo "Fixing root-level files..."
    for file in chess.html climbing.html consciousness.html ethics-maci.html languages.html mathematics.html meditation.html mimetic-theory.html music.html people.html physics.html public-speaking.html pyrolysis.html relationships.html soil.html space.html trees.html writing.html zoology.html; do
        if [ -f "/var/www/zaylegend/apps/knowledge-base/$file" ]; then
            echo "Processing $file..."
            
            # Fix preload references - replace all the broken VuePress chunks with clean preloads
            sed -i 's|<link rel="preload" href="assets/css/styles.css" as="style"><link rel="preload" href="assets/js/app.js" as="script"><link rel="preload" href="assets/js/vendor.js" as="script">.*|<link rel="preload" href="assets/css/styles.css" as="style">\n    <link rel="preload" href="assets/js/search.js" as="script">|' "/var/www/zaylegend/apps/knowledge-base/$file"
            
            # Fix script references at the end of the file
            sed -i 's|<script src="assets/js/app.js" defer></script><script src="assets/js/vendor.js" defer></script>.*|<script src="assets/js/search.js" defer></script>|' "/var/www/zaylegend/apps/knowledge-base/$file"
        fi
    done
}

# Function to fix one-level subdirectory files  
fix_subdirectory_files() {
    echo "Fixing subdirectory files..."
    
    # Tech files
    for file in tech/*.html; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "Processing tech/$filename..."
            
            # Fix preload references for subdirectory files
            sed -i 's|<link rel="preload" href="../assets/css/styles.css" as="style">\n    <link rel="preload" href="../assets/js/app.js" as="script">\n    <link rel="preload" href="../assets/js/vendor.js" as="script">\n    <link rel="preload" href="../assets/js/page.js" as="script">|<link rel="preload" href="../assets/css/styles.css" as="style">\n    <link rel="preload" href="../assets/js/search.js" as="script">|' "/var/www/zaylegend/apps/knowledge-base/$file"
            
            # Fix script references at the end of the file
            sed -i 's|<script src="../assets/js/app.js" defer></script><script src="../assets/js/vendor.js" defer></script><script src="../assets/js/page.js" defer></script>|<script src="../assets/js/search.js" defer></script>|' "/var/www/zaylegend/apps/knowledge-base/$file"
        fi
    done
    
    # Business files
    for file in business/*.html; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "Processing business/$filename..."
            
            # Fix script references
            sed -i 's|<script src="../assets/js/app.js" defer></script><script src="../assets/js/vendor.js" defer></script><script src="../assets/js/page.js" defer></script>|<script src="../assets/js/search.js" defer></script>|' "/var/www/zaylegend/apps/knowledge-base/$file"
        fi
    done
}

# Change to the knowledge base directory
cd /var/www/zaylegend/apps/knowledge-base

# Execute fixes
fix_root_level_files
fix_subdirectory_files

echo "HTML standardization complete!"