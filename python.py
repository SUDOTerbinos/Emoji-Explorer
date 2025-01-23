import tkinter as tk
from emoji.unicode_codes import EMOJI_DATA


def show_all_emojis():
    results.delete("1.0", tk.END)  
    for char, info in EMOJI_DATA.items():
        results.insert(tk.END, f"{char} - {info['en']}\n")  
def search_emoji(keyword):
    results.delete("1.0", tk.END)  
    if keyword.strip() == "":
        results.insert(tk.END, "Please enter a keyword to search.\n")
        return
    found = False
    for char, info in EMOJI_DATA.items():
        if keyword.lower() in info['en'].lower():
            results.insert(tk.END, f"{char} - {info['en']}\n")
            found = True
    if not found:
        results.insert(tk.END, f"No emojis found for '{keyword}'.\n")

def clear_results():
    search_entry.delete(0, tk.END)  
    results.delete("1.0", tk.END)  

root = tk.Tk()
root.title("Emoji Explorer")
root.geometry("500x600")

search_label = tk.Label(root, text="Search Emoji:", font=("Arial", 12))
search_label.pack(pady=5)

search_entry = tk.Entry(root, font=("Arial", 12), width=30)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", font=("Arial", 12), command=lambda: search_emoji(search_entry.get()))
search_button.pack(pady=5)

all_button = tk.Button(root, text="Show All Emojis", font=("Arial", 12), command=show_all_emojis)
all_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_results)
clear_button.pack(pady=5)

results = tk.Text(root, font=("Arial", 10), width=55, height=25)
results.pack(pady=10)

root.mainloop()
