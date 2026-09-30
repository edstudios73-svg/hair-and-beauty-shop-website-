#!/usr/bin/env python3
"""Regenerates favicons, app icons, manifest and the social share image from img/logo-source.png.
Run: python3 tools/make_assets.py"""
import json, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(R, *a)
l = Image.open(P("img", "logo-source.png")).convert("RGB")


def circle(im, size):
    im = im.resize((size, size), Image.LANCZOS).convert("RGBA")
    m = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    im.putalpha(m.resize((size, size), Image.LANCZOS))
    return im


circle(l, 512).save(P("img", "logo.png"), optimize=True)
for n, s in (("favicon-32", 32), ("favicon-192", 192), ("icon-512", 512)):
    circle(l, s).save(P("img", n + ".png"), optimize=True)
circle(l, 64).save(P("favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])


def on_bg(size, frac):
    c = Image.new("RGB", (size, size), (12, 7, 9))
    lg = circle(l, int(size * frac))
    c.paste(lg, ((size - lg.width) // 2, (size - lg.height) // 2), lg)
    return c


on_bg(180, .82).save(P("img", "apple-touch-icon.png"), optimize=True)
on_bg(512, .62).save(P("img", "icon-maskable-512.png"), optimize=True)

W, H = 1200, 630
g = Image.new("RGB", (W, H), (12, 7, 9))
d = ImageDraw.Draw(g)
d.ellipse((650, -200, 1400, 520), fill=(150, 20, 80))
d.ellipse((800, 250, 1300, 750), fill=(120, 90, 40))
g = g.filter(ImageFilter.GaussianBlur(120))
bg = Image.blend(Image.new("RGB", (W, H), (12, 7, 9)), g, .75)
ring = Image.new("RGBA", (336, 336), (0, 0, 0, 0))
ImageDraw.Draw(ring).ellipse((0, 0, 335, 335), outline=(216, 176, 106, 255), width=4)
lg = circle(l, 300)
bg.paste(ring, (72, 147), ring)
bg.paste(lg, (90, 165), lg)
dr = ImageDraw.Draw(bg)
F = lambda p, s: ImageFont.truetype(p, s)
serif = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
ital = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
dr.text((460, 150), "HAIR SALON · WOLVERHAMPTON", font=F(sans, 22), fill=(216, 176, 106))
dr.text((456, 198), "Marie's", font=F(serif, 84), fill=(246, 239, 231))
dr.text((456, 292), "Hair & Beauty", font=F(serif, 84), fill=(246, 239, 231))
dr.text((460, 425), "Look Good. Feel Good. Be You.", font=F(ital, 44), fill=(240, 215, 155))
dr.rounded_rectangle((460, 500, 800, 562), radius=31, fill=(224, 36, 111))
dr.text((630, 531), "Book online", font=F(sans, 26), fill=(255, 255, 255), anchor="mm")
dr.text((830, 531), "All hair types · Unisex", font=F(sans, 22), fill=(200, 185, 190), anchor="lm")
bg.save(P("img", "og-image.jpg"), quality=88, optimize=True)

json.dump({"name": "Marie's Hair & Beauty", "short_name": "Marie's",
           "description": "Unisex hair salon for all hair types in Wolverhampton. Book online.",
           "start_url": "/", "scope": "/", "display": "standalone", "background_color": "#0c0709",
           "theme_color": "#0c0709", "lang": "en-GB",
           "icons": [{"src": "img/favicon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "img/icon-512.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "img/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]},
          open(P("site.webmanifest"), "w"), indent=1)
print("assets built")
