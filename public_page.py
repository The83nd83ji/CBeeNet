# public_page.py

def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>CBeeNet · گروه اشتراک</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800;14..32,900&family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ===== RESET & BASE ===== */
* {{ margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }}
:root {{
  --bg: #0a0a08;
  --surface: rgba(13, 13, 10, 0.75);
  --surface2: #1a1a15;
  --surface3: #22221c;
  --border: rgba(255, 215, 0, 0.08);
  --border-glow: rgba(255, 215, 0, 0.30);
  --text: #f5f5dc;
  --text2: #c8c8a0;
  --text3: #6b6b40;
  --primary: #ffd700;
  --primary-light: #ffe44d;
  --primary-dark: #d4a800;
  --secondary: #ffc107;
  --accent: #ffd700;
  --green: #66bb6a;
  --green-bg: rgba(102, 187, 106, 0.12);
  --red: #ef5350;
  --red-bg: rgba(239, 83, 80, 0.12);
  --radius: 24px;
  --shadow: 0 20px 60px rgba(0,0,0,0.7);
  --glow: 0 0 40px rgba(255,215,0,0.12);
}}
html, body {{ height:100%; }}
body {{
  font-family: 'Vazirmatn', 'Inter', sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  direction: rtl;
  overflow-x: hidden;
  background-image:
    radial-gradient(circle at 10% 20%, rgba(255,215,0,0.06) 0%, transparent 50%),
    radial-gradient(circle at 90% 80%, rgba(255,215,0,0.04) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 0%, var(--bg) 100%);
}}

/* ===== ANIMATED BACKGROUND PARTICLES ===== */
.particles {{
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}}
.particle {{
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(255,215,0,0.25);
  border-radius: 50%;
  animation: floatParticle linear infinite;
}}
@keyframes floatParticle {{
  0% {{ transform: translateY(100vh) scale(0); opacity:0; }}
  10% {{ opacity:1; }}
  90% {{ opacity:1; }}
  100% {{ transform: translateY(-10vh) scale(1); opacity:0; }}
}}

/* ===== MAIN WRAP ===== */
.wrap {{
  position: relative;
  z-index: 10;
  max-width: 540px;
  margin: 0 auto;
  padding: 24px 16px 48px;
}}

/* ===== HEADER ===== */
.header {{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px 0 20px;
}}
.logo-wrap {{
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: #1a1a15;
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: 0 0 0 6px rgba(255,215,0,0.06), 0 20px 50px rgba(255,215,0,0.10);
  transition: transform 0.4s ease, border-color 0.5s;
}}
.logo-wrap:hover {{ transform: scale(1.05) rotate(-4deg); }}

/* ===== BEE ANIMATION ===== */
.bee-container {{
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.bee-container svg {{
  width: 100%;
  height: 100%;
  display: block;
}}
.wing-container-left {{
  transform-origin: 42px 40px;
  animation: flapLeft 0.5s ease-in-out infinite alternate;
}}
.wing-container-right {{
  transform-origin: 58px 40px;
  animation: flapRight 0.5s ease-in-out infinite alternate;
}}
@keyframes flapLeft {{
  0% {{ transform: rotate(0deg) scaleY(1); }}
  100% {{ transform: rotate(-35deg) scaleY(0.8); }}
}}
@keyframes flapRight {{
  0% {{ transform: rotate(0deg) scaleY(1); }}
  100% {{ transform: rotate(35deg) scaleY(0.8); }}
}}

/* حالت خاموش (غیرفعال) */
.logo-wrap.bee-off {{
  border-color: #2a2a25;
  box-shadow: 0 0 0 6px rgba(255,255,255,0.02), 0 20px 50px rgba(0,0,0,0.3);
}}
.logo-wrap.bee-on {{
  border-color: var(--primary);
  box-shadow: 0 0 0 6px rgba(255,215,0,0.15), 0 20px 50px rgba(255,215,0,0.25);
}}
.bee-off .bee-container svg {{
  filter: grayscale(1) opacity(0.3) brightness(0.8);
}}
.bee-off .wing-container-left,
.bee-off .wing-container-right {{
  animation-play-state: paused;
}}

.brand {{
  font-size: 28px;
  font-weight: 900;
  margin-top: 16px;
  background: linear-gradient(135deg, var(--primary-light), var(--secondary), var(--primary-light));
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: gradShift 6s ease infinite;
}}
@keyframes gradShift {{
  0% {{ background-position: 0% 50%; }}
  50% {{ background-position: 100% 50%; }}
  100% {{ background-position: 0% 50%; }}
}}
.tagline {{
  font-size: 12px;
  color: var(--text3);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-weight: 600;
  margin-top: 4px;
}}
.tele-link {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 16px;
  padding: 8px 22px;
  border-radius: 40px;
  background: rgba(255,215,0,0.08);
  border: 1px solid rgba(255,215,0,0.15);
  color: var(--primary-light);
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.25s;
  backdrop-filter: blur(4px);
}}
.tele-link:hover {{
  background: rgba(255,215,0,0.18);
  border-color: var(--primary);
  box-shadow: 0 0 30px rgba(255,215,0,0.15);
  transform: translateY(-2px);
}}

/* ===== GLASS CARD ===== */
.glass {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}}

/* ===== INFO CARD ===== */
.info-card {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 22px 24px;
  margin: 18px 0 16px;
  position: relative;
  overflow: hidden;
  transition: border-color 0.3s;
}}
.info-card:hover {{ border-color: var(--border-glow); }}
.info-card .glow-spot {{
  position: absolute;
  top: -60px;
  right: -60px;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(255,215,0,0.06), transparent 70%);
  pointer-events: none;
}}
.info-eyebrow {{
  font-size: 11px;
  font-weight: 700;
  color: var(--primary-light);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}}
.info-name {{
  font-size: 24px;
  font-weight: 800;
  background: linear-gradient(135deg, #fff, var(--primary-light));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin-bottom: 4px;
}}
.info-desc {{
  font-size: 13px;
  color: var(--text2);
  line-height: 1.7;
}}

/* ===== STATS ROW ===== */
.stats {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 18px;
}}
.stat-item {{
  background: var(--surface2);
  border-radius: 18px;
  padding: 16px 8px;
  text-align: center;
  border: 1px solid var(--border);
  transition: all 0.25s;
}}
.stat-item:hover {{
  border-color: var(--border-glow);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}}
