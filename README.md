# Basic Password Manager

This is a simple password manager application built using Python's Tkinter library for the graphical user interface (GUI). It generates strong, random passwords and allows you to store website credentials locally.

**Features:**

* **Password Generation:** Generates secure passwords with a mix of letters, numbers, and symbols.
* **Password Storage:** Saves website names, email/usernames, and passwords in a local text file (`Password.manager.text`).
* **Clipboard Integration:** Copies generated passwords to the clipboard for easy pasting.
* **Simple GUI:** User-friendly interface built with Tkinter.

**Disclaimer:**

* **Security:** This application stores passwords in plain text, which is **highly insecure**. It is intended for educational purposes only and should **not** be used for storing sensitive information in a real-world scenario.
* **Data Persistence:** Data is saved to a simple text file. For real world applications, using a database, or encrypted file is recommended.

**How to Use:**

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```
2.  **Run the Application:**
    ```bash
    python <your_script_name>.py
    ```
3.  **Enter Website and Email:**
    * Enter the website name and your email/username in the provided fields.
4.  **Generate Password:**
    * Click the "Generate Password" button to create a random password.
5.  **Save Password:**
    * Click the "Add" button to save the credentials to the local text file.
6.  **Copy Password:**
    * The generated password is automatically copied to your clipboard.

**Dependencies:**

* `tkinter` (standard Python library)
* `random` (standard Python library)
* `pyperclip` (install with `pip install pyperclip`)

**Future Improvements (Potential):**

* **Password Encryption:** Implement encryption to securely store passwords.
* **Database Integration:** Use a database (e.g., SQLite) for more structured data storage.
* **Password Strength Indicator:** Add a visual indicator for password strength.
* **Search Functionality:** Allow users to search for stored passwords.
* **Improved GUI:** Improve the user interface for a better user experience.

**Contributing:**

Feel free to contribute to this project by submitting pull requests or opening issues.

**License:**

This project is based on concepts taught in Dr. Angela Yu's 100 Days of Code Python course on Udemy. The code is provided for educational purposes and is intended to be used as a learning resource.

While the core concepts are derived from the course, the specific implementation and application are my own.

No specific license is attached to this project. If you intend to use or modify this code, please acknowledge the source of the learning material (Dr. Angela Yu's 100 Days of Code Python course on Udemy).

For any commercial use or distribution, please consult with the course instructor or Udemy regarding licensing and usage rights.
