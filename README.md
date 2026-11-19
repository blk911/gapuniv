# Gap University Website

A mobile-first, single-page marketing website for Gap University — helping young adults (17-23) find their footing.

**Live site:** https://blk911.github.io/gapuniv/

## Quick Start

1. **Enable GitHub Pages:**
   - Go to your repo Settings → Pages
   - Under "Build and deployment", select **GitHub Actions** as the source
   - The site will auto-deploy on every push to `main`

2. **Configure the contact form** (see [Form Setup](#form-setup) below)

3. **Update content** (see [Content Editing](#content-editing) below)

---

## Form Setup

The signup form uses [Formspree](https://formspree.io) (free tier: 50 submissions/month). Until configured, it falls back to a mailto: link so no data is lost.

### Option A: Formspree (Recommended)

1. Create a free account at https://formspree.io
2. Create a new form (name it "Gap University Signups")
3. Copy your **form ID** (looks like: `xrgvnqkp`)
4. Edit `form.js` and set your ID:
   ```javascript
   const FORMSPREE_ID = 'xrgvnqkp'; // Your actual form ID
   ```
5. Commit and push — form submissions now go to your Formspree dashboard

### Option B: Google Forms Embed

If you prefer Google Forms:
1. Create a Google Form with matching fields
2. Replace the `<form>` section in `index.html` with your embedded form

### Fallback Behavior

If Formspree isn't configured, the form shows a friendly message and a mailto: link so users can still reach you. Update the fallback email in `form.js`:

```javascript
const FALLBACK_EMAIL = 'hello@gapuniversity.com';
```

---

## Content Editing

### Event Date

Update the AI 101 talk date in `index.html`. Search for this comment:

```html
<!-- EDIT HERE: Update event date when confirmed -->
```

Change `Date coming soon` to your actual date/time.

### Spencer's Bio

Update the bio in `index.html`. Search for:

```html
<!-- EDIT HERE: Replace placeholder bio below -->
```

### Contact Email

Update the footer email in `index.html` and the fallback email in `form.js`.

---

## QR Code

The QR code points to: `https://blk911.github.io/gapuniv/`

### Regenerate QR Code

If you change to a custom domain:

```bash
# Install dependencies (one time)
pip3 install qrcode[pil] pillow

# Generate with default URL
python3 scripts/generate-qr.py

# Or specify a custom URL
python3 scripts/generate-qr.py --url "https://yourdomain.com"
```

The QR code is saved to `assets/qr-code.png`.

---

## Printable Cards

A print-ready sheet of 10 business-card-sized QR cards is included for posting around town.

### Files

- `print/qr-cards.html` — Source HTML (edit here to change card text)
- `print/qr-cards.pdf` — Ready-to-print PDF

### Regenerate PDF

```bash
python3 scripts/generate-pdf.py
```

Or open `print/qr-cards.html` in a browser and use Print → Save as PDF.

### Printing Tips

- **Paper:** US Letter (8.5" x 11")
- **Scale:** Print at 100% (do not "fit to page")
- **Stock:** Use cardstock for durability
- **Quantity:** Each sheet has 10 cards. For 1,000 cards, print 100 sheets.
- **Cut:** Follow the dashed lines

---

## File Structure

```
├── index.html          # Main website
├── styles.css          # All styles
├── form.js             # Form handling logic
├── favicon.svg         # Browser favicon
├── og-image.png        # Social sharing image
├── assets/
│   └── qr-code.png     # Generated QR code
├── print/
│   ├── qr-cards.html   # Printable card sheet source
│   └── qr-cards.pdf    # Ready-to-print PDF
├── scripts/
│   ├── generate-qr.py      # QR code generator
│   ├── generate-pdf.py     # PDF generator
│   └── generate-og-image.py # OG image generator
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Pages deployment
```

---

## Custom Domain

To use a custom domain (e.g., `gapuniversity.com`):

1. Add a `CNAME` file to the repo with your domain:
   ```
   gapuniversity.com
   ```

2. Configure DNS with your domain registrar:
   - For apex domain: Add A records pointing to GitHub's IPs
   - For subdomain: Add CNAME pointing to `blk911.github.io`

3. In repo Settings → Pages → Custom domain, enter your domain

4. Regenerate the QR code with the new URL:
   ```bash
   python3 scripts/generate-qr.py --url "https://gapuniversity.com"
   ```

5. Regenerate the PDF and commit changes

---

## Development

The site is static HTML/CSS/JS — no build step required.

To preview locally:
```bash
# Python
python3 -m http.server 8000

# Node
npx serve .
```

Then open http://localhost:8000

---

## Tech Notes

- **Mobile-first:** Designed for QR code scanning on phones
- **Fast:** No frameworks, minimal dependencies, ~50KB total
- **Accessible:** Semantic HTML, skip links, proper labels
- **SEO-ready:** Open Graph tags, meta descriptions, favicon

---

## License

© Gap University. All rights reserved.
