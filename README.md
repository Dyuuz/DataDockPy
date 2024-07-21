# DataDockPy
Program Overview:

This Python program provides basic user authentication functionality in python including registration, login, and password change features. User credentials and details are stored in a text file for simplicity. The program ensures optimized performance and handles errors gracefully.

Key Features:

Registration:
Users can create a new account by providing a unique username and password.
Passwords are stored in a text file (but not yet encrypted).
The program checks for existing usernames to prevent duplication.

Login:
Users can log in by providing their username and password.
The program verifies credentials against the stored data and handles incorrect login attempts.

Change Password:
Users can change their existing password after logging in.
The new password is validated and updated in file without any glitch.

File Storage:
User credentials are stored in a text file, with each line containing a username and password.

Error Handling:
The program includes comprehensive error handling to manage:
Incorrect input formats.
Duplicate usernames.
Authentication failures.
File access issues.

Code Optimization:
Efficient data handling using file operations.
Clear separation of concerns with class functions for each specifications.
Minimal resource usage with effective error management.
