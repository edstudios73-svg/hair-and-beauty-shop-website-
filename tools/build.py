#!/usr/bin/env python3
"""Generates the static pages. Run: python3 tools/build.py"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHONE, PHONE_T = "01902 471053", "01902471053"
EMAIL = "mariejaca@yahoo.com"
IG = "https://www.instagram.com/marieshairandbeautysalon/"
ADDR = "48 Victoria Street, Wolverhampton WV1 3PJ"
MAPS = "https://www.google.com/maps/search/?api=1&query=48+Victoria+Street+Wolverhampton+WV1+3PJ"

def svg(d, extra=""):
    return ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" %s>%s</svg>' % (extra, d))

ICONS = {
    "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.6 7.6L20 18M8.6 16.4L20 6"/>',
    "braid": '<path d="M8 3c4 3-4 6 0 9s-4 6 0 9M16 3c-4 3 4 6 0 9s4 6 0 9"/><path d="M12 3v18" opacity=".5"/>',
    "comb": '<path d="M3 8h18v4H3z"/><path d="M6 12v6M9 12v6M12 12v6M15 12v6M18 12v6"/>',
    "sparkle": '<path d="M12 3l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.500 6-11 6-11z"/>',
    "heart": '<path d="M12 20s-8-5-8-11a4.500 4.500 0 0 1 8-2.500A4.500 4.500 0 0 1 20 9c0 6-8 11-8 11z"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "phone": '<path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.500"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="1.500"/><path d="M21 16l-5-5-9 9"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "check": '<path d="M5 12.500l4.500 4.500L19 7"/>',
    "insta": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.500" cy="6.500" r=".8" fill="currentColor"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "gift": '<rect x="3" y="8" width="18" height="4"/><path d="M5 12v9h14v-9M12 8v13"/><path d="M12 8c-3 0-4-4-1-4 2 0 1 4 1 4zm0 0c3 0 4-4 1-4-2 0-1 4-1 4z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "star": '<path d="M12 3l2.800 5.800 6.200.9-4.500 4.400 1.100 6.200L12 17.300 6.400 20.300l1.100-6.200L3 9.700l6.200-.9z"/>',
    "users": '<circle cx="9" cy="8" r="3.500"/><path d="M2 20a7 7 0 0 1 14 0"/><path d="M16 4.500a3.500 3.500 0 0 1 0 7M18 14a7 7 0 0 1 4 6"/>',
    "send": '<path d="M21 3L10 14M21 3l-7 18-4-7-7-4z"/>',
    "download": '<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
}

def ic(name, cls=""):
    return svg(ICONS[name], 'class="%s"' % cls if cls else "")

SERVICES = [
    ("Hair Cuts", "scissors", "Clean cuts, fades and trims for men and women.", "Hair Cut"),
    ("Braids & Knotless", "braid", "Box braids, knotless braids and protective styles that last.", "Braids / Knotless"),
    ("Cornrows & Twists", "comb", "Neat, creative cornrows and twists, from simple to statement.", "Cornrows / Twists"),
    ("Hair Styling", "sparkle", "Blow-dries, sleek styles, curls and occasion hair.", "Hair Styling"),
    ("Colouring & Highlights", "drop", "Rich colour, highlights and finishing touches.", "Colouring / Highlights"),
    ("Hair Treatments", "heart", "Nourishing treatments to keep your hair healthy and growing.", "Hair Treatment"),
]

NAV = [("index.html", "Home", "home"), ("services.html", "Services", "scissors"),
       ("book.html", "Book", "calendar"), ("gallery.html", "Gallery", "image"),
       ("contact.html", "Contact", "user")]
DESK_NAV = [("index.html", "Home"), ("services.html", "Services"), ("gallery.html", "Gallery"),
            ("offers.html", "Offers"), ("careers.html", "Careers"), ("contact.html", "Contact")]


BACK = ('<a class="back" href="index.html" onclick="if(history.length>1){history.back();return false}" aria-label="Back">' + svg('<path d="M15 5l-7 7 7 7"/>') + '</a>')


def page(fname, title, desc, body, active, hero=None, script="", back=False):
    desk = "".join('<a href="%s"%s>%s</a>' % (h, ' class="on"' if h == fname else "", t) for h, t in DESK_NAV)
    tabs = "".join('<a href="%s" class="%s%s">%s<span>%s</span></a>' % (
        h, "on" if h == active else "", " mid" if h == "book.html" else "", ic(i), t) for h, t, i in NAV)
    hero_html = hero or ""
    back_html = BACK if back else ""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#c2185b">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/braids.jpg">
<link rel="icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body class="p-{fname.split('.')[0]}">
<header class="top">
  <div class="top-in">
    {back_html}
    <a class="brand" href="index.html"><img src="img/logo.png" alt="" width="40" height="40"><span>Marie's <b>Hair &amp; Beauty</b></span></a>
    <nav class="desk">{desk}</nav>
    <a class="btn sm" href="book.html">Book Appointment</a>
  </div>
</header>
{hero_html}
<main>
{body}
</main>
<footer class="foot">
  <div class="foot-in">
    <div><a class="brand" href="index.html"><img src="img/logo.png" alt="" width="44" height="44"><span>Marie's <b>Hair &amp; Beauty</b></span></a>
    <p>Unisex hair salon · All hair types</p></div>
    <div><h4>Visit</h4><p><a href="{MAPS}" target="_blank" rel="noopener">{ADDR}</a></p></div>
    <div><h4>Contact</h4><p><a href="tel:{PHONE_T}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <div><h4>Explore</h4><p><a href="services.html">Services</a> · <a href="gallery.html">Gallery</a> · <a href="offers.html">Offers</a> · <a href="careers.html">Careers</a> · <a href="{IG}" target="_blank" rel="noopener">Instagram</a></p></div>
  </div>
  <p class="copy">© <span id="yr"></span> Marie's Hair &amp; Beauty · Wolverhampton</p>
</footer>
<nav class="tabbar" aria-label="Main">{tabs}</nav>
<script src="app.js"></script>
{script}
</body>
</html>
"""


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)


