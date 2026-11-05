const fs = require('fs');
const path = require('path');

const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const CHANNEL_ID = '@VetriTNPSCApp';
const APP_URL = 'https://vetri-tnpsc-content.vercel.app';
const PDF_URL = `${APP_URL}/materials/vetri_tnpsc_group4_tamil_golden_revision.pdf`;

// Helper to call Telegram API
async function tg(method, body) {
  if (!BOT_TOKEN) {
    console.error('TELEGRAM_BOT_TOKEN is not configured');
    return { ok: false };
  }
  const url = `https://api.telegram.org/bot${BOT_TOKEN}/${method}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return res.json();
}

// Load content.json
function getQuestions() {
  try {
    const filePath = path.join(process.cwd(), 'content.json');
    if (fs.existsSync(filePath)) {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      return data.questions || [];
    }
  } catch (err) {
    console.error('Error reading content.json:', err);
  }
  return [];
}

// Check if user is a member of @VetriTNPSCApp
async function isChannelMember(userId) {
  try {
    const res = await tg('getChatMember', {
      chat_id: CHANNEL_ID,
      user_id: userId,
    });
    if (res.ok && res.result) {
      const status = res.result.status;
      return ['creator', 'administrator', 'member', 'restricted'].includes(status);
    }
  } catch (err) {
    console.error('Error checking membership:', err);
  }
  return false;
}

// Send Quiz Poll
async function sendQuizPoll(chatId, filterSubject = null) {
  let questions = getQuestions();
  if (filterSubject) {
    const filtered = questions.filter((q) => q.s === filterSubject);
    if (filtered.length > 0) questions = filtered;
  }
  if (!questions || questions.length === 0) {
    return tg('sendMessage', {
      chat_id: chatId,
      text: 'மன்னிக்கவும், தற்போது வினாக்கள் கிடைக்கவில்லை. சிறிது நேரம் கழித்து முயற்சிக்கவும்.',
    });
  }

  const q = questions[Math.floor(Math.random() * questions.length)];
  return tg('sendPoll', {
    chat_id: chatId,
    question: (q.q || '').slice(0, 300),
    options: (q.o || []).slice(0, 10),
    type: 'quiz',
    correct_option_id: q.a || 0,
    explanation: (q.e || '').slice(0, 200),
    is_anonymous: false,
  });
}

// Send Force-Join / PDF Material response
async function handleMaterialRequest(chatId, userId) {
  const isMember = await isChannelMember(userId);

  if (isMember) {
    const text = 
      `🎉 *வாழ்த்துகள்! நீங்கள் நமது அதிகாரப்பூர்வ சேனலில் இணைந்துள்ளதை உறுதி செய்தோம்!* 📚✨\n\n` +
      `இதோ உங்கள் TNPSC Group 4 & 2 தயாரிப்பிற்கான பிரத்யேக இலவச பாடக்குறிப்புகள்:\n\n` +
      `📕 *1. பொதுத்தமிழ் கோல்டன் ரிவிஷன் கையேடு (Direct PDF):*\n` +
      `சான்றோர்கள், அடைமொழிகள், 18 கீழ்க்கணக்கு நூல்கள், சொல்லும் பொருளும் & மாதிரி வினாக்கள் அடங்கியது.\n` +
      `👉 [இங்கே கிளிக் செய்து PDF தரவிறக்குங்கள்](${PDF_URL})\n\n` +
      `📖 *2. 6 முதல் 12-ஆம் வகுப்பு சமச்சீர் பாடப்புத்தகங்கள் (அதிகாரப்பூர்வ PDF):*\n` +
      `👉 https://tnschools.gov.in/textbooks\n\n` +
      `📱 *3. 50 வினாக்கள் OMR மாதிரி தேர்வுகள் (Mock Tests):*\n` +
      `👉 ${APP_URL}\n\n` +
      `💡 மேலும் புதிய வினாக்களை தினமும் எழுத @VetriTNPSCApp சேனலில் இணைந்திருங்கள்!`;

    const markup = {
      inline_keyboard: [
        [{ text: '📥 Golden Revision PDF தரவிறக்கம் செய்', url: PDF_URL }],
        [{ text: '🎯 வினாடி வினா எழுது (/quiz)', callback_data: 'run_quiz' }],
        [{ text: '🎁 நண்பர்களை அழைக்க & VIP வினாக்கள் பெற (/invite)', callback_data: 'run_invite' }],
        [{ text: '📱 Vetri TNPSC App-ல் பயிற்சி செய்', url: APP_URL }],
      ],
    };

    return tg('sendMessage', {
      chat_id: chatId,
      text: text,
      parse_mode: 'Markdown',
      disable_web_page_preview: false,
      reply_markup: markup,
    });
  } else {
    const text = 
      `⚠️ *இலவச Study Material PDF & பாடக்குறிப்புகளைப் பெற:*\n\n` +
      `முதலில் நமது அதிகாரப்பூர்வ Telegram சேனலான *@VetriTNPSCApp*-ல் இணைய வேண்டும்! \n\n` +
      `1. கீழே உள்ள *'சேனலில் இணையவும்'* பட்டனைத் தட்டி Join செய்யவும்.\n` +
      `2. பிறகு *'இணைந்துவிட்டேன் (Download PDF)'* பட்டனைத் தட்டவும்! 👇`;

    const markup = {
      inline_keyboard: [
        [{ text: '📢 @VetriTNPSCApp-ல் இணையவும்', url: 'https://t.me/VetriTNPSCApp' }],
        [{ text: '📥 இணைந்துவிட்டேன் (Download PDF)', callback_data: 'verify_join' }],
      ],
    };

    return tg('sendMessage', {
      chat_id: chatId,
      text: text,
      parse_mode: 'Markdown',
      reply_markup: markup,
    });
  }
}

