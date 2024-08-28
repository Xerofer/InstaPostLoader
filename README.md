# Instagram Post Downloader

## Overview

Download pictures (or videos) along with their captions and other metadata from Instagram.
It supports both private and public accounts and uses the `instaloader` library for downloading posts. The GUI is built using the `tkinter` library.

## Features

- Download posts from public Instagram accounts.
- Download posts from private Instagram accounts (requires login credentials).
- Automatically create folders for each post.

## Prerequisites

- Python 3.x
- `instaloader` library
- `tkinter` library (comes pre-installed with Python)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/instagram-post-downloader.git
   cd instagram-post-downloader

2. **Install Dependencies**

   ```bash
   pip install instaloader

## Usage 

1. **run the application**
    Execute the script to start the GUI application:
   ```bash
   python instagram_post_downloader.py

## Using the Application

### Select Account Type

- Choose between **Private Account** and **Public Account** radio buttons.
  - **Private Account**: You'll need to enter your Instagram username and password.
  - **Public Account**: You only need to enter the target Instagram username.

### Enter Target Username

- Enter the Instagram username of the account from which you want to download posts.

### Download Posts

- Click the `Download Posts` button to start downloading posts from the specified account.

## Folder Structure

- Posts will be saved in a folder named after the target username.
- Each post will be saved in a separate folder within the target username folder, named sequentially as `Post1`, `Post2`, etc.

## Error Handling

- If any required fields are empty or incorrect, an error message will be displayed.
- Common errors include authentication issues or incorrect target usernames.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Instaloader** for Instagram data extraction.
- **Tkinter** for creating the GUI.

## Contact

For any questions or issues, please contact [abdoufly1234@gmail.com].
