// Initialize Firebase
const firebaseConfig = {
    apiKey: "AIzaSyCSCJVxNn8N28Hpxt2SuBQz2-HyqMFAeH8",
    authDomain: "testproject-24d54.firebaseapp.com",
    databaseURL: "https://testproject-24d54-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "testproject-24d54",
    storageBucket: "testproject-24d54.appspot.com",
    messagingSenderId: "865886225620",
    appId: "1:865886225620:web:c3f95aec8e9d0dc4ede741"
};

firebase.initializeApp(firebaseConfig);

// Reference to Firestore database
const db = firebase.firestore();

// Function to fetch and display blog posts
function fetchBlogPosts() {
    db.collection("posts").get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            const postData = doc.data();
            // Construct HTML for displaying blog post
            const postHtml = `
                <div class="card mb-3">
                    <div class="card-body">
                        <h5 class="card-title">${postData.title}</h5>
                        <p class="card-text">${postData.content}</p>
                    </div>
                </div>
            `;
            // Append post to main content area
            document.getElementById("main-content").innerHTML += postHtml;
        });
    });
}

// Call function to fetch and display blog posts
fetchBlogPosts();


// Reference to Firebase Auth
const auth = firebase.auth();

// Login form
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    auth.signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Logged in successfully
            console.log('Logged in:', userCredential.user);
            // You can redirect the user to another page or perform other actions here
        })
        .catch((error) => {
            // Handle login errors
            console.error('Login error:', error.message);
        });
});

// Registration form
const registerForm = document.getElementById('registerForm');
registerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    auth.createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            // Registered successfully
            console.log('Registered:', userCredential.user);
            // You can redirect the user to another page or perform other actions here
        })
        .catch((error) => {
            // Handle registration errors
            console.error('Registration error:', error.message);
        });
});