.stat-label {{
  font-size: 9px;
  font-weight: 700;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}
.stat-value {{
  font-size: 22px;
  font-weight: 800;
  margin-top: 4px;
  background: linear-gradient(135deg, var(--primary-light), var(--secondary));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.stat-sub {{
  font-size: 10px;
  color: var(--text3);
  margin-top: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
}}
.dot-live {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--green);
  display: inline-block;
  animation: pulse-dot 1.8s infinite;
}}
@keyframes pulse-dot {{
  0%,100% {{ opacity:1; transform:scale(1); }}
  50% {{ opacity:0.2; transform:scale(0.6); }}
}}

/* ===== COPY ALL BAR ===== */
.copy-all {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 14px 20px;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  background: linear-gradient(135deg, rgba(255,215,0,0.06), rgba(255,193,7,0.04));
  border-color: rgba(255,215,0,0.10);
}}
.copy-all-text {{
  flex: 1;
  min-width: 130px;
}}
.copy-all-title {{
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--primary-light);
}}
.copy-all-sub {{
  font-size: 10px;
  color: var(--text3);
}}
.btn-copy-all {{
  font-family: inherit;
  font-size: 13px;
  font-weight: 800;
  padding: 8px 20px;
  border: none;
  border-radius: 40px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #000;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.25s;
  box-shadow: 0 4px 20px rgba(255,215,0,0.3);
}}
.btn-copy-all:hover {{
  transform: scale(1.03);
  box-shadow: 0 6px 30px rgba(255,215,0,0.5);
}}

/* ===== CONFIG LIST ===== */
.section-header {{
  font-size: 13px;
  font-weight: 800;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  margin: 24px 0 14px;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.section-header i {{ color: var(--primary-light); font-size: 18px; }}

.config-item {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 14px;
  overflow: hidden;
  border-color: var(--border);
  transition: border-color 0.3s, box-shadow 0.3s;
}}
.config-item:hover {{
  border-color: var(--border-glow);
  box-shadow: var(--glow);
}}
.config-header {{
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  cursor: pointer;
  user-select: none;
  transition: background 0.2s;
}}
.config-header:hover {{
  background: rgba(255,215,0,0.03);
}}
.config-label {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 700;
  flex: 1;
  min-width: 0;
}}
.config-badge-proto {{
  font-size: 9px;
  padding: 2px 10px;
  border-radius: 30px;
  font-weight: 700;
  background: rgba(255,215,0,0.10);
  color: var(--primary-light);
}}
.config-status {{
  font-size: 10px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 30px;
  display: flex;
  align-items: center;
  gap: 5px;
  white-space: nowrap;
}}
.config-status.on {{
  background: var(--green-bg);
  color: var(--green);
  border: 1px solid rgba(102,187,106,0.2);
}}
.config-status.off {{
  background: var(--red-bg);
  color: var(--red);
  border: 1px solid rgba(239,83,80,0.2);
}}
.config-toggle {{
  font-size: 20px;
  color: var(--text3);
  transition: transform 0.3s;
}}
.config-toggle.open {{ transform: rotate(180deg); }}

.config-body {{
  padding: 0 20px 20px;
  display: none;
}}
.config-body.open {{ display: block; }}

.usage-bar-wrap {{
  margin: 10px 0 8px;
}}
.usage-meta {{
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text3);
  margin-bottom: 4px;
}}
.usage-meta b {{ color: var(--text2); }}
.bar-track {{
  height: 6px;
  border-radius: 10px;
  background: rgba(255,215,0,0.06);
  overflow: hidden;
}}
.bar-fill {{
  height: 100%;
  border-radius: 10px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  transition: width 0.8s cubic-bezier(0.2,0.9,0.3,1);
  width: 0%;
}}
.remain-tag {{
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 12px;
  border-radius: 30px;
  margin-top: 8px;
}}
.remain-tag.ok {{ background: var(--green-bg); color: var(--green); }}
.remain-tag.warn {{ background: rgba(255,215,0,0.10); color: var(--primary-light); }}
.remain-tag.danger {{ background: var(--red-bg); color: var(--red); }}

/* ===== SERVER LIST ===== */
.server-list {{
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--border);
}}
.server-list-title {{
  font-size: 10px;
  font-weight: 700;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 10px;
}}
.server-list-title i {{ color: var(--primary-light); }}
.server-row {{
  background: var(--surface3);
  border-radius: 14px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
  border: 1px solid var(--border);
  transition: border-color 0.2s;
}}
.server-row:hover {{ border-color: var(--border-glow); }}
.server-index {{
  font-size: 10px;
  font-weight: 700;
  color: var(--text3);
  min-width: 24px;
}}
.server-address {{
  flex: 1;
  font-family: 'Inter', monospace;
  font-size: 10.5px;
  color: var(--text2);
  direction: ltr;
  text-align: left;
  word-break: break-all;
  line-height: 1.5;
  min-width: 0;
}}
.btn-copy {{
  font-family: inherit;
  font-size: 10px;
  font-weight: 700;
  padding: 5px 14px;
  border: none;
  border-radius: 30px;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: #000;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}}
.btn-copy:hover {{ transform: scale(1.05); box-shadow: 0 4px 15px rgba(255,215,0,0.3); }}

/* ===== FOOTER ===== */
.footer {{
  text-align: center;
  margin-top: 32px;
  padding: 16px 0 4px;
  font-size: 10px;
  color: var(--text3);
  letter-spacing: 0.05em;
}}
.footer a {{
  color: var(--primary-light);
  font-weight: 700;
  text-decoration: none;
  transition: 0.2s;
}}
.footer a:hover {{ text-decoration: underline; color: var(--secondary); }}

/* ===== TOAST ===== */
.toast {{
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(80px);
  background: var(--surface2);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 12px 24px;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.2,0.9,0.3,1);
  z-index: 999;
  pointer-events: none;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.6);
}}
.toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
.toast.success {{ border-color: rgba(255,215,0,0.3); background: rgba(255,215,0,0.08); color: var(--primary-light); }}

