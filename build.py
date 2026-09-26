#!/usr/bin/env python3
"""
LA County North pools — a redesign proposal for four lacountypools.com sites and a hub
that ties them together. Our own design; each pool keeps its own links and map; every
schedule comes from Pool Relay. Run `python3 build.py`; commit the HTML it writes.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = "https://www.swimoutlet.com/lacitypools/"
MORE = "https://lacountypools.com"


def activenet(center):
    return ("https://anc.apm.activecommunities.com/losangelescounty/activity/search?onlineSiteId=0"
            f"&amp;days_of_week=0000000&amp;activity_select_param=2&amp;center_ids={center}&amp;viewMode=list")


FALL_SESSIONS = [
    ("Session 1", "August 24 &ndash; September 4", "August 22"),
    ("Session 2", "September 8 &ndash; September 18", "September 5"),
    ("Session 3", "September 21 &ndash; October 2", "September 19"),
    ("Session 4", "October 5 &ndash; October 16", "October 3"),
    ("Session 5", "October 19 &ndash; October 30", "October 17"),
    ("Session 6", "November 2 &ndash; November 13", "October 31"),
    ("Session 7", "November 16 &ndash; November 20", "November 14"),
    ("Saturday Session 1", "August 29 &ndash; October 31", "August 22"),
    ("Saturday Session 2", "November 7 &ndash; December 19", "October 31"),
]
SUMMER_SESSIONS = [
    ("Session 1", "June 8 &ndash; June 19", "June 6"),
    ("Session 2", "June 22 &ndash; July 3", "June 20"),
    ("Session 3", "July 6 &ndash; July 17", "July 4"),
    ("Session 4", "July 20 &ndash; July 31", "July 18"),
    ("Session 5", "August 3 &ndash; August 14", "August 1"),
    ("Sessions 6 and 7", "Extended summer, dates to be announced", "To be announced"),
]

FALL_PROGRAMS = [
    ("Lap Swim", "schedule.html", "<b>Mon&ndash;Fri</b> 6&ndash;11am and 4&ndash;8pm. <b>Sat</b> 8&ndash;11am.<br>Lap pass $80 for 30 swims or $15 for 5."),
    ("Swim Lessons", "lessons.html", "Parent and Child through Level 4, and adults. Two-week weekday sessions and a Saturday session.<br>$25 a session."),
    ("Rec Swim", "schedule.html", "<b>Mon&ndash;Fri</b> 3&ndash;4pm. <b>Sat</b> 12:30&ndash;4pm.<br>Free for all ages."),
    ("Water Exercise", "schedule.html", "<b>Mon&ndash;Fri</b> 6am, 7:30am and 6pm. <b>Sat</b> 8am.<br>Aquacise pass $35 a month."),
]
SUMMER_PROGRAMS = [
    ("Everybody Swims", "schedule.html", "<b>Mon&ndash;Fri</b> 12:30&ndash;2:30pm. <b>Sat</b> 12:30&ndash;4pm.<br>Free for all ages."),
    ("Lap Swim", "schedule.html", "<b>Mon&ndash;Fri</b> 4&ndash;6pm. <b>Sat</b> 8&ndash;9am.<br>Lap pass $80 for 30 swims or $15 for 5."),
    ("Water Exercise", "schedule.html", "<b>Mon&ndash;Fri</b> 11am&ndash;noon. <b>Sat</b> 8&ndash;9am.<br>Aquacise pass $35 a month."),
    ("Swim Lessons", "lessons.html", "Two-week sessions from June 8 to August 14, and Saturdays.<br>$25 a session."),
]

POOLS = {
    "castaic": dict(
        name="Castaic Aquatic Center", short="Castaic", open=True,
        tagline="Four outdoor pools and a splash pad in the hills above Santa Clarita. The 50-meter pool is closed for now; everything runs in the 25-yard pool.",
        address="31350 Castaic Rd", city="Castaic, CA 91384", phone="661-294-6467",
        site="https://castaic.lacountypools.com", lessons_path="/lessons-fall/", teams_path="/sports-fall/",
        register=activenet(263), weather="https://forecast7.com/en/34d49n118d63/castaic/?unit=us",
        map=("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3288.5565688976503!2d-118.61871102399219!3d34.48877169455426"
             "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c27edcbe774f2f%3A0x1fee1ec6793f1a5a!2sCastaic%20Sports%20Complex%20Aquatic%20Center"
             "!5e0!3m2!1sen!2sus!4v1698981544090!5m2!1sen!2sus"),
        views=dict(finder="94hllfke9HUuzUaHoB2ZZH", week="R07JQHtJ4XjdAAarm8ofK7", lessons="1MbB9BQQR4z5zvvAvSFLvW", teams="FeqLr6dg7dmWVv650PO6tv"),
        facts=[("6am", "Lap swim opens weekdays; 8am Saturday"), ("Free", "Rec swim for all ages, weekdays 3&ndash;4pm"),
               ("4 pools", "50-meter (closed for now), 10-lane 25-yard, 3-lane shallow, splash pad"), ("Aug 24&ndash;Nov 21", "Fall season. Closed Sundays")],
        programs=FALL_PROGRAMS + [("Team Sports", "team-sports.html", "Youth water polo weekdays 5&ndash;6pm, ages 7 to 17. Swim team, dive team and artistic swimming dates to be announced.")],
        season="Fall 2026, August 24 to November 21", sessions=FALL_SESSIONS, current="Session 3",
        teams=[("Water Polo", "Fall 2026, August 24 to November 20.<br>Monday to Friday, 5&ndash;6pm.", False),
               ("Swim Team", "Winter season.<br>Monday to Friday, 5&ndash;6pm.", False),
               ("Dive Team", "Dates and times to be announced.", True),
               ("Artistic Swimming", "Dates and times to be announced.", True)],
    ),
    "sanfernando": dict(
        name="San Fernando Aquatic Center", short="San Fernando", open=True,
        tagline="A 50-meter competition pool with 1- and 3-meter boards, and a warm instructional pool with a slide.",
        address="300 Park Ave", city="San Fernando, CA 91340", phone="818-256-2033",
        site="https://sanfernando.lacountypools.com", lessons_path="/lessons-fall/", teams_path="/team-sports-fall/",
        register=activenet(49), weather="https://forecast7.com/en/34d05n118d24/los-angeles/?unit=us",
        map=("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3595.11423469314!2d-118.43450277258847!3d34.280829031542986"
             "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c291b6aa6805ef%3A0xa67e36857df1f639!2sSan%20Fernando%20Regional%20Pool"
             "!5e0!3m2!1sen!2sus!4v1756409394462!5m2!1sen!2sus"),
        views=dict(finder="51DBIEYUIMoEN9jSRu9QDU", week="2QLmKqixBB7xGg7QSda3Cw", lessons="nTDzi9ulel4Ls5FN2bv2C7", teams="2QLmKqixBB7xGg7QSda3Cw"),
        facts=[("6am", "Lap swim opens weekdays; 8am Saturday"), ("Free", "Rec swim for all ages, weekdays 3&ndash;4pm"),
               ("2 pools", "50-meter competition and 25-yard instructional"), ("Aug 24&ndash;Nov 21", "Fall season. Closed Sundays")],
        programs=FALL_PROGRAMS + [("Team Sports", "team-sports.html", "Youth water polo weekdays 5&ndash;6pm through November 20. The winter swim team starts November 30.")],
        season="Fall 2026, August 24 to November 21", sessions=FALL_SESSIONS + [("Winter Session 1", "November 30 &ndash; December 11", "Listed in registration now")], current="Session 3",
        teams=[("Water Polo", "Fall 2026, August 24 to November 20.<br>Monday to Friday, 5&ndash;6pm.", False),
               ("Swim Team", "Winter season, November 30 to February 26.<br>Monday to Friday, 6&ndash;7pm.", False),
               ("Dive Team", "Dates and times to be announced.", True),
               ("Artistic Swimming", "Dates and times to be announced.", True)],
    ),
    "valverde": dict(
        name="Val Verde Pool", short="Val Verde", open=False,
        tagline="A summer pool in Val Verde Community Regional Park. Open June to mid-August.",
        address="30300 Arlington St", city="Castaic, CA 91384", phone="(661) 257-7639",
        site="https://valverde.lacountypools.com", lessons_path="/lessons/", teams_path="/team-sports/",
        register="https://reservations.lacounty.gov", weather=None,
        map=("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3290.2329696901834!2d-118.66453865850413!3d34.44623360544478"
             "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80c27f8462d29435%3A0xbb391d2a4e01c1ad!2sVal%20Verde%20Pool"
             "!5e0!3m2!1sen!2sus!4v1778730096253!5m2!1sen!2sus"),
        views=dict(week="XGRvzq5ali9AZda9vHERI8"),
        facts=[("Closed", "Until next summer"), ("Free", "Everybody Swims, weekdays 12:30&ndash;2:30pm"),
               ("4pm", "Summer lap swim on weekdays"), ("Jun 8&ndash;Aug 15", "Summer 2026 season")],
        programs=SUMMER_PROGRAMS + [("Team Sports", "team-sports.html", "Summer swim team, water polo and artistic swimming, ages 7 to 17.")],
        season="Summer 2026, June 8 to August 15", sessions=SUMMER_SESSIONS, current=None,
        teams=[("Swim Team", "Summer, June 8 to August 15.<br>Monday to Friday, 5&ndash;6pm.", False),
               ("Water Polo", "Summer, June 8 to August 15.<br>Monday to Friday, 6&ndash;7pm.", False),
               ("Artistic Swimming", "Summer, June 8 to August 15.<br>Monday to Friday, 3&ndash;4pm.", False)],
    ),
    "elcariso": dict(
        name="El Cariso Pool", short="El Cariso", open=False,
        tagline="A summer pool in El Cariso Community Regional Park in Sylmar. Open June to mid-August.",
        address="13100 Hubbard St", city="Sylmar, CA 91342", phone="(818) 362-4686",
        site="https://elcariso.lacountypools.com", lessons_path="/lessons/", teams_path="/team-sports/",
        register="https://reservations.lacounty.gov", weather="https://forecast7.com/en/34d30n118d37/91342/?unit=us",
        map=("https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1362.291261489176!2d-118.4164323!3d34.3188275!3m2!1i1024!2i768"
             "!4f13.1!3m3!1m2!1s0x80c28e2214e2d745%3A0x7282ab96181b7941!2sEl%20Cariso%20Swimming%20Pool!5e1!3m2!1sen!2sus!4v1688067870182!5m2!1sen!2sus"),
        views=dict(week="WCpMrt0gqtcFBQcD85QAWQ"),
        facts=[("Closed", "Until next summer"), ("Free", "Everybody Swims, weekdays 12:30&ndash;2:30pm"),
               ("4pm", "Summer lap swim on weekdays"), ("Jun 8&ndash;Aug 15", "Summer 2026 season")],
        programs=SUMMER_PROGRAMS + [("Team Sports", "team-sports.html", "Summer swim team, dive team, water polo and artistic swimming, ages 7 to 17.")],
        season="Summer 2026, June 8 to August 15", sessions=SUMMER_SESSIONS, current=None,
        teams=[("Artistic Swimming", "Summer, June 8 to August 15.<br>Monday to Friday, 3&ndash;4pm.", False),
               ("Dive Team", "Summer, June 8 to August 15.<br>Monday to Friday, 4&ndash;5pm.", False),
               ("Swim Team", "Summer, June 8 to August 15.<br>Monday to Friday, 5&ndash;6pm.", False),
               ("Water Polo", "Summer, June 8 to August 15.<br>Monday to Friday, 6&ndash;7pm.", False)],
    ),
}
ORDER = ["castaic", "sanfernando", "valverde", "elcariso"]
NORTH = dict(day="FQH3HlrKj7t2dK5m0r9KXm", week="HTFHUTye6wQpQ71YFfSm2r")


def cal(token, title, cls=""):
    return f"""<div class="cal {cls}"><iframe width="100%" height="640" src="https://www.poolrelay.com/embed/{token}" title="{title}" loading="lazy"></iframe></div>
    <p class="capt">Updated live from the pool's schedule. <a href="https://www.poolrelay.com/v/{token}" target="_blank" rel="noopener">Open it full screen</a>.</p>"""


