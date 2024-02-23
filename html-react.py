import tkinter as tk
from tkinter import font
import re

def convert_style():
    html_code = html_input.get("1.0", "end-1c")

    # Use RE to find style related stuff
    style_regex = r'style="([^"]*)"'
    styles = re.findall(style_regex, html_code)

    for style in styles:

        style_properties = style.split(';')
        updated_properties = []

        for prop in style_properties:
            if ':' in prop:
                prop_name, prop_value = prop.split(':')
                updated_properties.append(f"'{prop_name.strip()}': '{prop_value.strip()}'")

        updated_style = '{{' + ','.join(updated_properties) + '}}'

        html_code = html_code.replace(f'style="{style}"', f'style={updated_style}')

    # Show output in the html_output
    html_output.delete("1.0", tk.END)
    html_output.insert(tk.END, html_code)

# GUI
window = tk.Tk()
window.title("HTML Style Converter")

instruction_font = font.Font(weight="bold", size=12)
instruction_label = tk.Label(window, text="HTML Code Converter by Jack", font=instruction_font)
instruction_label.pack(pady=5)

instruction_label = tk.Label(window, text="Input (Legacy HTML)")
instruction_label.pack(pady=3)

# Input

html_input = tk.Text(window, height=10, width=50)
html_input.pack(pady=10)

# Conver Button
convert_button = tk.Button(window, text="Convert", command=convert_style)
convert_button.pack()

instruction_label = tk.Label(window, text="Output (React Readable HTML)")
instruction_label.pack(pady=3)

# Output
html_output = tk.Text(window, height=10, width=50)
html_output.pack(pady=10)

window.mainloop()
