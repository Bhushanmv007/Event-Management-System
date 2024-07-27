document.addEventListener("DOMContentLoaded", function() {
    // Add an animation to the form fields on focus
    const formControls = document.querySelectorAll('.form-control');
    
    formControls.forEach(control => {
        control.addEventListener('focus', function() {
            control.style.boxShadow = '0 0 10px rgba(81, 203, 238, 1)';
            control.style.borderColor = 'rgba(81, 203, 238, 1)';
        });
        
        control.addEventListener('blur', function() {
            control.style.boxShadow = 'none';
            control.style.borderColor = '#ced4da';
        });
    });
    
    // Add smooth scrolling to links
    const links = document.querySelectorAll('a');
    
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            if (this.hash !== "") {
                event.preventDefault();
                const hash = this.hash;
                
                window.scrollTo({
                    top: document.querySelector(hash).offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animate button on hover
    const buttons = document.querySelectorAll('.btn-primary');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            button.style.transform = 'scale(1.05)';
            button.style.transition = 'transform 0.3s ease';
        });
        
        button.addEventListener('mouseleave', function() {
            button.style.transform = 'scale(1)';
        });
    });
    
    // Add fade-in effect to the card
    const card = document.querySelector('.card');
    card.style.opacity = 0;
    card.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        card.style.opacity = 1;
    }, 100);
});