def head(title, desc, root, photo):
    return f"""<!DOCTYPE html>
<!-- UNOFFICIAL PREVIEW. A redesign proposal, not a Los Angeles County website. Generated by build.py. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
</head>
<body style="--photo:url('{photo}')"><!-- the photo path is relative to style.css at the site root -->
<div class="ribbon"><b>Unofficial preview.</b> A redesign proposal for LA County's
  <a href="{MORE}" target="_blank" rel="noopener">lacountypools.com</a> sites, not a Los Angeles County page.
  Schedules by <a href="https://www.poolrelay.com" target="_blank" rel="noopener">Pool Relay</a>.</div>
"""


def pool_page(key, slug, title, desc, body, scripts=""):
    P = POOLS[key]

    def nav(href, label):
        cur = ' aria-current="page"' if href == slug else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    nearby = "".join(f'<li><a href="../{k}/index.html">{POOLS[k]["name"]}</a></li>' for k in ORDER if k != key)
    weather = f'<li><a href="{P["weather"]}" target="_blank" rel="noopener">Weather</a></li>' if P["weather"] else ""
    return head(title, desc, "../", f"{key}/pool.jpg") + f"""
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html">{P["name"]}<small>Swim, play, compete</small></a>
    <nav aria-label="Main">
      {nav("index.html", "Home")}
      {nav("schedule.html", "Schedule")}
      {nav("lessons.html", "Lessons")}
      {nav("team-sports.html", "Team Sports")}
      <a href="{STORE}" target="_blank" rel="noopener">Swim Store</a>
      <a href="../index.html">More Pools</a>
      <a class="register" href="{P["register"]}" target="_blank" rel="noopener">Register</a>
    </nav>
  </div>
</header>

<main>
{body}
</main>

<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        <h3>{P["name"]}</h3>
        {P["address"]}, {P["city"]}<br>
        <a href="tel:{P["phone"]}">{P["phone"]}</a><br>
        {"Closed Sundays" if P["open"] else "Open in summer"}
      </div>
      <div>
        <h3>Nearby pools</h3>
        <ul>{nearby}<li><a href="../index.html">All North County pools</a></li></ul>
      </div>
      <div>
        <h3>LA County Pools</h3>
        <ul>
          <li><a href="{MORE}" target="_blank" rel="noopener">Find another pool</a></li>
          <li><a href="{STORE}" target="_blank" rel="noopener">Swim store</a></li>
          <li><a href="{P["register"]}" target="_blank" rel="noopener">Register online</a></li>
          {weather}
        </ul>
      </div>
    </div>
    <p class="fine">Unofficial preview built to show a redesign of <a href="{P["site"]}/" target="_blank" rel="noopener">{P["site"].replace("https://", "")}</a>.
    Not affiliated with Los Angeles County Parks and Recreation. Pool photo from lacountypools.com.</p>
  </div>
</footer>
{scripts}
</body>
</html>
"""


