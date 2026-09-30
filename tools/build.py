#!/usr/bin/env python3
"""Static site generator. Run: python3 tools/build.py"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE, PHONE_T = "01902 471053", "01902471053"
EMAIL = "mariejaca@yahoo.com"
IG = "https://www.instagram.com/marieshairandbeautysalon/"
ADDR = "48 Victoria Street, Wolverhampton WV1 3PJ"
BASE = "https://maries-hair-and-beauty.vercel.app/"
MAPS = "https://www.google.com/maps/search/?api=1&query=48+Victoria+Street+Wolverhampton+WV1+3PJ"

ARROW = '<svg class="ar" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'

SERVICES = [
    ("Hair Cuts", "Sharp, clean cuts, fades and trims for everyone. Tell us the look you want and we'll shape it to suit you.", "Hair Cut"),
    ("Braids & Knotless", "Box braids, knotless braids and protective styles, neat at the root and made to last.", "Braids / Knotless"),
    ("Cornrows & Twists", "From simple and sleek to full statement patterns, every line parted with care.", "Cornrows / Twists"),
    ("Hair Styling", "Blow-dries, sleek finishes, curls and occasion hair for the days that matter.", "Hair Styling"),
    ("Colour & Highlights", "Rich colour, bright highlights and finishing touches that make your style glow.", "Colouring / Highlights"),
    ("Hair Treatments", "Nourishing treatments that keep your hair healthy, strong and ready to grow.", "Hair Treatment"),
]


WORKS = {
    "bob": ("Sleek bob with top knot", "Sleek side-parted bob with a small top knot against the flower wall"),
    "braids": ("Stitch braids & bun", "Neat stitch braids finished in a high bun"),
    "curls": ("Defined curls", "Soft defined curls against the flower wall"),
    "bantu": ("Bantu knots", "Slicked-back style with three bantu knots"),
    "locs": ("Loc maintenance", "Loc retwist with honey-brown tips"),
}


def photo(k, cls="", lazy=True):
    cap, alt = WORKS[k]
    return (f'<img class="{cls}" src="img/work-{k}.jpg" alt="{alt}" '
            f'{"loading=lazy " if lazy else ""}decoding="async">')


def q(v):
    return v.replace(" ", "%20").replace("&", "%26").replace("/", "%2F")


NAV = [("services.html", "Services"), ("gallery.html", "Gallery"), ("offers.html", "Offers"),
       ("careers.html", "Careers"), ("contact.html", "Contact")]


def page(fname, title, desc, body, hero, script=""):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' class="on"' if h == fname else "", t) for h, t in NAV)
    mob = "".join('<a href="%s" style="--i:%d">%s</a>' % (h, i, t) for i, (h, t) in enumerate([("index.html", "Home")] + NAV))
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0c0709">
<link rel="canonical" href="{BASE}{'' if fname == 'index.html' else fname}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Marie's Hair &amp; Beauty">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{BASE}{'' if fname == 'index.html' else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Marie's Hair &amp; Beauty: Look Good. Feel Good. Be You.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}img/og-image.jpg">
<meta name="apple-mobile-web-app-title" content="Marie's">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="img/favicon-192.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Manrope:wght@300..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HairSalon","name":"Marie's Hair & Beauty","telephone":"+441902471053","email":"{EMAIL}","url":"{BASE}","logo":"{BASE}img/icon-512.png","image":"{BASE}img/og-image.jpg","sameAs":["{IG}"],"address":{{"@type":"PostalAddress","streetAddress":"48 Victoria Street","addressLocality":"Wolverhampton","postalCode":"WV1 3PJ","addressCountry":"GB"}}}}</script>
</head>
<body class="pg-{fname.split('.')[0]}">
<div class="grain" aria-hidden="true"></div><div class="prog" aria-hidden="true"></div>
<header class="hdr" id="hdr">
  <a class="logo" href="index.html" aria-label="Marie's Hair &amp; Beauty, home"><img src="img/logo.png" alt="" width="44" height="44"><span>Marie's<small>Hair &amp; Beauty</small></span></a>
  <nav class="links" aria-label="Main">{links}</nav>
  <a class="btn sm" href="book.html" data-mag>Book now</a>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<div class="mnav" id="mnav" aria-hidden="true">{mob}<a class="mbook" href="book.html" style="--i:7">Book now {ARROW}</a>
<p style="--i:8"><a href="tel:{PHONE_T}">{PHONE}</a><br>{ADDR}</p></div>
{hero}
<main id="main">
{body}
</main>
<section class="cta dark">
  <div class="wrap">
    <p class="eyebrow" data-r>Ready when you are</p>
    <a class="mega" href="book.html" data-r><span>Book your</span> <em>style</em> {ARROW}</a>
  </div>
  <div class="marq sm" aria-hidden="true"><div><span>Look Good</span><span>Feel Good</span><span>Be You</span><span>Look Good</span><span>Feel Good</span><span>Be You</span><span>Look Good</span><span>Feel Good</span><span>Be You</span><span>Look Good</span><span>Feel Good</span><span>Be You</span></div></div>
</section>
<footer class="foot dark">
  <div class="wrap fgrid">
    <div><a class="logo" href="index.html"><img src="img/logo.png" alt="" width="52" height="52"><span>Marie's<small>Hair &amp; Beauty</small></span></a>
      <p class="mut">Unisex hair salon for all hair types.<br>Wolverhampton.</p></div>
    <div><h4>Visit</h4><p><a href="{MAPS}" target="_blank" rel="noopener">48 Victoria Street<br>Wolverhampton<br>WV1 3PJ</a></p></div>
    <div><h4>Talk to us</h4><p><a href="tel:{PHONE_T}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{IG}" target="_blank" rel="noopener">@marieshairandbeautysalon</a></p></div>
    <div><h4>Explore</h4><p><a href="services.html">Services</a><br><a href="gallery.html">Gallery</a><br><a href="offers.html">Offers</a><br><a href="careers.html">Careers</a><br><a href="book.html">Book</a></p></div>
  </div>
  <p class="wrap copy">© <span id="yr"></span> Marie's Hair &amp; Beauty. All rights reserved.</p>
</footer>
<script src="site.js"></script>
{script}
</body>
</html>
"""


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)


