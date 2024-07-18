# DataDockPy
Program Overview:

This Python program provides basic user authentication functionality including registration, login, and password change features. User credentials and details are stored in a text file for simplicity. The program ensures optimized performance and handles errors gracefully.

Key Features:

Registration:

Users can create a new account by providing a unique username and password.
Passwords are stored securely (hashed or encrypted, if applicable).
The program checks for existing usernames to prevent duplication.
Login:

Users can log in by providing their username and password.
The program verifies credentials against the stored data and handles incorrect login attempts.
Change Password:

Users can change their existing password after logging in.
The new password is validated and updated securely.
File Storage:

User credentials are stored in a text file, with each line containing a username and hashed password.
Error Handling:

The program includes comprehensive error handling to manage:
Incorrect input formats.
Duplicate usernames.
Authentication failures.
File access issues.
Code Optimization:

Efficient data handling using file operations.
Clear separation of concerns with modular functions for each feature.
Minimal resource usage with effective error management.
