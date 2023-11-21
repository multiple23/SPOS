import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Shopping Website")

# Define some colors
background_color = "#F4F4F4"
header_color = "#3498DB"
title_color = "#333333"

# Set the background color
root.configure(bg=background_color)

# Create a header frame
header_frame = tk.Frame(root, bg=header_color)
header_frame.pack(fill=tk.X)

# Create a custom font for the title
title_font = font.nametofont("TkDefaultFont")
title_font.configure(family="Cara", size=32, weight="bold")

# Create the title on the left side of the header
title_label = tk.Label(header_frame, text="Cara", font=title_font, fg="white", bg=header_color, padx=10)
title_label.pack(side=tk.LEFT, padx=10)

# Create navigation links in the header
nav_links = ["Home", "Shop", "Blog", "About", "Contact"]
for link in nav_links:
    link_label = tk.Label(header_frame, text=link, font=("Arial", 14), fg="white", bg=header_color, padx=10)
    link_label.pack(side=tk.LEFT, padx=10)

# Create an introduction block
intro_frame = tk.Frame(root, bg=background_color)
intro_frame.pack(pady=20)

intro_text = "Welcome to our online shopping website! Explore a wide range of products and find the best deals."
introduction_label = tk.Label(intro_frame, text=intro_text, font=("Arial", 16), fg=title_color, bg=background_color, wraplength=400, justify="center")
introduction_label.pack()

# Create a title label
title_label = tk.Label(root, text="Featured Products", font=("Arial", 20), fg=title_color, bg=background_color)
title_label.pack(pady=20)

# Create a product block
def create_product_block(product_name, product_description, price):
    product_block = tk.Frame(root, bg=background_color)
    product_block.pack(padx=20, pady=10, fill=tk.BOTH)

    product_button = tk.Button(product_block, text=product_name, bg=header_color, fg="white")
    product_button.pack(pady=5, fill=tk.X)

    description_label = tk.Label(product_block, text=product_description, font=("Arial", 12), bg=background_color)
    description_label.pack(pady=5)

    price_label = tk.Label(product_block, text=f"Price: ${price:.2f}", font=("Arial", 14, "bold"), bg=background_color)
    price_label.pack(pady=5)

# Create product blocks
create_product_block("Product 1", "This is a sample product description.", 19.99)
create_product_block("Product 2", "Another great product for you to explore.", 24.99)
create_product_block("Product 3", "Don't miss out on this fantastic offer.", 14.99)

# Create a footer
footer_label = tk.Label(root, text="© 2023 Shopping Website. All rights reserved.", font=("Arial", 10), fg=title_color, bg=background_color)
footer_label.pack(pady=20)

# Start the main loop
root.mainloop()
