import os
import json
import subprocess
import shutil

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
FFMPEG_PATH = shutil.which('ffmpeg') or r'C:\Users\manir\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.EXE'

def generate_short_video(question_idx=0, output_name='tnpsc_quiz_short_01.mp4'):
    os.makedirs('shorts', exist_ok=True)
    os.makedirs('temp_slides', exist_ok=True)

    # 1. Load Question
    with open('content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    questions = data.get('questions', [])
    if not questions:
        print("No questions found in content.json")
        return

    q = questions[question_idx % len(questions)]
    question_text = q.get('q', '')
    options = q.get('o', [])
    correct_idx = q.get('a', 0)
    explanation = q.get('e', '')
    letters = ['A', 'B', 'C', 'D']

    # 2. Template CSS & Base HTML
    base_css = """
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@500;700;800;900&display=swap');
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
        width: 1080px;
        height: 1920px;
        background: radial-gradient(circle at 50% 20%, #431407 0%, #1e0904 40%, #0a0301 100%),
                    linear-gradient(180deg, #18052e 0%, #0d021c 100%);
        background-color: #0d021c;
        color: #ffffff;
        font-family: 'Mukta Malar', 'Latha', 'Nirmala UI', sans-serif;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        padding: 90px 60px 100px;
        overflow: hidden;
    }
    .top-badge {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0f172a;
        font-weight: 900;
        font-size: 38px;
        padding: 16px 40px;
        border-radius: 100px;
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .question-card {
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(20px);
        border-radius: 36px;
        padding: 50px 44px;
        width: 100%;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }
    .q-title {
        font-size: 46px;
        font-weight: 800;
        line-height: 1.45;
        color: #ffffff;
        margin-bottom: 40px;
        text-align: center;
    }
    .options-grid {
        display: flex;
        flex-direction: column;
        gap: 24px;
        width: 100%;
    }
    .option-row {
        background: rgba(255, 255, 255, 0.06);
        border: 2px solid rgba(255, 255, 255, 0.16);
        border-radius: 24px;
        padding: 24px 30px;
        display: flex;
        align-items: center;
        gap: 24px;
        font-size: 38px;
        font-weight: 700;
    }
    .opt-circle {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
        font-weight: 900;
        flex-shrink: 0;
    }
    .option-row.correct {
        background: rgba(34, 197, 94, 0.35) !important;
        border-color: #22c55e !important;
        box-shadow: 0 0 30px rgba(34, 197, 94, 0.6);
        color: #86efac !important;
    }
    .option-row.correct .opt-circle {
        background: #22c55e;
        color: #052e16;
    }
    .timer-bar-wrap {
        width: 100%;
        height: 18px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 10px;
        overflow: hidden;
        margin-top: 40px;
    }
    .timer-bar {
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, #ef4444, #f59e0b, #10b981);
    }
    .footer-cta {
        text-align: center;
        width: 100%;
    }
    .footer-cta h3 {
        font-size: 38px;
        font-weight: 800;
        color: #fde047;
        margin-bottom: 12px;
    }
    .footer-cta p {
        font-size: 30px;
        color: #cbd5e1;
    }
    """

    # Generate Slide 1: Question + Options (Neutral)
    options_html_1 = ""
    for idx, opt in enumerate(options[:4]):
        options_html_1 += f"""
        <div class="option-row">
            <div class="opt-circle">{letters[idx]}</div>
            <div>{opt}</div>
        </div>
        """

    slide1_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base_css}</style></head>
    <body>
        <div class="top-badge">🎯 வெற்றி TNPSC குரூப் 4 & 2 சவால்</div>
        <div class="question-card">
            <div class="q-title">{question_text}</div>
            <div class="options-grid">
                {options_html_1}
            </div>
            <div class="timer-bar-wrap">
                <div class="timer-bar"></div>
            </div>
        </div>
        <div class="footer-cta">
            <h3>⏳ விடையை யோசியுங்கள்! (5 வினாடிகள்)</h3>
            <p>கமெண்ட்டில் உங்கள் விடையை பதிவிடுங்கள் 👇</p>
        </div>
    </body></html>
    """

    # Generate Slide 2: Correct Option Highlighted + Explanation
    options_html_2 = ""
    for idx, opt in enumerate(options[:4]):
        is_correct = (idx == correct_idx)
        cls = "option-row correct" if is_correct else "option-row"
        options_html_2 += f"""
        <div class="{cls}">
            <div class="opt-circle">{"✓" if is_correct else letters[idx]}</div>
            <div>{opt}</div>
        </div>
        """

    slide2_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base_css}
        .exp-box {{
            margin-top: 30px;
            background: rgba(59, 130, 246, 0.25);
            border-left: 6px solid #3b82f6;
            padding: 24px 30px;
            border-radius: 0 16px 16px 0;
            font-size: 32px;
            color: #93c5fd;
            line-height: 1.45;
        }}
    </style></head>
    <body>
        <div class="top-badge" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white;">
            🎉 சரியான விடை: {letters[correct_idx]}!
        </div>
        <div class="question-card">
            <div class="q-title">{question_text}</div>
            <div class="options-grid">
                {options_html_2}
            </div>
            {f'<div class="exp-box">💡 <b>விளக்கம்:</b> {explanation}</div>' if explanation else ''}
        </div>
        <div class="footer-cta">
            <h3>👏 நீங்கள் சரியாக விடையளித்தீர்களா?</h3>
            <p>அடுத்த வினாடி-வினாவிற்கு சேனலை சப்ஸ்கிரைப் செய்யவும்!</p>
        </div>
    </body></html>
    """

    # Generate Slide 3: Outro Screen
    slide3_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{base_css}
        .outro-card {{
            background: rgba(255, 255, 255, 0.08);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 40px;
            padding: 60px 40px;
            text-align: center;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        }}
        .tg-badge {{
            display: inline-block;
            background: #0088cc;
            color: white;
            font-size: 40px;
            font-weight: 800;
            padding: 24px 50px;
            border-radius: 100px;
            margin: 40px 0;
            box-shadow: 0 10px 30px rgba(0, 136, 204, 0.4);
        }}
    </style></head>
    <body>
        <div class="top-badge">📚 இலவச TNPSC Study Materials</div>
        <div class="outro-card">
            <h1 style="font-size: 56px; color: #fde047; margin-bottom: 24px;">தினமும் 50 வினாக்கள் OMR மாதிரி தேர்வு எழுத!</h1>
            <p style="font-size: 36px; line-height: 1.6; color: #e2e8f0;">
                சமச்சீர் பாடப்புத்தகங்கள் & பொதுத்தமிழ் Golden Revision PDF இலவசமாகப் பெற:
            </p>
            <div class="tg-badge">✈️ Telegram: @VetriTNPSCApp</div>
            <p style="font-size: 34px; color: #a5f3fc; font-weight: 700;">
                கமெண்ட் பாக்ஸில் உள்ள நேரடி லிங்க்கை கிளிக் செய்யவும்! 👇
            </p>
        </div>
        <div class="footer-cta">
            <h3>📱 Vetri TNPSC App - Google Play Store</h3>
            <p>vetri-tnpsc-content.vercel.app</p>
        </div>
    </body></html>
    """

    slides = [
        ('temp_slides/slide1.html', 'temp_slides/slide1.png', slide1_html),
        ('temp_slides/slide2.html', 'temp_slides/slide2.png', slide2_html),
        ('temp_slides/slide3.html', 'temp_slides/slide3.png', slide3_html),
    ]

    print("Rendering slides to 1080x1920 PNG images using Chrome...")
    for html_file, png_file, content in slides:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        cmd = [
            CHROME_PATH,
            '--headless=new',
            '--disable-gpu',
            '--window-size=1080,1920',
            '--hide-scrollbars',
            f'--screenshot={os.path.abspath(png_file)}',
            f'file:///{os.path.abspath(html_file)}'
        ]
        subprocess.run(cmd, check=True)

    # 3. Stitch with ffmpeg
    output_path = os.path.join('shorts', output_name)
    print(f"Stitching video using ffmpeg to {output_path}...")

    # Slide 1: 5s, Slide 2: 5s, Slide 3: 4s -> Total 14s
    concat_file = 'temp_slides/concat.txt'
    with open(concat_file, 'w', encoding='utf-8') as f:
        f.write(f"file '{os.path.abspath('temp_slides/slide1.png')}'\n")
        f.write("duration 5.5\n")
        f.write(f"file '{os.path.abspath('temp_slides/slide2.png')}'\n")
        f.write("duration 5.5\n")
        f.write(f"file '{os.path.abspath('temp_slides/slide3.png')}'\n")
        f.write("duration 3.5\n")
        f.write(f"file '{os.path.abspath('temp_slides/slide3.png')}'\n")

    cmd = [
        FFMPEG_PATH, '-y',
        '-f', 'concat', '-safe', '0', '-i', concat_file,
        '-pix_fmt', 'yuv420p',
        '-c:v', 'libx264',
        '-r', '30',
        output_path
    ]
    subprocess.run(cmd, check=True)

    # Cleanup temp
    shutil.rmtree('temp_slides', ignore_errors=True)

    if os.path.exists(output_path):
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"SUCCESS: Generated YouTube Short video at {output_path} ({size_mb:.2f} MB)")
        return output_path
    else:
        print("ERROR: Failed to create video.")
        return None

if __name__ == '__main__':
    generate_short_video(0, 'tnpsc_group4_daily_short_01.mp4')
