def conversion(markdown_text):
    """
    Converts basic Markdown syntax into HTML.
    """
    lines = markdown_text.split('\n')  # Split the input text into lines
    html_output = ""

    for line in lines:
        line = line.strip()  
        if not line: 
            continue
        
        # Heading conversion 
        if line.startswith('#'):
            level = line.count('#')  
            line = line.lstrip('#').strip()  
            html_output += "<h" + str(level) + ">" + line + "</h" + str(level) + ">\n"
        # Bold text conversion (e.g., **bold**)
        elif '**' in line:
            bold_text = line.replace('**', '<b>', 1).replace('**', '</b>', 1)
            html_output += "<p>" + bold_text + "</p>\n"
        # Paragraph conversion (for regular text)
        else:
            html_output += "<p>" + line.strip() + "</p>\n"

    return html_output

def main():
    markdown_text = """# Heading 1
## Heading 2
This is **bold text**.
This is a regular paragraph.
    """

    html = conversion(markdown_text)
    print(html)

main()
