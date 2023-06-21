import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os


#function for converting img to pdf

def img_to_pdf(images,pdf_name):
    try:
        #create a new pdf file
        pdf=Image.open(images[0])
        pdf.save(pdf_name,"PDF",resolution=100.0,save_all=True,append_images=images[1:])
        messagebox.showinfo("Succes","Images have been converted")

    except Exception as e:
        messagebox.showerror("Error","Failed to convert\n"+str(e))
    
def selecting_images():
    images=filedialog.askopenfilenames(title="Select images",filetypes=(("Image files","*.jpg;*.jpeg;*.png"),("All files","*.*")),initialdir="C:/")
    return images

# function to select pdf name and path

def select_pdf():
    pdf=filedialog.asksaveasfilename(title="Save PDF as ",defaultextension=".pdf",initialdir="C:/",filetypes=(("PDF files","*.pdf"),("All files","*.*")))
    return pdf

#create GUI
root=tk.Tk()
root.title("PDF converter")
selecting_images_btn=tk.Button(root,text="Select images",command=selecting_images)
selecting_pdf_btn=tk.Button(root,text="Select pdf",command=select_pdf)
convert_btn=tk.Button(root,text="convert",command=lambda: img_to_pdf(selecting_images(),select_pdf()))
selecting_images_btn.pack()
selecting_pdf_btn.pack()
convert_btn.pack()
root.mainloop()

