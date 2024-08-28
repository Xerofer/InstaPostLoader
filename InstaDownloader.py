import tkinter as tk
from tkinter import messagebox
import instaloader
import os

def toggle_private_account():
    if is_private.get() == 1:
        # Show Instagram credentials fields
        username_label.pack(pady=5)
        username_entry.pack(pady=5)
        password_label.pack(pady=5)
        password_entry.pack(pady=5)
    else:
        # Hide Instagram credentials fields
        username_label.pack_forget()
        username_entry.pack_forget()
        password_label.pack_forget()
        password_entry.pack_forget()

def download_posts():
    if is_private.get() == 1:
        instagram_username = username_entry.get()
        instagram_password = password_entry.get()
        target_username = target_username_entry.get()

        if not instagram_username or not instagram_password or not target_username:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            # Create an Instaloader instance
            L = instaloader.Instaloader()

            # Login to Instagram
            L.login(instagram_username, instagram_password)

            # Fetch the profile of the target Instagram account
            profile = instaloader.Profile.from_username(L.context, target_username)

            # Create a folder to store the downloaded posts
            download_folder = target_username
            os.makedirs(download_folder, exist_ok=True)

            os.chdir(download_folder)

            # Counter to keep track of post numbers
            post_counter = 1

            # Download all the posts of the target user and save each post in the main folder
            for post in profile.get_posts():
                # Create a folder for each post using a number
                post_folder = os.path.join(download_folder, f"Post{post_counter}")
                

                # Download and save the post in its respective folder
                L.download_post(post, post_folder)

                # Increment the post counter
                post_counter += 1

            messagebox.showinfo("Success", f"All posts from {target_username} have been downloaded to {download_folder}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        target_username = target_username_entry.get()

        if not target_username:
            messagebox.showerror("Error", "Please enter the target username.")
            return

        try:
            # Create an Instaloader instance
            L = instaloader.Instaloader()

            # Fetch the profile of the target Instagram account
            profile = instaloader.Profile.from_username(L.context, target_username)

            # Create a folder to store the downloaded posts
            download_folder = target_username
            os.makedirs(download_folder, exist_ok=True)

            os.chdir(download_folder)

            # Counter to keep track of post numbers
            post_counter = 1

            # Download all the posts of the target user and save each post in the main folder
            for post in profile.get_posts():
                # Create a folder for each post using a number
                post_folder = os.path.join(download_folder, f"Post{post_counter}")
                

                # Download and save the post in its respective folder
                L.download_post(post, post_folder)

                # Increment the post counter
                post_counter += 1

            messagebox.showinfo("Success", f"All posts from {target_username} have been downloaded to {download_folder}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Instagram Post Downloader")

# Private/Public Account Selection
is_private = tk.IntVar()
is_private.set(0)

private_radio = tk.Radiobutton(root, text="Private Account", variable=is_private, value=1, command=toggle_private_account)
private_radio.pack(pady=5)

public_radio = tk.Radiobutton(root, text="Public Account", variable=is_private, value=0, command=toggle_private_account)
public_radio.pack(pady=5)

# Instagram Username Label and Entry (hidden by default)
username_label = tk.Label(root, text="Your Instagram Username:")
username_entry = tk.Entry(root, width=30)

# Instagram Password Label and Entry (hidden by default)
password_label = tk.Label(root, text="Your Instagram Password:")
password_entry = tk.Entry(root, width=30, show="*")

# Target Username Label and Entry (shown by default)
target_username_label = tk.Label(root, text="Target Instagram Username:")
target_username_label.pack(pady=5)
target_username_entry = tk.Entry(root, width=30)
target_username_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download Posts", command=download_posts)
download_button.pack(pady=20)

# Run the application
root.mainloop()
