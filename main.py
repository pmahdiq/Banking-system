import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget
)
from PySide6.QtCore import Qt

class AuthDialog(QDialog):
    """
    A small, modal dialog window asking the user to Log In or Sign Up.
    The choice is communicated via print and the dialog closing.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Authentication Required")
        self.setFixedSize(300, 150) # Set a fixed, small size

        # Remove the 'What's This?' help button and customize flags
        flags = self.windowFlags()
        flags &= ~Qt.WindowContextHelpButtonHint
        self.setWindowFlags(flags)


        # --- 1. Main Layout ---
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # --- 2. Prompt Label ---
        prompt_label = QLabel("Welcome! What would you like to do?")
        prompt_label.setAlignment(Qt.AlignCenter)
        prompt_label.setStyleSheet("font-size: 14pt; font-weight: bold;")

        # --- 3. Button Layout (Horizontal) ---
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        # --- 4. Log In Button ---
        self.login_button = QPushButton("Log In")
        self.login_button.setDefault(True) # Set as default action
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.setStyleSheet(
            "padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;"
        )
        # Connect to action handler
        self.login_button.clicked.connect(self.handle_login_choice)

        # --- 5. Sign Up Button ---
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setCursor(Qt.PointingHandCursor)
        self.signup_button.setStyleSheet(
            "padding: 10px; background-color: #2196F3; color: white; border: none; border-radius: 5px;"
        )
        # Connect to action handler
        self.signup_button.clicked.connect(self.handle_signup_choice)

        # Add buttons to the horizontal layout
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)

        # --- 6. Add components to Main Layout ---
        main_layout.addWidget(prompt_label)
        main_layout.addLayout(button_layout)


    def handle_login_choice(self):
        """Action when Log In is clicked."""
        print("User chose: Log In (Next, open Page X)")
        # In a real app, this is where you'd trigger opening the next window (Page X)
        self.done(QDialog.Accepted) # Closes the dialog

    def handle_signup_choice(self):
        """Action when Sign Up is clicked."""
        print("User chose: Sign Up (Next, open Page Y)")
        # In a real app, this is where you'd trigger opening the next window (Page Y)
        self.done(QDialog.Accepted) # Closes the dialog


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instantiate and show the dialog
    dialog = AuthDialog()
    
    # exec() runs the dialog modally (blocks until the user makes a choice)
    result = dialog.exec() 
    
    # Check the result after the dialog closes
    if result == QDialog.Accepted:
        print("Dialog successfully completed a choice.")
    else:
        print("Dialog was closed/cancelled.")

    sys.exit(app.exec())