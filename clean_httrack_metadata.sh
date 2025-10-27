#!/bin/bash

# Script to clean HTTrack metadata from HTML files
# This removes the unprofessional HTTrack comments and metadata

echo "🧹 Cleaning HTTrack metadata from knowledge base files..."

# Find all HTML files and process them
find . -name "*.html" -type f | while read -r file; do
    echo "Processing: $file"
    
    # Create a temporary file
    temp_file="${file}.tmp"
    
    # Remove HTTrack comments and metadata lines
    sed '/<!-- Mirrored from.*HTTrack.*-->/d' "$file" | \
    sed '/<!-- Added by HTTrack -->/d' | \
    sed '/<!-- \/Added by HTTrack -->/d' | \
    sed 's/<!-- Added by HTTrack --><meta.*><!-- \/Added by HTTrack -->//' > "$temp_file"
    
    # Replace original file if changes were made
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        echo "  ✅ Cleaned: $file"
    else
        rm "$temp_file"
        echo "  ⏭️  No changes needed: $file"
    fi
done

echo "🎉 HTTrack metadata cleanup complete!"
echo ""
echo "📊 Summary:"
echo "  - Removed HTTrack mirror comments"
echo "  - Removed HTTrack metadata tags"
echo "  - Preserved all content and functionality"
echo ""
echo "✨ Your knowledge base now looks professional!"