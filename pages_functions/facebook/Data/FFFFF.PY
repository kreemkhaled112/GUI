import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser

class MyApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings Example")

        # Create a label
        self.label = tk.Label(root, text="Enter your text:")
        self.label.pack()

        # Create a text entry widget
        self.textbox = tk.Entry(root, width=30)
        self.textbox.pack()

        # Create a button to insert text
        self.insert_button = tk.Button(root, text="Insert Text", command=self.insert_text)
        self.insert_button.pack()

        # Create a button to save settings
        self.save_button = tk.Button(root, text="Save Settings", command=self.save_settings)
        self.save_button.pack()

        # Load settings from the configuration file
        self.load_settings()

    def insert_text(self):
        text_to_insert = "Hello, World!"
        # Insert text into the textbox
        self.textbox.insert(0, text_to_insert)

    def save_settings(self):
        # Save the current settings to the configuration file
        config = ConfigParser()
        config['Settings'] = {'DefaultText': self.textbox.get()}

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

        messagebox.showinfo("Settings Saved", "Settings have been saved.")

    def load_settings(self):
        try:
            # Load settings from the configuration file
            config = ConfigParser()
            config.read('settings.ini')

            default_text = config.get('Settings', 'DefaultText')
            self.textbox.insert(0, default_text)

            messagebox.showinfo("Settings Loaded", "Settings have been loaded.")
        except Exception as e:
            messagebox.showwarning("Error", f"An error occurred while loading settings:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()
