import base64
import urllib.request
import os

icons = {
    "html": "https://skillicons.dev/icons?i=html",
    "css": "https://skillicons.dev/icons?i=css",
    "javascript": "https://skillicons.dev/icons?i=javascript",
    "typescript": "https://skillicons.dev/icons?i=typescript",
    "react": "https://skillicons.dev/icons?i=react",
    "tailwind": "https://skillicons.dev/icons?i=tailwind",
    "vite": "https://skillicons.dev/icons?i=vite"
}

svg_path = "/Users/xiaoka/KK5241/assets/skills.svg"

try:
    if not os.path.exists(svg_path):
        print(f"File not found: {svg_path}")
        exit(1)

    with open(svg_path, "r") as f:
        content = f.read()

    for name, url in icons.items():
        print(f"Downloading {name}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = response.read()
                # Determine mime type based on magic numbers or headers if strict, 
                # but skillicons returns svgs.
                mime_type = "image/svg+xml"
                
                b64_data = base64.b64encode(data).decode('utf-8')
                data_uri = f"data:{mime_type};base64,{b64_data}"
                
                target_url = f"https://skillicons.dev/icons?i={name}"
                if target_url in content:
                    content = content.replace(target_url, data_uri)
                    print(f"Replaced {name}")
                else:
                    print(f"Warning: URL for {name} not found in SVG file.")
        except Exception as e:
            print(f"Failed to process {name}: {e}")

    with open(svg_path, "w") as f:
        f.write(content)
    print("Optimization complete.")

except Exception as e:
    print(f"Error: {e}")
