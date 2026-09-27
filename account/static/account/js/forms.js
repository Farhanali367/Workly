/* ================================================================
   SKILL BRIDGE — Form Validation Library
   Client-side validation rules and states for all frontend forms
   ================================================================ */

document.addEventListener('DOMContentLoaded', () => {
    // Select all forms with class needs-validation
    const forms = document.querySelectorAll('.needs-validation');

    forms.forEach(form => {
        form.addEventListener('submit', event => {
            // Check form validity using HTML5 constraints
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                showToast('Please correct the highlighted errors.', 'error');
            } else {
                // Form is valid - simulate submission success
                event.preventDefault();
                const submitBtn = form.querySelector('[type="submit"]');
                const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';
                
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...`;
                }

                setTimeout(() => {
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = originalText;
                    }
                    showToast('Action completed successfully!');
                    form.reset();
                    form.classList.remove('was-validated');
                    
                    // Redirect if a data-redirect attribute is present
                    const redirectUrl = form.getAttribute('data-redirect');
                    if (redirectUrl) {
                        window.location.href = redirectUrl;
                    }
                }, 1500);
            }

            form.classList.add('was-validated');
        }, false);

        // Real-time individual field validation on input
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('input', () => {
                validateField(input);
            });
            input.addEventListener('blur', () => {
                validateField(input);
            });
        });
    });

    // Custom Validation Rules helper
    function validateField(field) {
        if (field.hasAttribute('required') && !field.value.trim()) {
            field.setCustomValidity('This field is required.');
            return;
        }

        // Email validation
        if (field.type === 'email') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(field.value)) {
                field.setCustomValidity('Please enter a valid email address.');
                return;
            }
        }

        // Password matching for registration/reset
        if (field.id === 'confirmPassword') {
            const passwordField = document.getElementById('password');
            if (passwordField && field.value !== passwordField.value) {
                field.setCustomValidity('Passwords do not match.');
                return;
            }
        }

        // Minimum length validation
        const minLength = field.getAttribute('minlength');
        if (minLength && field.value.length < parseInt(minLength)) {
            field.setCustomValidity(`Must be at least ${minLength} characters.`);
            return;
        }

        // If it passes all, reset custom validity
        field.setCustomValidity('');
    }
});
