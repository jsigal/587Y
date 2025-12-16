"""Script to convert PlantUML files to PNG and PDF using PlantUML server"""
import requests
import base64
import zlib
import os
from PIL import Image
import io

def encode_plantuml(text):
    """Encode PlantUML text using the correct algorithm with DEFLATE compression"""
    # The text should include @startuml and @enduml
    # Compress using deflate (zlib uses DEFLATE algorithm)
    compressed = zlib.compress(text.encode('utf-8'), level=9)
    
    # Base64 encode
    encoded = base64.b64encode(compressed).decode('ascii')
    
    # Translate to PlantUML's URL-safe encoding
    # Map: 0-9 -> 0-9, A-Z -> A-Z, a-z -> a-z, + -> -, / -> _
    encoded = encoded.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    ))
    
    # Add ~1 prefix to indicate DEFLATE compression
    # ~0 = uncompressed, ~1 = DEFLATE, ~h = HUFFMAN (old)
    return '~1' + encoded

def convert_puml_to_png(puml_file):
    """Convert PlantUML to PNG"""
    try:
        with open(puml_file, 'r', encoding='utf-8') as f:
            puml_content = f.read()
        
        # Encode
        encoded = encode_plantuml(puml_content)
        
        # Use PlantUML server
        url = f'http://www.plantuml.com/plantuml/png/{encoded}'
        
        print(f"Converting {puml_file} to PNG...")
        response = requests.get(url, timeout=60)
        
        # Check response
        if response.status_code != 200:
            print(f"  Error: HTTP {response.status_code}")
            return False
        
        # Check if it's actually a PNG
        if not response.content.startswith(b'\x89PNG'):
            # Might be an error message
            error_text = response.content[:200].decode('utf-8', errors='ignore')
            print(f"  Error: Server returned non-PNG data: {error_text[:100]}")
            return False
        
        # Save PNG
        png_file = puml_file.replace('.puml', '.png')
        with open(png_file, 'wb') as f:
            f.write(response.content)
        
        print(f"  [OK] Created {png_file} ({len(response.content)} bytes)")
        return png_file
        
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def convert_png_to_pdf(png_file):
    """Convert PNG to PDF"""
    try:
        pdf_file = png_file.replace('.png', '.pdf')
        print(f"Converting {png_file} to PDF...")
        
        img = Image.open(png_file)
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])
            img = rgb_img
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.save(pdf_file, 'PDF', resolution=100.0)
        print(f"  [OK] Created {pdf_file}")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False

if __name__ == "__main__":
    puml_files = [
        'cardlib_enum_uml.puml',
        'poker_uml.puml',
        'blackjack_uml.puml',
        'tehigame_2player_uml.puml'
    ]
    
    # Clean up old files
    print("Cleaning up old files...")
    for puml_file in puml_files:
        base = puml_file.replace('.puml', '')
        for ext in ['.png', '.pdf']:
            old_file = base + ext
            if os.path.exists(old_file):
                os.remove(old_file)
    
    print("\nGenerating diagrams...\n")
    
    for puml_file in puml_files:
        if os.path.exists(puml_file):
            png_file = convert_puml_to_png(puml_file)
            if png_file:
                convert_png_to_pdf(png_file)
            print()
        else:
            print(f"File not found: {puml_file}\n")
    
    print("Done!")

