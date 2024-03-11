import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js'
import { getAuth, signInWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js'

const firebaseConfig = {
    apiKey: "AIzaSyCSCJVxNn8N28Hpxt2SuBQz2-HyqMFAeH8",
    authDomain: "testproject-24d54.firebaseapp.com",
    databaseURL: "https://testproject-24d54-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "testproject-24d54",
    storageBucket: "testproject-24d54.appspot.com",
    messagingSenderId: "865886225620",
    appId: "1:865886225620:web:c3f95aec8e9d0dc4ede741"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Get the authentication instance
const auth = getAuth();




// Login form submission
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Logged in successfully
            console.log('Logged in:', userCredential.user);
            // Redirect the user to another page
            window.location.href = '127.0.0.1:5500/sessonTest/index.html';
            // Replace with your desired URL
        })
        .catch((error) => {
            // Handle login errors
            console.error('Login error:', error.message);
        });
});
