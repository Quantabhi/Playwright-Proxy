from playwright.sync_api import sync_playwright
from urllib.parse import urlparse

# Parse the proxy URL
proxy_url = urlparse("http://username:password@hostname:port")

# Extract the username and password
username = proxy_url.username
password = proxy_url.password

# Extract the host and port
host = proxy_url.hostname
port = proxy_url.port

def useproxy_search():
    # Launch Playwright
    with sync_playwright() as p:
        # Launch Chromium browser
        browser = p.chromium.launch(
            headless=False,
            proxy={
                "server": f"http://{host}:{port}",
                "username": username,
                "password": password
            }
        )
        # Create a new browsing context and page
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the specified URL (replace 'put your url' with the actual URL)
        page.goto('put your url')

        # Wait for the page to reach a network idle state
        page.wait_for_load_state('networkidle')

        # Close the browser
        browser.close()

if __name__ == '__main__':
    useproxy_search()
