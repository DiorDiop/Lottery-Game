#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import tkinter as tk
import random


# In[2]:


# Generate a random ticket
def generate_lottery_numbers():
    ticket_numbers = [random.randint(10, 99) for _ in range(6)]
    random.shuffle(ticket_numbers)
    return ticket_numbers


# In[3]:


# Get the user's ticket number
def check_lottery():
    user_numbers = [int(entry.get()) for entry in user_number_entries]
    generated_numbers = generate_lottery_numbers()

    if user_numbers == generated_numbers:
        result_label.config(text="Congratulations! You win!")
    else:
        result_label.config(text="Sorry, you lose. Better luck next time.")


# In[4]:


# Sets the title of the window
app = tk.Tk()
app.title("Lottery Game")


# In[5]:


# Store entry widgets
user_number_entries = []

for i in range(6):
    label = tk.Label(app, text=f"Enter Number {i + 1}:")
    label.pack()
    entry = tk.Entry(app)
    entry.pack()
    user_number_entries.append(entry)


# In[6]:


# Add the button 
generate_button = tk.Button(app, text="Generate Lottery Numbers", command=check_lottery)
generate_button.pack()


# In[7]:


# The main application window
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()


# In[ ]:




