import tkinter as tk
import whois
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

# Define a custom function to perform a WHOIS lookup
def custom_whois(url):
    try:
        return whois.whois(url)
    except TypeError:
        # Handle the TypeError raised by the 'python-whois' library
        return "WHOIS information not available"

def searchForUrl():
    url = UrlText.get()
    domain_info = custom_whois(url)
    filename = ''
    if 'www.' in url:
        filename = url.split('.')[1]
    else:
        filename = url.split('.')[0]
    with open(filename + ".txt", "w") as f:
        f.write(str(domain_info))
  # Show a message box when the scan is done
    messagebox.showinfo("Scan Completed", "WHOIS scan has been completed!")

def exitForm():
    window.quit()

window = tk.Tk()
window.geometry("800x400")
window.title("Web Scanner")

# Load the background image
background_image = Image.open("D:/BS- Computer Sciences/WebScanner/ifti.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

label1 = tk.Label(window, text="IM Cybertron Web Scanner", font=("arial", 16, "bold"), fg='blue', bg='yellow', relief='solid')
label1.pack(fill=tk.BOTH)

UrlLabel = tk.Label(window, text="Enter URL: ", font=("arial", 12, "bold"))
UrlLabel.place(x=50, y=150)

ScanButton = tk.Button(window, text="Scan", font=("arial", 12, "bold"), bg='green', width=6, command=searchForUrl)
ScanButton.place(x=315, y=200)

ExitButton = tk.Button(window, text="Exit", font=("arial", 12, "bold"), bg='green', width=6, command=exitForm)
ExitButton.place(x=415, y=200)

UrlText = tk.Entry(window, textvar='', width=60)
UrlText.place(x=220, y=150)

window.mainloop()
