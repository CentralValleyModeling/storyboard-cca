document.addEventListener('DOMContentLoaded', function() {
    var hash = window.location.hash;
    
    scrollToId = (id) => {
        var ref = document.getElementById(id);
        if (ref) {
            setTimeout(function() {
                console.debug("jumping to id: " + id)
                ref.scrollIntoView({
                    behavior: 'smooth', 
                    block: 'start'
                });
            }, 100);
        }
    }

    // Observe mutations to the body to detect when elements are added
    var observer = new MutationObserver(
        function(mutations, obs) {
            if (document.getElementById(hash.substring(1))) {
                scrollToId(hash.substring(1));
                obs.disconnect(); // Stop observing after the element is found and scrolled to
            };
        }
    );

    if (hash) {
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

    // Handle hash change events as well
    window.addEventListener('hashchange', function() {
        hash = window.location.hash;
        scrollToId(hash.substring(1));
    });
});