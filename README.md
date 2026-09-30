# NakshatraLife Twin

An astronomy-themed Streamlit demo that brings together traditional IKS context and an evolving, self-reported daily routine.

## Open it locally

**macOS (Python 3.10+):** double-click [`run_local.command`](run_local.command) in the project folder. It creates a local Python environment if needed, installs the requirements, starts Streamlit on port `8501`, and Streamlit opens the app in your browser.

**Windows (Python 3.10+):** double-click [`run_local.bat`](run_local.bat).

Or start it from a terminal in this folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
NAKSHATRALIFE_LOCAL_PERSIST=1 \\
.venv/bin/python -m streamlit run app.py --server.port 8501
```

Then open the local URL printed by Streamlit, normally [http://localhost:8501](http://localhost:8501).

> The localhost link opens the app only after its local server is running. A link in GitHub or a README cannot start software on your computer; use the launcher first. The launcher starts the server and opens the browser automatically.

## What this demo includes

- Profile setup using name, email, birth date, birth time, birth city, and the city for the daily guide.
- Estimated birth Nakshatra, Pada, and Janma Raasi.
- Selected-day Nakshatra and a nine-Tara reflection.
- Estimated Rahu Kalam, Yamagandam, and Gulikai windows for a limited city list.
- Newspaper-style daily Raasi / Star Palan sections, practical avoid prompts, and a publisher link.
- A Digital Twin score based on recent routine check-ins.
- Check-ins for sleep, movement, focused learning, and water, plus seven-day analytics.
- Adaptive recommendations and feedback, a What-If score simulator, and an IKS Context page.

## Data and accuracy

This is a frontend-only demo. It does not start a separate API at port `4000`, use `PLANTCARE_API_URL`, or require a database seed command. Demo check-ins are created the first time the app runs. The included local launchers save profile, check-ins, and feedback to `.nakshatralife_state.json` in this folder, which is excluded from Git. Keep that file to retain local demo data; remove it only if you want to reset your profile and check-ins to the demo defaults. In hosted deployments, visitor data stays in that visitor's Streamlit session and is not written to a shared server file; it resets when the session ends.

## Deploy a hosted demo

This repository is ready for [Streamlit Community Cloud](https://share.streamlit.io/). Sign in with GitHub, choose **Create app**, select `Swe7ha-07/NakshtraLife`, branch `main`, and entrypoint `app.py`. The app needs only the root `requirements.txt`. Community Cloud will assign a shareable `*.streamlit.app` URL after deployment; replace the local link above with that URL once the app has been created. Anyone can visit a public app without starting your computer's local server.

Because this GitHub repository is public, the deployed app will also be public by default. Visitor profiles, check-ins, and feedback are session-only and are not stored permanently by this demo.

The birth-star and daily time calculations are estimates. Results can differ from a location-aware ephemeris or a published Panchangam, especially near a Nakshatra boundary, in places with daylight-saving changes, or under a different Panchangam convention. Tithi, Yoga, and Karana are not calculated. Palan and routine suggestions are cultural/educational reflections, not verified forecasts, medical advice, financial advice, or validated health measures.

Background references: [Tamil Panchangam overview](https://www.drikpanchang.com/tamil/tamil-month-panchangam.html), [Rahu Kalam weekday table](https://panchangam.com/raahu-kalam-chart/), [Tara Bala overview](https://panchangtime.com/methodology/tarabala), [Nakshatra divisions and traditional rulers](https://www.crescentastrology.com/nakshatra), and [U.S. Naval Observatory notes on rise/set algorithms](https://aa.usno.navy.mil/faq/rs_algor).
