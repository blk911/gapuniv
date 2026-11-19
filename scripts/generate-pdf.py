#!/usr/bin/env python3
"""
Generate PDF from QR cards HTML using headless Chrome/Chromium.

Usage:
    python3 scripts/generate-pdf.py

Requires: Chrome or Chromium installed, or use weasyprint as fallback.
"""

import os
import subprocess
import sys

def find_chrome():
    """Find Chrome/Chromium executable."""
    candidates = [
        '/usr/bin/chromium-browser',
        '/usr/bin/chromium',
        '/usr/bin/google-chrome',
        '/usr/bin/google-chrome-stable',
        '/snap/bin/chromium',
        'chromium-browser',
        'chromium',
        'google-chrome',
    ]
    
    for candidate in candidates:
        try:
            result = subprocess.run([candidate, '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                return candidate
        except FileNotFoundError:
            continue
    return None

def generate_with_chrome(html_path, pdf_path):
    """Generate PDF using headless Chrome."""
    chrome = find_chrome()
    if not chrome:
        return False
    
    # Chrome headless PDF generation
    cmd = [
        chrome,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        f'--print-to-pdf={pdf_path}',
        '--print-to-pdf-no-header',
        '--no-margins',
        f'file://{html_path}'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and os.path.exists(pdf_path):
            return True
        print(f"Chrome error: {result.stderr}")
    except Exception as e:
        print(f"Chrome failed: {e}")
    
    return False

def generate_with_weasyprint(html_path, pdf_path):
    """Generate PDF using WeasyPrint."""
    try:
        from weasyprint import HTML, CSS
        
        HTML(filename=html_path).write_pdf(
            pdf_path,
            stylesheets=[CSS(string='@page { size: letter; margin: 0.5in; }')]
        )
        return True
    except ImportError:
        print("WeasyPrint not installed. Run: pip3 install weasyprint")
        return False
    except Exception as e:
        print(f"WeasyPrint failed: {e}")
        return False

def main():
    # Get paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    html_path = os.path.join(project_root, 'print', 'qr-cards.html')
    pdf_path = os.path.join(project_root, 'print', 'qr-cards.pdf')
    
    if not os.path.exists(html_path):
        print(f"Error: HTML file not found: {html_path}")
        sys.exit(1)
    
    print("Generating PDF from QR cards HTML...")
    
    # Try Chrome first
    if generate_with_chrome(html_path, pdf_path):
        print(f"✓ PDF generated with Chrome: {pdf_path}")
        return
    
    # Try WeasyPrint as fallback
    print("Chrome not available, trying WeasyPrint...")
    if generate_with_weasyprint(html_path, pdf_path):
        print(f"✓ PDF generated with WeasyPrint: {pdf_path}")
        return
    
    print("\n⚠ Could not generate PDF automatically.")
    print("Manual options:")
    print(f"  1. Open {html_path} in a browser and Print → Save as PDF")
    print("  2. Install Chrome/Chromium and run this script again")
    print("  3. Install WeasyPrint: pip3 install weasyprint")
    sys.exit(1)

if __name__ == "__main__":
    main()
