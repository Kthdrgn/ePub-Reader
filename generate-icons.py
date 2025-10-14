#!/usr/bin/env python3
"""
Simple PWA Icon Generator
Generates icon-192.png and icon-512.png for your PWA
No dependencies required beyond Python standard library!
"""

def create_icon_svg(size):
    """Create an SVG icon that can be converted to PNG"""
    scale = size / 192
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2563eb;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1e40af;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="{size}" height="{size}" fill="url(#bg)"/>
  
  <!-- Book outer -->
  <rect x="{50*scale}" y="{40*scale}" width="{92*scale}" height="{112*scale}" fill="white"/>
  
  <!-- Book inner -->
  <rect x="{55*scale}" y="{45*scale}" width="{82*scale}" height="{102*scale}" fill="#2563eb"/>
  
  <!-- Text lines -->
  <rect x="{65*scale}" y="{60*scale}" width="{30*scale}" height="{4*scale}" fill="white"/>
  <rect x="{65*scale}" y="{75*scale}" width="{50*scale}" height="{4*scale}" fill="white"/>
  <rect x="{65*scale}" y="{90*scale}" width="{50*scale}" height="{4*scale}" fill="white"/>
  <rect x="{65*scale}" y="{105*scale}" width="{40*scale}" height="{4*scale}" fill="white"/>
</svg>'''
    
    return svg

def save_svg(filename, content):
    """Save SVG content to file"""
    with open(filename, 'w') as f:
        f.write(content)
    print(f'✓ Created {filename}')

def main():
    print('🎨 Generating PWA Icons...\n')
    
    # Generate SVG icons
    svg_192 = create_icon_svg(192)
    svg_512 = create_icon_svg(512)
    
    save_svg('icon-192.svg', svg_192)
    save_svg('icon-512.svg', svg_512)
    
    print('\n✅ SVG icons generated!')
    print('\nTo convert to PNG, you can:')
    print('1. Use create-icons.html (open in browser)')
    print('2. Use an online converter: https://cloudconvert.com/svg-to-png')
    print('3. Use ImageMagick: convert icon-192.svg icon-192.png')
    print('4. Use Inkscape: inkscape icon-192.svg --export-png=icon-192.png')
    
    # Try to use PIL if available
    try:
        from PIL import Image, ImageDraw
        
        def create_png_icon(size):
            img = Image.new('RGB', (size, size))
            draw = ImageDraw.Draw(img)
            
            # Gradient background
            for y in range(size):
                r = int(37 + (30 - 37) * y / size)
                g = int(99 + (64 - 99) * y / size)
                b = int(235 + (175 - 235) * y / size)
                draw.line([(0, y), (size, y)], fill=(r, g, b))
            
            scale = size / 192
            
            # Book
            draw.rectangle([50*scale, 40*scale, 142*scale, 152*scale], fill='white')
            draw.rectangle([55*scale, 45*scale, 137*scale, 147*scale], fill='#2563eb')
            draw.rectangle([65*scale, 60*scale, 95*scale, 64*scale], fill='white')
            draw.rectangle([65*scale, 75*scale, 115*scale, 79*scale], fill='white')
            draw.rectangle([65*scale, 90*scale, 115*scale, 94*scale], fill='white')
            draw.rectangle([65*scale, 105*scale, 105*scale, 109*scale], fill='white')
            
            return img
        
        print('\n📸 PIL/Pillow found! Generating PNG icons...')
        icon_192 = create_png_icon(192)
        icon_192.save('icon-192.png', 'PNG')
        print('✓ Created icon-192.png')
        
        icon_512 = create_png_icon(512)
        icon_512.save('icon-512.png', 'PNG')
        print('✓ Created icon-512.png')
        
        print('\n✅ PNG icons generated successfully!')
        
    except ImportError:
        print('\n💡 Tip: Install Pillow for automatic PNG generation:')
        print('   pip install pillow')

if __name__ == '__main__':
    main()
