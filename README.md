# 🔗 URL Shortener

A simple Python script to shorten URLs using various shortening services like TinyURL, Bitly, and is.gd. 

## 🚀 Features

- 🌐 Supports multiple URL shortening services
  - TinyURL (default)
  - Bitly
  - is.gd
- ⚙️ Easy to use and extend
- 🐍 Lightweight with minimal dependencies

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hu5o-dev/url-shortener.git
   cd url-shortener
   ```

2. Install the required Python package:

   ```bash
   pip install pyshorteners
   ```

## 🛠️ Usage

To shorten a URL, run the script with the desired long URL and optional shortening service:

```bash
python url_shortener.py <long_url> [service]
```

- `<long_url>`: The URL you want to shorten (required).
- `[service]`: The URL shortening service to use (optional, defaults to `tinyurl`).

### 🔧 Examples

- Shorten a URL using TinyURL (default):

  ```bash
  python url_shortener.py https://www.example.com
  ```

- Shorten a URL using Bitly:

  ```bash
  python url_shortener.py https://www.example.com bitly
  ```

- Shorten a URL using is.gd:

  ```bash
  python url_shortener.py https://www.example.com isgd
  ```

## 📝 Notes

- If no service is provided, the script defaults to using TinyURL.
- You can easily add more shortening services by modifying the `shorten_url` function in the script.

## 🎉 Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions, feel free to reach out via GitHub issues or directly at hugo@hugo.city.
