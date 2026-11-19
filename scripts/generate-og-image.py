#!/usr/bin/env python3
"""
Generate Open Graph image for Gap University.

Usage:
    python3 scripts/generate-og-image.py
"""

import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow not installed.")
    print("Run: pip3 install pillow")
    sys.exit(1)

def generate_og_image(output_path: str) -> None:
    """Generate a simple but effective OG image."""
    
    # OG image dimensions (1200x630 is standard)
    width, height = 1200, 630
    
    # Colors
    bg_color = (37, 99, 235)  # Primary blue
    text_color = (255, 255, 255)
    accent_color = (245, 158, 11)  # Amber accent
    
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a font, fall back to default
    try:
        # Try system fonts
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ]
        title_font = None
        subtitle_font = None
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                title_font = ImageFont.truetype(font_path, 72)
                subtitle_font = ImageFont.truetype(font_path, 36)
                break
        
        if not title_font:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
    except Exception:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Draw accent bar at top
    draw.rectangle([(0, 0), (width, 8)], fill=accent_color)
    
    # Draw title
    title = "Gap University"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = bbox[2] - bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 200), title, font=title_font, fill=text_color)
    
    # Draw tagline
    tagline = "Find Your Footing. Find Your Slot."
    bbox = draw.textbbox((0, 0), tagline, font=subtitle_font)
    tagline_width = bbox[2] - bbox[0]
    tagline_x = (width - tagline_width) // 2
    draw.text((tagline_x, 300), tagline, font=subtitle_font, fill=text_color)
    
    # Draw location
    location = "Castle Rock, Colorado"
    bbox = draw.textbbox((0, 0), location, font=subtitle_font)
    loc_width = bbox[2] - bbox[0]
    loc_x = (width - loc_width) // 2
    draw.text((loc_x, 420), location, font=subtitle_font, fill=(200, 220, 255))
    
    # Draw accent bar at bottom
    draw.rectangle([(0, height - 8), (width, height)], fill=accent_color)
    
    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', optimize=True)
    print(f"✓ OG image generated: {output_path}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_path = os.path.join(project_root, 'og-image.png')
    
    generate_og_image(output_path)

if __name__ == "__main__":
    main()
