import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Shopping Website")

# Define colors
background_color = "#F4F4F4"
title_color = "#333333"
button_color = "#3498DB"
product_block_bg = "#FFFFFF"
header_bg = "#3498DB"
header_text_color = "#FFFFFF"
footer_bg = "#333333"
footer_text_color = "#FFFFFF"

# Set the background color
root.configure(bg=background_color)

# Create a title label
title_font = font.nametofont("TkDefaultFont")
title_font.configure(size=24, weight="bold")

title_label = tk.Label(root, text="Shopping Product Collection", font=title_font, fg=title_color, bg=background_color)
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

# Create a product frame
product_frame = tk.Frame(root, bg=background_color)
product_frame.pack()

# Function to create a product block
def create_product_block(image_path, brand, product_name, price):
    product_block = tk.Frame(product_frame, bg=product_block_bg, borderwidth=2, relief="solid")
    product_block.grid(columnspan=2, padx=20, pady=10, sticky="nsew")

    image_label = tk.Label(product_block, text="Product Image", font=("Arial", 12), bg=product_block_bg)
    image_label.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

    brand_label = tk.Label(product_block, text=brand, font=("Arial", 14, "bold"), fg=button_color, bg=product_block_bg)
    brand_label.grid(row=0, column=1, sticky="w")

    product_name_label = tk.Label(product_block, text=product_name, font=("Arial", 12), bg=product_block_bg)
    product_name_label.grid(row=1, column=1, sticky="w")

    price_label = tk.Label(product_block, text=f"Price: ${price:.2f}", font=("Arial", 14, "bold"), fg=button_color, bg=product_block_bg)
    price_label.grid(row=2, column=1, sticky="w")

    buy_button = tk.Button(product_block, text="Buy Now", font=("Arial", 12), bg=button_color, fg="white", width=15)
    buy_button.grid(row=3, column=1, padx=10, pady=10)

# Sample product data
products = [
    {"image_path": "img/products/f1.jpg", "brand": "Adidas", "product_name": "Cartoon Astronaut T-Shirts", "price": 78},
    {"image_path": "img/products/f2.jpg", "brand": "Nike", "product_name": "Space Exploration Hoodie", "price": 64.99},
    {"image_path": "img/products/f3.jpg", "brand": "Puma", "product_name": "Galaxy Print Sneakers", "price": 59.99},
    {"image_path": "img/products/f4.jpg", "brand": "Reebok", "product_name": "Starry Night Leggings", "price": 44.95},
    {"image_path": "img/products/f5.jpg", "brand": "Adidas", "product_name": "Astronaut Graphic Backpack", "price": 39.99},
    {"image_path": "img/products/f6.jpg", "brand": "Nike", "product_name": "Planetary Sports Shoes", "price": 69.99},
    {"image_path": "img/products/f7.jpg", "brand": "Puma", "product_name": "Comet Track Jacket", "price": 55.00},
    {"image_path": "img/products/f8.jpg", "brand": "Reebok", "product_name": "Meteor Shower Tank Top", "price": 29.95},
    # Add more product data as needed
]

# Create product blocks
for product_data in products:
    create_product_block(**product_data)

# Create a footer
footer_label = tk.Label(root, text="© 2023 Shopping Website. All rights reserved.", font=("Arial", 10), fg=footer_text_color, bg=footer_bg)
footer_label.pack(pady=20)

# Start the main loop
root.mainloop()