def phero(eyebrow, title, sub, fx=True):
    return f"""<section class="phero dark">
  {'<canvas class="fx" aria-hidden="true"></canvas>' if fx else ''}<div class="veil"></div>
  <div class="wrap"><p class="eyebrow" data-r>{eyebrow}</p><h1 data-split>{title}</h1><p class="sub" data-r>{sub}</p></div>
</section>"""


# ============================================================== HOME
hero = f"""<section class="hero dark" id="top">
  <canvas class="fx" aria-hidden="true"></canvas><div class="veil"></div>
  <div class="wrap hgrid">
    <div class="hcopy">
      <p class="eyebrow" data-r>Unisex hair salon · All hair types · Wolverhampton</p>
      <h1 data-split>Look Good. <em>Feel Good.</em> Be You.</h1>
      <p class="lead" data-r data-d="3">Braids, knotless, cornrows, colour, cuts and more, in Marie's brand-new salon at 48 Victoria Street.</p>
      <div class="hcta" data-r data-d="4"><a class="btn" href="book.html" data-mag>Book appointment {ARROW}</a><a class="btn line" href="services.html" data-mag>Explore services</a></div>
    </div>
    <div class="hpics" aria-hidden="true">
      <figure class="arch a1" data-speed="-30">{photo("braids", lazy=False)}</figure>
      <figure class="arch a2" data-speed="40">{photo("bob", lazy=False)}</figure>
      <figure class="arch a3" data-speed="-55">{photo("curls", lazy=False)}</figure>
      <a class="seal" href="offers.html" data-mag aria-label="Re-grand opening offer: 10% off">
        <svg viewBox="0 0 200 200"><defs><path id="c" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs><text><textPath href="#c">RE-GRAND OPENING · 1ST OCTOBER 2026 · 14 DAYS · </textPath></text></svg>
        <b>10<small>%</small></b><span>off</span>
      </a>
    </div>
  </div>
  <a class="scroll" href="#intro" aria-label="Scroll down"><i></i>Scroll</a>
</section>"""

