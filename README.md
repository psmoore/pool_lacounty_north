# LA County North pools — redesign proposal with live Pool Relay schedules

A hub and four pool sites in one design: Castaic Aquatic Center, San Fernando Aquatic Center, Val Verde Pool and El
Cariso Pool (the county's former North Agency pools with their own lacountypools.com sites). Each keeps its own links,
map and phone; every schedule, and the "In the water now" board, comes live from [Pool Relay](https://www.poolrelay.com).

Not an official Los Angeles County site. It says so in a ribbon across the top.

Built with `python3 build.py` (all content lives in its `POOLS` config); served by GitHub Pages.

## Sources (read 2026-09-25)

- Each pool's lacountypools.com home, lessons and team sports pages.
- LA County ActiveNet (`rest/activities/list` with `center_ids`, then `rest/activity/detail/meetingandregistrationdates/{id}`):
  Castaic 263, San Fernando Regional Pool 49, Val Verde Pool 198, El Cariso Pool 194 (the last two list nothing; closed).

## What is ours / worth asking

- **San Fernando's fall grid is identical to Castaic's**, minute for minute. Val Verde's and El Cariso's summer grids are
  identical to each other. Copied template text, or truly the same hours?
- San Fernando: registration already lists winter lessons (Nov 30 – Dec 11), water exercise to February and the winter
  swim team; the site says winter is TBA. The swim team is named "(5:00 PM)" in registration but meets 6–7pm; the Team
  Sports page says 5–6pm. Address: the site says 300 Park Ave; the county's pool list says 208 Park Ave.
- Val Verde and El Cariso: "Everybody Swims" lists Saturday twice (12:30–2:30 and 12:30–4). El Cariso's Parent and
  Child class is listed at 11am, the same hour as Water Exercise. Summer lap swim 4–6pm shares the pool with lessons
  and all four team sports.
- Pools are split into areas (lap lanes, lessons, water exercise, teams, open swim) because no page says how they share water.
