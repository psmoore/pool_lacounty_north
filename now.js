// The live board: reads a pool's schedule from Pool Relay and says what is in the water
// right now and what's next, in the pool's time zone. Same data as every calendar on the
// site, so a change made in chat shows up here too.
//
//   <div class="now" data-view="TOKEN" data-closed="…" data-multi>
//     data-view    the Pool Relay public view to read
//     data-closed  what to say when nothing is scheduled in the coming week (a seasonal pool)
//     data-multi   several pools: name the pool on each line
(function () {
  const TZ = "America/Los_Angeles";
  const board = document.querySelector(".now[data-view]");
  if (!board) return;
  const VIEW = board.dataset.view;
  const multi = board.hasAttribute("data-multi");
  const list = board.querySelector("ul");
  const when = board.querySelector(".when");
  const title = board.querySelector("h2 .label");

  const parts = (d) => Object.fromEntries(new Intl.DateTimeFormat("en-US", {
    timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23",
  }).formatToParts(d).map((p) => [p.type, p.value]));
  const p = parts(new Date());
  const today = `${p.year}-${p.month}-${p.day}`;
  const nowMin = +p.hour * 60 + +p.minute;
  const addDays = (iso, n) => { const d = new Date(iso + "T12:00:00Z"); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); };
  const mins = (hhmm) => { const [h, m] = hhmm.split(":").map(Number); return h * 60 + m; };
  const clock = (hhmm) => {
    let [h, m] = hhmm.split(":").map(Number); const ap = h >= 12 ? "pm" : "am"; h = h % 12 || 12;
    return m ? `${h}:${String(m).padStart(2, "0")}${ap}` : `${h}${ap}`;
  };
  const span = (a, b) => {
    const ap = (t) => (+t.split(":")[0] >= 12 ? "pm" : "am");
    const bare = (t) => clock(t).replace(/[ap]m$/, "");
    return ap(a) === ap(b) ? `${bare(a)}–${clock(b)}` : `${clock(a)}–${clock(b)}`;
  };
  const dayName = (iso) => new Date(iso + "T12:00:00Z").toLocaleDateString("en-US", { weekday: "long", timeZone: "UTC" });
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  fetch(`https://www.poolrelay.com/api/public/views/${VIEW}/project?from=${today}&to=${addDays(today, 7)}`)
    .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(({ occurrences, facilities }) => {
      // Which facility each area belongs to, for boards that cover several pools.
      const facOf = {};
      const walk = (n, top) => { facOf[n.id] = top; (n.children || []).forEach((c) => walk(c, top)); };
      (facilities || []).forEach((f) => walk(f, f.shortName || f.longName));
      const where = (o) => (multi ? facOf[o.areaIds?.[0]] || "" : "");
      const row = (o, live) =>
        `<li class="${live ? "live" : ""}"><span class="t">${live ? "Now" : clock(o.start)}</span>` +
        `<span class="what">${esc(o.title)}${multi ? `<span class="fac">${esc(where(o))}</span>` : ""}` +
        `<span class="sub">${live ? "until " + clock(o.end) : span(o.start, o.end)}</span></span></li>`;

      const seen = new Set();
      const occ = occurrences
        .filter((o) => !o.allDay)
        .filter((o) => { const k = `${o.date}|${o.start}|${o.end}|${o.title}|${where(o)}`; if (seen.has(k)) return false; seen.add(k); return true; })
        .sort((a, b) => (a.date + a.start).localeCompare(b.date + b.start));
      const todays = occ.filter((o) => o.date === today);
      const live = todays.filter((o) => mins(o.start) <= nowMin && nowMin < mins(o.end));
      const later = todays.filter((o) => mins(o.start) > nowMin).slice(0, live.length ? 4 : 6);

      let html = live.map((o) => row(o, true)).join("");
      if (later.length) {
        html += (live.length ? `<li class="later-h" aria-hidden="true"><span class="later">Later today</span></li>` : "") +
          later.map((o) => row(o, false)).join("");
      }
      if (!live.length && !later.length) {
        const next = occ.find((o) => o.date > today);
        if (next) {
          when.textContent = `Nothing else in the water today. Next up, ${dayName(next.date)}:`;
          html = occ.filter((o) => o.date === next.date).slice(0, 4).map((o) => row(o, false)).join("");
        } else {
          board.classList.add("closed");
          if (title) title.textContent = "Closed for the season";
          when.textContent = board.dataset.closed || "Nothing is scheduled this week.";
        }
      } else {
        when.textContent = `${dayName(today)}, ${clock(`${p.hour}:${p.minute}`)}`;
      }
      list.innerHTML = html;
    })
    .catch(() => {
      when.textContent = "The live schedule didn't load. The calendar below has every session.";
    });
})();