marq = "".join("<span>%s</span>" % t for t in ["Braids", "Knotless", "Cornrows", "Twists", "Hair Styling", "Colour", "Highlights", "Hair Cuts", "Treatments"] * 2)

svc_rows = "".join(f"""<li><a href="book.html?service={q(v)}"><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p><span class="go">Book {ARROW}</span></a></li>"""
                   for i, (t, d, v) in enumerate(SERVICES))

home = f"""
<section class="intro light" id="intro">
  <div class="wrap">
    <p class="eyebrow dk" data-r>Welcome to Marie's</p>
    <p class="statement" id="statement">Marie's is a unisex hair salon for every hair type. A place where braids are neat, colour is rich, and everyone walks out feeling exactly like themselves.</p>
  </div>
</section>

<div class="marq" aria-hidden="true"><div>{marq}</div></div>

<section class="services light" id="services">
  <div class="wrap">
    <div class="shead"><p class="eyebrow dk" data-r>What we do</p><h2 data-split>Services, done <em>beautifully.</em></h2></div>
    <ul class="slist">{svc_rows}</ul>
    <p class="more" data-r><a class="tlink" href="services.html">See all services {ARROW}</a></p>
  </div>
</section>

<section class="work dark">
  <div class="wrap">
    <div class="shead"><p class="eyebrow" data-r>Recent work</p><h2 data-split>Fresh from <em>the chair.</em></h2></div>
  </div>
  <div class="rail" id="rail" tabindex="0" aria-label="Recent work">
    {"".join(f'<figure data-tilt>{photo(k)}<figcaption>{WORKS[k][0]}</figcaption></figure>' for k in ("bob", "braids", "curls", "bantu", "locs"))}
    <a class="railend" href="gallery.html"><span>See the gallery</span>{ARROW}</a>
  </div>
</section>

<section class="offer" id="offer">
  <div class="wrap ogrid">
    <div>
      <p class="eyebrow" data-r>Re-Grand Opening · 1st October 2026</p>
      <h2 data-split>10% off any hairstyle. <em>For 14 days.</em></h2>
      <p class="lead" data-r>Celebrate with us. Styling, cuts, colouring, highlights and treatments, all 10% off when you book from 1st to 14th October.</p>
      <div class="cd" id="cd" aria-live="polite"></div>
      <a class="btn dk" href="book.html?offer=1" data-mag>Claim the offer {ARROW}</a>
    </div>
    <div class="big10" aria-hidden="true">10<small>%</small></div>
  </div>
</section>

<section class="steps light">
  <div class="wrap">
    <div class="shead"><p class="eyebrow dk" data-r>Booking</p><h2 data-split>Four steps. <em>That's it.</em></h2></div>
    <ol class="sgrid">
      <li data-r><b>01</b><h3>Choose</h3><p>Pick the service you'd like.</p></li>
      <li data-r data-d="1"><b>02</b><h3>Date</h3><p>Choose a day on the calendar.</p></li>
      <li data-r data-d="2"><b>03</b><h3>Time</h3><p>Select a time that suits you.</p></li>
      <li data-r data-d="3"><b>04</b><h3>Confirm</h3><p>Send your details. We'll confirm by phone or email.</p></li>
    </ol>
  </div>
</section>

<section class="visit dark">
  <div class="wrap vgrid">
    <div>
      <p class="eyebrow" data-r>Find us</p>
      <h2 data-split>48 Victoria Street, <em>Wolverhampton.</em></h2>
      <p class="lead" data-r>WV1 3PJ. Call us on <a href="tel:{PHONE_T}">{PHONE}</a> or send a message, and follow the latest styles on Instagram.</p>
      <div class="hcta" data-r><a class="btn" href="{MAPS}" target="_blank" rel="noopener" data-mag>Get directions {ARROW}</a><a class="btn line" href="contact.html" data-mag>Contact</a></div>
    </div>
    <a class="hire" href="careers.html" data-tilt data-r>
      <span class="pillt">We're hiring</span>
      <h3>Hairstylist,<br><em>join our team.</em></h3>
      <p>Competitive pay, flexible hours, training and a loyal client base.</p>
      <span class="go">View the role {ARROW}</span>
    </a>
  </div>
</section>
"""
write("index.html", page("index.html", "Marie's Hair & Beauty | Hair Salon in Wolverhampton",
      "Marie's Hair & Beauty: unisex hair salon for all hair types at 48 Victoria Street, Wolverhampton. Braids, knotless, cornrows, colour and cuts. Book online.",
      home, hero, script=""))