// Handle Referral / Invite
async function handleInviteRequest(chatId, userId) {
  const inviteLink = `https://t.me/VetriTNPSCQuizBot?start=ref_${userId}`;
  const shareText = 
    `🎯 TNPSC Group 4 & 2 தேர்வுக்கு தயாராகிறீர்களா? 📚✨\n` +
    `தினசரி இலவச வினாடி வினா, சமச்சீர் தமிழ் குறிப்புகள் & Golden Revision PDF பெற வெற்றி TNPSC Bot-ல் இணையுங்கள்! 👇\n` +
    inviteLink;
  const tgShareUrl = `https://t.me/share/url?url=${encodeURIComponent(inviteLink)}&text=${encodeURIComponent('🎯 TNPSC Group 4 & 2 இலவச வினாடி வினா & Golden Revision PDF பெற வெற்றி TNPSC Bot-ல் இணையுங்கள்! 📚✨')}`;
  const waShareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareText)}`;

  const text = 
    `🎁 *வெற்றி TNPSC நண்பர்கள் அழைப்பு திட்டம் (Invite & Earn VIP Rewards)!* 🌟\n\n` +
    `உங்கள் தனிப்பட்ட Referral Link:\n` +
    `👉 \`${inviteLink}\`\n\n` +
    `💡 *எப்படி செயல்படுகிறது?*\n` +
    `1. கீழே உள்ள *'Telegram-ல் பகிருங்கள்'* அல்லது *'WhatsApp-ல் பகிருங்கள்'* பட்டனைத் தட்டி உங்கள் TNPSC நண்பர்கள் மற்றும் ஸ்டடி குரூப்களுக்கு பகிருங்கள்.\n` +
    `2. உங்கள் நண்பர்கள் இந்த லிங்கை கிளிக் செய்து இணையும்போது, நீங்கள் புதிய பிரத்யேக Mock Tests மற்றும் VIP Study Materials இலவசமாக பெறலாம்!\n\n` +
    `இப்போதே ஒரு நண்பருக்கு பகிர்ந்து உதவுங்கள்! 👇`;

  const markup = {
    inline_keyboard: [
      [{ text: '✈️ Telegram-ல் பகிருங்கள் (1-Tap Share)', url: tgShareUrl }],
      [{ text: '💬 WhatsApp-ல் பகிருங்கள்', url: waShareUrl }],
      [{ text: '🎯 வினாடி வினா எழுது (/quiz)', callback_data: 'run_quiz' }],
      [{ text: '📥 இலவச Study Material PDF (/pdf)', callback_data: 'get_pdf' }],
    ],
  };

  return tg('sendMessage', {
    chat_id: chatId,
    text: text,
    parse_mode: 'Markdown',
    reply_markup: markup,
  });
}

