"""Script to convert PlantUML files to PNG, SVG, and PDF images"""
import os
import sys

try:
    from plantuml import PlantUML
    PLANTUML_AVAILABLE = True
except ImportError:
    PLANTUML_AVAILABLE = False
    print("plantuml library not available. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plantuml", "six"])
    from plantuml import PlantUML
    PLANTUML_AVAILABLE = True

from PIL import Image

def convert_puml_to_images(puml_file):
    """Convert a PlantUML file to PNG, SVG, and PDF"""
    try:
        print(f"\nProcessing {puml_file}...")
        
        # Read the PlantUML file
        with open(puml_file, 'r', encoding='utf-8') as f:
            puml_content = f.read()
        
        # Create PlantUML processor
        # Use the online server
        server = PlantUML(url='http://www.plantuml.com/plantuml/')
        
        # Generate PNG
        png_file = puml_file.replace('.puml', '.png')
        print(f"  Generating {png_file}...")
        try:
            png_data = server.processes(puml_content)
            if png_data and len(png_data) > 0:
                with open(png_file, 'wb') as f:
                    f.write(png_data)
                print(f"  ✓ Created {png_file}")
                
                # Convert PNG to PDF
                pdf_file = puml_file.replace('.puml', '.pdf')
                print(f"  Generating {pdf_file}...")
                try:
                    img = Image.open(png_file)
                    if img.mode == 'RGBA':
                        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                        rgb_img.paste(img, mask=img.split()[3])
                        img = rgb_img
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(pdf_file, 'PDF', resolution=100.0)
                    print(f"  ✓ Created {pdf_file}")
                except Exception as e:
                    print(f"  ✗ Error creating PDF: {e}")
            else:
                print(f"  ✗ No data returned for PNG")
        except Exception as e:
            print(f"  ✗ Error generating PNG: {e}")
            import traceback
            traceback.print_exc()
        
        # Generate SVG
        svg_file = puml_file.replace('.puml', '.svg')
        print(f"  Generating {svg_file}...")
        try:
            svg_data = server.processes(puml_content, fmt='svg')
            if svg_data and len(svg_data) > 0:
                with open(svg_file, 'wb') as f:
                    f.write(svg_data)
                print(f"  ✓ Created {svg_file}")
            else:
                print(f"  ✗ No data returned for SVG")
        except Exception as e:
            print(f"  ✗ Error generating SVG: {e}")
        
    except Exception as e:
        print(f"Error processing {puml_file}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # List of PlantUML files to convert
    puml_files = [
        'cardlib_enum_uml.puml',
        'poker_uml.puml',
        'blackjack_uml.puml',
        'tehigame_2player_uml.puml'
    ]
    
    # Delete old corrupted files
    print("Cleaning up old files...")
    for puml_file in puml_files:
        base = puml_file.replace('.puml', '')
        for ext in ['.png', '.pdf', '.svg']:
            old_file = base + ext
            if os.path.exists(old_file):
                try:
                    os.remove(old_file)
                except:
                    pass
    
    print("\nGenerating UML diagrams...\n")
    
    # Convert each file
    for puml_file in puml_files:
        if os.path.exists(puml_file):
            convert_puml_to_images(puml_file)
        else:
            print(f"File not found: {puml_file}")
    
    print("\nDone!")