/* ===== LOADING / EMPTY ===== */
.state-placeholder {{
  text-align: center;
  padding: 80px 20px;
}}
.state-placeholder i {{
  font-size: 52px;
  color: var(--text3);
  display: block;
  margin-bottom: 16px;
  opacity: 0.4;
}}
.state-placeholder p {{ font-size: 14px; color: var(--text3); }}
.spinner i {{
  animation: spin 1.2s linear infinite;
  color: var(--primary-light);
}}
@keyframes spin {{ to {{ transform: rotate(360deg); }} }}

/* ===== RESPONSIVE ===== */
@media (max-width: 480px) {{
  .stats {{ grid-template-columns: 1fr 1fr; }}
  .stats .stat-item:last-child {{ grid-column: 1 / -1; }}
  .copy-all {{ flex-direction: column; align-items: stretch; text-align: center; }}
  .btn-copy-all {{ justify-content: center; }}
  .config-header {{ flex-wrap: wrap; }}
  .config-label {{ min-width: 100%; }}
}}
@media (max-width: 380px) {{
  .stats {{ grid-template-columns: 1fr; }}
  .server-row {{ flex-wrap: wrap; }}
}}
</style>
</head>
<body>

<!-- Particles -->
<div class="particles" id="particles"></div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<!-- Main -->
<div class="wrap">
  <div class="header">
    <div class="logo-wrap" id="logoWrap">
      <div class="bee-container" id="beeContainer">
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <path d="M 44 24 L 40 15 L 42 12 L 38 6" fill="none" stroke="#ffcc00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M 56 24 L 60 15 L 58 12 L 62 6" fill="none" stroke="#ffcc00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <circle cx="50" cy="30" r="12" fill="#ffcc00" />
          <path d="M 45 32 Q 47 28 49 32" fill="none" stroke="#1a1a15" stroke-width="2" stroke-linecap="round" />
          <path d="M 51 32 Q 53 28 55 32" fill="none" stroke="#1a1a15" stroke-width="2" stroke-linecap="round" />
          <g class="wing-container-left">
            <polygon points="42,40 6,12 35,40" fill="#ffcc00" />
          </g>
          <g class="wing-container-right">
            <polygon points="58,40 94,12 65,40" fill="#ffcc00" />
          </g>
          <g class="wing-container-left">
            <polygon points="40,45 24,32 35,45" fill="#e6b800" />
          </g>
          <g class="wing-container-right">
            <polygon points="60,45 76,32 65,45" fill="#e6b800" />
          </g>
          <ellipse cx="50" cy="65" rx="18" ry="22" fill="#ffcc00" />
          <path d="M 33 56 L 67 56" stroke="#1a1a15" stroke-width="4" />
          <path d="M 32 65 L 68 65" stroke="#1a1a15" stroke-width="4" />
          <path d="M 34 74 L 66 74" stroke="#1a1a15" stroke-width="4" />
          <polygon points="50,86 46,98 54,98" fill="#ffcc00" />
        </svg>
      </div>
    </div>
    <div class="brand">CBeeNet</div>
    <div class="tagline">SUBSCRIPTION</div>
    <a class="tele-link" href="https://t.me/CBeeNet" target="_blank">
      <i class="ti ti-brand-telegram"></i> @CBeeNet
    </a>
  </div>

  <div id="root">
    <div class="state-placeholder spinner">
      <i class="ti ti-loader-2"></i>
      <p>در حال دریافت اطلاعات…</p>
    </div>
  </div>

  <div class="footer">
    کانال رسمی <a href="https://t.me/CBeeNet" target="_blank">@CBeeNet</a> · v10
  </div>
</div>

<script>
// ===== CONFIG =====
const API_URL = "/api/public/sub/{uuid_key}";
let allLinks = [];

// ===== HELPERS =====
function fmtB(b) {{
  if (!b || b === 0) return "0 B";
  if (b < 1024) return b + " B";
  if (b < 1048576) return (b / 1024).toFixed(1) + " KB";
  if (b < 1073741824) return (b / 1048576).toFixed(2) + " MB";
  if (b < 1099511627776) return (b / 1073741824).toFixed(2) + " GB";
  return (b / 1099511627776).toFixed(2) + " TB";
}}
function esc(s) {{
  return String(s || "").replace(/[&<>"']/g, c => ({{
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }})[c]);
}}
function protoLabel(protocols) {{
  if (!protocols || !protocols.length) return '<span class="config-badge-proto">VLESS · WS</span>';
  const labels = {{
    'vless-ws': 'VLESS · WS',
    'xhttp-packet-up': 'XHTTP · packet-up',
    'xhttp-stream-up': 'XHTTP · stream-up',
    'trojan-ws': 'Trojan · WS'
  }};
  return protocols.map(p => `<span class="config-badge-proto">${{labels[p] || 'VLESS · WS'}}</span>`).join('');
}}

// ===== PARTICLES =====
(function initParticles() {{
  const container = document.getElementById('particles');
  for (let i = 0; i < 25; i++) {{
    const el = document.createElement('div');
    el.className = 'particle';
    el.style.left = Math.random() * 100 + '%';
    el.style.width = el.style.height = (2 + Math.random() * 4) + 'px';
    el.style.animationDuration = (10 + Math.random() * 20) + 's';
    el.style.animationDelay = (Math.random() * 20) + 's';
    el.style.opacity = 0.2 + Math.random() * 0.3;
    container.appendChild(el);
  }}
}})();

// ===== BEE CONTROL =====
function setBeeState(on) {{
  const wrap = document.getElementById('logoWrap');
  const container = document.getElementById('beeContainer');
  if (on) {{
    wrap.classList.remove('bee-off');
    wrap.classList.add('bee-on');
    container.classList.remove('bee-off');
  }} else {{
    wrap.classList.remove('bee-on');
    wrap.classList.add('bee-off');
    container.classList.add('bee-off');
  }}
}}

