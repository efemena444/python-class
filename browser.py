import webbrowser

def open_browser():
    url = input("Enter the URL you want to open: ")
    webbrowser.open(url)

# Start the web browser
open_browser()