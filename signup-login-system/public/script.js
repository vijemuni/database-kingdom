/*async function signup() {
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    try {
        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, password }),
        });
        const data = await response.json();
        console.log('Server response:', data);
        document.getElementById('message').innerText = data.message;
        if (data.error) {
            console.error('Server error:', data.error);
        }
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('message').innerText = 'An error occurred. Please try again.';
    }
}

async function login() {
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password }),
        });
        const data = await response.json();
        console.log('Server response:', data);
        document.getElementById('message').innerText = data.message;
        if (response.ok) {
            localStorage.setItem('token', data.token);
            console.log('Token stored in localStorage');
        }
        if (data.error) {
            console.error('Server error:', data.error);
        }
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('message').innerText = 'An error occurred. Please try again.';
    }
}