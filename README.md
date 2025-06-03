# SRI Hash Generator

This little Python script helps you generate Subresource Integrity (SRI) hashes for external resources like CSS files or JavaScript libraries.

## Why is this necessary?

When you include external files from a Content Delivery Network (CDN) in your website, you're trusting that the CDN will always deliver the correct and uncompromised version of that file. While CDNs are generally reliable, there's always a tiny chance that a CDN could be compromised, or the file itself could be accidentally altered.

That's where Subresource Integrity (SRI) comes in! By adding an `integrity` attribute to your `<script>` or `<link>` tags, you tell the browser to check the hash of the fetched resource against the hash you provided. If the hashes don't match, the browser will refuse to load the resource. This acts as a security check, ensuring that the file hasn't been tampered with.

This script makes it easy to generate those crucial SRI hashes!

## How to Use It

1.  **Save the script:** Save the Python code as `generate_sri.py` in your project.

2.  **Run from your terminal:** Open your terminal or command prompt, navigate to where you saved the script, and run it using `python generate_sri.py`.

    You can provide the URLs directly:

    ```bash
    python generate_sri.py "[https://cdn.tailwindcss.com/3.4.3](https://cdn.tailwindcss.com/3.4.3)" "[https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Space+Grotesk:wght@400;700&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Space+Grotesk:wght@400;700&display=swap)"
    ```

    Or, for a clearer output, you can give each URL a friendly name:

    ```bash
    python generate_sri.py "MyTailwind=[https://cdn.tailwindcss.com/3.4.3](https://cdn.tailwindcss.com/3.4.3)" "GoogleFonts=[https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Space+Grotesk:wght@400;700&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Space+Grotesk:wght@400;700&display=swap)"
    ```

3.  **Copy and paste:** The script will print the generated SRI hashes. Simply copy these values and paste them into the `integrity` attribute of your `<link>` or `<script>` tags in your `index.html` file (or wherever you're including your external resources).

    **Example for CSS:**

    ```html
    <link rel="stylesheet" href="[https://cdn.tailwindcss.com/3.4.3](https://cdn.tailwindcss.com/3.4.3)" integrity="sha384-..." crossorigin="anonymous">
    ```

    **Example for JavaScript:**

    ```html
    <script src="[https://example.com/some-library.js](https://example.com/some-library.js)" integrity="sha384-..." crossorigin="anonymous"></script>
    ```

    Remember to always include `crossorigin="anonymous"` when using SRI.
