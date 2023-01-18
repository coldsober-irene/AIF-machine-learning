    
# FULL CODES
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table to store the image
cursor.execute('''CREATE TABLE images
                (image_data BLOB, image_name TEXT)''')

# Open the image file
with open('image.jpg', 'rb') as f:
    # Read the image data
    img_data = f.read()

    # Insert the image into the database
    cursor.execute("INSERT INTO images (image_data, image_name) VALUES (?,?)",(sqlite3.Binary(img_data), 'image.jpg'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