def svc_chip_grid():
    return "".join('<a class="svc" href="book.html?service=%s"><i>%s</i><span>%s</span></a>' % (
        v.replace(" ", "%20").replace("&", "%26").replace("/", "%2F"), ic(i), t.split(" &")[0])
        for t, i, _, v in SERVICES)

# ---------------------------------------------------------------- HOME
hero = f"""
<section class="hero">
  <div class="hero-in">
    <div class="hero-txt">
      <p class="hi">Welcome to</p>
      <h1>Marie's Hair &amp; Beauty <em>— Your Salon, Your Schedule</em></h1>
      <p class="lead">Unisex hair salon for all hair types at 48 Victoria Street, Wolverhampton. Braids, knotless, cornrows, colour, cuts and more.</p>
      <a class="search" href="book.html">{ic("calendar")}<span>Book your style in under a minute</span><b>{ic("arrow")}</b></a>
      <div class="hero-cta"><a class="btn gold" href="book.html">Get Started</a><a class="btn ghost-w" href="tel:{PHONE_T}">{ic("phone")} Call us</a></div>
    </div>
    <div class="hero-pics" aria-hidden="true">
      <img class="p1" src="img/cornrow.jpg" alt=""><img class="p2" src="img/braids.jpg" alt=""><img class="p3" src="img/curls.jpg" alt="">
    </div>
  </div>
</section>"""

home = f"""
<section class="wrap sec">
  <div class="sec-h"><h2>Special Offers</h2><a href="offers.html">See All {ic("arrow")}</a></div>
  <a class="offer-card" href="offers.html">
    <div>
      <small>Re-Grand Opening · 1st October 2026</small>
      <h3>Get <span>10% off</span> any hairstyle for 14 days</h3>
      <div class="cd" id="cd" aria-live="polite"></div>
      <span class="btn gold sm">Claim offer</span>
    </div>
    <div class="off-badge"><b>10%</b><span>OFF</span></div>
  </a>
</section>

<section class="wrap sec">
  <div class="sec-h"><h2>Services</h2><a href="services.html">See All {ic("arrow")}</a></div>
  <div class="svc-row">{svc_chip_grid()}</div>
</section>

<section class="wrap sec">
  <div class="sec-h"><h2>Our Recent Work</h2><a href="gallery.html">See All {ic("arrow")}</a></div>
  <div class="hscroll">
    <a href="gallery.html"><img src="img/braids.jpg" alt="Knotless braids with gold highlights" loading="lazy"></a>
    <a href="gallery.html"><img src="img/curls.jpg" alt="Defined natural curls" loading="lazy"></a>
    <a href="gallery.html"><img src="img/cornrow.jpg" alt="Braided updo" loading="lazy"></a>
    <a href="gallery.html"><img src="img/sleek.jpg" alt="Sleek neat style" loading="lazy"></a>
  </div>
</section>

<section class="wrap sec">
  <div class="sec-h"><h2>Why Marie's</h2></div>
  <div class="feat">
    <div>{ic("users")}<h3>Unisex</h3><p>Men and women are both welcome.</p></div>
    <div>{ic("heart")}<h3>All hair types</h3><p>Skilled with every texture, length and style.</p></div>
    <div>{ic("calendar")}<h3>Easy booking</h3><p>Pick a service, date and time online.</p></div>
    <div>{ic("pin")}<h3>Find us easily</h3><p>48 Victoria Street, Wolverhampton WV1 3PJ.</p></div>
  </div>
</section>

<section class="wrap sec">
  <div class="promo">
    <div><small>We're Hiring</small><h3>Hairstylist — join our team</h3><p>Passionate, skilled and friendly? Come and grow with us.</p></div>
    <a class="btn" href="careers.html">View role</a>
  </div>
</section>
<div class="sticky-cta"><a class="btn block" href="book.html">Book Appointment</a></div>
"""
write("index.html", page("index.html", "Marie's Hair & Beauty | Hair Salon in Wolverhampton",
      "Marie's Hair & Beauty — unisex hair salon for all hair types at 48 Victoria Street, Wolverhampton. Braids, knotless, cornrows, colour, cuts. Book online.",
      home, "index.html", hero=hero))

