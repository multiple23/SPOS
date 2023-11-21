import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Shopping Blog")
root.geometry("800x600")  # Set an initial window size

# Define colors
background_color = "#F4F4F4"
title_color = "#333333"
button_color = "#3498DB"
blog_bg = "#FFFFFF"
header_bg = "#3498DB"
header_text_color = "#FFFFFF"
footer_bg = "#333333"
footer_text_color = "#FFFFFF"

# Set the background color
root.configure(bg=background_color)

# Create a title label
title_font = font.nametofont("TkDefaultFont")
title_font.configure(size=24, weight="bold")

title_label = tk.Label(root, text="Shopping Blog", font=title_font, fg=title_color, bg=background_color)
title_label.pack(pady=20)

# Create a header with navigation links
header_frame = tk.Frame(root, bg=header_bg)
header_frame.pack(fill="x")

def navigate_to_page(page):
    # You can add functionality here to navigate to the selected page
    print(f"Navigating to {page}")

home_button = tk.Button(header_frame, text="Home", font=("Arial", 12), command=lambda: navigate_to_page("Home"), bg=header_bg, fg=header_text_color)
shop_button = tk.Button(header_frame, text="Shop", font=("Arial", 12), command=lambda: navigate_to_page("Shop"), bg=header_bg, fg=header_text_color)
blog_button = tk.Button(header_frame, text="Blog", font=("Arial", 12), command=lambda: navigate_to_page("Blog"), bg=header_bg, fg=header_text_color)
contact_button = tk.Button(header_frame, text="Contact", font=("Arial", 12), command=lambda: navigate_to_page("Contact"), bg=header_bg, fg=header_text_color)
about_button = tk.Button(header_frame, text="About", font=("Arial", 12), command=lambda: navigate_to_page("About"), bg=header_bg, fg=header_text_color)

home_button.pack(side="left", padx=10, pady=10)
shop_button.pack(side="left", padx=10, pady=10)
blog_button.pack(side="left", padx=10, pady=10)
contact_button.pack(side="left", padx=10, pady=10)
about_button.pack(side="left", padx=10, pady=10)

# Create a blog frame
blog_frame = tk.Frame(root, bg=background_color)
blog_frame.pack(fill="both", expand=True)

# Add a vertical scrollbar for the blog frame
scrollbar = tk.Scrollbar(blog_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create a Canvas to hold the blog posts and connect it to the scrollbar
canvas = tk.Canvas(blog_frame, bg=background_color, yscrollcommand=scrollbar.set)
canvas.pack(fill="both", expand=True)
scrollbar.config(command=canvas.yview)

# Create a frame inside the canvas to hold the blog posts
blog_posts_frame = tk.Frame(canvas, bg=background_color)
canvas.create_window((0, 0), window=blog_posts_frame, anchor="nw")

# Function to create a blog post
def create_blog_post(image_path, title, content):
    blog_post = tk.Frame(blog_posts_frame, bg=blog_bg, borderwidth=2, relief="solid")
    blog_post.grid(row=len(blog_posts_frame.winfo_children()), column=0, padx=20, pady=10, sticky="nsew")

    image_label = tk.Label(blog_post, text="Blog Image", font=("Arial", 12), bg=blog_bg)
    image_label.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

    title_label = tk.Label(blog_post, text=title, font=("Arial", 16, "bold"), fg=button_color, bg=blog_bg)
    title_label.grid(row=0, column=1, sticky="w")

    content_label = tk.Label(blog_post, text=content, font=("Arial", 12), bg=blog_bg)
    content_label.grid(row=1, column=1, sticky="w")

    read_more_button = tk.Button(blog_post, text="Read More", font=("Arial", 12), bg=button_color, fg="white")
    read_more_button.grid(row=2, column=1, padx=10, pady=10)

# Sample blog post data
blog_posts = [
    {"image_path": "img/blog/b1.jpg", "title": "The cotton-Jersey zip-up Hoodies", "content": "KickStarter man braid godard coloring book. Baclette weistcoat selfies yrwolf chartreuse hexagon irony, godard...."},
    {"image_path": "img/blog/b2.jpg", "title": "How to style a Quiff", "content": "KickStarter man braid godard coloring book. Baclette weistcoat selfies yrwolf chartreuse hexagon irony, godard...."},
    {"image_path": "img/blog/b3.jpg", "title": "Must-Have Skater Girl items", "content": "KickStarter man braid godard coloring book. Baclette weistcoat selfies yrwolf chartreuse hexagon irony, godard...."},
    {"image_path": "img/blog/b4.jpg", "title": "Runway-Inspired Trends", "content": "KickStarter man braid godard coloring book. Baclette weistcoat selfies yrwolf chartreuse hexagon irony, godard...."},
    {"image_path": "img/blog/b5.jpg", "title": "AM20 Menswear Trends", "content": "KickStarter man braid godard coloring book. Baclette weistcoat selfies yrwolf chartreuse hexagon irony, godard...."},
    # Add more blog post data as needed
]

# Create blog posts
for post_data in blog_posts:
    create_blog_post(**post_data)

# Configure the Canvas to expand with the window
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", configure_canvas)

# Create a footer
footer_label = tk.Label(root, text="© 2023 Shopping Blog. All rights reserved.", font=("Arial", 10), fg=footer_text_color, bg=footer_bg)
footer_label.pack(pady=20, fill="x")

# Update the window to make it responsive
root.update()

# Set the Canvas width to match the window width
canvas.config(width=blog_frame.winfo_width())

# Start the main loop
root.mainloop()