# ============================================================== SERVICES
big = "".join(f"""<article class="sv" data-r>
  <span class="n">0{i+1}</span>
  <div><h2>{t}</h2><p>{d}</p><p class="mut">Add notes on length, colour or inspiration when you book and we'll be ready for you.</p></div>
  <a class="btn" href="book.html?service={q(v)}" data-mag>Book {ARROW}</a></article>""" for i, (t, d, v) in enumerate(SERVICES))
body = f"""
<section class="light pad"><div class="wrap narrow0">{big}
  <div class="note" data-r><b>Opening offer</b> 10% off any hairstyle, 1st–14th October 2026. <a class="tlink" href="offers.html">See details {ARROW}</a></div>
  <p class="center mut" data-r>Not sure what you need? <a href="contact.html">Message us</a> or call <a href="tel:{PHONE_T}">{PHONE}</a> and we'll help you choose.</p>
</div></section>"""
write("services.html", page("services.html", "Services | Marie's Hair & Beauty",
      "Hair cuts, braids, knotless, cornrows, twists, styling, colour, highlights and treatments at Marie's Hair & Beauty, Wolverhampton.",
      body, phero("Services", "Every style, <em>every texture.</em>", "Unisex. All hair types. Done with care.")))

# ============================================================== GALLERY
tiles = "".join(f'<button class="gt" data-k="{k}" aria-label="View: {WORKS[k][0]}" data-r data-d="{i}">{photo(k)}<span>{WORKS[k][0]}</span></button>' for i, k in enumerate(("bob", "braids", "curls", "bantu", "locs")))
tiles += f'<a class="gt ig" href="{IG}" target="_blank" rel="noopener" data-r data-d="5"><em>More on</em><b>Instagram</b><small>@marieshairandbeautysalon</small>{ARROW}</a>'
body = f"""
<section class="light pad"><div class="wrap">
  <div class="masonry">{tiles}</div>
</div></section>
<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Photo viewer"><button class="lx" aria-label="Close">×</button><button class="lp" aria-label="Previous">‹</button><figure><img id="lbi" alt=""><figcaption id="lbc"></figcaption></figure><button class="ln" aria-label="Next">›</button></div>
"""
write("gallery.html", page("gallery.html", "Gallery | Marie's Hair & Beauty",
      "See recent braids, knotless, cornrows and styles from Marie's Hair & Beauty in Wolverhampton.",
      body, phero("Gallery", "Fresh from <em>the chair.</em>", "Real work from the salon, one client at a time."), script='<script src="gallery.js"></script>'))

# ============================================================== OFFERS
body = f"""
<section class="offer big" id="offer">
  <div class="wrap ogrid">
    <div>
      <p class="eyebrow" data-r>Re-Grand Opening</p>
      <h2 data-split>10% off any hairstyle. <em>14 days.</em></h2>
      <p class="lead" data-r>From 1st October 2026 at 48 Victoria Street, Wolverhampton.</p>
      <div class="cd" id="cd" aria-live="polite"></div>
      <a class="btn dk" href="book.html?offer=1" data-mag>Book with 10% off {ARROW}</a>
    </div>
    <div class="big10" aria-hidden="true">10<small>%</small></div>
  </div>
</section>
<section class="light pad"><div class="wrap two">
  <div data-r><h2 class="h2s">How it works</h2>
    <ol class="nlist"><li><b>Book online</b> for any date from 1st to 14th October 2026.</li><li>The booking form applies the offer to your request automatically.</li><li>We'll confirm your appointment by phone or email.</li></ol></div>
  <div data-r data-d="1"><h2 class="h2s">What's included</h2>
    <ul class="ticks"><li>Hair Styling</li><li>Hair Cuts</li><li>Colouring</li><li>Highlights</li><li>Hair Treatments</li></ul>
    <p class="mut">Questions about the offer? Call <a href="tel:{PHONE_T}">{PHONE}</a>.</p></div>
</div></section>"""
write("offers.html", page("offers.html", "Offers | Marie's Hair & Beauty",
      "Re-Grand Opening offer: 10% off any hairstyle for 14 days from 1st October 2026 at Marie's Hair & Beauty, Wolverhampton.",
      body, phero("Offers", "Celebrate with <em>us.</em>", "Our re-grand opening offer is live from 1st October.", fx=True)))