# ---------------------------------------------------------------- SERVICES
cards = "".join(f"""<article class="lcard"><i>{ic(i)}</i><div><h3>{t}</h3><p>{d}</p></div>
<a class="btn sm" href="book.html?service={v.replace(' ', '%20').replace('&', '%26').replace('/', '%2F')}">Book</a></article>""" for t, i, d, v in SERVICES)
body = f"""
<section class="wrap sec">
  <div class="pagehead"><h1>Our Services</h1><p>Unisex. All hair types. Every style done with care.</p></div>
  <div class="list">{cards}</div>
  <div class="note-card">{ic("gift")}<p><b>Opening offer:</b> 10% off any hairstyle from 1st to 14th October 2026. <a href="offers.html">Details</a></p></div>
  <p class="mut center">Not sure what you need? <a href="contact.html">Message us</a> or call <a href="tel:{PHONE_T}">{PHONE}</a> and we'll advise.</p>
</section>
<div class="sticky-cta"><a class="btn block" href="book.html">Book Appointment</a></div>
"""
write("services.html", page("services.html", "Services | Marie's Hair & Beauty",
      "Hair cuts, braids, knotless, cornrows, styling, colouring, highlights and treatments at Marie's Hair & Beauty, Wolverhampton.", body, "services.html", back=True))

# ---------------------------------------------------------------- GALLERY
g = [("braids.jpg", "Knotless braids with gold highlights", "tall"), ("curls.jpg", "Defined natural curls", ""),
     ("cornrow.jpg", "Braided updo", ""), ("sleek.jpg", "Sleek neat style", "tall")]
tiles = "".join(f'<button class="tile {c}" data-i="{n}" aria-label="Open photo: {a}"><img src="img/{f}" alt="{a}" loading="lazy"></button>'
                for n, (f, a, c) in enumerate(g))
body = f"""
<section class="wrap sec">
  <div class="pagehead"><h1>Gallery</h1><p>Fresh from the chair. More on <a href="{IG}" target="_blank" rel="noopener">@marieshairandbeautysalon</a></p></div>
  <div class="gal">{tiles}</div>
  <p class="center"><a class="btn ghost" href="{IG}" target="_blank" rel="noopener">{ic("insta")} See more on Instagram</a></p>
</section>
<div class="lb" id="lb" hidden><button class="lb-x" aria-label="Close">×</button><button class="lb-p" aria-label="Previous">‹</button><img id="lbi" alt=""><button class="lb-n" aria-label="Next">›</button></div>
<div class="sticky-cta"><a class="btn block" href="book.html">Book a style like this</a></div>
"""
lb = """<script>
(function(){var t=[].slice.call(document.querySelectorAll('.tile')),lb=document.getElementById('lb'),im=document.getElementById('lbi'),i=0;
function show(n){i=(n+t.length)%t.length;var s=t[i].querySelector('img');im.src=s.src;im.alt=s.alt;lb.hidden=false;document.body.style.overflow='hidden'}
function hide(){lb.hidden=true;document.body.style.overflow=''}
t.forEach(function(b,n){b.addEventListener('click',function(){show(n)})});
lb.querySelector('.lb-x').onclick=hide;lb.querySelector('.lb-p').onclick=function(){show(i-1)};lb.querySelector('.lb-n').onclick=function(){show(i+1)};
lb.addEventListener('click',function(e){if(e.target===lb)hide()});
document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)})})();
</script>"""
write("gallery.html", page("gallery.html", "Gallery | Marie's Hair & Beauty",
      "See recent braids, knotless, cornrows and styles from Marie's Hair & Beauty in Wolverhampton.", body, "gallery.html", script=lb, back=True))

