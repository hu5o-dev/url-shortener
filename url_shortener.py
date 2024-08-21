import pyshorteners
import sys

def shorten_url(long_url, service="tinyurl"):
    try:
        shortener = pyshorteners.Shortener()
        
        
        if service == "tinyurl":
            short_url = shortener.tinyurl.short(long_url)
        elif service == "bitly":
            short_url = shortener.bitly.short(long_url)
        elif service == "isgd":
            short_url = shortener.isgd.short(long_url)
        else:
            print(f"Service '{service}' not recognized. Using TinyURL as default.")
            short_url = shortener.tinyurl.short(long_url)
        
        return short_url
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python url_shortener.py <long_url> [service]")
    else:
        long_url = sys.argv[1]
        service = sys.argv[2] if len(sys.argv) == 3 else "tinyurl"
        short_url = shorten_url(long_url, service)
        
        if short_url:
            print(f"Shortened URL: {short_url}")
        else:
            print("Failed to shorten the URL.")