# ============================================================== CAREERS
body = f"""
<section class="light pad"><div class="wrap two">
  <div>
    <p class="lead dk" data-r>We're looking for a passionate, skilled and friendly hairstylist to be part of our growing salon family.</p>
    <h2 class="h2s" data-r>What we're looking for</h2>
    <ul class="ticks" data-r><li>Qualified and experienced (or strongly skilled and ready to grow)</li><li>Passion for hair, creativity and current trends</li><li>Great communication and customer service skills</li><li>Reliable, professional and a team player</li></ul>
    <h2 class="h2s" data-r>We offer</h2>
    <ul class="ticks" data-r><li>A supportive and friendly working environment</li><li>Competitive pay, plus commission or performance incentives</li><li>Flexible working hours (or discuss your availability)</li><li>Opportunities for ongoing training and development</li><li>A loyal client base and a beautiful salon space</li></ul>
  </div>
  <form class="card form" id="apply" novalidate data-r>
    <h2>Apply now</h2>
    <label>Full name<input name="name" required autocomplete="name"></label>
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>Email<input name="email" type="email" autocomplete="email"></label>
    <label>Experience &amp; availability<textarea name="msg" rows="4" placeholder="Tell us about your experience, qualifications and when you can work"></textarea></label>
    <p class="err" role="alert"></p>
    <button class="btn block" type="submit">Send application {ARROW}</button>
    <p class="mut sm">This opens your email app with your application ready to send to {EMAIL}. You can attach your CV or portfolio there.</p>
  </form>
</div></section>"""
write("careers.html", page("careers.html", "Careers | Marie's Hair & Beauty",
      "We're hiring a hairstylist at Marie's Hair & Beauty, Wolverhampton. Competitive pay, flexible hours, training and a loyal client base.",
      body, phero("Careers · We're hiring", "Hairstylist. <em>Join our team.</em>", "Grow with a friendly, ambitious salon."),
      script='<script>mailForm("apply","Hairstylist application",["name","phone","email","msg"],{name:"Name",phone:"Phone",email:"Email",msg:"Experience & availability"})</script>'))

# ============================================================== CONTACT
body = f"""
<section class="light pad"><div class="wrap">
  <div class="ccards">
    <a href="tel:{PHONE_T}" data-r><span>Call</span><b>{PHONE}</b>{ARROW}</a>
    <a href="mailto:{EMAIL}" data-r data-d="1"><span>Email</span><b>{EMAIL}</b>{ARROW}</a>
    <a href="{MAPS}" target="_blank" rel="noopener" data-r data-d="2"><span>Visit</span><b>48 Victoria Street, WV1 3PJ</b>{ARROW}</a>
    <a href="{IG}" target="_blank" rel="noopener" data-r data-d="3"><span>Instagram</span><b>@marieshairandbeautysalon</b>{ARROW}</a>
  </div>
  <div class="two cgrid">
    <div class="map" data-r><iframe title="Map to Marie's Hair &amp; Beauty" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=48+Victoria+Street+Wolverhampton+WV1+3PJ&amp;output=embed"></iframe></div>
    <form class="card form" id="msgf" novalidate data-r data-d="1">
      <h2>Send a message</h2>
      <label>Name<input name="name" required autocomplete="name"></label>
      <label>Phone or email<input name="contact" required></label>
      <label>Message<textarea name="msg" rows="4" required></textarea></label>
      <p class="err" role="alert"></p>
      <button class="btn block" type="submit">Send message {ARROW}</button>
    </form>
  </div>
</div></section>"""
write("contact.html", page("contact.html", "Contact | Marie's Hair & Beauty",
      "Find Marie's Hair & Beauty at 48 Victoria Street, Wolverhampton WV1 3PJ. Call 01902 471053 or email to book.",
      body, phero("Contact", "Let's talk <em>hair.</em>", "We'd love to hear from you.", fx=True),
      script='<script>mailForm("msgf","Website enquiry",["name","contact","msg"],{name:"Name",contact:"Contact",msg:"Message"})</script>'))

