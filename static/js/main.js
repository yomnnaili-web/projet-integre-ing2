// Animations et interactions
document.addEventListener('DOMContentLoaded', function() {
    // Animation des cartes au scroll
    const cards = document.querySelectorAll('.feature-card, .domaine-card, .metier-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s, transform 0.5s';
        observer.observe(card);
    });
    
    // Validation du questionnaire
    const questionnaireForm = document.querySelector('.questionnaire-form');
    if (questionnaireForm) {
        questionnaireForm.addEventListener('submit', function(e) {
            const questions = document.querySelectorAll('.question-block');
            let allAnswered = true;
            
            questions.forEach(question => {
                const radios = question.querySelectorAll('input[type="radio"]');
                const answered = Array.from(radios).some(radio => radio.checked);
                if (!answered) {
                    allAnswered = false;
                }
            });
            
            if (!allAnswered) {
                e.preventDefault();
                alert('Veuillez répondre à toutes les questions');
            }
        });
    }
});
