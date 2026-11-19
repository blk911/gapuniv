#!/usr/bin/env python3
"""
Generate QR code for Gap University website.

Usage:
    python3 scripts/generate-qr.py [--url URL]

The QR code will be saved to assets/qr-code.png
"""

import argparse
import os
import sys

try:
    import qrcode
    from PIL import Image
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip3 install qrcode[pil] pillow")
    sys.exit(1)

# ============================================
# CONFIGURATION - Default URL for QR code
# Change this when you have a custom domain
# ============================================
DEFAULT_URL = "https://blk911.github.io/gapuniv/"

def generate_qr_code(url: str, output_path: str) -> None:
    """Generate a QR code for the given URL."""
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for better scanning
        box_size=10,
        border=2,  # Minimal border for compact cards
    )
    
    # Add data
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image with custom colors
    img = qr.make_image(fill_color="#1f2937", back_color="white")
    
    # Save the image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"✓ QR code generated: {output_path}")
    print(f"  URL: {url}")

def main():
    parser = argparse.ArgumentParser(description="Generate QR code for Gap University")
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"URL to encode in QR code (default: {DEFAULT_URL})"
    )
    parser.add_argument(
        "--output",
        default="assets/qr-code.png",
        help="Output path for QR code image (default: assets/qr-code.png)"
    )
    
    args = parser.parse_args()
    
    # Get script directory to resolve paths relative to project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_path = os.path.join(project_root, args.output)
    
    generate_qr_code(args.url, output_path)

if __name__ == "__main__":
    main()
