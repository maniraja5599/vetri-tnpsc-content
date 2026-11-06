import json
from datetime import datetime

with open('content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_questions = [
  {
    "id": "ta0001",
    "s": "ta",
    "t": "கவிதை & இலக்கியம்",
    "d": "2026-11-06",
    "q": "தமிழ்ப்பசி என்னும் தலைப்பிலான புகழ்பெற்ற பாடலை இயற்றியவர் யார்?",
    "qe": "Who authored the renowned poem titled 'Thamizh Pasi'?",
    "o": ["பாரதிதாசன்", "க. சச்சிதானந்தன்", "முடியரசன்", "வாணிதாசன்"],
    "oe": ["Bharathidasan", "K. Satchidanandan", "Mudiyarasan", "Vaanidasan"],
    "a": 1,
    "e": "தமிழ்ப்பசி என்னும் உணர்ச்சிமிக்க பாடலை இயற்றியவர் ஈழத்துக் கவிஞர் க. சச்சிதானந்தன் ஆவார் (9-ஆம் வகுப்பு சமச்சீர் தமிழ்)."
  },
  {
    "id": "ta0002",
    "s": "ta",
    "t": "ஐஞ்சிறு காப்பியங்கள்",
    "d": "2026-11-06",
    "q": "குண்டலகேசி என்னும் பௌத்த நூலுக்கு மறுப்பாக எழுதப்பட்ட சமண தர்க்க நூல் எது?",
    "qe": "Which Jain work was written as a refutation to the Buddhist epic Kundalakesi?",
    "o": ["மணிமேகலை", "நீலகேசி", "வளையாபதி", "யசோதர காவியம்"],
    "oe": ["Manimekalai", "Neelakesi", "Valayapathi", "Yasodhara Kaviyam"],
    "a": 1,
    "e": "குண்டலகேசிக்கு மறுப்பாக எழுதப்பட்ட தர்க்க நூல் நீலகேசி ஆகும். இது ஐஞ்சிறு காப்பியங்களுள் ஒன்றாகும்."
  },
  {
    "id": "ta0003",
    "s": "ta",
    "t": "சான்றோர்கள் & அடைமொழிகள்",
    "d": "2026-11-06",
    "q": "சொல்லின் செல்வர் என்று தமிழ் அறிஞர்களால் போற்றப்படுபவர் யார்?",
    "qe": "Who among Tamil scholars is widely celebrated with the title 'Solin Selvar'?",
    "o": ["ரா. பி. சேதுப்பிள்ளை", "திரு. வி. கலியாணசுந்தரனார்", "உ. வே. சாமிநாதையர்", "பரிதிமாற்கலைஞர்"],
    "oe": ["R. P. Sethupillai", "Thiru. Vi. Ka.", "U. V. Swaminatha Iyer", "Parithimar Kalaignar"],
    "a": 0,
    "e": "ரா. பி. சேதுப்பிள்ளை சொல்லின் செல்வர் எனப் புகழப்படுகிறார். (இலக்கியத்தில் அனுமன் சொல்லின் செல்வன் என அழைக்கப்படுகிறார்)."
  },
  {
    "id": "ta0004",
    "s": "ta",
    "t": "அகராதியியல்",
    "d": "2026-11-06",
    "q": "வீரமாமுனிவர் 1732-இல் தொகுத்து வெளியிட்ட தமிழின் முதல் அகரமுதலி எது?",
    "qe": "Which is considered the first Tamil dictionary, compiled by Veeramamunivar in 1732?",
    "o": ["திவாகர நிகண்டு", "சதுரகராதி", "பிங்கல நிகண்டு", "சூடாமணி நிகண்டு"],
    "oe": ["Thivakara Nigandu", "Chathuragarathi", "Pingala Nigandu", "Choodamani Nigandu"],
    "a": 1,
    "e": "வீரமாமுனிவர் இயற்றிய சதுரகராதி தமிழின் முதல் அகராதியாகும். இது பெயர், பொருள், தொகை, தொடை என 4 பிரிவுகளைக் கொண்டது."
  },
  {
    "id": "ta0005",
    "s": "ta",
    "t": "திராவிட மொழியியல்",
    "d": "2026-11-06",
    "q": "திராவிட மொழிகளின் ஒப்பிலக்கணம் (A Comparative Grammar of the Dravidian Languages) என்ற நூலை 1856-இல் வெளியிட்டவர் யார்?",
    "qe": "Who published the landmark work 'A Comparative Grammar of the Dravidian Languages' in 1856?",
    "o": ["ஜி. யு. போப்", "ராபர்ட் கால்டுவெல்", "வீரமாமுனிவர்", "பிரான்சிஸ் எல்லிஸ்"],
    "oe": ["G. U. Pope", "Robert Caldwell", "Veeramamunivar", "Francis Ellis"],
    "a": 1,
    "e": "ராபர்ட் கால்டுவெல் 1856-இல் இந்நாலை வெளியிட்டு, திராவிட மொழிகள் சமஸ்கிருத சார்பற்ற தனித்துக் குடும்பம் என்பதை நிறுவினார்."
  },
  {
    "id": "ta0006",
    "s": "ta",
    "t": "சங்க இலக்கியம்",
    "d": "2026-11-06",
    "q": "உண்டி கொடுத்தோர் உயிர் கொடுத்தோரே - என்னும் வரலாற்றுப் பாடல் வரிகள் இடம்பெற்றுள்ள சங்க நூல் எது?",
    "qe": "In which Sangam work does the celebrated verse 'Undi Koduthor Uyir Koduthore' prominently appear?",
    "o": ["அகநானூறு", "புறநானூறு", "நற்றிணை", "ஐங்குறுநூறு"],
    "oe": ["Agananuru", "Purananuru", "Natrinai", "Ainkurunuru"],
    "a": 1,
    "e": "புறநானூற்றில் குடபுலவியனார் பாண்டியன் நெடுஞ்செழியனுக்கு பாடிய 18-ஆம் பாடலில் இவ்வரிகள் இடம்பெற்றுள்ளன. (மணிமேகலையிலும் இதே வரி வருகிறது)."
  },
  {
    "id": "ta0007",
    "s": "ta",
    "t": "தமிழ் இலக்கணம்",
    "d": "2026-11-06",
    "q": "தமிழ் இலக்கணத்தில் பகுபத உறுப்புகள் மொத்தம் எத்தனை வகைப்படும்?",
    "qe": "In Tamil grammar, into how many components (Pagupadha Uruppukal) can a word be segmented?",
    "o": ["4 வகைகள்", "5 வகைகள்", "6 வகைகள்", "7 வகைகள்"],
    "oe": ["4 types", "5 types", "6 types", "7 types"],
    "a": 2,
    "e": "பகுபத உறுப்புகள் 6 வகைப்படும். அவை: பகுதி, விகுதி, இடைநிலை, சந்தி, சாரியை, விகாரம் ஆகும்."
  },
  {
    "id": "ta0008",
    "s": "ta",
    "t": "சான்றோர்கள் & அடைமொழிகள்",
    "d": "2026-11-06",
    "q": "மேடைத் தமிழின் முன்னோடியும், சிறந்த எழுத்தாளருமான திரு. வி. க. எவ்வாறு சிறப்பிக்கப்படுகிறார்?",
    "qe": "By what affectionate honorific is the scholar-orator Thiru. Vi. Kalyanasundaranar known?",
    "o": ["தமிழ் தென்றல்", "தமிழ் தாத்தா", "கவிமணி", "தனித்தமிழ் தந்தை"],
    "oe": ["Thamizh Thendral", "Thamizh Thaatha", "Kavimani", "Thani Thamizh Thanthai"],
    "a": 0,
    "e": "திரு. வி. கலியாணசுந்தரனார் மனித வாழ்க்கையும் காந்தியடிகளும், பெண்ணின் பெருமை போன்ற நூல்களை எழுதியவர்; இவர் தமிழ்த்தென்றல் எனப்படுகிறார்."
  },
  {
    "id": "ta0009",
    "s": "ta",
    "t": "பாரதியார் வாழ்க்கை",
    "d": "2026-11-06",
    "q": "சுப்பிரமணிய பாரதியாரின் 11-ஆம் வயதில் அவரது கவிப்புலமையைப் பாராட்டி பாரதி பட்டம் வழங்கியவர் யார்?",
    "qe": "Who conferred the title 'Bharathi' on poet Subramania Bharathi when he was just 11 years old?",
    "o": ["எட்டயபுர மன்னர்", "வ. உ. சிதம்பரனார்", "பாரதிதாசன்", "சேதுபதி மன்னர்"],
    "oe": ["King of Ettayapuram", "V. O. Chidambaranar", "Bharathidasan", "King Sethupathi"],
    "a": 0,
    "e": "எட்டயபுர சமஸ்தானத்து மன்னர் பாரதியாரின் கவித்திறமையைக் கண்டு வியந்து அவருக்கு பாரதி (சரஸ்வதி) என்ற பட்டத்தை அளித்தார்."
  },
  {
    "id": "ta0010",
    "s": "ta",
    "t": "திருக்குறள் சிறப்புகள்",
    "d": "2026-11-06",
    "q": "திருக்குறள் முழுவதிலும் இடம்பெற்றுள்ள இரு மரங்கள் எவை?",
    "qe": "Which two trees are explicitly mentioned across the verses of Thirukkural?",
    "o": ["பனை, மூங்கில்", "வேம்பு, ஆலமரம்", "மாமரம், தென்னை", "புன்னை, மருது"],
    "oe": ["Palmyra & Bamboo", "Neem & Banyan", "Mango & Coconut", "Punnai & Marudhu"],
    "a": 0,
    "e": "திருக்குறளில் குறிப்பிடப்பட்டுள்ள இரண்டு மரங்கள்: பனை மற்றும் மூங்கில். (இடம்பெற்ற ஒரே விதை: குன்றிமணி)."
  },
  {
    "id": "ta0011",
    "s": "ta",
    "t": "பதினெண்மேற்கணக்கு",
    "d": "2026-11-06",
    "q": "எட்டுத்தொகை நூல்களுள் ஒன்றான நற்றிணை நூலைத் தொகுப்பித்த மன்னர் யார்?",
    "qe": "Which patron king commissioned the compilation of the Sangam anthology 'Natrinai'?",
    "o": ["பன்னாடு தந்த மாறன் வழுதி", "உக்கிரப் பெருவழுதி", "பூரிக்கோ", "சேரன் செங்குட்டுவன்"],
    "oe": ["Pannadu Thantha Maran Vazhuthi", "Ukkira Peru Vazhuthi", "Poorikko", "Cheran Senguttuvan"],
    "a": 0,
    "e": "நற்றிணையைத் தொகுத்தவர் பெயர் அறியப்படவில்லை. ஆனால் இந்நூலை தொகுப்பித்தவர் பாண்டிய மன்னன் பன்னாடு தந்த பாண்டியன் மாறன் வழுதி ஆவார்."
  },
  {
    "id": "ta0012",
    "s": "ta",
    "t": "திருவள்ளுவர் சிறப்புகள்",
    "d": "2026-11-06",
    "q": "மாதனுபங்கி, செந்நாப்போதார், பொய்யில் புலவர் ஆகிய சிறப்புப் பெயர்கள் யாரைக் குறிக்கும்?",
    "qe": "To which revered poet do the titles Madhanubangi, Sennaapothar, and Poyyil Pulavar refer?",
    "o": ["திருவள்ளுவர்", "கம்பர்", "இளங்கோவடிகள்", "கபிலர்"],
    "oe": ["Thiruvalluvar", "Kambar", "Ilango Adigal", "Kapilar"],
    "a": 0,
    "e": "உலகப் பொதுமறையாம் திருக்குறளை யாத்த திருவள்ளுவருக்கு மாதனுபங்கி, செந்நாப்போதார், தெய்வப்புலவர், நாயனார் போன்ற சிறப்புப் பெயர்கள் உண்டு."
  },
  {
    "id": "ta0013",
    "s": "ta",
    "t": "சங்க இலக்கியம்",
    "d": "2026-11-06",
    "q": "யாதும் ஊரே யாவரும் கேளிர்; தீதும் நன்றும் பிறர்தர வாரா என்று உலகப் பொதுமையை முழங்கியவர் யார்?",
    "qe": "Who proclaimed universal brotherhood in Purananuru with the phrase 'Yathum Oore Yaavarum Kelir'?",
    "o": ["கணியன் பூங்குன்றனார்", "கபிலர்", "பரணர்", "ஔவையார்"],
    "oe": ["Kaniyan Poongundranar", "Kapilar", "Paranar", "Avvaiyar"],
    "a": 0,
    "e": "புறநானூற்றின் 192-ஆம் பாடலில் உலக மக்கள் யாவரும் உடன்பிறப்புகள் என்ற உன்னதக் கருத்தை கணியன் பூங்குன்றனார் வெளிப்படுத்தியுள்ளார்."
  },
  {
    "id": "ta0014",
    "s": "ta",
    "t": "சான்றோர்கள் & தமிழ் தொண்டு",
    "d": "2026-11-06",
    "q": "பனையோலைகளில் அழியும் நிலையில் இருந்த பண்டைத் தமிழ் நூல்களை அச்சு வடிவில் பதிப்பித்து மீட்ட தமிழ்த் தாத்தா யார்?",
    "qe": "Who is reverently remembered as 'Thamizh Thaatha' for preserving palm-leaf manuscripts into printed books?",
    "o": ["உ. வே. சாமிநாதையர்", "மறைமலை அடிகள்", "தேவநேயப் பாவாணர்", "பரிதிமாற்கலைஞர்"],
    "oe": ["U. V. Swaminatha Iyer", "Maraimalai Adigal", "Devaneya Pavanar", "Parithimar Kalaignar"],
    "a": 0,
    "e": "வாழ்நாள் முழுவதும் ஓலைச்சுவடிகளைத் தேடித் திரிந்து சிலப்பதிகாரம், மணிமேகலை, புறநானூறு முதலிய நூல்களை அச்சிட்ட உ. வே. சாமிநாதையர் தமிழ்த் தாத்தா எனப்படுகிறார்."
  },
  {
    "id": "ta0015",
    "s": "ta",
    "t": "தற்காலக் கவிதை",
    "d": "2026-11-06",
    "q": "தெய்வ வள்ளுவன் நெய்த குறள்தான் தேசம் உடுத்திய நூலாடை என்று திருக்குறளைப் போற்றிய கவிஞர் யார்?",
    "qe": "Which modern poet glorified Thirukkural as the garment worn by the nation in his poetry?",
    "o": ["தாராபாரதி", "சுரதா", "பட்டுக்கோட்டை கல்யாணசுந்தரம்", "கண்ணதாசன்"],
    "oe": ["Thara Bharathi", "Suradha", "Pattukkottai Kalyanasundaram", "Kannadasan"],
    "a": 0,
    "e": "கவிஞாயிறு தாராபாரதி தனது பாரதம் அன்றைய நாற்றங்கால் கவிதையில் திருக்குறளை தேசம் உடுத்திய நூலாடை என உவமித்துள்ளார்."
  }
]

existing_ids = set(q['id'] for q in data['questions'])
added = 0
for q in new_questions:
    if q['id'] not in existing_ids:
        data['questions'].append(q)
        added += 1

data['updated'] = datetime.now().strftime('%Y-%m-%d')
with open('content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully added {added} new General Tamil questions! Total questions now: {len(data['questions'])}")
