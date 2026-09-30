from __future__ import annotations

import json
import math
from datetime import date, datetime, timedelta
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
STATE_FILE = APP_DIR / ".nakshatralife_state.json"

st.set_page_config(page_title="NakshatraLife Twin", page_icon="🌙", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');
:root{--night:#080d25;--panel:rgba(20,28,70,.72);--line:rgba(178,190,255,.17);--gold:#f2c96b;--teal:#54d4c1;--ink:#eef0ff;--muted:#a9b0d6}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.stApp{color:var(--ink);background:radial-gradient(850px 560px at 85% -8%,#4a3aa844,transparent 60%),radial-gradient(700px 500px at -4% 38%,#1e8f9a2e,transparent 60%),linear-gradient(180deg,#0a1030,#050818);background-attachment:fixed}
.stApp:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.34;background-image:radial-gradient(1px 1px at 12% 18%,#fff 60%,transparent),radial-gradient(1.5px 1.5px at 71% 22%,#fff 60%,transparent),radial-gradient(1px 1px at 38% 66%,#fff 60%,transparent),radial-gradient(1px 1px at 91% 73%,#fff 60%,transparent),radial-gradient(1px 1px at 52% 90%,#fff 60%,transparent);background-size:230px 200px;animation:twinkle 7s ease-in-out infinite alternate}
@keyframes twinkle{from{opacity:.18}to{opacity:.5}}
[data-testid="stHeader"]{background:transparent}
[data-testid="stSidebar"]{background:linear-gradient(180deg,rgba(10,17,54,.96),rgba(7,11,38,.96));border-right:1px solid var(--line)}
[data-testid="stSidebar"] *{color:var(--ink)}
h1,h2,h3{font-family:'Cormorant Garamond',Georgia,serif!important;letter-spacing:.01em}
h1{font-size:clamp(2.3rem,4vw,3.4rem)!important}
h2{font-size:2rem!important}
.stMarkdown p,.stCaption{color:#c0c5e4}
[data-testid="stMetric"]{padding:17px 19px;border:1px solid var(--line);border-radius:16px;background:var(--panel);backdrop-filter:blur(12px);box-shadow:0 12px 34px #0003}
[data-testid="stMetricLabel"]{color:var(--muted)} [data-testid="stMetricValue"]{color:var(--gold);font-family:'Cormorant Garamond',serif}
div[data-testid="stVerticalBlockBorderWrapper"]{border-color:var(--line)!important;background:rgba(20,28,70,.58)!important;border-radius:17px!important;backdrop-filter:blur(12px)}
.stButton>button,.stFormSubmitButton>button{border-radius:12px;border:1px solid #f2c96b66;background:linear-gradient(135deg,#f2c96b,#d89a40);color:#17132b;font-weight:700;min-height:42px;transition:transform .18s,box-shadow .18s}
.stButton>button:hover,.stFormSubmitButton>button:hover{transform:translateY(-2px);box-shadow:0 8px 26px #f2c96b33;color:#17132b;border-color:var(--gold)}
.stTextInput input,.stSelectbox div[data-baseweb="select"],.stDateInput input,.stTimeInput input,.stNumberInput input{background:#0a1030!important;color:var(--ink)!important;border-color:var(--line)!important}
.stTabs [data-baseweb="tab"]{color:var(--muted)}
a{color:var(--gold)!important}
hr{border-color:var(--line)}
.small-label{font-size:.72rem;letter-spacing:.19em;text-transform:uppercase;color:var(--gold);font-weight:700}
.hero{padding:1.5rem 1.8rem;border:1px solid #f2c96b45;border-radius:20px;background:linear-gradient(125deg,#1c2870bb,#2a1d6a88);box-shadow:0 18px 52px #0003}
.pill{display:inline-block;padding:.3rem .65rem;border-radius:100px;background:#f2c96b1d;border:1px solid #f2c96b4a;color:var(--gold);font-size:.78rem}
.callout{padding:1rem 1.2rem;border-left:3px solid var(--gold);border-radius:8px;background:#f2c96b13;margin:.5rem 0 1rem}
.avoid{padding:1rem 1.2rem;border:1px solid #d78a8266;border-radius:12px;background:#7d393522}
footer{visibility:hidden}
@media(prefers-reduced-motion:reduce){.stApp:before{animation:none}}
</style>
""", unsafe_allow_html=True)

STARS = ['Ashwini','Bharani','Krittika','Rohini','Mrigashira','Ardra','Punarvasu','Pushya','Ashlesha','Magha','Purva Phalguni','Uttara Phalguni','Hasta','Chitra','Swati','Vishakha','Anuradha','Jyeshtha','Mula','Purva Ashadha','Uttara Ashadha','Shravana','Dhanishta','Shatabhisha','Purva Bhadrapada','Uttara Bhadrapada','Revati']
RASIS = ['Mesha','Rishabha','Mithuna','Kataka','Simha','Kanni','Thula','Vrischika','Dhanusu','Makara','Kumbha','Meena']
RASI_FACTS = {
'Mesha':('Aries','Mars','Initiative, courage, and beginning new efforts.'),'Rishabha':('Taurus','Venus','Steadiness, care for resources, and appreciation of beauty.'),'Mithuna':('Gemini','Mercury','Curiosity, communication, and learning through exchange.'),'Kataka':('Cancer','Moon','Care, belonging, and attention to home and community.'),'Simha':('Leo','Sun','Creative expression, generosity, and responsibility in visibility.'),'Kanni':('Virgo','Mercury','Attention to detail, service, and practical refinement.'),'Thula':('Libra','Venus','Balance, dialogue, and awareness of relationships.'),'Vrischika':('Scorpio','Mars','Depth, persistence, and transformation.'),'Dhanusu':('Sagittarius','Jupiter','Learning, exploration, and meaning-making.'),'Makara':('Capricorn','Saturn','Patience, structure, and steady effort.'),'Kumbha':('Aquarius','Saturn','Community, systems thinking, and independent ideas.'),'Meena':('Pisces','Jupiter','Imagination, compassion, and reflective insight.')}
STAR_FACTS = {
'Ashwini':('Ketu','Horse head','Initiative, swift response, and renewal.'),'Bharani':('Venus','Vessel','Endurance, responsibility, and transformation.'),'Krittika':('Sun','Flame / blade','Discernment, refinement, and focused energy.'),'Rohini':('Moon','Chariot / growth','Nourishment, creativity, and cultivation.'),'Mrigashira':('Mars','Deer head','Curiosity, exploration, and seeking.'),'Ardra':('Rahu','Teardrop','Change, inquiry, and emotional intensity.'),'Punarvasu':('Jupiter','Quiver','Renewal, return, and resourcefulness.'),'Pushya':('Saturn','Nourishing flower','Care, support, and steady learning.'),'Ashlesha':('Mercury','Coiled serpent','Perception, strategy, and close observation.'),'Magha':('Ketu','Royal throne','Ancestry, stewardship, and respect for lineage.'),'Purva Phalguni':('Venus','Hammock','Creativity, ease, and connection.'),'Uttara Phalguni':('Sun','Bed','Commitment, generosity, and dependable support.'),'Hasta':('Moon','Open hand','Skill, dexterity, and making things tangible.'),'Chitra':('Mars','Bright jewel','Design, distinction, and imaginative craft.'),'Swati':('Rahu','Young shoot / wind','Adaptability, independence, and movement.'),'Vishakha':('Jupiter','Triumphal arch','Purpose, ambition, and sustained effort.'),'Anuradha':('Saturn','Lotus','Friendship, cooperation, and devotion.'),'Jyeshtha':('Mercury','Earring / umbrella','Protection, responsibility, and seniority.'),'Mula':('Ketu','Roots','Research, foundations, and uncovering causes.'),'Purva Ashadha':('Venus','Fan','Conviction, renewal, and resilience.'),'Uttara Ashadha':('Sun','Elephant tusk','Perseverance, principle, and lasting effort.'),'Shravana':('Moon','Ear','Listening, study, and transmission of knowledge.'),'Dhanishta':('Mars','Drum','Rhythm, collective work, and resourcefulness.'),'Shatabhisha':('Rahu','Empty circle','Inquiry, privacy, and restoration.'),'Purva Bhadrapada':('Jupiter','Front legs of a cot','Intensity, ideals, and reflection.'),'Uttara Bhadrapada':('Saturn','Back legs of a cot','Depth, patience, and steadiness.'),'Revati':('Mercury','Fish / drum','Guidance, protection, and completion.')}
CITIES = {
'Chennai':(13.0827,80.2707,5.5),'Bengaluru':(12.9716,77.5946,5.5),'Mumbai':(19.076,72.8777,5.5),'Delhi':(28.6139,77.209,5.5),'Coimbatore':(11.0168,76.9558,5.5),'Madurai':(9.9252,78.1198,5.5),'Singapore':(1.3521,103.8198,8),'London':(51.5072,-0.1276,0),'New York':(40.7128,-74.006,-4)}
METRICS = {'sleep':('Sleep','h',8),'activity':('Movement','min',30),'study':('Focused learning','min',60),'water':('Water','glasses',8)}
TARA_NAMES = ['Janma','Sampat','Vipat','Kshema','Pratyari','Sadhaka','Naidhana','Mitra','Parama Mitra']
TARA_GUIDANCE = {
'Janma':('Keep the day steady: attend to familiar routines and personal reflection.','If your custom observes Janma Tara, defer major auspicious beginnings.'),'Sampat':('Traditionally associated with resources; organize finances or practical next steps.','Treat this as a cultural reflection, not a promise of financial gain.'),'Vipat':('Keep plans simple, check details, and leave extra time for transitions.','Some traditions defer major new beginnings on Vipat Tara.'),'Kshema':('Traditionally associated with wellbeing; focus on maintenance, rest, and supportive routines.','Do not use the reading in place of health advice.'),'Pratyari':('Work through existing tasks carefully and communicate expectations clearly.','Some traditions postpone significant beginnings on Pratyari Tara.'),'Sadhaka':('Choose one focused task and make steady progress toward it.','No particular outcome is guaranteed.'),'Naidhana':('Prefer routine, review, and low-pressure tasks.','Many Tara Bala traditions avoid auspicious beginnings on Naidhana Tara.'),'Mitra':('Make time for cooperation, learning, or a thoughtful conversation.','Keep ordinary judgment central to important decisions.'),'Parama Mitra':('Traditionally associated with support; use the day for constructive collaboration.','This is a cultural reading, not a guarantee of success.')}
RAHU = {'Sunday':7,'Monday':1,'Tuesday':6,'Wednesday':4,'Thursday':5,'Friday':3,'Saturday':2}
YAMA = {'Sunday':4,'Monday':3,'Tuesday':2,'Wednesday':1,'Thursday':0,'Friday':6,'Saturday':5}
GULI = {'Sunday':6,'Monday':5,'Tuesday':4,'Wednesday':3,'Thursday':2,'Friday':1,'Saturday':0}


def demo_rows():
    sleep=[6.5,7,6,7.5,6.5,8,7]; activity=[20,35,15,40,25,30,45]; study=[50,65,35,70,45,80,60]; water=[6,7,5,8,6,7,8]
    today=date.today()
    return [{'date':(today-timedelta(days=6-i)).isoformat(),'sleep':sleep[i],'activity':activity[i],'study':study[i],'water':water[i]} for i in range(7)]


def load_state():
    if STATE_FILE.exists():
        try: return json.loads(STATE_FILE.read_text())
        except (OSError, json.JSONDecodeError): pass
    return {'profile':None,'checkins':demo_rows(),'feedback':{}}


def save_state():
    STATE_FILE.write_text(json.dumps({'profile':st.session_state.profile,'checkins':st.session_state.checkins,'feedback':st.session_state.feedback},indent=2))


def moon_star(on_date: date, time_text: str, city_name: str):
    lat,lon,tz=CITIES.get(city_name,CITIES['Chennai'])
    try: hour,minute=map(int,time_text.split(':'))
    except (ValueError,AttributeError): hour,minute=12,0
    utc=datetime(on_date.year,on_date.month,on_date.day,hour,minute)-timedelta(hours=tz)
    jd=utc.timestamp()/86400+2440587.5; t=(jd-2451545)/36525
    L=(218.3164477+481267.88123421*t-0.0015786*t*t)%360
    D=(297.8501921+445267.1114034*t-0.0018819*t*t)%360
    M=(357.5291092+35999.0502909*t-0.0001536*t*t)%360
    Mp=(134.9633964+477198.8675055*t+0.0087414*t*t)%360
    F=(93.272095+483202.0175233*t-0.0036539*t*t)%360
    r=math.pi/180
    lonmoon=L+6.289*math.sin(Mp*r)+1.274*math.sin((2*D-Mp)*r)+.658*math.sin(2*D*r)+.214*math.sin(2*Mp*r)-.186*math.sin(M*r)-.114*math.sin(2*F*r)
    sidereal=(lonmoon-24.1)%360; width=360/27; idx=int(sidereal//width)
    return {'name':STARS[idx],'pada':int((sidereal%width)/width*4)+1,'rasi':RASIS[int(sidereal//30)]}


def solar_times(day: date, city: str):
    lat,lon,tz=CITIES.get(city,CITIES['Chennai'])
    n=day.timetuple().tm_yday; g=2*math.pi/365*(n-1)
    dec=.006918-.399912*math.cos(g)+.070257*math.sin(g)-.006758*math.cos(2*g)+.000907*math.sin(2*g)-.002697*math.cos(3*g)+.00148*math.sin(3*g)
    latitude=math.radians(lat); zenith=math.radians(90.833)
    cosh=math.cos(zenith)/(math.cos(latitude)*math.cos(dec))-math.tan(latitude)*math.tan(dec)
    if cosh>1 or cosh < -1:return None
    H=math.degrees(math.acos(cosh)); eq=229.18*(.000075+.001868*math.cos(g)-.032077*math.sin(g)-.014615*math.cos(2*g)-.040849*math.sin(2*g))
    noon=720-4*lon-eq+tz*60
    return noon-4*H,noon+4*H


def clock_text(minutes):
    value=round(minutes)%1440
    return f'{value//60:02d}:{value%60:02d}'


def day_windows(day: date, city: str):
    solar=solar_times(day,city)
    if not solar:return []
    rise,set_=solar; eighth=(set_-rise)/8; weekday=day.strftime('%A'); rows=[]
    for label,slots in [('Rahu Kalam',RAHU),('Yamagandam',YAMA),('Gulikai Kalam',GULI)]:
        start=rise+eighth*slots[weekday]; end=start+eighth
        rows.append({'label':label,'start':clock_text(start),'end':clock_text(end),'sort':start})
    return sorted(rows,key=lambda row:row['sort'])


def season_for(day):
    month=day.month
    if month in (4,5):return 'Ilavenil','Early summer in the traditional Tamil seasonal cycle.'
    if month in (6,7):return 'Mudhuvenil','Peak summer; seasonal customs differ by region.'
    if month in (8,9):return 'Kaar','Monsoon season in the traditional cycle.'
    if month in (10,11):return 'Kuthir','Cool season; a time for seasonal routine reflection.'
    if month in (12,1):return 'Munpani','Dewy/cool season in the traditional cycle.'
    return 'Pinpani','Late cool season moving toward warmer months.'


def average(rows,key): return sum(float(row.get(key,0) or 0) for row in rows)/len(rows) if rows else 0.0

def score_for(avg): return round(sum(min(100,avg[key]/METRICS[key][2]*100) for key in METRICS)/4)

def render_palan(day, birth, day_star, tara, focus):
    if not birth:
        st.info('Add your birth details in the profile to personalize this reading.')
        return
    raasi=birth['rasi']; rasi=RASI_FACTS[raasi]; tone={
        'Sunday':'Set a clear intention, then leave room for rest.','Monday':'Keep plans flexible and notice what needs attention.','Tuesday':'Choose one task that benefits from direct, steady effort.','Wednesday':'Make space for useful conversations and learning.','Thursday':'Review the bigger picture before choosing your next step.','Friday':'Bring care and creativity to one task or interaction.','Saturday':'Favor patience, organization, and a measured pace.'}[day.strftime('%A')]
    cautious=tara in ('Vipat','Pratyari','Naidhana')
    financial=('Keep financial and business decisions measured; review costs, agreements, and timelines before committing.' if cautious else 'Use a practical approach to work and money; check details and plan before acting on an opportunity.')
    avoid=('Avoid rushing important commitments, unnecessary arguments, and signing or spending without checking details.' if cautious else 'Avoid overpromising, impulsive spending, and letting minor disagreements grow.')
    if tara=='Janma':avoid='Avoid overloading the day or making a major choice under pressure.'
    st.markdown(f"### Daily Predictions for {rasi[0]} Rasi · {birth['name']}\n<span class='pill'>{day.strftime('%A, %d %B %Y')} · {tara or 'Birth-star reflection'}</span>",unsafe_allow_html=True)
    st.markdown(f"<div class='callout'><b>Today's traditional theme</b><br>{TARA_GUIDANCE.get(tara,TARA_GUIDANCE['Janma'])[0]} {tone}</div>",unsafe_allow_html=True)
    items=[('Financial & Business',financial),('Work & Career',f"{TARA_GUIDANCE.get(tara,TARA_GUIDANCE['Janma'])[0]} {tone}"),('Family & Relationships',f"Favor patient, direct conversation and make room for others’ perspectives. {rasi[2]}"),('Health & Routine',f"Treat wellbeing as a routine check-in, not a prediction. Choose one manageable habit; recent tracked focus: {focus}.")]
    cols=st.columns(2)
    for i,(heading,text) in enumerate(items):
        with cols[i%2]:
            with st.container(border=True):st.markdown(f"**{heading}**\n\n{text}")
    st.markdown(f"<div class='avoid'><b>Things to avoid</b><br>{avoid}<br><small>Optional cultural cues only; not predictions or safety advice.</small></div>",unsafe_allow_html=True)
    codes={'Mesha':'MESHAM','Rishabha':'RISHABAM','Mithuna':'MITHUNAM','Kataka':'KATAKAM','Simha':'SIMMAM','Kanni':'KANNI','Thula':'THULAM','Vrischika':'VIRUCHIKAM','Dhanusu':'DANUSU','Makara':'MAKARAM','Kumbha':'KUMBAM','Meena':'MEENAM'}
    url=f"https://www.tamildailycalendar.com/tamil_rasi_palan_today.php?msg=Tamil%20Rasi%20Palan%20Today&rasi={codes[raasi]}"
    st.markdown(f"**Publisher reference:** [Open today's {rasi[0]} Rasi Palan]({url})")
    st.caption(f"Estimated day Nakshatra: {day_star['name'] if day_star else 'unavailable'}. Original demo reflection, not a verified forecast; publications may disagree.")


if 'initialized' not in st.session_state:
    saved=load_state()
    st.session_state.profile=saved.get('profile')
    st.session_state.checkins=saved.get('checkins') or demo_rows()
    st.session_state.feedback=saved.get('feedback') or {}
    st.session_state.initialized=True
    st.session_state.selected_day=date.today()

st.sidebar.markdown("## 🌙 NakshatraLife Twin")
st.sidebar.caption('IKS · ADAPTIVE LIFESTYLE COMPANION')

if not st.session_state.profile:
    left,right=st.columns([1.05,1])
    with left:
        st.markdown("<div class='hero'><div class='small-label'>IKS · LIFESTYLE TWIN</div><h1>Your day,<br><i>in living context.</i></h1><p>Connect traditional context with your changing daily routine.</p></div>",unsafe_allow_html=True)
        st.markdown("### ✦ A tradition-led lifestyle companion")
        st.caption('Cultural information and habit reflection; not a prediction.')
    with right:
        st.title('Start your Twin')
        st.write('Enter your details to estimate your birth Nakshatra and Janma Raasi.')
        with st.form('profile_form'):
            name=st.text_input('Your name')
            email=st.text_input('Email address',placeholder='you@example.com')
            birth_date=st.date_input('Birth date',value=date(2000,1,1),min_value=date(1900,1,1),max_value=date.today())
            birth_time=st.time_input('Birth time',value=datetime.strptime('12:00','%H:%M').time(),step=300)
            birth_city=st.selectbox('Birth city',list(CITIES))
            current_city=st.selectbox("Today's city",list(CITIES),index=0)
            submitted=st.form_submit_button('Create my Twin',use_container_width=True)
        if submitted:
            if not name.strip() or not email.strip():st.error('Please enter your name and email address.')
            else:
                st.session_state.profile={'name':name.strip(),'email':email.strip(),'birthDate':birth_date.isoformat(),'birthTime':birth_time.strftime('%H:%M'),'birthCity':birth_city,'city':current_city}
                save_state(); st.rerun()
    st.stop()

def go_to_page(name):
    st.session_state.active_page=name


profile=st.session_state.profile
birth=moon_star(date.fromisoformat(profile['birthDate']),profile.get('birthTime','12:00'),profile.get('birthCity','Chennai'))
raasi=RASI_FACTS[birth['rasi']][0]
st.sidebar.markdown(f"**{profile['name']}**  \n{birth['name']} · Pada {birth['pada']}  \n{raasi} · {profile.get('city','Chennai')}")
page=st.sidebar.radio('YOUR LIVING GUIDE',['Today','Digital Twin','Check-in','Analytics','Recommendations','What-If','My Star & Rasi','Daily Palan','IKS Context'],label_visibility='collapsed',key='active_page')
if st.sidebar.button('Sign out',use_container_width=True):
    st.session_state.profile=None; save_state(); st.rerun()
st.sidebar.divider()
st.sidebar.caption('Your demo profile and routine are saved locally on this computer.')

selected_day=st.date_input('Selected day',value=st.session_state.selected_day,key='date_selector')
st.session_state.selected_day=selected_day
rows=sorted(st.session_state.checkins,key=lambda row:row['date'])[-7:]
avg={key:average(rows,key) for key in METRICS}; score=score_for(avg)
focus_key=min(METRICS,key=lambda key:avg[key]/METRICS[key][2]); focus=METRICS[focus_key][0].lower()
day_star=moon_star(selected_day,'12:00',profile.get('city','Chennai'))
tara=TARA_NAMES[((STARS.index(day_star['name'])-STARS.index(birth['name'])+27)%27)%9] if day_star else None
windows=day_windows(selected_day,profile.get('city','Chennai'))
recent_by_date={row['date']:row for row in rows}; today_key=date.today().isoformat()

st.markdown('<div class="small-label">NAKSHATRALIFE TWIN</div>',unsafe_allow_html=True)
if page=='Today':
    st.title('Your day, in context.')
    st.caption(f"{profile['name']}, here is your Tamil Panchangam-inspired guide for {selected_day.strftime('%A, %d %B %Y')}.")
    live=None
    if selected_day==date.today():
        now=datetime.now(); current=now.hour*60+now.minute
        for w in windows:
            a,b=map(lambda x:int(x[:2])*60+int(x[3:]),(w['start'],w['end']))
            if a<=current<b:live=w;break
    with st.container(border=True):
        st.markdown(f"<div class='hero'><div class='small-label'>TODAY'S SKY + ROUTINE</div><h2>{'A traditional window is active' if live else 'Your guide is ready'}</h2><p>{live['label']+' is underway. Some Tamil traditions avoid beginning auspicious activities during this interval.' if live else f'Your routine score is {score}/100 across recent check-ins. Use the daily context as a reflection alongside your own judgment.'}</p><span class='pill'>☀ {profile.get('city','Chennai')} &nbsp; · &nbsp; ◉ {score}% routine score</span></div>",unsafe_allow_html=True)
    st.subheader('Panchangam windows · estimated local time')
    cols=st.columns(3)
    for i,w in enumerate(windows):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"**{w['label']}**")
                st.markdown(f"### {w['start']} – {w['end']}")
                st.caption('Traditionally avoided for starting auspicious new ventures.' + (' · HAPPENING NOW' if live and live['label']==w['label'] else ''))
    st.subheader('Daily Raasi / Star Palan')
    render_palan(selected_day,birth,day_star,tara,focus)
    st.subheader('Your Digital Twin · routine snapshot')
    cols=st.columns(4)
    for col,key in zip(cols,METRICS):
        label,unit,goal=METRICS[key]
        col.metric(label,f"{avg[key]:.1f} {unit}",f"{min(100,round(avg[key]/goal*100))}% of reference")
    st.button('Add today’s check-in',type='primary',on_click=go_to_page,args=('Check-in',))
elif page=='Digital Twin':
    st.title('Your routine, taking shape.')
    st.caption('An evolving summary of your self-reported routine. It updates when you add a check-in.')
    cols=st.columns([1,3])
    cols[0].metric('Routine score',f'{score}/100')
    cols[1].markdown(f"### {'A steady rhythm is emerging' if score>=75 else 'Your routine is taking shape' if score>=50 else 'A few small habits are ready to grow'}")
    st.subheader(f'Seven-day averages · {len(rows)} recent demo / saved days')
    cols=st.columns(4)
    for col,key in zip(cols,METRICS):
        label,unit,goal=METRICS[key]; col.metric(label,f'{avg[key]:.1f} {unit}',f'{min(100,round(avg[key]/goal*100))}% of reference')
    with st.container(border=True):
        st.markdown('**How the Twin adapts**')
        st.write('Each check-in updates the rolling routine averages and score. Recommendation feedback is saved and influences which routine gaps are surfaced first. All values are self-reported demo data stored on this computer.')
    st.button('View analytics',on_click=go_to_page,args=('Analytics',))
elif page=='Check-in':
    st.title('How did today go?')
    st.caption('Track a few routine signals. This is for reflection, not health assessment.')
    existing=recent_by_date.get(today_key,{})
    with st.form('checkin_form'):
        cols=st.columns(2); values={}
        for i,key in enumerate(METRICS):
            label,unit,goal=METRICS[key]
            values[key]=cols[i%2].number_input(f'{label} ({unit})',min_value=0.0,max_value=24.0 if key=='sleep' else 600.0,step=.5 if key=='sleep' else 1.0,value=float(existing.get(key,{'sleep':7,'activity':30,'study':45,'water':7}[key])))
            cols[i%2].caption(f'Personal reference: {goal} {unit}')
        submitted=st.form_submit_button('Save check-in',type='primary')
    if submitted:
        st.session_state.checkins=[row for row in st.session_state.checkins if row['date']!=today_key]
        st.session_state.checkins.append({'date':today_key,**values});st.session_state.checkins.sort(key=lambda row:row['date'])
        save_state();st.toast('Check-in saved — your Digital Twin has been updated.',icon='✅');st.success('Your Digital Twin has been updated. Open Digital Twin or Analytics to see the refreshed view.')
elif page=='Analytics':
    st.title('Patterns from your check-ins.')
    st.caption('Seven-day trends, reference comparisons, and recent routine records.')
    cols=st.columns(4)
    for col,key in zip(cols,METRICS):
        label,unit,goal=METRICS[key];col.metric(f'{label} avg',f'{avg[key]:.1f} {unit}')
    st.subheader('Daily trends · last seven recorded days')
    chart_data={METRICS[k][0]:[float(row[k]) for row in rows] for k in ('sleep','activity','study')}
    if rows:st.bar_chart(chart_data)
    else:st.info('No check-ins yet.')
    st.subheader('Recent check-ins')
    if rows:st.dataframe([{'Date':row['date'],'Sleep (h)':row['sleep'],'Movement (min)':row['activity'],'Focused learning (min)':row['study'],'Water (glasses)':row['water']} for row in reversed(st.session_state.checkins)],use_container_width=True,hide_index=True)
elif page=='Recommendations':
    st.title('Small steps, shaped around you.')
    st.caption('Rule-based suggestions from your recent routine and selected-day traditional context.')
    copies={'sleep':('Try a consistent wind-down time tonight. Your recent sleep average is below your 8-hour reference.','Avoid making a drastic schedule change; move bedtime gradually.'),'activity':('Add a comfortable 10-minute walk or stretch break today.','Avoid treating a missed activity goal as failure; resume with a manageable step.'),'study':('Schedule one short, distraction-light focus block.','Avoid filling every open hour; include breaks.'),'water':('Keep water nearby and check in with thirst throughout the day.','Avoid forcing a fixed amount without considering your needs or medical advice.')}
    keys=sorted(METRICS,key=lambda key:avg[key]/METRICS[key][2]+({'Helpful':.25,'Later':.1,'Not helpful':.5}.get(st.session_state.feedback.get(key),0)))
    for i,key in enumerate(keys[:3],1):
        label=METRICS[key][0]; body,avoid=copies[key]
        with st.container(border=True):
            st.markdown(f"<span class='small-label'>0{i} · {label.upper()} + {tara or 'GENERAL'} REFLECTION</span>",unsafe_allow_html=True)
            st.markdown(f'### A small {label.lower()} reset')
            st.write(body+' '+TARA_GUIDANCE.get(tara,TARA_GUIDANCE['Janma'])[0])
            st.caption('Consider: '+avoid)
            choice=st.radio('Was this useful?',('No feedback','Helpful','Not helpful','Later'),horizontal=True,key=f'feedback_{key}',index=('No feedback','Helpful','Not helpful','Later').index(st.session_state.feedback.get(key,'No feedback')) if st.session_state.feedback.get(key) else 0,label_visibility='collapsed')
            if choice!='No feedback' and st.session_state.feedback.get(key)!=choice:
                st.session_state.feedback[key]=choice;save_state();st.toast('Feedback saved; future suggestions will adapt.',icon='✨')
elif page=='What-If':
    st.title('Explore a routine change.')
    st.caption('The projection is arithmetic on recent entries, not a health forecast.')
    with st.container(border=True):
        metric=st.selectbox('Routine measure',list(METRICS),format_func=lambda key:METRICS[key][0])
        maximum=4 if metric=='water' else 60; minimum=1 if metric=='water' else 5; step=1 if metric=='water' else 5
        change=st.slider('Change to recent daily average',minimum,maximum,1 if metric=='water' else 30,step=step)
        unit='minutes of sleep' if metric=='sleep' else 'glasses per day' if metric=='water' else 'minutes per day'
        delta=change/60 if metric=='sleep' else change
        projected_avg={**avg,metric:avg[metric]+delta}
        projected_exact=sum(min(100,projected_avg[k]/METRICS[k][2]*100) for k in METRICS)/4
        current_exact=sum(min(100,avg[k]/METRICS[k][2]*100) for k in METRICS)/4
        st.write(f'Add **{change} {unit}** to the recent average for {METRICS[metric][0]}.')
        c1,c2=st.columns(2);c1.metric('Current routine score',f'{current_exact:.1f}/100');c2.metric('Projected routine score',f'{projected_exact:.1f}/100',f'{projected_exact-current_exact:+.1f}')
        if avg[metric]>=METRICS[metric][2]:st.info('This measure is already at or above its reference goal, so its score contribution is capped.')
        st.caption('The selected change is applied to the recent average. Real routines vary; this scenario does not predict personal outcomes.')
elif page=='My Star & Rasi':
    st.title('Your birth star and Moon sign.')
    st.caption('Estimated from your birth details; conventions and ephemerides can differ.')
    c1,c2=st.columns([1,2])
    with c1:
        with st.container(border=True):st.markdown('<div class="small-label">YOUR NAKSHATRA</div>',unsafe_allow_html=True);st.markdown(f'## ✦ {birth["name"]}');st.metric('Pada',birth['pada'])
    with c2:
        with st.container(border=True):
            fact=RASI_FACTS[birth['rasi']];sf=STAR_FACTS[birth['name']]
            st.markdown(f"**Janma Raasi**\n\n{fact[0]} · {birth['rasi']}\n\n{fact[2]}")
            st.markdown(f"**Traditional ruler** · {sf[0]}  \n**Symbol** · {sf[1]}  \n**Common traditional themes** · {sf[2]}")
    st.info(f"Birth details used: {profile['birthDate']} at {profile['birthTime']} in {profile['birthCity']}. These are cultural themes, not personality tests, destiny, or health guidance.")
elif page=='Daily Palan':
    st.title('Your day’s traditional reading.')
    st.caption('Select a date above to view a general reading for your birth star and Moon sign.')
    render_palan(selected_day,birth,day_star,tara,focus)
elif page=='IKS Context':
    st.title('Four knowledge layers meet your routine.')
    st.caption('Traditional context and self-reported lifestyle signals are shown as cultural frameworks, not scientific predictors.')
    season,season_text=season_for(selected_day)
    cards=[('01 · NAKSHATRA',birth['name'],f"Estimated birth star from the entered birth time and city, Pada {birth['pada']}."),('02 · PANCHANGA',f"Vara: {selected_day.strftime('%A')} · Nakshatra: {day_star['name'] if day_star else '—'}",'Tithi, Yoga, and Karana are not calculated in this preview. Daily time windows are approximate.'),('03 · DINACHARYA','Routine signals from your check-ins','Sleep, movement, focused learning, and water entries form a simple daily rhythm view.'),('04 · RITUCHARYA',season,season_text+' Seasonal customs vary by place and tradition.')]
    cols=st.columns(2)
    for i,(heading,title,text) in enumerate(cards):
        with cols[i%2]:
            with st.container(border=True):st.markdown(f'<div class="small-label">{heading}</div><h3>{title}</h3><p>{text}</p>',unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('**Closed-loop model**')
        st.write('IKS context + check-in data → updated Twin → routine analytics → contextual suggestion → your feedback → next suggestion adapts.')

st.divider()
st.caption('Traditional context and self-reported habit reflection; not a scientific forecast. Data remains in a local JSON file on this computer.')
