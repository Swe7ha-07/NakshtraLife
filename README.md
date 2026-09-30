# NakshatraLife Twin — IKS-informed lifestyle analytics

A browser-only React/Vite demo connecting Indian Knowledge Systems context with an evolving, self-reported lifestyle profile.

## Run locally

```sh
npm install
npm run dev
```

Open `http://localhost:3000`.

## Included in this preview

- Local demo profile creation with name, email, birth date/time, birth city, and the city for the daily guide.
- A birth-star estimate (Janma Nakshatra and Pada) based on a compact low-precision lunar longitude model and a Lahiri-like sidereal offset.
- A selected-day Nakshatra estimate and a traditional nine-Tara relationship to the birth star, with a context-aware “try / set aside” reflection.
- A birth profile with estimated Moon sign (Janma Raasi), birth Nakshatra, Pada, traditional ruling planet, symbol, and non-deterministic theme notes.
- A newspaper-style daily Raasi / Star Palan on Today and a separate date-selectable Palan page, written as a general traditional reflection.
- The Today page keeps the daily time periods, then shows Raasi-based financial, career, family, and routine themes, practical “avoid” prompts, and links to current publisher pages for lucky details that vary between sources.
- A success toast after saving a check-in, followed by the refreshed Digital Twin view.
- Date-selectable Rahu Kalam, Yamagandam, and Gulikai windows for a limited city list, estimated from local sunrise and sunset.
- A Digital Twin dashboard that recomputes routine averages and a demo consistency score from check-ins.
- Dinacharya check-ins for sleep, movement, focused learning, and water; seeded sample entries make the demo populated on first use.
- Seven-day analytics with reference comparisons and a compact trend chart.
- Rule-based recommendations that combine routine gaps with the day’s Tara reflection; feedback changes which gaps are prioritized next.
- A What-If slider that calculates a simple scenario score from recent values.
- An IKS Context page for Nakshatra, Panchanga, Dinacharya, and Ritucharya. Panchanga fields this preview cannot calculate reliably are labeled as unavailable.

Profile, check-ins, and feedback are saved in browser `localStorage`; this is not production authentication and data does not sync across devices. City coordinates and time zones are a small static demo list. This preview is not a substitute for a location-aware ephemeris or a published Panchangam: results near a Nakshatra boundary, in places with daylight-saving changes, at high latitudes, or under a different Panchangam convention may differ. Tithi, Yoga, and Karana are not calculated, and the demo does not claim to provide authoritative “good/bad” predictions. Recommendations and score are educational prototype logic, not medical advice or validated health measures.

The daily Palan copy is generated in this app from the estimated birth Moon sign, birth star, selected date's estimated midday star, and Tara category. It is not sourced from or copied from a newspaper and should not be read as a factual forecast.

Traditional and cultural information only. It is not medical, financial, or scientific advice.

Background references used for the terminology and conventions: [Tamil Panchangam overview](https://www.drikpanchang.com/tamil/tamil-month-panchangam.html), [Rahu Kalam weekday table](https://panchangam.com/raahu-kalam-chart/), [Tara Bala overview](https://panchangtime.com/methodology/tarabala), [Nakshatra divisions and traditional rulers](https://www.crescentastrology.com/nakshatra), and [U.S. Naval Observatory notes on rise/set algorithms](https://aa.usno.navy.mil/faq/rs_algor).
