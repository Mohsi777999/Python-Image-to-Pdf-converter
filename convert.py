import tkinter as tk
from tkinter import filedialog
from img2pdf import convert

def convert_images_to_pdf():
    """Converts images selected by the user to a PDF file."""

    # Get list of image file paths
    image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("JPEG Images", "*.jpg"), ("PNG Images", "*.png")])

    # Check if any files were selected
    if not image_paths:
        return

    # Create a PDF file
    try:
        pdf_bytes = convert(image_paths)
        with open("Your-Images.pdf", "wb") as pdf_file:
            pdf_file.write(pdf_bytes)
        print("Images converted to PDF successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create the Tkinter application
root = tk.Tk()
root.title("Image to PDF Converter")

# Create a button to trigger image selection and conversion
convert_button = tk.Button(root, text="Convert Images", command=convert_images_to_pdf)
convert_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