// ===== DATA FETCH =====
async function loadData() {{
  try {{
    const r = await fetch(API_URL);
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return await r.json();
  }} catch (e) {{
    console.error('Fetch error:', e);
    return null;
  }}
}}

// ===== RENDER =====
function render(d) {{
  const root = document.getElementById('root');
  if (!d || !d.links || !d.links.length) {{
    root.innerHTML = `<div class="state-placeholder">
      <i class="ti ti-link-off"></i>
      <p>کانفیگی یافت نشد</p>
    </div>`;
    setBeeState(false);
    return;
  }}
  allLinks = d.links;
  d.links.forEach(l => l._lines = l.vless_link ? l.vless_link.split("\\n").filter(x => x) : []);

  // Determine if any link is active and has remaining quota (or unlimited)
  const hasActive = d.links.some(l => l.active && (l.limit_bytes === 0 || l.used_bytes < l.limit_bytes));
  setBeeState(hasActive);

  const active = d.links.filter(l => l.active).length;
  const totalUsed = d.links.reduce((s, l) => s + (l.used_bytes || 0), 0);
  let html = '';

  // Info card
  html += `<div class="info-card">
    <div class="glow-spot"></div>
    <div class="info-eyebrow"><i class="ti ti-folder"></i> ${{d.links.length === 1 ? 'کانفیگ' : 'گروه دسترسی'}}</div>
    <div class="info-name">${{esc(d.name || 'CBeeNet')}}</div>
    ${{d.desc ? `<div class="info-desc">${{esc(d.desc)}}</div>` : ''}}
  </div>`;

  // Stats
  html += `<div class="stats">
    <div class="stat-item">
      <div class="stat-label">وضعیت</div>
      <div class="stat-value">${{d.links.length === 1 ? (d.links[0].active ? 'فعال' : 'غیرفعال') : active + '/' + d.links.length}}</div>
      <div class="stat-sub"></div>
    </div>
    <div class="stat-item">
      <div class="stat-label">مصرف کل</div>
      <div class="stat-value">${{fmtB(totalUsed)}}</div>
      <div class="stat-sub">مجموع</div>
    </div>
    <div class="stat-item">
      <div class="stat-label">اتصالات</div>
      <div class="stat-value">${{d.active_connections || 0}}</div>
      <div class="stat-sub"><span class="dot-live"></span> آنلاین</div>
    </div>
  </div>`;

  // Copy all bar
  const allVlessLinks = d.links.map(l => l.vless_link || '').filter(x => x);
  if (allVlessLinks.length > 0) {{
    html += `<div class="copy-all">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه کانفیگ‌ها</div>
        <div class="copy-all-sub">${{allVlessLinks.length}} لینک · با یک کلیک</div>
      </div>
      <button class="btn-copy-all" onclick="copyAll()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{allVlessLinks.length}})</button>
    </div>`;
  }}

  // Config list header
  html += `<div class="section-header"><i class="ti ti-link"></i> کانفیگ‌ها (${{d.links.length}})</div>`;

  // Config items
  for (let i = 0; i < d.links.length; i++) {{
    const l = d.links[i];
    const pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
    const remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
    const rf = remain < 0 ? '∞' : fmtB(remain);
    const rc = remain < 0 ? 'ok' : (remain < 1048576 ? 'danger' : (remain < 1073741824 ? 'warn' : 'ok'));
    const statusClass = l.active ? 'on' : 'off';
    const statusIcon = l.active ? 'circle-check' : 'circle-x';
    const statusText = l.active ? 'فعال' : 'غیرفعال';
    const protoBadges = l.protocols ? protoLabel(l.protocols) : '<span class="config-badge-proto">VLESS · WS</span>';

    html += `<div class="config-item">
      <div class="config-header" onclick="toggleBody(this)">
        <div class="config-label">
          <span>${{esc(l.label)}}</span>
          ${{protoBadges}}
        </div>
        <span class="config-status ${{statusClass}}"><i class="ti ti-${{statusIcon}}"></i> ${{statusText}}</span>
        <span class="config-toggle"><i class="ti ti-chevron-down"></i></span>
      </div>
      <div class="config-body">
        <div class="usage-bar-wrap">
          <div class="usage-meta">
            <span>مصرف: <b>${{l.used_fmt}}</b></span>
            <span>سهمیه: <b>${{l.limit_fmt}}</b></span>
          </div>
          <div class="bar-track"><div class="bar-fill" style="width:${{pct}}%;"></div></div>
          <span class="remain-tag ${{rc}}"><i class="ti ${{remain < 0 ? 'ti-infinity' : 'ti-database'}}"></i> ${{remain < 0 ? 'نامحدود' : 'باقی: ' + rf}}</span>
        </div>
        ${{l._lines.length ? `<div class="server-list">
          <div class="server-list-title"><i class="ti ti-server-2"></i> سرورهای دسترسی</div>
          ${{l._lines.map((line, j) => `
            <div class="server-row">
              <span class="server-index">#${{j+1}}</span>
              <span class="server-address">${{esc(line)}}</span>
              <button class="btn-copy" onclick="copyText('${{esc(line)}}')"><i class="ti ti-copy"></i> کپی</button>
            </div>
          `).join('')}}
        </div>` : ''}}
      </div>
    </div>`;
  }}

  root.innerHTML = html;
}}

// ===== TOGGLE =====
function toggleBody(headerEl) {{
  const body = headerEl.nextElementSibling;
  const toggle = headerEl.querySelector('.config-toggle');
  body.classList.toggle('open');
  toggle.classList.toggle('open');
}}

// ===== COPY =====
function copyText(t) {{
  navigator.clipboard.writeText(t).then(() => {{
    showToast('✅ کپی شد', 'success');
  }});
}}
function copyAll() {{
  const all = allLinks.map(l => l.vless_link || '').filter(x => x).join('\\n');
  if (!all) {{
    showToast('❌ لینکی برای کپی نیست', '');
    return;
  }}
  navigator.clipboard.writeText(all).then(() => {{
    showToast('✅ همه ' + allLinks.length + ' کانفیگ کپی شد', 'success');
  }});
}}
function showToast(msg, type = '') {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show ' + (type || '');
  clearTimeout(t._hide);
  t._hide = setTimeout(() => t.classList.remove('show'), 3000);
}}