// Main serverless handler
module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(200).send('Vetri TNPSC Telegram Webhook Serverless Function is active 🚀');
  }

  const update = req.body;
  if (!update) {
    return res.status(200).json({ ok: true });
  }

  try {
    // 1. Handle Callback Queries (Button Clicks)
    if (update.callback_query) {
      const cb = update.callback_query;
      const chatId = cb.message.chat.id;
      const userId = cb.from.id;
      const data = cb.data;

      if (data === 'verify_join') {
        const isMember = await isChannelMember(userId);
        if (isMember) {
          await tg('answerCallbackQuery', {
            callback_query_id: cb.id,
            text: 'நன்றி! நீங்கள் சேனலில் இணைந்துள்ளீர்கள்!',
            show_alert: true,
          });
          await handleMaterialRequest(chatId, userId);
        } else {
          await tg('answerCallbackQuery', {
            callback_query_id: cb.id,
            text: 'தயவுசெய்து முதலில் @VetriTNPSCApp சேனலில் "Join" செய்யவும்!',
            show_alert: true,
          });
        }
      } else if (data === 'run_quiz') {
        await tg('answerCallbackQuery', { callback_query_id: cb.id });
        await sendQuizPoll(chatId);
      } else if (data === 'run_invite') {
        await tg('answerCallbackQuery', { callback_query_id: cb.id });
        await handleInviteRequest(chatId, userId);
      } else if (data === 'get_pdf') {
        await tg('answerCallbackQuery', { callback_query_id: cb.id });
        await handleMaterialRequest(chatId, userId);
      }
      return res.status(200).json({ ok: true });
    }

    // 2. Handle Text Messages
    const message = update.message;
    if (!message || !message.text) {
      return res.status(200).json({ ok: true });
    }

    const chatId = message.chat.id;
    const userId = message.from.id;
    const text = message.text.trim();
    const firstName = message.from.first_name || 'தோழரே';

    // Handle /start (with possible referral parameter: /start ref_12345)
    if (text.startsWith('/start')) {
      const parts = text.split(' ');
      if (parts.length > 1) {
        const param = parts[1];
        if (param.startsWith('ref_')) {
          const inviterId = param.replace('ref_', '');
          if (inviterId && inviterId !== String(userId)) {
            // Notify inviter
            try {
              await tg('sendMessage', {
                chat_id: inviterId,
                text: `🎉 *சூப்பர் செய்தி!* உங்கள் நண்பர் *${firstName}* உங்கள் அழைப்பின் மூலம் வெற்றி TNPSC Bot-ல் இணைந்துள்ளார்! 🚀✨\n\nதொடர்ந்து நண்பர்களை அழைத்து VIP மெட்டீரியல்களை அன்லாக் செய்யுங்கள்! (/invite)`,
                parse_mode: 'Markdown',
              });
            } catch (err) {
              console.error('Failed to notify inviter:', err);
            }
          }
        } else if (param.includes('pdf') || param.includes('material')) {
          await handleMaterialRequest(chatId, userId);
          return res.status(200).json({ ok: true });
        }
      }

      const welcomeText = 
        `வணக்கம் ${firstName}! 🎯 *Vetri TNPSC* அதிகாரப்பூர்வ வினாடி வினா பாட்டிற்கு உங்களை அன்போடு வரவேற்கிறோம்! 📚✨\n\n` +
        `TNPSC Group 4, Group 2 & VAO தேர்வுகளுக்கு தயாராக நீங்கள் விரும்பியவாறு பயிற்சி பெறலாம்:\n\n` +
        `🔹 */quiz* — உடனடி நேரடி வினாடி வினா\n` +
        `🔹 */tamil* — 6-12 சமச்சீர் பொதுத்தமிழ் இலக்கணம் & இலக்கியம்\n` +
        `🔹 */ca* — இன்றைய புதிய நடப்பு நிகழ்வுகள்\n` +
        `🔹 */invite* — நண்பர்களை அழைத்து VIP தேர்வுகள் பெற\n` +
        `🔹 */pdf* — பொதுத்தமிழ் Golden Revision PDF & குறிப்புகள்\n\n` +
        `கீழே உள்ள பட்டன்களைப் பயன்படுத்தி உடனே தொடங்கலாம்! 👇`;

      const markup = {
        keyboard: [
          [{ text: '🎯 ஒரு வினாடி வினா எழுது (/quiz)' }, { text: '🎁 நண்பர்களை அழைக்க (/invite)' }],
          [{ text: '📚 சமச்சீர் தமிழ் (/tamil)' }, { text: '⚡ நடப்பு நிகழ்வுகள் (/ca)' }],
          [{ text: '📥 இலவச Golden Revision PDF (/pdf)' }],
        ],
        resize_keyboard: true,
        one_time_keyboard: false,
      };

      await tg('sendMessage', {
        chat_id: chatId,
        text: welcomeText,
        parse_mode: 'Markdown',
        reply_markup: markup,
      });
      return res.status(200).json({ ok: true });
    }

    if (text === '/quiz' || text.includes('/quiz') || text.includes('ஒரு வினாடி வினா')) {
      await sendQuizPoll(chatId);
      return res.status(200).json({ ok: true });
    }

    if (text === '/tamil' || text.includes('/tamil') || text.includes('சமச்சீர் தமிழ்')) {
      await sendQuizPoll(chatId, 'ta');
      return res.status(200).json({ ok: true });
    }

    if (text === '/ca' || text.includes('/ca') || text.includes('நடப்பு நிகழ்வுகள்')) {
      await sendQuizPoll(chatId, 'ca');
      return res.status(200).json({ ok: true });
    }

    if (text === '/invite' || text.includes('/invite') || text.includes('நண்பர்களை அழைக்க')) {
      await handleInviteRequest(chatId, userId);
      return res.status(200).json({ ok: true });
    }

    if (text === '/pdf' || text.includes('/pdf') || text.includes('Study Material') || text.includes('Golden Revision')) {
      await handleMaterialRequest(chatId, userId);
      return res.status(200).json({ ok: true });
    }

    // Default reply
    await tg('sendMessage', {
      chat_id: chatId,
      text: `வணக்கம் ${firstName}! வினாடி வினா எழுத /quiz அல்லது சமச்சீர் தமிழ் படிக்க /tamil அல்லது நண்பர்களை அழைக்க /invite அல்லது Study Material பெற /pdf என டைப் செய்யவும்! 🎯`,
    });

  } catch (err) {
    console.error('Error handling webhook update:', err);
  }

  return res.status(200).json({ ok: true });
};