def rows(programs):
    out = []
    for name, href, hrs in programs:
        out.append(f"""      <a class="row" href="{href}">
        <h3>{name}</h3>
        <div class="hrs">{hrs}</div>
        <span class="go">See {name.lower()}</span>
      </a>""")
    return "\n".join(out)


def home(key):
    P = POOLS[key]
    closed = "The pool reopens next summer. Last summer's schedule is below." if not P["open"] else ""
    status = ('<span class="status open">Open Monday to Saturday</span>' if P["open"]
              else '<span class="status closed">Closed until next summer</span>')
    finder = (cal(P["views"]["finder"], P["name"] + ", one day") if "finder" in P["views"] else
              f'<p class="note">The calendar opens on this week, when the pool is closed. Use the arrows to step back to June, July or August.</p>'
              + cal(P["views"]["week"], P["name"] + ", summer schedule"))
    visit_weather = f'<dt>Weather</dt><dd><a href="{P["weather"]}" target="_blank" rel="noopener">Local forecast</a></dd>' if P["weather"] else ""
    facts = "".join(f"<div><b>{b}</b><span>{s}</span></div>" for b, s in P["facts"])
    return f"""
<section class="hero">
  <div class="pennants" aria-hidden="true"></div>
  <div class="wrap">
    <div>
      <h1>{P["name"]}</h1>
      <p class="tag">{P["tagline"]}</p>
      {status}
    </div>
    <div class="now" data-view="{P["views"]["week"]}" data-closed="{closed}" aria-live="polite">
      <h2><span class="dot" aria-hidden="true"></span><span class="label">In the water now</span></h2>
      <p class="when">Checking the schedule&hellip;</p>
      <ul></ul>
      <p class="foot"><a href="schedule.html">{"See the whole week" if P["open"] else "See last summer's schedule"}</a></p>
    </div>
  </div>
</section>

<div class="facts"><div class="wrap">{facts}</div></div>

<section class="block">
  <div class="wrap">
    <div class="intro">
      <h2>{"Find a swim time" if P["open"] else "Summer schedule"}</h2>
      <p>{"Everything in the water on one calendar. Pick a day, or use the Teams menu to show one program." if P["open"]
          else "Everything that ran in the pool last summer, from June 8 to August 15. Use the Teams menu to show one program."}</p>
    </div>
    {finder}
  </div>
</section>

<section class="block" style="padding-top:0">
  <div class="wrap">
    <h2>Programs</h2>
    <div class="lanes">
{rows(P["programs"])}
    </div>
  </div>
</section>

<hr class="rope">

<section class="block visit">
  <div class="wrap grid">
    <div>
      <h2>Visit</h2>
      <dl>
        <dt>Address</dt><dd>{P["address"]}<br>{P["city"]}</dd>
        <dt>Phone</dt><dd><a href="tel:{P["phone"]}">{P["phone"]}</a></dd>
        <dt>Open</dt><dd>{"Monday to Saturday. Closed Sundays." if P["open"] else "Summer only, June to mid-August."}</dd>
        {visit_weather}
      </dl>
    </div>
    <div class="map"><iframe src="{P["map"]}" title="Map to {P["name"]}" loading="lazy"
      referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
</section>
"""