# ---------------------------------------------------------------- OFFERS
body = f"""
<section class="wrap sec narrow">
  <div class="offer-card big">
    <div>
      <small>Re-Grand Opening</small>
      <h1>10% off <span>any hairstyle</span><br>for 14 days</h1>
      <p>Celebrate our re-opening at 48 Victoria Street with 10% off hair styling, cuts, colouring, highlights and treatments.</p>
      <div class="cd" id="cd" aria-live="polite"></div>
    </div>
    <div class="off-badge"><b>10%</b><span>OFF</span></div>
  </div>
  <div class="panel">
    <h2>How it works</h2>
    <ol class="steps">
      <li><b>Book online</b> for any date from 1st to 14th October 2026.</li>
      <li>The booking form applies the offer to your request automatically.</li>
      <li>We'll confirm your appointment by phone or email.</li>
    </ol>
    <h2>Included</h2>
    <ul class="ticks"><li>Hair Styling</li><li>Hair Cuts</li><li>Colouring</li><li>Highlights</li><li>Hair Treatments</li></ul>
    <p class="mut">Offer runs from 1st October 2026 for 14 days. Questions? Call <a href="tel:{PHONE_T}">{PHONE}</a>.</p>
  </div>
</section>
<div class="sticky-cta"><a class="btn block" href="book.html?offer=1">Claim 10% Off</a></div>
"""
write("offers.html", page("offers.html", "Offers | Marie's Hair & Beauty",
      "Re-Grand Opening offer: 10% off any hairstyle for 14 days from 1st October 2026 at Marie's Hair & Beauty, Wolverhampton.", body, "offers.html", back=True))

# ---------------------------------------------------------------- CAREERS
body = f"""
<section class="wrap sec narrow">
  <div class="pagehead"><small class="pill">We're hiring</small><h1>Hairstylist</h1><p>Join our team. We're looking for a passionate, skilled and friendly hairstylist to be part of our growing salon family.</p></div>
  <div class="two">
    <div class="panel"><h2>What we're looking for</h2><ul class="ticks">
      <li>Qualified and experienced (or strongly skilled and ready to grow)</li><li>Passion for hair, creativity and current trends</li>
      <li>Great communication and customer service skills</li><li>Reliable, professional and a team player</li></ul></div>
    <div class="panel"><h2>We offer</h2><ul class="ticks">
      <li>A supportive and friendly working environment</li><li>Competitive pay, plus commission or performance incentives</li>
      <li>Flexible working hours (or discuss your availability)</li><li>Opportunities for ongoing training and development</li>
      <li>A loyal client base and a beautiful salon space</li></ul></div>
  </div>
  <form class="panel form" id="apply" novalidate>
    <h2>Apply now</h2>
    <label>Full name<input name="name" required autocomplete="name"></label>
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>Email<input name="email" type="email" autocomplete="email"></label>
    <label>Experience &amp; availability<textarea name="msg" rows="4" placeholder="Tell us about your experience, qualifications and when you can work"></textarea></label>
    <p class="err" role="alert"></p>
    <button class="btn block" type="submit">Send application</button>
    <p class="mut small">This opens your email app with your application ready to send to {EMAIL}. You can also attach your CV or portfolio there.</p>
  </form>
</section>
"""
write("careers.html", page("careers.html", "Careers | Marie's Hair & Beauty",
      "We're hiring a hairstylist at Marie's Hair & Beauty, Wolverhampton. Competitive pay, flexible hours, training and a loyal client base.", body, "careers.html", back=True,
      script='<script>mailForm("apply","Hairstylist application",["name","phone","email","msg"],{name:"Name",phone:"Phone",email:"Email",msg:"Experience & availability"})</script>'))

