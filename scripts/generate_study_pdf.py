import os
import subprocess

def create_study_pdf():
    os.makedirs('materials', exist_ok=True)
    html_path = os.path.abspath('materials/golden_revision_temp.html')
    pdf_path = os.path.abspath('materials/vetri_tnpsc_group4_tamil_golden_revision.pdf')

    html_content = """<!DOCTYPE html>
<html lang="ta">
<head>
<meta charset="UTF-8">
<title>Vetri TNPSC - பொதுத்தமிழ் Golden Revision Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;600;700;800&display=swap');
  
  @page {
    size: A4;
    margin: 15mm 15mm 20mm 15mm;
    @top-center {
      content: "வெற்றி TNPSC - குரூப் 4 & VAO பொதுத்தமிழ் வழிகாட்டி | Telegram: @VetriTNPSCApp";
      font-size: 9pt;
      color: #64748b;
      font-family: 'Mukta Malar', 'Latha', 'Nirmala UI', sans-serif;
    }
    @bottom-center {
      content: "இலவச கல்வி வழிகாட்டி | நண்பர்களுக்கு பகிருங்கள் | https://t.me/VetriTNPSCApp";
      font-size: 9pt;
      color: #64748b;
      font-family: 'Mukta Malar', 'Latha', 'Nirmala UI', sans-serif;
    }
  }

  body {
    font-family: 'Mukta Malar', 'Latha', 'Nirmala UI', 'Segoe UI', sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }

  .cover-card {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    color: white;
    padding: 24px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(30, 58, 138, 0.2);
  }
  .cover-card h1 {
    margin: 0 0 8px 0;
    font-size: 22pt;
    font-weight: 800;
    letter-spacing: 0.5px;
  }
  .cover-card h2 {
    margin: 0 0 12px 0;
    font-size: 14pt;
    color: #fde047;
    font-weight: 700;
  }
  .cover-card p {
    margin: 0 0 14px 0;
    font-size: 10.5pt;
    color: #e2e8f0;
  }
  .cta-badge {
    display: inline-block;
    background: #ffffff;
    color: #1e3a8a;
    font-weight: 800;
    padding: 8px 18px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 10.5pt;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  }

  .section-title {
    background: #f1f5f9;
    color: #0f172a;
    border-left: 5px solid #2563eb;
    padding: 8px 12px;
    font-size: 12pt;
    font-weight: 700;
    margin: 20px 0 10px 0;
    border-radius: 0 6px 6px 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 16px;
    font-size: 9.5pt;
  }
  th {
    background: #1e3a8a;
    color: white;
    text-align: left;
    padding: 7px 10px;
    font-weight: 700;
  }
  td {
    border-bottom: 1px solid #e2e8f0;
    padding: 6px 10px;
    vertical-align: top;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }

  .qa-block {
    margin-bottom: 10px;
    padding: 8px 12px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
  }
  .qa-q {
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 4px;
  }
  .qa-a {
    color: #166534;
    font-weight: 600;
    margin-left: 12px;
  }
  .qa-exp {
    color: #64748b;
    font-size: 9pt;
    margin-left: 12px;
  }

  .promo-banner {
    background: #eff6ff;
    border: 2px dashed #3b82f6;
    border-radius: 10px;
    padding: 14px;
    text-align: center;
    margin: 24px 0;
  }
  .promo-banner h3 {
    margin: 0 0 6px 0;
    color: #1d4ed8;
    font-size: 13pt;
  }
  .promo-banner p {
    margin: 0 0 10px 0;
    font-size: 10pt;
    color: #334155;
  }
  .btn-join {
    background: #0088cc;
    color: white;
    padding: 8px 16px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
  }

  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

  <!-- Cover Banner -->
  <div class="cover-card">
    <h1>வெற்றி TNPSC: பொதுத்தமிழ் கோல்டன் ரிவிஷன்</h1>
    <h2>TNPSC Group 4, Group 2 & VAO பிரத்யேக கையேடு 2024-2025</h2>
    <p>சமச்சீர் கல்வி 6-12 முக்கிய சான்றோர்கள், அடைமொழிகள், நூல்கள் மற்றும் தேர்வு வினா-விடை</p>
    <a href="https://t.me/VetriTNPSCApp" class="cta-badge">🎯 இலவச ஆன்லைன் டெஸ்ட் எழுத Telegram-ல் இணையவும் (@VetriTNPSCApp)</a>
  </div>

  <!-- SECTION 1 -->
  <div class="section-title">பகுதி 1: அடைமொழியால் குறிக்கப்படும் சான்றோர்கள் & சிறப்புப் பெயர்கள்</div>
  <table>
    <thead>
      <tr>
        <th style="width: 45%;">அடைமொழி / சிறப்புப் பெயர்</th>
        <th style="width: 55%;">சான்றோர் / கவிஞர்</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>தேசியக் கவி, மகாகவி, பாட்டுக்கொரு புலவன்</td><td>பாரதியார்</td></tr>
      <tr><td>பாவேந்தர், புரட்சிக் கவிஞர், தமிழ்க்கவிஞர்</td><td>பாரதிதாசன்</td></tr>
      <tr><td>தமிழ் தாத்தா</td><td>உ.வே. சாமிநாதையர் (உ.வே.சா)</td></tr>
      <tr><td>செக்கிழுத்த செம்மல், கப்பலோட்டிய தமிழன்</td><td>வ.உ. சிதம்பரனார் (வ.உ.சி)</td></tr>
      <tr><td>நாமக்கல் கவிஞர், காந்தியக் கவிஞர்</td><td>வெ. இராமலிங்கம் பிள்ளை</td></tr>
      <tr><td>கவிமணி</td><td>தேசிக விநாயகம்பிள்ளை</td></tr>
      <tr><td>மக்கள் கவிஞர்</td><td>பட்டுக்கோட்டை கல்யாணசுந்தரம்</td></tr>
      <tr><td>உவமைக் கவிஞர்</td><td>சுரதா (சுப்புரத்தினதாசன்)</td></tr>
      <tr><td>கவிக்கோ</td><td>அப்துல் ரகுமான்</td></tr>
      <tr><td>கவியரசு</td><td>கண்ணதாசன்</td></tr>
      <tr><td>மொழிஞாயிறு</td><td>தேவநேயப் பாவாணர்</td></tr>
      <tr><td>திராவிட சாஸ்திரி</td><td>பரிதிமாற்கலைஞர் (வி.கோ. சூரியநாராயண சாஸ்திரியார்)</td></tr>
      <tr><td>பாவலரேறு</td><td>பெருஞ்சித்திரனார்</td></tr>
      <tr><td>தனித்தமிழ் இயக்கத்தின் தந்தை</td><td>மறைமலையடிகள்</td></tr>
      <tr><td>கவிஞர் திலகம், கவிச்சக்கரவர்த்தி</td><td>கம்பர்</td></tr>
      <tr><td>தென்னாட்டின் பெர்னாட்ஷா</td><td>பேரறிஞர் அண்ணா</td></tr>
      <tr><td>தமிழ்த் தென்றல்</td><td>திரு. வி. கலியாணசுந்தரனார் (திரு.வி.க)</td></tr>
      <tr><td>குழந்தைக் கவிஞர்</td><td>அழ. வள்ளியப்பா</td></tr>
      <tr><td>சொல்லின் செல்வர்</td><td>ரா. பி. சேதுப்பிள்ளை</td></tr>
      <tr><td>சொல்லின் செல்வன் (இலக்கியத்தில்)</td><td>அனுமன்</td></tr>
      <tr><td>சிலம்புச் செல்வர்</td><td>ம. பொ. சிவஞானம் (ம.பொ.சி)</td></tr>
    </tbody>
  </table>

  <!-- SECTION 2 -->
  <div class="section-title">பகுதி 2: பதினெண்கீழ்க்கணக்கு நூல்கள் & ஆசிரியர்கள் அட்டவணை</div>
  <table>
    <thead>
      <tr>
        <th>வரிசை</th>
        <th>நூலின் பெயர்</th>
        <th>ஆசிரியர்</th>
        <th>பாடல்கள் / வகை</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>திருக்குறள்</td><td>திருவள்ளுவர்</td><td>1330 குறள்கள் (அறநூல்)</td></tr>
      <tr><td>2</td><td>நாலடியார்</td><td>சமண முனிவர்கள்</td><td>400 வெண்பாக்கள் (அறநூல்)</td></tr>
      <tr><td>3</td><td>நான்மணிக்கடிகை</td><td>விளம்பி நாகனார்</td><td>104 பாடல்கள் (அறநூல்)</td></tr>
      <tr><td>4</td><td>இன்னா நாற்பது</td><td>கபிலர்</td><td>40 பாடல்கள் (அறநூல்)</td></tr>
      <tr><td>5</td><td>இனியவை நாற்பது</td><td>பூதஞ்சேந்தனார்</td><td>40 பாடல்கள் (அறநூல்)</td></tr>
      <tr><td>6</td><td>திரிகடுகம்</td><td>நல்லாதனார்</td><td>100 பாடல்கள் (மருந்து நூல்)</td></tr>
      <tr><td>7</td><td>ஆசாரக்கோவை</td><td>பெருவாயின் முள்ளியார்</td><td>100 பாடல்கள் (ஆசாரம்)</td></tr>
      <tr><td>8</td><td>பழமொழி நானூறு</td><td>முன்றுறை அரையனார்</td><td>400 பாடல்கள் (பழமொழிகள்)</td></tr>
      <tr><td>9</td><td>சிறுபஞ்சமூலம்</td><td>காரியாசான்</td><td>102 பாடல்கள் (5 மூலிகைகள்)</td></tr>
      <tr><td>10</td><td>ஏலாதி</td><td>கணிமேதாவியார்</td><td>81 பாடல்கள் (6 மூலிகைகள்)</td></tr>
      <tr><td>11</td><td>முதுமொழிக்காஞ்சி</td><td>மதுரைக்கூடலூர் கிழார்</td><td>100 பாடல்கள் (அறநூல்)</td></tr>
      <tr><td>12</td><td>கார் நாற்பது</td><td>மதுரை கண்ணங்கூத்தனார்</td><td>40 பாடல்கள் (அகநூல் - முல்லை)</td></tr>
      <tr><td>13</td><td>ஐந்திணை ஐம்பது</td><td>மாறன் பொறையனார்</td><td>50 பாடல்கள் (அகநூல்)</td></tr>
      <tr><td>14</td><td>ஐந்திணை எழுபது</td><td>மூவாதியார்</td><td>70 பாடல்கள் (அகநூல்)</td></tr>
      <tr><td>15</td><td>திணைமொழி ஐம்பது</td><td>கண்ணன் சேந்தனார்</td><td>50 பாடல்கள் (அகநூல்)</td></tr>
      <tr><td>16</td><td>திணைமாலை நூற்றைம்பது</td><td>கணிமேதாவியார்</td><td>150 பாடல்கள் (அகநூல்)</td></tr>
      <tr><td>17</td><td>கைந்நிலை</td><td>புல்லங்காடனார்</td><td>60 பாடல்கள் (அகநூல்)</td></tr>
      <tr><td>18</td><td>களவழி நாற்பது</td><td>பொய்கையார்</td><td>40 பாடல்கள் (புறநூல் - போர்)</td></tr>
    </tbody>
  </table>

  <!-- Promo Box 1 -->
  <div class="promo-banner">
    <h3>📢 தினமும் 10 புதிய TNPSC வினாடி-வினா எழுத வேண்டுமா?</h3>
    <p>ஒவ்வொரு நாளும் பொதுத்தமிழ், நடப்பு நிகழ்வுகள் மற்றும் கணிதம் உடனுக்குடன் உங்கள் மொபைலில் பெற:</p>
    <a href="https://t.me/VetriTNPSCApp" class="btn-join">👉 Telegram சேனலில் இணையுங்கள் (@VetriTNPSCApp)</a>
  </div>

  <div class="page-break"></div>

  <!-- SECTION 3 -->
  <div class="section-title">பகுதி 3: சொல்லும் பொருளும் - தேர்விற்கு மிக அவசியமானவை</div>
  <table>
    <thead>
      <tr>
        <th style="width: 30%;">சொல்</th>
        <th style="width: 70%;">பொருள்</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>நல்கூர்ந்தார்</td><td>வறியவர் / ஏழை</td></tr>
      <tr><td>ஆழி</td><td>கடல் / மோதிரம்</td></tr>
      <tr><td>புனல்</td><td>நீர் / ஆற்று நீர்</td></tr>
      <tr><td>கழனி</td><td>வயல்</td></tr>
      <tr><td>பரிதி</td><td>சூரியன்</td></tr>
      <tr><td>மதி</td><td>நிலவு / அறிவு</td></tr>
      <tr><td>அரி</td><td>சிங்கம் / விஷ்ணு / நெற்கதிர்</td></tr>
      <tr><td>மாதவம்</td><td>பெருந்தவம்</td></tr>
      <tr><td>வெய்யோன்</td><td>சூரியன்</td></tr>
      <tr><td>செவ்வி</td><td>காலம் / நற்பருவம் / அழகு</td></tr>
      <tr><td>தார்</td><td>மாலை</td></tr>
      <tr><td>நிரை</td><td>பசுக்கூட்டம் / ஒழுங்கு</td></tr>
      <tr><td>கிளை</td><td>உறவினர் / மரக்கிளை</td></tr>
      <tr><td>ஊன்</td><td>இறைச்சி / உணவு</td></tr>
      <tr><td>ஊண்</td><td>உணவு உட்கொள்ளுதல்</td></tr>
      <tr><td>அல்கல்</td><td>இரவு / தங்குதல்</td></tr>
      <tr><td>யாணர்</td><td>புதுவருவாய்</td></tr>
      <tr><td>ஞமலி</td><td>நாய்</td></tr>
      <tr><td>உழை</td><td>மான் / பக்கம்</td></tr>
      <tr><td>ஈகை</td><td>கொடை</td></tr>
    </tbody>
  </table>

  <!-- SECTION 4 -->
  <div class="section-title">பகுதி 4: TNPSC Group 4 முந்தைய ஆண்டு முக்கிய வினா-விடைகள் (மாதிரி வினாக்கள்)</div>

  <div class="qa-block">
    <div class="qa-q">1. "யாதும் ஊரே யாவரும் கேளிர்" - என்ற உலகப் புகழ்மிக்க வரிகளைப் பாடியவர் யார்?</div>
    <div class="qa-a">விடை: கணியன் பூங்குன்றனார்</div>
    <div class="qa-exp">விளக்கம்: இது புறநானூற்றில் 192-ஆம் பாடலில் இடம்பெற்றுள்ளது.</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">2. 'திராவிட மொழிகளின் ஒப்பிலக்கணம்' என்ற வரலாற்றுச் சிறப்புமிக்க நூலை எழுதியவர் யார்?</div>
    <div class="qa-a">விடை: இராபர்ட் கால்டுவெல் (Robert Caldwell, 1856)</div>
    <div class="qa-exp">விளக்கம்: தென்னிந்திய மொழிகள் தனித்த குடும்பம் என நிறுவியவர்.</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">3. 'உழவர் ஏரடிக்கும் சிறுகோலே அரசரது செங்கோலை நடத்தும் கோல்' எனக் கூறியவர் யார்?</div>
    <div class="qa-a">விடை: கம்பர் (ஏரெழுபது)</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">4. திருக்குறளுக்கு உரை எழுதிய பதின்மருள் யாருடைய உரை மிகச் சிறந்ததாகப் போற்றப்படுகிறது?</div>
    <div class="qa-a">விடை: பரிமேலழகர் உரை</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">5. தமிழ்நாட்டில் காந்தியக் கவிஞர் என்று அன்போடு அழைக்கப்படுபவர் யார்?</div>
    <div class="qa-a">விடை: வெ. இராமலிங்கம் பிள்ளை (நாமக்கல் கவிஞர்)</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">6. 'குடிமக்கள் காப்பியம்' என்று போற்றப்படும் தமிழ் இலக்கியம் எது?</div>
    <div class="qa-a">விடை: சிலப்பதிகாரம் (இளங்கோவடிகள்)</div>
    <div class="qa-exp">விளக்கம்: மன்னர்களை அன்றி எளிய மக்களை காப்பியத் தலைவர்களாகக் கொண்டதால் இவ்வாறு அழைக்கப்படுகிறது.</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">7. "எழுது என்றான்" - என்பது எவ்வகைத் தொடர்?</div>
    <div class="qa-a">விடை: வினைமுற்றுத் தொடர்</div>
  </div>

  <div class="qa-block">
    <div class="qa-q">8. 'செம்மொழித் தமிழ் மாநாடு' முதன்முதலில் எங்கு யாரால் நடத்தப்பட்டது?</div>
    <div class="qa-a">விடை: கோவை (2010), கலைஞர் மு. கருணாநிதி அவர்களால்.</div>
  </div>

  <!-- End Call to Action -->
  <div class="promo-banner" style="background: #f0fdf4; border-color: #22c55e;">
    <h3 style="color: #15803d;">🎉 முழு வினாடி வினா & OMR மாதிரி தேர்வுகள் எழுத!</h3>
    <p style="color: #166534;">இந்த கையேட்டை உங்கள் TNPSC பயிலும் நண்பர்கள் மற்றும் வாட்ஸ்அப் குரூப்களுக்கு பகிருங்கள்.<br>தினமும் இலவசமாக தேர்வு எழுத கீழே உள்ள லிங்க்கை கிளிக் செய்யவும்:</p>
    <div style="margin-top: 10px;">
      <a href="https://t.me/VetriTNPSCApp" class="btn-join" style="background: #0088cc; margin: 4px;">✈️ Telegram சேனல்: @VetriTNPSCApp</a>
      <a href="https://vetri-tnpsc-content.vercel.app" class="btn-join" style="background: #16a34a; margin: 4px;">📱 ஆன்லைன் Mock Test எழுதுங்கள்</a>
    </div>
  </div>

</body>
</html>
"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    cmd = [
        chrome,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_path}',
        f'file:///{html_path}'
    ]
    subprocess.run(cmd, check=True)

    if os.path.exists(html_path):
        os.remove(html_path)

    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"SUCCESS: Generated PDF at {pdf_path} ({size_kb:.1f} KB)")
    else:
        print("ERROR: PDF was not generated.")

if __name__ == '__main__':
    create_study_pdf()
