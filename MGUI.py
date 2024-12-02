import customtkinter as ctk

# Function to add a new todo item
def add_todo():
    todo = entry.get()
    if todo.strip():  # Ensure the input is not empty or whitespace
        label = ctk.CTkLabel(scrollable_frame, text=todo)
        label.pack(pady=5, anchor="w")  # Adjust alignment for better presentation
        entry.delete(0, ctk.END)

# Create the main application window
root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

# Title Label
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

# Scrollable Frame for displaying tasks
scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack(pady=10)

# Entry widget for adding tasks
entry = ctk.CTkEntry(root, placeholder_text="Add todo")
entry.pack(fill="x", padx=10, pady=(10, 5))

# Button to add tasks
add_button = ctk.CTkButton(root, text="Add", command=add_todo)
add_button.pack(padx=10, pady=10)

# Start the application's event loop
root.mainloop()
