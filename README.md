# HTML to React
 Python tool that can convert html to React readable beacause of that style issue.

**React Error: Style prop value must be an object react/style-prop-object**

For example:

```html
style="margin-right: 16px;height: 42px;border-radius: 28px;width: 42px;"
```

to

```html
style={{'margin-right': '16px','height': '42px','border-radius': '28px','width': '42px'}}
```

It would be annoying to change it one-by-one manually, so I made this tool.

# Hot to use?

- Make sure you have python installed.
- Right click the file and open as Python.
- Copy & paste the HTML code to Input text field.
- Hit "Convert" button
- Copy the code from the Output text field and paste anywhere you want.
- Enjoy
