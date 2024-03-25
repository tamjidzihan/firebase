import pyrebase

config = {
  "apiKey": "AIzaSyCSCJVxNn8N28Hpxt2SuBQz2-HyqMFAeH8",
  "authDomain": "testproject-24d54.firebaseapp.com",
  "databaseURL": "https://testproject-24d54-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "testproject-24d54",
  "storageBucket": "testproject-24d54.appspot.com",
  "messagingSenderId": "865886225620",
  "appId": "1:865886225620:web:30a7aa1f51f6239bede741"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


user_info =  {
    'kind': 'identitytoolkit#SignupNewUserResponse', 
    'idToken':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFlYzU4NjcwNGNhOTZiZDcwMzZiMmYwZDI4MGY5NDlmM2E5NzZkMzgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdGVzdHByb2plY3QtMjRkNTQiLCJhdWQiOiJ0ZXN0cHJvamVjdC0yNGQ1NCIsImF1dGhfdGltZSI6MTcwODE5NDk4MSwidXNlcl9pZCI6IlZoZnNFNFBJUllPMjIwdEZadGdCUkxlYmg5VzIiLCJzdWIiOiJWaGZzRTRQSVJZTzIyMHRGWnRnQlJMZWJoOVcyIiwiaWF0IjoxNzA4MTk0OTgxLCJleHAiOjE3MDgxOTg1ODEsImVtYWlsIjoidGFtamlkemloYW5AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInRhbWppZHppaGFuQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.O9rSum1lk5O3ZYuHgda0RgpRov94Bkx1V4RdmYgLvazLFzzaUqAb0LkMLGhfDvAOVQBJEybkA61o75r_7yTq8KC_asdUYCwO5X6siYrgiydllURzi5UEvbQjBiZiuZrGKwuivdFdJDgvFL23Yky0bfuET12aRxdpNM-Y60M5ioclS-o9cfwjncPtXbSRjVT_uGGalW7RFpOFY9Mn4Ah19hnbulTq08jCpuYvjr0fRV3xCiFfii2KeQfgBfdnQuJsaDWTQOiPx3eBwPdeCuuotwonf50ubeqHUpWfXmrTZ8hFZsihFRzQQlSvCsmB-O-L9niwTKyVofxkipvKoplBRA', 
    'email': 'tamjidzihan@gmail.com', 
    'refreshToken':'AMf-vBysEp6Mk8fIiLneWV-8XDtljl7TduQ6fVBtXZF9f7z-ucfZmFw7sJieb_M6WMvNb45jTqH9BNqaQjA2ZQJEYIeZIVeUeZojjg5KKxmuYhlJtX3wVDL8ucA6g3wguV1zCOs8x2hyXeljZzmzISI_vo0kk5PCsKGZ4iCVnSooCeAWUy_uzmO2yStKC6d3hy9n88IFLDwDfsme5FGqmpUjyHTs5YNHhw', 
    'expiresIn': '3600', 
    'localId': 'VhfsE4PIRYO220tFZtgBRLebh9W2'
    }

# database.child("user").update({"newData": "Hello, Firebase user 1 update!"})


# email = "admin@admin.com"
# password = "admin1234"

email = "root@root.com"
password = "root1234"



try:
    user = auth.create_user_with_email_and_password(email, password)
    print("User created successfully:", user)
except Exception as e:
    print("Error creating user:", e)



# try:
#     user = auth.sign_in_with_email_and_password(email, password)
#     print("User logged in successfully:", user)
# except Exception as e:
#     print("Error logging in:", e)