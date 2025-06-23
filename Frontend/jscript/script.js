document.addEventListener('DOMContentLoaded', function () {

    // LOGIN
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async function (event) {
            event.preventDefault();  // Prevent form from reloading the page

            // Get input values
            const useremail = document.getElementById('login-username').value;
            const password = document.getElementById('login-password').value;

            try {
                const response = await fetch('http://localhost:5000/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ useremail, password }) // ✅ JSON keys match Python API
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    alert('✅ Login successful!');
                    console.log('User:', result.user);

                    // Optional: Save user in localStorage
                    // localStorage.setItem('user', JSON.stringify(result.user));

                    // Optional: Redirect to dashboard
                    // window.location.href = 'dashboard.html';
                } else {
                    alert('❌ ' + result.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('❌ Failed to connect to the server.');
            }
        });
    }

    // SIGNUP
    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', async function (event) {
            event.preventDefault();  // Prevent form from reloading the page

            // Get input values
            const name = document.getElementById('signup-username').value;
            const useremail = document.getElementById('signup-email').value;
            const firstname = document.getElementById('signup-firstname').value;
            const lastname = document.getElementById('signup-lastname').value;
            const password = document.getElementById('signup-password').value;

            try {
                const response = await fetch('http://localhost:5000/api/signup', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, useremail, firstname, lastname, password }) // ✅ JSON keys match Python API
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    alert('✅ Signup successful! Please login.');
                    console.log('Registered User:', result);

                    // Optional: Redirect to login page
                    // window.location.href = 'login.html';
                } else {
                    alert('❌ ' + result.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('❌ Failed to connect to the server.');
            }
        });
    }
});
