import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

def generate_qr():
    lens_data = {
        "Brand": brand_var.get(),
        "Lens Type": lens_type_var.get(),
        "Index": index_var.get(),
        "Shape": shape_var.get(),
        "Spherical": spherical_var.get(),
        "Cylindrical": cylindrical_var.get(),
        "Axis": axis_var.get(),
        "Addl": addl_var.get()
    }

    qr_content = "\n".join(f"{key}: {value}" for key, value in lens_data.items())
    qr_img = qrcode.make(qr_content)
    qr_img.save("lens_qr.png")
    messagebox.showinfo("Success", "QR Code Saved as 'lens_qr.png'")
    
    # Show QR code in GUI
    img = Image.open("lens_qr.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# GUI Setup
app = tk.Tk()
app.title("Lens QR Code Generator")
app.geometry("400x650")

# Input Fields
fields = [
    ("Brand", "brand_var"),
    ("Lens Type", "lens_type_var"),
    ("Index", "index_var"),
    ("Shape", "shape_var"),
    ("Spherical", "spherical_var"),
    ("Cylindrical", "cylindrical_var"),
    ("Axis", "axis_var"),
    ("Addl", "addl_var")
]

for label, var_name in fields:
    tk.Label(app, text=label).pack()
    globals()[var_name] = tk.StringVar()
    tk.Entry(app, textvariable=globals()[var_name], width=30).pack()

# Generate Button
tk.Button(app, text="Generate QR Code", command=generate_qr).pack(pady=10)

# QR Display Area
qr_label = tk.Label(app)
qr_label.pack(pady=20)

app.mainloop()