def schedule(key):
    P = POOLS[key]
    note = "" if P["open"] else '<p class="note">The pool is closed until next summer. Use the arrows to step back to June, July or August 2026.</p>'
    return f"""
<section class="pagehead"><div class="wrap">
  <h1>Pool schedule</h1>
  <p>{P["season"]}. Use the Teams menu to show one program.</p>
</div></section>
<section class="block"><div class="wrap">
  {note}{cal(P["views"]["week"], P["name"] + ", the week", "tall")}
</div></section>
"""


def lessons(key):
    P = POOLS[key]
    body = "".join(
        '<tr%s><td>%s</td><td>%s</td><td>%s</td></tr>' % (' class="current"' if s == P["current"] else "", s, d, r)
        for s, d, r in P["sessions"])
    cal_block = (f"""<section class="block"><div class="wrap">
  <div class="intro"><h2>This session's classes</h2>
    <p>Classes starting at the same time share one block. Use the Practice Groups menu to show one level.</p></div>
  {cal(P["views"]["lessons"], P["name"] + " swim lessons")}
</div></section>""" if "lessons" in P["views"] else "")
    return f"""
<section class="pagehead"><div class="wrap">
  <h1>Swim lessons</h1>
  <p>Parent and Child through Level 4{", and adults" if P["open"] else ""}. $25 a session. No refunds.</p>
</div></section>
{cal_block}
<section class="block"{' style="padding-top:0"' if cal_block else ""}><div class="wrap">
  <div class="intro">
    <h2>{"Fall sessions" if P["open"] else "Summer sessions"}</h2>
    <p>Registration opens the Saturday before each session. <a href="{P["register"]}" target="_blank" rel="noopener">Register online</a>.</p>
  </div>
  <div class="scroll"><table class="sessions">
    <thead><tr><th>Session</th><th>Dates</th><th>Registration opens</th></tr></thead>
    <tbody>{body}</tbody>
  </table></div>
</div></section>
"""


