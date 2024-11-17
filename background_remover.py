import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image
import os

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")

        # GUI Layout
        self.input_label = tk.Label(root, text="Input File: None")
        self.input_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Remove Background & Save", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.status_label = tk.Label(root, text="Status: Waiting for input...", fg="blue")
        self.status_label.pack(pady=10)

        # Variables to store paths
        self.input_path = None
        self.output_path = None

    def select_image(self):
        # Open file dialog to select input image
        self.input_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if not self.input_path:
            self.status_label.config(text="Status: No file selected", fg="red")
            return

        # Update input label and enable save button
        self.input_label.config(text=f"Input File: {os.path.basename(self.input_path)}")
        self.save_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Ready to process", fg="green")

    def save_image(self):
        if not self.input_path:
            self.status_label.config(text="Status: No input file selected", fg="red")
            return

        # Open file dialog to select output file path
        self.output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not self.output_path:
            self.status_label.config(text="Status: Save canceled", fg="red")
            return

        try:
            # Load input image and remove background
            input_image = Image.open(self.input_path)
            output_image = remove(input_image)

            # Save the output image
            output_image.save(self.output_path)

            self.status_label.config(text=f"Status: Saved to {self.output_path}", fg="green")
            messagebox.showinfo("Success", f"Background removed and saved to:\n{self.output_path}")
        except Exception as e:
            self.status_label.config(text=f"Status: Error - {e}", fg="red")
            messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
