// Simple search functionality for knowledge base
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-box input');
    const searchResults = document.createElement('div');
    searchResults.className = 'search-results';
    searchResults.style.cssText = `
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        border: 1px solid #eaecef;
        border-radius: 6px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        max-height: 400px;
        overflow-y: auto;
        z-index: 1000;
        display: none;
    `;
    
    const searchBox = document.querySelector('.search-box');
    searchBox.style.position = 'relative';
    searchBox.appendChild(searchResults);

    // Pages data for search
    const pages = [
        // AI Engineering Course
        { title: 'AI Engineering Course Overview', url: 'ai-engineering/index.html', content: 'AI Engineering course overview comprehensive guide artificial intelligence machine learning' },
        { title: 'AI Engineering Syllabus', url: 'ai-engineering/syllabus.html', content: 'syllabus curriculum weeks transformer fundamentals fine-tuning agents multimodal' },
        { title: 'Foundations (Week 0-1)', url: 'ai-engineering/foundations.html', content: 'foundations week 0 1 setup environment transformer architecture attention mechanisms' },
        { title: 'Core Applications (Week 2-3)', url: 'ai-engineering/core-applications.html', content: 'core applications week 2 3 fine-tuning RAG vector databases agents frameworks' },
        { title: 'Advanced Techniques (Week 4-5)', url: 'ai-engineering/advanced-techniques.html', content: 'advanced techniques week 4 5 reasoning multimodal vision language models' },
        { title: 'Capstone & Advanced (Week 6-7)', url: 'ai-engineering/capstone-advanced.html', content: 'capstone advanced week 6 7 projects deployment optimization scaling' },
        
        // Mindfulness Course
        { title: 'Mindfulness Course', url: 'courses/mindfulness.html', content: 'mindfulness meditation awareness present moment breathing exercises' },
        
        // Tech
        { title: 'AI Development', url: 'tech/ai-development.html', content: 'AI development artificial intelligence machine learning tools frameworks' },
        { title: 'Development Workflows', url: 'tech/development-workflows.html', content: 'development workflows processes coding practices git version control' },
        { title: 'Session Recaps', url: 'tech/session-recaps.html', content: 'session recaps learning notes programming sessions' },
        { title: 'Automation Tools', url: 'tech/automation-tools.html', content: 'automation tools scripts productivity efficiency workflow automation' },
        { title: 'Docker Cheatsheet', url: 'tech/docker.html', content: 'docker containers virtualization containerization commands cheatsheet' },
        { title: 'PostgreSQL Cheatsheet', url: 'tech/postgresql.html', content: 'postgresql postgres database SQL queries commands administration' },
        { title: 'Regex Cheatsheet', url: 'tech/regex.html', content: 'regex regular expressions pattern matching text processing' },
        { title: 'HTML Cheatsheet', url: 'tech/html-cheatsheet.html', content: 'HTML markup tags elements web development frontend' },
        { title: 'VSCode Snippets', url: 'tech/vscode-snippets.html', content: 'VSCode snippets code templates editor shortcuts productivity' },
        
        // Business
        { title: 'Hiring', url: 'business/hiring.html', content: 'hiring recruitment talent acquisition interviews candidate selection' },
        { title: 'Management', url: 'business/management.html', content: 'management leadership team building organizational skills' },
        { title: 'Sales', url: 'business/sales.html', content: 'sales selling techniques customer acquisition revenue growth' },
        { title: 'Marketing', url: 'business/marketing.html', content: 'marketing promotion advertising brand building customer engagement' },
        { title: 'Fundraising', url: 'business/fundraising.html', content: 'fundraising investment venture capital startup funding' },
        
        // Philosophy
        { title: 'Ethics', url: 'philosophy/ethics.html', content: 'ethics moral philosophy values principles right wrong' },
        { title: 'Buddhism', url: 'philosophy/buddhism.html', content: 'buddhism meditation enlightenment suffering four noble truths' },
        { title: 'Stoicism', url: 'philosophy/stoicism.html', content: 'stoicism philosophy resilience acceptance control emotional regulation' },
        
        // People
        { title: 'Lee Kuan Yew', url: 'people/lee-kuan-yew.html', content: 'Lee Kuan Yew Singapore leadership governance political philosophy' },
        { title: 'Jensen Huang', url: 'people/jensen-huang.html', content: 'Jensen Huang NVIDIA AI technology leadership innovation' },
        { title: 'Elon Musk', url: 'people/elon-musk.html', content: 'Elon Musk Tesla SpaceX innovation entrepreneurship technology' },
        
        // Miscellaneous
        { title: 'Chess', url: 'chess.html', content: 'chess strategy tactics openings endgame board game' },
        { title: 'Mathematics', url: 'mathematics.html', content: 'mathematics calculus algebra geometry statistics probability' },
        { title: 'Physics', url: 'physics.html', content: 'physics quantum mechanics relativity thermodynamics science' },
        { title: 'Meditation', url: 'meditation.html', content: 'meditation mindfulness awareness breathing techniques practice' },
        { title: 'Writing', url: 'writing.html', content: 'writing communication storytelling grammar composition techniques' },
        { title: 'Music', url: 'music.html', content: 'music theory composition instruments rhythm melody harmony' }
    ];

    let searchTimeout;

    searchInput.addEventListener('input', function(e) {
        const query = e.target.value.trim().toLowerCase();
        
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            if (query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }

            const results = pages.filter(page => 
                page.title.toLowerCase().includes(query) || 
                page.content.toLowerCase().includes(query)
            ).slice(0, 8); // Limit to 8 results

            if (results.length === 0) {
                searchResults.innerHTML = '<div style="padding: 12px; color: #666; font-style: italic;">No results found</div>';
                searchResults.style.display = 'block';
                return;
            }

            searchResults.innerHTML = results.map(result => `
                <a href="${result.url}" style="
                    display: block;
                    padding: 12px 16px;
                    color: #2c3e50;
                    text-decoration: none;
                    border-bottom: 1px solid #eaecef;
                    transition: background-color 0.1s;
                " onmouseover="this.style.backgroundColor='#f8f9fa'" onmouseout="this.style.backgroundColor='transparent'">
                    <div style="font-weight: 600; margin-bottom: 4px;">${highlightMatch(result.title, query)}</div>
                    <div style="font-size: 12px; color: #666; line-height: 1.3;">${getSnippet(result.content, query)}</div>
                </a>
            `).join('');

            searchResults.style.display = 'block';
        }, 200);
    });

    // Close search results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchBox.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });

    // Handle escape key
    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            searchResults.style.display = 'none';
            searchInput.blur();
        }
    });

    function highlightMatch(text, query) {
        const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
        return text.replace(regex, '<mark style="background-color: #fff3cd; padding: 1px 2px;">$1</mark>');
    }

    function getSnippet(content, query) {
        const index = content.toLowerCase().indexOf(query.toLowerCase());
        if (index === -1) return content.substring(0, 60) + '...';
        
        const start = Math.max(0, index - 30);
        const end = Math.min(content.length, index + query.length + 30);
        let snippet = content.substring(start, end);
        
        if (start > 0) snippet = '...' + snippet;
        if (end < content.length) snippet = snippet + '...';
        
        return highlightMatch(snippet, query);
    }

    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }
});