# ---------------------------------------------------------------- CONTACT
body = f"""
<section class="wrap sec narrow">
  <div class="pagehead"><h1>Contact &amp; Location</h1><p>We'd love to hear from you.</p></div>
  <div class="quick">
    <a href="tel:{PHONE_T}">{ic("phone")}<b>Call</b><span>{PHONE}</span></a>
    <a href="mailto:{EMAIL}">{ic("mail")}<b>Email</b><span>{EMAIL}</span></a>
    <a href="{MAPS}" target="_blank" rel="noopener">{ic("pin")}<b>Directions</b><span>48 Victoria Street, WV1 3PJ</span></a>
    <a href="{IG}" target="_blank" rel="noopener">{ic("insta")}<b>Instagram</b><span>@marieshairandbeautysalon</span></a>
  </div>
  <div class="map"><iframe title="Map to Marie's Hair & Beauty" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=48+Victoria+Street+Wolverhampton+WV1+3PJ&amp;output=embed"></iframe></div>
  <form class="panel form" id="msgf" novalidate>
    <h2>Send us a message</h2>
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Phone or email<input name="contact" required></label>
    <label>Message<textarea name="msg" rows="4" required></textarea></label>
    <p class="err" role="alert"></p>
    <button class="btn block" type="submit">Send message</button>
  </form>
</section>
"""
write("contact.html", page("contact.html", "Contact | Marie's Hair & Beauty",
      "Find Marie's Hair & Beauty at 48 Victoria Street, Wolverhampton WV1 3PJ. Call 01902 471053 or email to book.", body, "contact.html", back=True,
      script='<script>mailForm("msgf","Website enquiry",["name","contact","msg"],{name:"Name",contact:"Contact",msg:"Message"})</script>'))

# ---------------------------------------------------------------- BOOK
chips = "".join(f'<button type="button" class="chip" data-v="{v}"><i>{ic(i)}</i><span>{t}</span></button>' for t, i, _, v in SERVICES)
body = f"""
<section class="wrap sec narrow booking" id="bk">
  <div class="pagehead"><h1>Book Appointment</h1><p>Four quick steps. We'll confirm your slot by phone or email.</p></div>
  <ol class="prog" id="prog"><li class="on">Service</li><li>Date</li><li>Time</li><li>Details</li></ol>

  <div class="step on" data-s="0">
    <h2>Choose a service</h2>
    <div class="chips">{chips}<button type="button" class="chip" data-v="Not sure, advise me"><i>{ic("star")}</i><span>Not sure</span></button></div>
  </div>
  <div class="step" data-s="1">
    <h2>Pick a date</h2>
    <p class="mut small" id="dnote"></p>
    <div class="dates" id="dates"></div>
  </div>
  <div class="step" data-s="2">
    <h2>Choose a time</h2>
    <div class="times" id="times"></div>
    <p class="mut small">Time slots are requests. We'll confirm availability with you.</p>
  </div>
  <div class="step" data-s="3">
    <h2>Your details</h2>
    <form class="form flat" id="df" novalidate>
      <label>Full name<input name="name" required autocomplete="name"></label>
      <label>Phone<input name="phone" type="tel" required autocomplete="tel" placeholder="07xxx xxxxxx"></label>
      <label>Email <small>(optional)</small><input name="email" type="email" autocomplete="email"></label>
      <label>Notes <small>(style, length, colour, anything we should know)</small><textarea name="notes" rows="3"></textarea></label>
      <label class="chk"><input type="checkbox" id="disc"> Apply the opening 10% discount (bookings 1–14 Oct 2026)</label>
      <label class="chk"><input type="checkbox" id="rem" checked> Remember my details on this device</label>
    </form>
  </div>
  <p class="err" id="err" role="alert"></p>

  <div class="summary" id="sum" hidden></div>
  <div class="bar"><button class="btn ghost" id="prev" type="button" hidden>Back</button><button class="btn block" id="next" type="button" disabled>Continue</button></div>

  <div class="done" id="done" hidden>
    <div class="tick">{ic("check")}</div>
    <h2>Request ready to send</h2>
    <p id="dmsg"></p>
    <div class="summary" id="dsum"></div>
    <p class="mut small">Your email app should have opened with the booking ready. Tap <b>Send</b> there to finish. If it didn't open, use the button below.</p>
    <a class="btn block" id="mailbtn" href="#">{ic("send")} Send booking email</a>
    <button class="btn ghost block" id="icsbtn" type="button">{ic("download")} Add to my calendar</button>
    <a class="btn ghost block" href="tel:{PHONE_T}">{ic("phone")} Call {PHONE}</a>
    <a class="link" href="book.html">Make another booking</a>
  </div>
</section>
"""
write("book.html", page("book.html", "Book Appointment | Marie's Hair & Beauty",
      "Book your hair appointment online at Marie's Hair & Beauty, Wolverhampton. Choose a service, date and time.", body, "book.html", back=True,
      script='<script src="book.js"></script>'))
print("built")
