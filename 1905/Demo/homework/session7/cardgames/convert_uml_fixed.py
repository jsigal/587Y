"""Script to convert PlantUML files to PNG, SVG, and PDF images using PlantUML server"""
import requests
import base64
import zlib
import os

def encode_plantuml(text):
    """Encode PlantUML text for URL using correct PlantUML encoding"""
    # Remove @startuml and @enduml if present (server adds them)
    text = text.strip()
    if text.startswith('@startuml'):
        # Find the actual content
        lines = text.split('\n')
        # Skip @startuml and @enduml
        content_lines = [line for line in lines if not line.strip().startswith('@startuml') and not line.strip().startswith('@enduml')]
        text = '\n'.join(content_lines)
    
    # Compress the text
    compressed = zlib.compress(text.encode('utf-8'))
    
    # Base64 encode
    encoded = base64.b64encode(compressed).decode('utf-8')
    
    # PlantUML uses a special URL-safe encoding
    # Replace standard base64 characters with PlantUML's encoding
    encoded = encoded.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    ))
    
    return encoded

def convert_puml_to_image(puml_file, output_format='png'):
    """Convert a PlantUML file to an image format"""
    try:
        # Read the PlantUML file
        with open(puml_file, 'r', encoding='utf-8') as f:
            puml_content = f.read()
        
        # Generate the image
        output_file = puml_file.replace('.puml', f'.{output_format}')
        print(f"Converting {puml_file} to {output_file}...")
        
        # Encode the PlantUML content
        encoded = encode_plantuml(puml_content)
        
        # Use PlantUML server to generate image
        # Try different URL formats
        urls = [
            f'http://www.plantuml.com/plantuml/{output_format}/{encoded}',
            f'https://www.plantuml.com/plantuml/{output_format}/{encoded}',
        ]
        
        success = False
        for url in urls:
            try:
                # Download the image
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                
                # Check if response is actually an image (not HTML error)
                content_type = response.headers.get('Content-Type', '')
                content_start = response.content[:100]
                
                if 'html' in content_type.lower() or b'<html' in content_start.lower() or b'error' in content_start.lower():
                    print(f"  Warning: Server returned HTML/error for {url}")
                    continue
                
                # Check for PNG signature
                if output_format == 'png' and not content_start.startswith(b'\x89PNG'):
                    print(f"  Warning: Response doesn't look like a PNG file")
                    # Still try to save it, might be valid
                
                # Write to file
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                
                print(f"Successfully created {output_file}")
                success = True
                break
            except Exception as e:
                print(f"  Error with {url}: {e}")
                continue
        
        if not success:
            print(f"Failed to convert {puml_file} to {output_format}")
            return False
        
        return True
    except Exception as e:
        print(f"Error converting {puml_file}: {e}")
        import traceback
        traceback.print_exc()
        return False

def convert_png_to_pdf(png_file):
    """Convert PNG to PDF using PIL/Pillow if available"""
    try:
        from PIL import Image
        pdf_file = png_file.replace('.png', '.pdf')
        print(f"Converting {png_file} to {pdf_file}...")
        
        # Open PNG and convert to PDF
        img = Image.open(png_file)
        # Convert to RGB if necessary (PDF doesn't support RGBA)
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            img = rgb_img
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.save(pdf_file, 'PDF', resolution=100.0)
        print(f"Successfully created {pdf_file}")
        return True
    except ImportError:
        print("PIL/Pillow not available. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"Error converting PNG to PDF: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # List of PlantUML files to convert
    puml_files = [
        'cardlib_enum_uml.puml',
        'poker_uml.puml',
        'blackjack_uml.puml',
        'tehigame_2player_uml.puml'
    ]
    
    # Delete old files first
    print("Cleaning up old files...")
    for puml_file in puml_files:
        base = puml_file.replace('.puml', '')
        for ext in ['.png', '.pdf', '.svg']:
            old_file = base + ext
            if os.path.exists(old_file):
                try:
                    os.remove(old_file)
                    print(f"Removed {old_file}")
                except:
                    pass
    
    print("\nGenerating new diagrams...\n")
    
    # Convert each file to PNG and SVG
    for puml_file in puml_files:
        if os.path.exists(puml_file):
            print(f"\nProcessing {puml_file}...")
            # Generate PNG (works)
            if convert_puml_to_image(puml_file, 'png'):
                # Convert PNG to PDF
                png_file = puml_file.replace('.puml', '.png')
                convert_png_to_pdf(png_file)
            
            # Generate SVG (should work)
            convert_puml_to_image(puml_file, 'svg')
        else:
            print(f"File not found: {puml_file}")

