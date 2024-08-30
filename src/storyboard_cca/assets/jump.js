document.addEventListener('DOMContentLoaded', function() {
    var hash = window.location.hash;
    
    function scrollToHash() {
        if (hash && document.getElementById(hash.substring(1))) {
            document.getElementById(hash.substring(1)).scrollIntoView();
        }
    }

    // Add a small delay to ensure elements are rendered
    setTimeout(scrollToHash, 1000); // Adjust the delay time (300 ms) as needed

    // Listen for URL hash changes
    window.addEventListener('hashchange', function() {
        hash = window.location.hash;
        setTimeout(scrollToHash, 1000); // Delay scroll for hash change as well
    });
});