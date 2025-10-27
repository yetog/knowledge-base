#!/bin/bash

# Comprehensive HTML standardization script
# Fixes broken script references, preload patterns, and navigation for all HTML files

echo "Starting comprehensive HTML standardization..."

# Navigate to the knowledge base directory
cd /var/www/zaylegend/apps/knowledge-base

# Function to fix massive broken preload references in root-level files
fix_root_level_preloads() {
    local file="$1"
    echo "Fixing preloads in root-level file: $file"
    
    # Replace massive preload/prefetch chain with clean minimal preloads
    sed -i 's|<link rel="preload" href="assets/css/styles.css" as="style"><link rel="preload" href="assets/js/app.js" as="script"><link rel="preload" href="assets/js/vendor.js" as="script">.*|<link rel="preload" href="assets/css/styles.css" as="style">\n    <link rel="preload" href="assets/js/search.js" as="script">|' "$file"
    
    # Fix script references at the end
    sed -i 's|<script src="assets/js/app.js" defer></script><script src="assets/js/vendor.js" defer></script>.*|<script src="assets/js/search.js" defer></script>|' "$file"
}

# Function to fix broken script references in subdirectory files  
fix_subdirectory_scripts() {
    local file="$1"
    echo "Fixing scripts in subdirectory file: $file"
    
    # Fix preload references
    sed -i 's|<link rel="preload" href="../assets/js/app.js" as="script">|<link rel="preload" href="../assets/js/search.js" as="script">|g' "$file"
    sed -i 's|<link rel="preload" href="../assets/js/vendor.js" as="script">||g' "$file"
    sed -i 's|<link rel="preload" href="../assets/js/page.js" as="script">||g' "$file"
    
    # Fix script references at the end
    sed -i 's|<script src="../assets/js/app.js" defer></script><script src="../assets/js/vendor.js" defer></script><script src="../assets/js/page.js" defer></script>|<script src="../assets/js/search.js" defer></script>|' "$file"
}

# Function to add Courses navigation to files missing it
add_courses_navigation() {
    local file="$1"
    local relative_path="$2"
    
    # Check if file already has Courses navigation
    if ! grep -q "Courses" "$file"; then
        echo "Adding Courses navigation to: $file"
        
        if [ "$relative_path" = "root" ]; then
            # Root level files
            sed -i 's|</ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Business</span>|</ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Courses</span> <!----></p> <ul class="sidebar-links sidebar-group-items"><li><section class="sidebar-group depth-1"><p class="sidebar-heading"><span>AI Engineering</span> <!----></p> <ul class="sidebar-links sidebar-group-items"><li><a class='\''sidebar-link'\'' href='\''ai-engineering/index.html'\''>Course Overview</a></li><li><a class='\''sidebar-link'\'' href='\''ai-engineering/syllabus.html'\''>Full Syllabus</a></li><li><a class='\''sidebar-link'\'' href='\''ai-engineering/foundations.html'\''>Foundations (Week 0-1)</a></li><li><a class='\''sidebar-link'\'' href='\''ai-engineering/core-applications.html'\''>Core Applications (Week 2-3)</a></li><li><a class='\''sidebar-link'\'' href='\''ai-engineering/advanced-techniques.html'\''>Advanced Techniques (Week 4-5)</a></li><li><a class='\''sidebar-link'\'' href='\''ai-engineering/capstone-advanced.html'\''>Capstone & Advanced (Week 6-7)</a></li></ul></section></li><li><a class='\''sidebar-link'\'' href='\''courses/mindfulness.html'\''>Mindfulness Course</a></li></ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Business</span>|' "$file"
        else
            # Subdirectory files
            sed -i 's|</ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Business</span>|</ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Courses</span> <!----></p> <ul class="sidebar-links sidebar-group-items"><li><section class="sidebar-group depth-1"><p class="sidebar-heading"><span>AI Engineering</span> <!----></p> <ul class="sidebar-links sidebar-group-items"><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/index.html'\''>Course Overview</a></li><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/syllabus.html'\''>Full Syllabus</a></li><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/foundations.html'\''>Foundations (Week 0-1)</a></li><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/core-applications.html'\''>Core Applications (Week 2-3)</a></li><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/advanced-techniques.html'\''>Advanced Techniques (Week 4-5)</a></li><li><a class='\''sidebar-link'\'' href='\''../ai-engineering/capstone-advanced.html'\''>Capstone & Advanced (Week 6-7)</a></li></ul></section></li><li><a class='\''sidebar-link'\'' href='\''../courses/mindfulness.html'\''>Mindfulness Course</a></li></ul></section></li><li><section class="sidebar-group depth-0"><p class="sidebar-heading"><span>Business</span>|' "$file"
        fi
    fi
}

# Process root-level files
echo "Processing root-level files..."
for file in chess.html climbing.html consciousness.html ethics-maci.html languages.html mathematics.html meditation.html mimetic-theory.html music.html people.html physics.html public-speaking.html pyrolysis.html relationships.html soil.html space.html trees.html writing.html zoology.html; do
    if [ -f "$file" ]; then
        echo "Processing root file: $file"
        fix_root_level_preloads "$file"
        add_courses_navigation "$file" "root"
    fi
done

# Process subdirectory files
echo "Processing subdirectory files..."

# Tech files
for file in tech/*.html; do
    if [ -f "$file" ]; then
        echo "Processing tech file: $file"
        fix_subdirectory_scripts "$file"
        add_courses_navigation "$file" "sub"
    fi
done

# Business files
for file in business/*.html; do
    if [ -f "$file" ]; then
        echo "Processing business file: $file"
        fix_subdirectory_scripts "$file"
        add_courses_navigation "$file" "sub"
    fi
done

# Philosophy files
for file in philosophy/*.html; do
    if [ -f "$file" ]; then
        echo "Processing philosophy file: $file"
        fix_subdirectory_scripts "$file"
        add_courses_navigation "$file" "sub"
    fi
done

# People files
for file in people/*.html; do
    if [ -f "$file" ]; then
        echo "Processing people file: $file"
        fix_subdirectory_scripts "$file"
        add_courses_navigation "$file" "sub"
    fi
done

# Levels files
for file in levels/*.html; do
    if [ -f "$file" ]; then
        echo "Processing levels file: $file"
        fix_subdirectory_scripts "$file"
        add_courses_navigation "$file" "sub"
    fi
done

# Courses files (mindfulness.html)
for file in courses/*.html; do
    if [ -f "$file" ]; then
        echo "Processing courses file: $file"
        fix_subdirectory_scripts "$file"
        # Courses files already have courses navigation, but might need the AI Engineering section
    fi
done

echo "Comprehensive HTML standardization complete!"
echo "Summary of changes:"
echo "- Fixed broken script references (app.js, vendor.js, page.js -> search.js)"
echo "- Cleaned massive broken preload/prefetch lists"
echo "- Added missing Courses navigation sections"
echo "- Standardized patterns across all directory levels"