def teams(key):
    P = POOLS[key]
    cards = "".join('<div%s><h3>%s</h3><p>%s</p></div>' % (' class="tba"' if tba else "", n, t) for n, t, tba in P["teams"])
    return f"""
<section class="pagehead"><div class="wrap">
  <h1>Team sports</h1>
  <p>Ages 7 to 17. Swimmers must swim at Level 3 and be comfortable in the water. $25 per team per league.</p>
</div></section>
<section class="block"><div class="wrap">
  <div class="teams">{cards}</div>
</div></section>
<section class="block" style="padding-top:0"><div class="wrap">
  <div class="intro">
    <h2>Practice schedule</h2>
    <p>Use the Teams menu to show team sports. <a href="{P["register"]}" target="_blank" rel="noopener">Register online</a>.</p>
  </div>
  {cal(P["views"]["teams"] if "teams" in P["views"] else P["views"]["week"], P["name"] + " team sports")}
</div></section>
"""


def hub():
    rws = []
    for k in ORDER:
        P = POOLS[k]
        chip = '<span class="chip open">Open now</span>' if P["open"] else '<span class="chip closed">Summer only</span>'
        rws.append(f"""      <a class="row" href="{k}/index.html">
        <div class="thumb" style="background-image:url('{k}/pool.jpg')" role="img" aria-label="{P["name"]}"></div>
        <div><h3>{P["name"]}{chip}</h3><p class="tagline">{P["tagline"]}</p>
          <p>{P["address"]}, {P["city"]} &middot; {P["phone"]}</p></div>
        <span class="go">Visit {P["short"]}</span>
      </a>""")
    body = f"""
<section class="hero">
  <div class="pennants" aria-hidden="true"></div>
  <div class="wrap">
    <div>
      <h1>North County Pools</h1>
      <p class="tag">Four LA County pools from Sylmar to Castaic, on one schedule. Two are open this fall; two open in summer.</p>
    </div>
    <div class="now" data-view="{NORTH["week"]}" data-multi aria-live="polite">
      <h2><span class="dot" aria-hidden="true"></span><span class="label">In the water now</span></h2>
      <p class="when">Checking every pool&hellip;</p>
      <ul></ul>
      <p class="foot"><a href="#today">Every pool, today</a></p>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The pools</h2>
    <div class="pools">
{chr(10).join(rws)}
    </div>
  </div>
</section>

<section class="block" id="today" style="padding-top:0">
  <div class="wrap">
    <div class="intro">
      <h2>Every pool, one day</h2>
      <p>One row per pool. Pick a day to see where you can swim, or open the week to compare.</p>
    </div>
    {cal(NORTH["day"], "North County pools, one day")}
  </div>
</section>
"""
    return head("North County Pools — LA County", "Four LA County pools on one live schedule.", "", "sanfernando/pool.jpg") + f"""
<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html">LA County Pools<small>North County</small></a>
    <nav aria-label="Main">
      {"".join(f'<a href="{k}/index.html">{POOLS[k]["short"]}</a>' for k in ORDER)}
      <a href="{STORE}" target="_blank" rel="noopener">Swim Store</a>
      <a href="{MORE}" target="_blank" rel="noopener">All County Pools</a>
    </nav>
  </div>
</header>
<main>{body}</main>
<footer><div class="wrap">
  <p class="fine">Unofficial preview built to show one live schedule across LA County's pools. Not affiliated with Los Angeles
  County Parks and Recreation. Pool photos from lacountypools.com.</p>
</div></footer>
<script src="now.js" defer></script>
</body></html>
"""


if __name__ == "__main__":
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub())
    for k in ORDER:
        P = POOLS[k]
        pages = [
            ("index.html", P["name"], P["tagline"], home(k), '<script src="../now.js" defer></script>'),
            ("schedule.html", f"Pool schedule — {P['name']}", "The week at the pool.", schedule(k), ""),
            ("lessons.html", f"Swim lessons — {P['name']}", "Swim lessons by level and session.", lessons(k), ""),
            ("team-sports.html", f"Team sports — {P['name']}", "Team sports practice.", teams(k), ""),
        ]
        for slug, title, desc, body, js in pages:
            with open(os.path.join(HERE, k, slug), "w", encoding="utf-8") as f:
                f.write(pool_page(k, slug, title, desc, body, js))
    print("built hub +", len(ORDER), "pools")