// ===== INIT =====
(async function init() {{
  const data = await loadData();
  if (data) {{
    render(data);
  }} else {{
    document.getElementById('root').innerHTML = `
      <div class="state-placeholder">
        <i class="ti ti-alert-circle" style="color:var(--red)"></i>
        <p>خطا در بارگذاری</p>
      </div>
    `;
    setBeeState(false);
  }}
}})();
</script>
</body>
</html>"""

def get_single_sub_page_html(uuid: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>CBeeNet · کانفیگ تکی</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800;14..32,900&family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ===== RESET & BASE (همان استایل صفحه گروه) ===== */
* {{ margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }}
:root {{
  --bg: #0a0a08;
  --surface: rgba(13, 13, 10, 0.75);
  --surface2: #1a1a15;
  --surface3: #22221c;
  --border: rgba(255, 215, 0, 0.08);
  --border-glow: rgba(255, 215, 0, 0.30);
  --text: #f5f5dc;
  --text2: #c8c8a0;
  --text3: #6b6b40;
  --primary: #ffd700;
  --primary-light: #ffe44d;
  --primary-dark: #d4a800;
  --secondary: #ffc107;
  --accent: #ffd700;
  --green: #66bb6a;
  --green-bg: rgba(102, 187, 106, 0.12);
  --red: #ef5350;
  --red-bg: rgba(239, 83, 80, 0.12);
  --radius: 24px;
  --shadow: 0 20px 60px rgba(0,0,0,0.7);
  --glow: 0 0 40px rgba(255,215,0,0.12);
}}
html, body {{ height:100%; }}
body {{
  font-family: 'Vazirmatn', 'Inter', sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  direction: rtl;
  overflow-x: hidden;
  background-image:
    radial-gradient(circle at 10% 20%, rgba(255,215,0,0.06) 0%, transparent 50%),
    radial-gradient(circle at 90% 80%, rgba(255,215,0,0.04) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 0%, var(--bg) 100%);
}}
.particles {{
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}}
.particle {{
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(255,215,0,0.25);
  border-radius: 50%;
  animation: floatParticle linear infinite;
}}
@keyframes floatParticle {{
  0% {{ transform: translateY(100vh) scale(0); opacity:0; }}
  10% {{ opacity:1; }}
  90% {{ opacity:1; }}
  100% {{ transform: translateY(-10vh) scale(1); opacity:0; }}
}}
.wrap {{
  position: relative;
  z-index: 10;
  max-width: 540px;
  margin: 0 auto;
  padding: 24px 16px 48px;
}}
.header {{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px 0 20px;
}}
.logo-wrap {{
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: #1a1a15;
  border: 2px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: 0 0 0 6px rgba(255,215,0,0.06), 0 20px 50px rgba(255,215,0,0.10);
  transition: transform 0.4s ease, border-color 0.5s;
}}
.logo-wrap:hover {{ transform: scale(1.05) rotate(-4deg); }}
.bee-container {{
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.bee-container svg {{
  width: 100%;
  height: 100%;
  display: block;
}}
.wing-container-left {{
  transform-origin: 42px 40px;
  animation: flapLeft 0.5s ease-in-out infinite alternate;
}}
.wing-container-right {{
  transform-origin: 58px 40px;
  animation: flapRight 0.5s ease-in-out infinite alternate;
}}
@keyframes flapLeft {{
  0% {{ transform: rotate(0deg) scaleY(1); }}
  100% {{ transform: rotate(-35deg) scaleY(0.8); }}
}}
@keyframes flapRight {{
  0% {{ transform: rotate(0deg) scaleY(1); }}
  100% {{ transform: rotate(35deg) scaleY(0.8); }}
}}
.logo-wrap.bee-off {{
  border-color: #2a2a25;
  box-shadow: 0 0 0 6px rgba(255,255,255,0.02), 0 20px 50px rgba(0,0,0,0.3);
}}
.logo-wrap.bee-on {{
  border-color: var(--primary);
  box-shadow: 0 0 0 6px rgba(255,215,0,0.15), 0 20px 50px rgba(255,215,0,0.25);
}}
.bee-off .bee-container svg {{
  filter: grayscale(1) opacity(0.3) brightness(0.8);
}}
.bee-off .wing-container-left,
.bee-off .wing-container-right {{
  animation-play-state: paused;
}}
.brand {{
  font-size: 28px;
  font-weight: 900;
  margin-top: 16px;
  background: linear-gradient(135deg, var(--primary-light), var(--secondary), var(--primary-light));
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: gradShift 6s ease infinite;
}}
@keyframes gradShift {{
  0% {{ background-position: 0% 50%; }}
  50% {{ background-position: 100% 50%; }}
  100% {{ background-position: 0% 50%; }}
}}
.tagline {{
  font-size: 12px;
  color: var(--text3);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-weight: 600;
  margin-top: 4px;
}}
.tele-link {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 16px;
  padding: 8px 22px;
  border-radius: 40px;
  background: rgba(255,215,0,0.08);
  border: 1px solid rgba(255,215,0,0.15);
  color: var(--primary-light);
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.25s;
  backdrop-filter: blur(4px);
}}
.tele-link:hover {{
  background: rgba(255,215,0,0.18);
  border-color: var(--primary);
  box-shadow: 0 0 30px rgba(255,215,0,0.15);
  transform: translateY(-2px);
}}
.glass {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}}
.info-card {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 22px 24px;
  margin: 18px 0 16px;
  position: relative;
  overflow: hidden;
  transition: border-color 0.3s;
}}
.info-card:hover {{ border-color: var(--border-glow); }}
.info-card .glow-spot {{
  position: absolute;
  top: -60px;
  right: -60px;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(255,215,0,0.06), transparent 70%);
  pointer-events: none;
}}
.info-eyebrow {{
  font-size: 11px;
  font-weight: 700;
  color: var(--primary-light);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}}
.info-name {{
  font-size: 24px;
  font-weight: 800;
  background: linear-gradient(135deg, #fff, var(--primary-light));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin-bottom: 4px;
}}
.info-desc {{
  font-size: 13px;
  color: var(--text2);
  line-height: 1.7;
}}
.stats {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 18px;
}}
.stat-item {{
  background: var(--surface2);
  border-radius: 18px;
  padding: 16px 8px;
  text-align: center;
  border: 1px solid var(--border);
  transition: all 0.25s;
}}
.stat-item:hover {{
  border-color: var(--border-glow);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}}
.stat-label {{
  font-size: 9px;
  font-weight: 700;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}
.stat-value {{
  font-size: 22px;
  font-weight: 800;
  margin-top: 4px;
  background: linear-gradient(135deg, var(--primary-light), var(--secondary));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.stat-sub {{
  font-size: 10px;
  color: var(--text3);
  margin-top: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
}}
.dot-live {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--green);
  display: inline-block;
  animation: pulse-dot 1.8s infinite;
}}
@keyframes pulse-dot {{
  0%,100% {{ opacity:1; transform:scale(1); }}
  50% {{ opacity:0.2; transform:scale(0.6); }}
}}
.copy-all {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 14px 20px;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  background: linear-gradient(135deg, rgba(255,215,0,0.06), rgba(255,193,7,0.04));
  border-color: rgba(255,215,0,0.10);
}}
.copy-all-text {{
  flex: 1;
  min-width: 130px;
}}
.copy-all-title {{
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--primary-light);
}}
.copy-all-sub {{
  font-size: 10px;
  color: var(--text3);
}}
.btn-copy-all {{
  font-family: inherit;
  font-size: 13px;
  font-weight: 800;
  padding: 8px 20px;
  border: none;
  border-radius: 40px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #000;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.25s;
  box-shadow: 0 4px 20px rgba(255,215,0,0.3);
}}
.btn-copy-all:hover {{
  transform: scale(1.03);
  box-shadow: 0 6px 30px rgba(255,215,0,0.5);
}}
.section-header {{
  font-size: 13px;
  font-weight: 800;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  margin: 24px 0 14px;
  display: flex;
  align-items: center;
  gap: 10px;
}}
.section-header i {{ color: var(--primary-light); font-size: 18px; }}
.config-item {{
  background: var(--surface);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 14px;
  overflow: hidden;
  border-color: var(--border);
  transition: border-color 0.3s, box-shadow 0.3s;
}}
.config-item:hover {{
  border-color: var(--border-glow);
  box-shadow: var(--glow);
}}
.config-header {{
  padding: 16px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  cursor: pointer;
  user-select: none;
  transition: background 0.2s;
}}
.config-header:hover {{
  background: rgba(255,215,0,0.03);
}}
.config-label {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 700;
  flex: 1;
  min-width: 0;
}}
.config-badge-proto {{
  font-size: 9px;
  padding: 2px 10px;
  border-radius: 30px;
  font-weight: 700;
  background: rgba(255,215,0,0.10);
  color: var(--primary-light);
}}
.config-status {{
  font-size: 10px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 30px;
  display: flex;
  align-items: center;
  gap: 5px;
  white-space: nowrap;
}}
.config-status.on {{
  background: var(--green-bg);
  color: var(--green);
  border: 1px solid rgba(102,187,106,0.2);
}}
.config-status.off {{
  background: var(--red-bg);
  color: var(--red);
  border: 1px solid rgba(239,83,80,0.2);
}}
.config-toggle {{
  font-size: 20px;
  color: var(--text3);
  transition: transform 0.3s;
}}
.config-toggle.open {{ transform: rotate(180deg); }}
.config-body {{
  padding: 0 20px 20px;
  display: none;
}}
.config-body.open {{ display: block; }}
.usage-bar-wrap {{
  margin: 10px 0 8px;
}}
.usage-meta {{
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text3);
  margin-bottom: 4px;
}}
.usage-meta b {{ color: var(--text2); }}
.bar-track {{
  height: 6px;
  border-radius: 10px;
  background: rgba(255,215,0,0.06);
  overflow: hidden;
}}
.bar-fill {{
  height: 100%;
  border-radius: 10px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  transition: width 0.8s cubic-bezier(0.2,0.9,0.3,1);
  width: 0%;
}}
.remain-tag {{
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 12px;
  border-radius: 30px;
  margin-top: 8px;
}}
.remain-tag.ok {{ background: var(--green-bg); color: var(--green); }}
.remain-tag.warn {{ background: rgba(255,215,0,0.10); color: var(--primary-light); }}
.remain-tag.danger {{ background: var(--red-bg); color: var(--red); }}
.server-list {{
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--border);
}}
.server-list-title {{
  font-size: 10px;
  font-weight: 700;
  color: var(--text3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 10px;
}}
.server-list-title i {{ color: var(--primary-light); }}
.server-row {{
  background: var(--surface3);
  border-radius: 14px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
  border: 1px solid var(--border);
  transition: border-color 0.2s;
}}
.server-row:hover {{ border-color: var(--border-glow); }}
.server-index {{
  font-size: 10px;
  font-weight: 700;
  color: var(--text3);
  min-width: 24px;
}}
.server-address {{
  flex: 1;
  font-family: 'Inter', monospace;
  font-size: 10.5px;
  color: var(--text2);
  direction: ltr;
  text-align: left;
  word-break: break-all;
  line-height: 1.5;
  min-width: 0;
}}
.btn-copy {{
  font-family: inherit;
  font-size: 10px;
  font-weight: 700;
  padding: 5px 14px;
  border: none;
  border-radius: 30px;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: #000;
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  transition: all 0.2s;
  flex-shrink: 0;
}}
.btn-copy:hover {{ transform: scale(1.05); box-shadow: 0 4px 15px rgba(255,215,0,0.3); }}
.footer {{
  text-align: center;
  margin-top: 32px;
  padding: 16px 0 4px;
  font-size: 10px;
  color: var(--text3);
  letter-spacing: 0.05em;
}}
.footer a {{
  color: var(--primary-light);
  font-weight: 700;
  text-decoration: none;
  transition: 0.2s;
}}
.footer a:hover {{ text-decoration: underline; color: var(--secondary); }}
.toast {{
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(80px);
  background: var(--surface2);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 12px 24px;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.2,0.9,0.3,1);
  z-index: 999;
  pointer-events: none;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.6);
}}
.toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
.toast.success {{ border-color: rgba(255,215,0,0.3); background: rgba(255,215,0,0.08); color: var(--primary-light); }}
.state-placeholder {{
  text-align: center;
  padding: 80px 20px;
}}
.state-placeholder i {{
  font-size: 52px;
  color: var(--text3);
  display: block;
  margin-bottom: 16px;
  opacity: 0.4;
}}
.state-placeholder p {{ font-size: 14px; color: var(--text3); }}
.spinner i {{
  animation: spin 1.2s linear infinite;
  color: var(--primary-light);
}}
@keyframes spin {{ to {{ transform: rotate(360deg); }} }}
@media (max-width: 480px) {{
  .stats {{ grid-template-columns: 1fr 1fr; }}
  .stats .stat-item:last-child {{ grid-column: 1 / -1; }}
  .copy-all {{ flex-direction: column; align-items: stretch; text-align: center; }}
  .btn-copy-all {{ justify-content: center; }}
  .config-header {{ flex-wrap: wrap; }}
  .config-label {{ min-width: 100%; }}
}}
@media (max-width: 380px) {{
  .stats {{ grid-template-columns: 1fr; }}
  .server-row {{ flex-wrap: wrap; }}
}}
</style>
</head>
<body>

<!-- Particles -->
<div class="particles" id="particles"></div>

<!-- Toast -->
<div class="toast" id="toast"></div>

<!-- Main -->
<div class="wrap">
  <div class="header">
    <div class="logo-wrap" id="logoWrap">
      <div class="bee-container" id="beeContainer">
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <path d="M 44 24 L 40 15 L 42 12 L 38 6" fill="none" stroke="#ffcc00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M 56 24 L 60 15 L 58 12 L 62 6" fill="none" stroke="#ffcc00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <circle cx="50" cy="30" r="12" fill="#ffcc00" />
          <path d="M 45 32 Q 47 28 49 32" fill="none" stroke="#1a1a15" stroke-width="2" stroke-linecap="round" />
          <path d="M 51 32 Q 53 28 55 32" fill="none" stroke="#1a1a15" stroke-width="2" stroke-linecap="round" />
          <g class="wing-container-left">
            <polygon points="42,40 6,12 35,40" fill="#ffcc00" />
          </g>
          <g class="wing-container-right">
            <polygon points="58,40 94,12 65,40" fill="#ffcc00" />
          </g>
          <g class="wing-container-left">
            <polygon points="40,45 24,32 35,45" fill="#e6b800" />
          </g>
          <g class="wing-container-right">
            <polygon points="60,45 76,32 65,45" fill="#e6b800" />
          </g>
          <ellipse cx="50" cy="65" rx="18" ry="22" fill="#ffcc00" />
          <path d="M 33 56 L 67 56" stroke="#1a1a15" stroke-width="4" />
          <path d="M 32 65 L 68 65" stroke="#1a1a15" stroke-width="4" />
          <path d="M 34 74 L 66 74" stroke="#1a1a15" stroke-width="4" />
          <polygon points="50,86 46,98 54,98" fill="#ffcc00" />
        </svg>
      </div>
    </div>
    <div class="brand">CBeeNet</div>
    <div class="tagline">SINGLE CONFIG</div>
    <a class="tele-link" href="https://t.me/CBeeNet" target="_blank">
      <i class="ti ti-brand-telegram"></i> @CBeeNet
    </a>
  </div>

  <div id="root">
    <div class="state-placeholder spinner">
      <i class="ti ti-loader-2"></i>
      <p>در حال دریافت اطلاعات…</p>
    </div>
  </div>

  <div class="footer">
    کانال رسمی <a href="https://t.me/CBeeNet" target="_blank">@CBeeNet</a> · v10
  </div>
</div>

<script>
// ===== CONFIG =====
const API_URL = "/api/public/sub-single/{uuid}";
let allLinks = [];

// ===== HELPERS =====
function fmtB(b) {{
  if (!b || b === 0) return "0 B";
  if (b < 1024) return b + " B";
  if (b < 1048576) return (b / 1024).toFixed(1) + " KB";
  if (b < 1073741824) return (b / 1048576).toFixed(2) + " MB";
  if (b < 1099511627776) return (b / 1073741824).toFixed(2) + " GB";
  return (b / 1099511627776).toFixed(2) + " TB";
}}
function esc(s) {{
  return String(s || "").replace(/[&<>"']/g, c => ({{
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }})[c]);
}}
function protoLabel(protocols) {{
  if (!protocols || !protocols.length) return '<span class="config-badge-proto">VLESS · WS</span>';
  const labels = {{
    'vless-ws': 'VLESS · WS',
    'xhttp-packet-up': 'XHTTP · packet-up',
    'xhttp-stream-up': 'XHTTP · stream-up',
    'trojan-ws': 'Trojan · WS'
  }};
  return protocols.map(p => `<span class="config-badge-proto">${{labels[p] || 'VLESS · WS'}}</span>`).join('');
}}

// ===== PARTICLES =====
(function initParticles() {{
  const container = document.getElementById('particles');
  for (let i = 0; i < 25; i++) {{
    const el = document.createElement('div');
    el.className = 'particle';
    el.style.left = Math.random() * 100 + '%';
    el.style.width = el.style.height = (2 + Math.random() * 4) + 'px';
    el.style.animationDuration = (10 + Math.random() * 20) + 's';
    el.style.animationDelay = (Math.random() * 20) + 's';
    el.style.opacity = 0.2 + Math.random() * 0.3;
    container.appendChild(el);
  }}
}})();

// ===== BEE CONTROL =====
function setBeeState(on) {{
  const wrap = document.getElementById('logoWrap');
  const container = document.getElementById('beeContainer');
  if (on) {{
    wrap.classList.remove('bee-off');
    wrap.classList.add('bee-on');
    container.classList.remove('bee-off');
  }} else {{
    wrap.classList.remove('bee-on');
    wrap.classList.add('bee-off');
    container.classList.add('bee-off');
  }}
}}

// ===== DATA FETCH =====
async function loadData() {{
  try {{
    const r = await fetch(API_URL);
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return await r.json();
  }} catch (e) {{
    console.error('Fetch error:', e);
    return null;
  }}
}}

// ===== RENDER =====
function render(d) {{
  const root = document.getElementById('root');
  if (!d || !d.links || !d.links.length) {{
    root.innerHTML = `<div class="state-placeholder">
      <i class="ti ti-link-off"></i>
      <p>کانفیگی یافت نشد</p>
    </div>`;
    setBeeState(false);
    return;
  }}
  const l = d.links[0];
  l._lines = l.vless_link ? l.vless_link.split("\\n").filter(x => x) : [];

  const hasActive = l.active && (l.limit_bytes === 0 || l.used_bytes < l.limit_bytes);
  setBeeState(hasActive);

  let html = '';

  // Info card
  html += `<div class="info-card">
    <div class="glow-spot"></div>
    <div class="info-eyebrow"><i class="ti ti-link"></i> کانفیگ تکی</div>
    <div class="info-name">${{esc(l.label)}}</div>
    ${{d.desc ? `<div class="info-desc">${{esc(d.desc)}}</div>` : ''}}
  </div>`;

  // Stats
  const pct = l.limit_bytes > 0 ? Math.min(100, (l.used_bytes / l.limit_bytes) * 100) : 0;
  const remain = l.limit_bytes > 0 ? Math.max(0, l.limit_bytes - l.used_bytes) : -1;
  const rf = remain < 0 ? '∞' : fmtB(remain);
  const rc = remain < 0 ? 'ok' : (remain < 1048576 ? 'danger' : (remain < 1073741824 ? 'warn' : 'ok'));
  const statusClass = l.active ? 'on' : 'off';
  const statusIcon = l.active ? 'circle-check' : 'circle-x';
  const statusText = l.active ? 'فعال' : 'غیرفعال';
  const protoBadges = l.protocols ? protoLabel(l.protocols) : '<span class="config-badge-proto">VLESS · WS</span>';

  html += `<div class="stats">
    <div class="stat-item">
      <div class="stat-label">وضعیت</div>
      <div class="stat-value">${{statusText}}</div>
      <div class="stat-sub"></div>
    </div>
    <div class="stat-item">
      <div class="stat-label">مصرف</div>
      <div class="stat-value">${{fmtB(l.used_bytes || 0)}}</div>
      <div class="stat-sub">از ${{l.limit_fmt}}</div>
    </div>
    <div class="stat-item">
      <div class="stat-label">اتصالات</div>
      <div class="stat-value">${{d.active_connections || 0}}</div>
      <div class="stat-sub"><span class="dot-live"></span> آنلاین</div>
    </div>
  </div>`;

  // Copy all (single link)
  if (l.vless_link) {{
    html += `<div class="copy-all">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی لینک</div>
        <div class="copy-all-sub">یک لینک · کپی کامل</div>
      </div>
      <button class="btn-copy-all" onclick="copyAll()"><i class="ti ti-clipboard-copy"></i> کپی لینک</button>
    </div>`;
  }}

  // Config card
  html += `<div class="config-item">
    <div class="config-header" onclick="toggleBody(this)">
      <div class="config-label">
        <span>${{esc(l.label)}}</span>
        ${{protoBadges}}
      </div>
      <span class="config-status ${{statusClass}}"><i class="ti ti-${{statusIcon}}"></i> ${{statusText}}</span>
      <span class="config-toggle"><i class="ti ti-chevron-down"></i></span>
    </div>
    <div class="config-body">
      <div class="usage-bar-wrap">
        <div class="usage-meta">
          <span>مصرف: <b>${{l.used_fmt}}</b></span>
          <span>سهمیه: <b>${{l.limit_fmt}}</b></span>
        </div>
        <div class="bar-track"><div class="bar-fill" style="width:${{pct}}%;"></div></div>
        <span class="remain-tag ${{rc}}"><i class="ti ${{remain < 0 ? 'ti-infinity' : 'ti-database'}}"></i> ${{remain < 0 ? 'نامحدود' : 'باقی: ' + rf}}</span>
      </div>
      ${{l._lines.length ? `<div class="server-list">
        <div class="server-list-title"><i class="ti ti-server-2"></i> سرورهای دسترسی</div>
        ${{l._lines.map((line, j) => `
          <div class="server-row">
            <span class="server-index">#${{j+1}}</span>
            <span class="server-address">${{esc(line)}}</span>
            <button class="btn-copy" onclick="copyText('${{esc(line)}}')"><i class="ti ti-copy"></i> کپی</button>
          </div>
        `).join('')}}
      </div>` : ''}}
    </div>
  </div>`;

  root.innerHTML = html;
}}

// ===== TOGGLE =====
function toggleBody(headerEl) {{
  const body = headerEl.nextElementSibling;
  const toggle = headerEl.querySelector('.config-toggle');
  body.classList.toggle('open');
  toggle.classList.toggle('open');
}}

// ===== COPY =====
function copyText(t) {{
  navigator.clipboard.writeText(t).then(() => {{
    showToast('✅ کپی شد', 'success');
  }});
}}
function copyAll() {{
  const l = allLinks[0];
  if (!l || !l.vless_link) {{
    showToast('❌ لینکی برای کپی نیست', '');
    return;
  }}
  navigator.clipboard.writeText(l.vless_link).then(() => {{
    showToast('✅ لینک کپی شد', 'success');
  }});
}}
function showToast(msg, type = '') {{
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show ' + (type || '');
  clearTimeout(t._hide);
  t._hide = setTimeout(() => t.classList.remove('show'), 3000);
}}

// ===== INIT =====
(async function init() {{
  const data = await loadData();
  if (data) {{
    allLinks = data.links || [];
    render(data);
  }} else {{
    document.getElementById('root').innerHTML = `
      <div class="state-placeholder">
        <i class="ti ti-alert-circle" style="color:var(--red)"></i>
        <p>خطا در بارگذاری</p>
      </div>
    `;
    setBeeState(false);
  }}
}})();
</script>
</body>
</html>"""
