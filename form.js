/**
 * Gap University - Form Handling
 * 
 * This script handles form submission with the following priority:
 * 1. Formspree (if configured)
 * 2. mailto: fallback (if Formspree not configured)
 * 
 * To configure Formspree:
 * 1. Create a free account at https://formspree.io
 * 2. Create a new form and copy your form ID (looks like: xrgvnqkp)
 * 3. Set FORMSPREE_ID below to your form ID
 */

// ============================================
// CONFIGURATION - Set your Formspree ID here
// ============================================
const FORMSPREE_ID = ''; // e.g., 'xrgvnqkp'

// Fallback email for mailto: link (when Formspree not configured)
const FALLBACK_EMAIL = 'hello@gapuniversity.com';

// ============================================
// Form Handling Logic
// ============================================
(function() {
    'use strict';

    const form = document.getElementById('signup-form');
    const successMessage = document.getElementById('form-success');
    const fallbackMessage = document.getElementById('form-fallback');
    const mailtoLink = document.getElementById('mailto-link');

    if (!form) return;

    // Check if Formspree is configured
    const isFormspreeConfigured = FORMSPREE_ID && FORMSPREE_ID.trim() !== '';

    if (isFormspreeConfigured) {
        // Set the form action to Formspree
        form.action = `https://formspree.io/f/${FORMSPREE_ID}`;
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Gather form data
        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone') || 'Not provided',
            role: formData.get('role'),
            message: formData.get('message') || 'No message'
        };

        if (isFormspreeConfigured) {
            // Submit to Formspree
            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });

                if (response.ok) {
                    // Success - show success message
                    form.hidden = true;
                    successMessage.hidden = false;
                } else {
                    // Formspree error - fall back to mailto
                    showMailtoFallback(data);
                }
            } catch (error) {
                // Network error - fall back to mailto
                console.error('Form submission error:', error);
                showMailtoFallback(data);
            }
        } else {
            // Formspree not configured - show mailto fallback
            showMailtoFallback(data);
        }
    });

    function showMailtoFallback(data) {
        // Build mailto link with form data
        const subject = encodeURIComponent('Gap University - New Contact');
        const body = encodeURIComponent(
            `Name: ${data.name}\n` +
            `Email: ${data.email}\n` +
            `Phone: ${data.phone}\n` +
            `I am a: ${data.role}\n` +
            `\nMessage:\n${data.message}`
        );

        mailtoLink.href = `mailto:${FALLBACK_EMAIL}?subject=${subject}&body=${body}`;
        
        // Hide form, show fallback
        form.hidden = true;
        fallbackMessage.hidden = false;
    }
})();