# ============================================================== BOOK
opts = "".join(f'<button type="button" class="opt" data-v="{v}"><b>0{i+1}</b><span>{t}</span></button>' for i, (t, d, v) in enumerate(SERVICES))
opts += '<button type="button" class="opt" data-v="Not sure, advise me"><b>07</b><span>Not sure yet</span></button>'
body = f"""
<section class="light pad booking"><div class="wrap bgrid">
  <div class="bsteps" id="bk">
    <section class="bs open" id="s1" data-s="0"><header><i>1</i><h2>Service</h2><button class="edit" type="button">Change</button></header>
      <div class="bbody"><div class="opts">{opts}</div></div></section>
    <section class="bs" id="s2" data-s="1"><header><i>2</i><h2>Date</h2><button class="edit" type="button">Change</button></header>
      <div class="bbody"><div class="cal"><div class="calh"><button type="button" id="cprev" aria-label="Previous month">‹</button><b id="cmonth"></b><button type="button" id="cnext" aria-label="Next month">›</button></div>
      <div class="cdow"><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span></div><div class="cgrid2" id="cdays"></div>
      <p class="mut sm"><i class="dot"></i> Opening offer: 10% off (1–14 Oct 2026)</p></div></div></section>
    <section class="bs" id="s3" data-s="2"><header><i>3</i><h2>Time</h2><button class="edit" type="button">Change</button></header>
      <div class="bbody"><div class="times" id="times"></div><p class="mut sm">Times are requests. We'll confirm availability with you.</p></div></section>
    <section class="bs" id="s4" data-s="3"><header><i>4</i><h2>Your details</h2></header>
      <div class="bbody"><form class="form" id="df" novalidate>
        <div class="row2"><label>Full name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel" placeholder="07xxx xxxxxx"></label></div>
        <label>Email <small>(optional)</small><input name="email" type="email" autocomplete="email"></label>
        <label>Notes <small>(style, length, colour, inspiration)</small><textarea name="notes" rows="3"></textarea></label>
        <label class="chk"><input type="checkbox" id="rem" checked> Remember my details on this device</label>
      </form></div></section>
  </div>
  <aside class="bsum" id="bsum">
    <h3>Your appointment</h3>
    <dl><div><dt>Service</dt><dd id="v-s">Choose a service</dd></div><div><dt>Date</dt><dd id="v-d">Pick a date</dd></div><div><dt>Time</dt><dd id="v-t">Select a time</dd></div><div id="v-o" hidden><dt>Offer</dt><dd>10% opening discount</dd></div></dl>
    <p class="err" id="err" role="alert"></p>
    <button class="btn block" id="go" type="button" disabled>Request booking {ARROW}</button>
    <p class="mut sm">We'll confirm by phone or email. Prefer to talk? <a href="tel:{PHONE_T}">{PHONE}</a></p>
  </aside>
</div></section>
<div class="modal" id="done" hidden><div class="mbox">
  <div class="tick"><svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg></div>
  <h2>Request ready to send</h2><p id="dmsg"></p><dl id="dsum"></dl>
  <p class="mut sm">Your email app should have opened with the booking ready. Press <b>Send</b> to finish. If it didn't open, use the button below.</p>
  <a class="btn block" id="mailbtn" href="#">Send booking email {ARROW}</a>
  <button class="btn line block" id="icsbtn" type="button">Add to my calendar</button>
  <a class="tlink" href="book.html">Make another booking</a>
</div></div>"""
write("book.html", page("book.html", "Book Appointment | Marie's Hair & Beauty",
      "Book your hair appointment online at Marie's Hair & Beauty, Wolverhampton. Choose a service, date and time.",
      body, phero("Book", "Your chair <em>is waiting.</em>", "Choose a service, pick a day, select a time. It takes under a minute.", fx=True),
      script='<script src="book.js"></script>'))
print("built")
