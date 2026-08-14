# pages.py - CBee Gateway v1.0.0 (3X-UI Style, Unified Color, No Profile, Advanced Server Name)
import json

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · CBee</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
html, body { height:100%; overflow:hidden; }
body {
  font-family: 'Vazirmatn', sans-serif;
  background: #0d1117;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  position: relative;
}
.bg-canvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  background: radial-gradient(ellipse at 20% 30%, rgba(22,119,255,0.12) 0%, transparent 60%),
              radial-gradient(ellipse at 80% 70%, rgba(22,119,255,0.06) 0%, transparent 55%),
              #0d1117;
}
.bg-canvas::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(48,54,61,0.15) 1px, transparent 1px),
    linear-gradient(90deg, rgba(48,54,61,0.15) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: gridMove 20s linear infinite;
}
@keyframes gridMove {
  0% { transform: translate(0,0); }
  100% { transform: translate(50px,50px); }
}
.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(100px);
  z-index: 0;
  pointer-events: none;
  animation: floatOrb 18s ease-in-out infinite alternate;
}
.o1 { width: 500px; height: 500px; background: rgba(22,119,255,0.06); top: -200px; right: -150px; animation-delay: 0s; }
.o2 { width: 400px; height: 400px; background: rgba(22,119,255,0.04); bottom: -150px; left: -120px; animation-delay: 6s; }
.o3 { width: 300px; height: 300px; background: rgba(22,119,255,0.03); top: 50%; left: 50%; transform: translate(-50%, -50%); animation-delay: 3s; }
@keyframes floatOrb {
  0% { transform: translate(0,0) scale(1); }
  33% { transform: translate(60px,-70px) scale(1.1); }
  66% { transform: translate(-40px,40px) scale(0.9); }
  100% { transform: translate(30px,-30px) scale(1.05); }
}
.wrap { position: relative; z-index: 10; width: 100%; max-width: 420px; }
.card {
  background: #161b22;
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid #30363d;
  border-radius: 32px;
  padding: 40px 34px 34px;
  box-shadow: 0 24px 64px rgba(0,0,0,0.7), 0 0 80px rgba(22,119,255,0.04);
  position: relative;
  overflow: hidden;
}
.card::before {
  content: '';
  position: absolute;
  top: -80px;
  right: -80px;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(22,119,255,0.05), transparent 70%);
  pointer-events: none;
}
.brand {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
  position: relative;
  z-index: 1;
}
.brand-name {
  font-size: 42px;
  font-weight: 900;
  font-family: 'Vazirmatn', sans-serif;
  background: linear-gradient(135deg, #1677ff, #0050b3);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: -0.02em;
  text-shadow: 0 0 40px rgba(22,119,255,0.15);
}
.brand-sub {
  font-size: 11px;
  color: #8b949e;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 600;
  margin-top: 4px;
}
h1 {
  font-size: 20px;
  font-weight: 800;
  color: #f0f6fc;
  margin-bottom: 4px;
  letter-spacing: -0.02em;
}
.sub {
  font-size: 12px;
  color: #8b949e;
  margin-bottom: 24px;
  line-height: 1.7;
}
.err {
  display: none;
  background: rgba(239,68,68,0.12);
  border: 1px solid rgba(239,68,68,0.3);
  border-radius: 12px;
  padding: 10px 14px;
  margin-bottom: 14px;
  font-size: 12px;
  color: #f87171;
  align-items: center;
  gap: 8px;
}
.err.show { display: flex; }
.field {
  margin-bottom: 18px;
  position: relative;
  z-index: 1;
}
.field label {
  display: block;
  font-size: 10.5px;
  font-weight: 700;
  color: #8b949e;
  margin-bottom: 7px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.inp-wrap {
  position: relative;
}
input[type="password"] {
  width: 100%;
  padding: 14px 48px 14px 18px;
  border-radius: 14px;
  border: 1px solid #30363d;
  background: rgba(0,0,0,0.3);
  color: #f0f6fc;
  font-family: inherit;
  font-size: 14px;
  outline: none;
  transition: all 0.25s;
}
input[type="password"]:focus {
  border-color: rgba(22,119,255,0.5);
  background: rgba(0,0,0,0.4);
  box-shadow: 0 0 0 4px rgba(22,119,255,0.08);
}
.ic {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: #8b949e;
  font-size: 18px;
  pointer-events: none;
  transition: 0.2s;
}
input:focus + .ic { color: #1677ff; }
.btn {
  width: 100%;
  padding: 14px;
  border-radius: 14px;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg, #1677ff, #0050b3);
  color: #fff;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: 0 4px 24px rgba(22,119,255,0.3);
  transition: all 0.25s;
  position: relative;
  overflow: hidden;
}
.btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #0050b3, #1677ff);
  opacity: 0;
  transition: opacity 0.3s;
}
.btn:hover::before { opacity: 1; }
.btn:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(22,119,255,0.45); }
.btn:active { transform: translateY(0) scale(0.98); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }
.btn span { position: relative; z-index: 1; display: flex; align-items: center; gap: 6px; }
.footer {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #30363d;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 11px;
  color: #8b949e;
}
.footer a {
  color: #1677ff;
  font-weight: 700;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: 0.2s;
}
.footer a:hover { color: #0050b3; text-decoration: underline; }
@keyframes spin { to { transform: rotate(360deg); } }
@media (max-width: 440px) {
  .card { padding: 28px 20px 24px; }
  .brand-name { font-size: 32px; }
}
</style>
</head>
<body>
<div class="bg-canvas"></div>
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-name">CBee</div>
      <div class="brand-sub">Gateway · v1.0.0</div>
    </div>
    <h1>ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="••••••••" autofocus required>
          <i class="ti ti-key ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn">
        <span><i class="ti ti-login-2"></i> ورود به داشبورد</span>
      </button>
    </form>
    <div class="footer">
      <a href="https://t.me/CBeeNet" target="_blank"><i class="ti ti-brand-telegram"></i> @CBeeNet</a>
    </div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit', async e => {
  e.preventDefault();
  const btn = document.getElementById('btn');
  const err = document.getElementById('err');
  const et = document.getElementById('err-text');
  err.classList.remove('show');
  btn.disabled = true;
  btn.querySelector('span').innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try {
    const r = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password: document.getElementById('pw').value })
    });
    if (!r.ok) {
      const d = await r.json().catch(() => ({}));
      throw new Error(d.detail || 'رمز عبور اشتباه است');
    }
    location.href = '/CFOX';
  } catch (e) {
    et.textContent = e.message;
    err.classList.add('show');
    btn.disabled = false;
    btn.querySelector('span').innerHTML = '<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CBee · Gateway</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0d1117;
  --bg2:#161b22;
  --bg3:#1c2333;
  --card:#161b22;
  --card-b:#30363d;
  --card-bh:rgba(22,119,255,0.20);
  --accent:#1677ff;
  --accent2:#4096ff;
  --accent-d:rgba(22,119,255,0.12);
  --accent-glow:rgba(22,119,255,0.35);
  --green:#10b981;
  --green-bg:rgba(16,185,129,0.10);
  --green-t:#34d399;
  --red:#ef4444;
  --red-bg:rgba(239,68,68,0.10);
  --red-t:#f87171;
  --amber:#f59e0b;
  --amber-bg:rgba(245,158,11,0.10);
  --amber-t:#fbbf24;
  --purple:#7c3aed;
  --purple-bg:rgba(124,58,237,0.10);
  --t1:#f0f6fc;
  --t2:#8b949e;
  --t3:#6e7681;
  --sidebar-w:248px;
  --radius:16px;
  --shadow:0 8px 32px rgba(0,0,0,0.4);
}
[data-theme="dark-blue"]{
  --accent:#1677ff;
  --accent2:#4096ff;
  --accent-d:rgba(22,119,255,0.12);
  --accent-glow:rgba(22,119,255,0.35);
  --card-bh:rgba(22,119,255,0.20);
}
[data-theme="dark-red"]{
  --accent:#ef4444;
  --accent2:#f87171;
  --accent-d:rgba(239,68,68,0.12);
  --accent-glow:rgba(239,68,68,0.35);
  --card-bh:rgba(239,68,68,0.20);
}
[data-theme="dark-yellow"]{
  --accent:#f59e0b;
  --accent2:#fbbf24;
  --accent-d:rgba(245,158,11,0.12);
  --accent-glow:rgba(245,158,11,0.35);
  --card-bh:rgba(245,158,11,0.20);
}
[data-theme="light-blue"]{
  --bg:#f6f8fa;
  --bg2:#ffffff;
  --bg3:#eaeef2;
  --card:#ffffff;
  --card-b:#d0d7de;
  --card-bh:rgba(22,119,255,0.25);
  --accent:#1677ff;
  --accent2:#4096ff;
  --accent-d:rgba(22,119,255,0.08);
  --accent-glow:rgba(22,119,255,0.25);
  --t1:#24292f;
  --t2:#57606a;
  --t3:#8b949e;
  --shadow:0 8px 28px rgba(0,0,0,0.08);
}
[data-theme="light-red"]{
  --bg:#f6f8fa;
  --bg2:#ffffff;
  --bg3:#eaeef2;
  --card:#ffffff;
  --card-b:#d0d7de;
  --card-bh:rgba(239,68,68,0.25);
  --accent:#ef4444;
  --accent2:#f87171;
  --accent-d:rgba(239,68,68,0.08);
  --accent-glow:rgba(239,68,68,0.25);
  --t1:#24292f;
  --t2:#57606a;
  --t3:#8b949e;
  --shadow:0 8px 28px rgba(0,0,0,0.08);
}
[data-theme="light-yellow"]{
  --bg:#f6f8fa;
  --bg2:#ffffff;
  --bg3:#eaeef2;
  --card:#ffffff;
  --card-b:#d0d7de;
  --card-bh:rgba(245,158,11,0.25);
  --accent:#f59e0b;
  --accent2:#fbbf24;
  --accent-d:rgba(245,158,11,0.08);
  --accent-glow:rgba(245,158,11,0.25);
  --t1:#24292f;
  --t2:#57606a;
  --t3:#8b949e;
  --shadow:0 8px 28px rgba(0,0,0,0.08);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s, border-color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);flex-shrink:0;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:900;color:#fff;font-family:'Vazirmatn',sans-serif;display:none}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:24px;font-weight:900;color:var(--t1);font-family:'Vazirmatn',sans-serif;letter-spacing:-0.02em}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px;border-radius:8px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(245,158,11,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#1DA1F2,#0D8BD9);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:center;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:900;color:#fff;font-family:'Vazirmatn',sans-serif;display:none}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:18px;font-weight:900;font-family:'Vazirmatn',sans-serif}
.mob-right{display:none;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:var(--purple)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.sparkline-row{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:22px}
.sparkline-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px 18px 14px;transition:all .2s;position:relative;overflow:hidden}
.sparkline-card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.sparkline-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.sparkline-label{font-size:10.5px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:5px}
.sparkline-label i{font-size:14px;color:var(--accent)}
.sparkline-value{font-size:26px;font-weight:800;color:var(--t1);letter-spacing:-.02em;line-height:1.2}
.sparkline-value .unit{font-size:13px;font-weight:500;color:var(--t3);margin-right:3px}
.sparkline-chart{height:50px;margin-top:6px;position:relative}
.sparkline-chart canvas{width:100% !important;height:100% !important}
.sparkline-sub{font-size:9.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:4px}
.sparkline-sub .dot{width:5px;height:5px;border-radius:50%;display:inline-block;background:var(--accent)}
@media(max-width:768px){.sparkline-row{grid-template-columns:1fr;gap:12px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:var(--accent);color:#fff;box-shadow:0 2px 12px var(--accent-glow)}
.btn-p:hover{background:var(--accent2);box-shadow:0 4px 18px var(--accent-glow)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:var(--accent)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b)}
.btn-g:hover{background:var(--accent-d);border-color:var(--accent)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,0.2)}
.btn-d:hover{background:rgba(239,68,68,0.2)}
.btn-pur{background:var(--purple-bg);color:var(--purple);border:1px solid rgba(124,58,237,0.2)}
.btn-pur:hover{background:rgba(124,58,237,0.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.2)}
.btn-amber:hover{background:rgba(245,158,11,0.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--card-b);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:200px}
.ch-lg{position:relative;height:300px}
.ch-sm{position:relative;height:160px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme^="light"] .fi,[data-theme^="light"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:var(--accent);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px var(--accent-d)}
.fs option{background:var(--bg2)}
[data-theme^="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,0.2);color:var(--amber-t)}
.create-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:var(--radius);padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px var(--accent-glow)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
[data-theme^="light"] .cp-block{background:var(--accent-d)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme^="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:var(--accent-d);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px var(--accent-glow)}
.proto-group{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px}
.proto-btn{padding:8px 18px;border-radius:12px;border:2px solid var(--card-b);background:rgba(0,0,0,0.2);color:var(--t2);font-family:inherit;font-size:11.5px;font-weight:600;cursor:pointer;transition:all 0.2s ease;user-select:none;outline:none;letter-spacing:0.02em}
.proto-btn:hover{border-color:var(--card-bh);background:var(--accent-d);color:var(--t1)}
.proto-btn.active{border-color:var(--accent);background:var(--accent-d);color:var(--accent2);box-shadow:0 0 0 1px var(--accent),0 4px 12px var(--accent-glow);transform:translateY(-1px)}
.proto-btn .proto-badge{display:inline-block;font-size:8px;background:rgba(255,255,255,0.06);padding:1px 6px;border-radius:4px;margin-right:4px;color:var(--t3);font-weight:400}
[data-theme^="light"] .proto-btn{background:rgba(255,255,255,0.4)}
[data-theme^="light"] .proto-btn.active{background:var(--accent-d);border-color:var(--accent);color:var(--accent)}
.count-chips{display:flex;gap:6px;margin-top:9px}
.count-chip{font-size:10.5px;font-weight:700;padding:5px 14px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.count-chip:hover{background:var(--accent-d);color:var(--accent2)}
.count-chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px var(--accent-glow)}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px var(--accent-glow);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px var(--accent-glow)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){.cp-row{grid-template-columns:1fr}.cp-footer{flex-direction:column;align-items:stretch}.cp-submit-btn{justify-content:center}}
.srv-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px var(--accent-glow)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme^="light"] .srv-tile{background:var(--accent-d)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}
.pw-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px var(--accent-glow)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme^="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--accent)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px var(--accent-glow);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px var(--accent-glow)}
.pw-submit:active{transform:translateY(0) scale(.98)}
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:var(--radius);padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:var(--radius)}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}
@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}
@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(22,119,255,.07);border:1px solid rgba(22,119,255,.2);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--accent);word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:var(--radius);padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(124,58,237,.14),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(124,58,237,.35)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme^="light"] .sub-card-stats{background:var(--accent-d)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-card-url-row{margin:14px 20px 0;background:rgba(22,119,255,.08);border:1px dashed rgba(22,119,255,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--accent);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:var(--accent);transform:scale(1.1)}
.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:var(--radius);grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}
.modal-v2{background:var(--card);backdrop-filter:blur(16px);border:1px solid var(--card-b);border-radius:var(--radius);padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(124,58,237,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme^="light"] .modal-v2-input{background:rgba(255,255,255,0.8)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d);background:rgba(0,0,0,.28)}
[data-theme^="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:var(--accent-d);border:1px solid var(--card-b);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(124,58,237,.4);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(124,58,237,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px var(--accent-glow)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme^="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:var(--accent-d)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:var(--accent-d);border-color:var(--accent)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}
@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(16px);border:1px solid var(--card-b);border-radius:var(--radius);padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid var(--card-b)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(16px);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:var(--accent-d)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple)}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}
@media(max-width:880px){.cfg-row{flex-wrap:wrap}.cfg-divider-v{display:none}.cfg-usage-col{min-width:100%;order:5}}
@media(max-width:768px){.cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}.cfg-card{border-radius:16px}.cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}.cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}.cfg-identity{min-width:0;flex:1}.cfg-usage-col{min-width:0}.cfg-exp-col{min-width:0}.cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}.cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid var(--card-b);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid var(--card-b)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}
@media(max-width:1050px){.sidebar{transform:translateX(100%)}.sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}.sb-close{display:flex}.main{margin-right:0;padding-top:70px}.mob-top{display:flex}.metrics{grid-template-columns:1fr 1fr}.g2,.g3{grid-template-columns:1fr}}
@media(max-width:500px){.metrics{grid-template-columns:1fr}.main{padding:62px 12px 50px}.sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}}

/* ===== Custom Scroll ===== */
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--accent);border-radius:10px}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه جدید</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">انصراف</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> ساخت گروه</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:16px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo" style="display:none">CB</div>
    <span class="mob-title">CBee</span>
  </div>
  <div class="mob-right" style="display:none">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img" style="display:none">CB</div>
    <div><div class="logo-name">CBee</div><div class="logo-sub">Gateway · v1.0.0</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    <a class="tg-btn" href="https://t.me/CBeeNet" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> @CBeeNet</a>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<!-- ========== صفحه داشبورد ========== -->
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>

  <!-- 3 Sparkline Cards - Unified Color -->
  <div class="sparkline-row">
    <div class="sparkline-card">
      <div class="sparkline-top">
        <span class="sparkline-label"><i class="ti ti-gauge"></i> بار نسبی</span>
        <span class="sparkline-value" id="spark-load">0<span class="unit">%</span></span>
      </div>
      <div class="sparkline-chart"><canvas id="sparkLoad"></canvas></div>
      <div class="sparkline-sub"><span class="dot"></span> لحظه‌ای</div>
    </div>
    <div class="sparkline-card">
      <div class="sparkline-top">
        <span class="sparkline-label"><i class="ti ti-database"></i> مصرف کل</span>
        <span class="sparkline-value" id="spark-traffic">0<span class="unit">MB</span></span>
      </div>
      <div class="sparkline-chart"><canvas id="sparkTraffic"></canvas></div>
      <div class="sparkline-sub"><span class="dot"></span> از راه‌اندازی</div>
    </div>
    <div class="sparkline-card">
      <div class="sparkline-top">
        <span class="sparkline-label"><i class="ti ti-plug-connected"></i> اتصالات</span>
        <span class="sparkline-value" id="spark-conns">0</span>
      </div>
      <div class="sparkline-chart"><canvas id="sparkConns"></canvas></div>
      <div class="sparkline-sub"><span class="dot"></span> لحظه‌ای</div>
    </div>
  </div>

  <!-- وضعیت سرویس و خلاصه کانفیگ‌ها -->
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · 3 mode</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● فعال v1.0.0</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">CBee Gateway v1.0.0 · 2026 · Railway</span>
    <a class="df-link" href="https://t.me/CBeeNet" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/CBeeNet</a>
  </div>
</section>

<!-- ========== سایر صفحات (همانند قبل) ========== -->
<!-- لینک‌ها -->
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل‌های انتقال (چندگانه)</div>
        <div class="proto-group" id="proto-group">
          <button class="proto-btn active" data-proto="vless-ws" onclick="toggleProtoBtn(this)">VLESS / WS <span class="proto-badge">WebSocket</span></button>
          <button class="proto-btn" data-proto="xhttp-packet-up" onclick="toggleProtoBtn(this)">XHTTP · packet-up <span class="proto-badge">Siz10</span></button>
          <button class="proto-btn" data-proto="xhttp-stream-up" onclick="toggleProtoBtn(this)">XHTTP · stream-up <span class="proto-badge">Siz10</span></button>
        </div>
        <div style="margin-top:12px;display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--accent-d);border-radius:10px;border:1px solid var(--card-b)">
          <span style="font-size:12px;font-weight:700;color:var(--t2)"><i class="ti ti-layers-intersect"></i> تعداد ساخت هم‌زمان</span>
          <div class="count-chips">
            <span class="count-chip active" onclick="setCount(1,this)">۱</span>
            <span class="count-chip" onclick="setCount(5,this)">۵</span>
            <span class="count-chip" onclick="setCount(10,this)">۱۰</span>
            <span class="count-chip" onclick="setCount(50,this)">۵۰</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>

<!-- گروه‌های ساب -->
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>

<!-- سابسکریپشن -->
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی (هر کانفیگ)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون <i class="ti ti-rss"></i> کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">شامل تمام کانفیگ‌های فعال.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک سابسکریپشن گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>

<!-- ترافیک -->
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<!-- اتصالات -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div><div class="conn-hero-label">اتصالات زنده</div><div class="conn-hero-val" id="ch-count">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-transfer"></i></div><div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div><div class="conn-hero-val" id="ch-traffic">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-clock"></i></div><div class="conn-hero-label">میانگین مدت اتصال</div><div class="conn-hero-val" id="ch-avgdur">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div><div class="conn-hero-label">آی‌پی‌های یکتا</div><div class="conn-hero-val" id="ch-uniq">—</div></div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>

<!-- امنیت -->
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card"><div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div>
    </div>
    <div class="card"><div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک</span><span class="sr-v" style="color:var(--green-t)">● اختیاری</span></div>
    </div>
  </div>
</section>

<!-- لاگ‌ها -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>

<!-- خطاها -->
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>

<!-- تست WebSocket -->
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>

<!-- ========== صفحه تنظیمات (پیشرفته) ========== -->
<section class="pg" id="pg-settings">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="tb-sub">مدیریت پیکربندی پنل</div></div>
    <div class="tb-right"><span class="badge bg-blue">v1.0.0</span></div>
  </div>
  <div class="g2">
    <!-- بخش تغییر تم -->
    <div class="card">
      <div class="card-title"><i class="ti ti-palette"></i> تغییر تم</div>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div>
          <label style="font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px">تم تاریک</label>
          <div style="display:flex;gap:10px;flex-wrap:wrap">
            <button class="btn btn-p" style="background:#1677ff;color:#fff;box-shadow:0 2px 8px rgba(22,119,255,0.4)" onclick="setTheme('dark-blue')"><i class="ti ti-circle"></i> آبی</button>
            <button class="btn btn-p" style="background:#ef4444;color:#fff;box-shadow:0 2px 8px rgba(239,68,68,0.4)" onclick="setTheme('dark-red')"><i class="ti ti-circle"></i> قرمز</button>
            <button class="btn btn-p" style="background:#f59e0b;color:#000;box-shadow:0 2px 8px rgba(245,158,11,0.4)" onclick="setTheme('dark-yellow')"><i class="ti ti-circle"></i> زرد</button>
          </div>
        </div>
        <div>
          <label style="font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px">تم روشن</label>
          <div style="display:flex;gap:10px;flex-wrap:wrap">
            <button class="btn btn-p" style="background:#1677ff;color:#fff;box-shadow:0 2px 8px rgba(22,119,255,0.3)" onclick="setTheme('light-blue')"><i class="ti ti-circle"></i> آبی</button>
            <button class="btn btn-p" style="background:#ef4444;color:#fff;box-shadow:0 2px 8px rgba(239,68,68,0.3)" onclick="setTheme('light-red')"><i class="ti ti-circle"></i> قرمز</button>
            <button class="btn btn-p" style="background:#f59e0b;color:#000;box-shadow:0 2px 8px rgba(245,158,11,0.3)" onclick="setTheme('light-yellow')"><i class="ti ti-circle"></i> زرد</button>
          </div>
        </div>
        <div class="cl"><i class="ti ti-info-circle"></i><span>تم پیش‌فرض: <strong id="current-theme-display">dark-yellow</strong></span></div>
      </div>
    </div>

    <!-- بخش تنظیمات نام سرور (پیشرفته) -->
    <div class="card">
      <div class="card-title"><i class="ti ti-server-2"></i> تنظیمات نام سرور</div>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div class="fg">
          <label>نام اصلی سرور (Server Name)</label>
          <input class="fi" id="server-name-input" placeholder="مثلاً: CBeeNet" style="width:100%">
          <span style="font-size:9px;color:var(--t3)">این نام در قالب <code>{name}</code> استفاده می‌شود</span>
        </div>
        <div class="fg">
          <label>پیشوند (Prefix) - اختیاری</label>
          <input class="fi" id="server-prefix-input" placeholder="مثلاً: MyServer" style="width:100%">
          <span style="font-size:9px;color:var(--t3)">در قالب <code>{prefix}</code> استفاده می‌شود</span>
        </div>
        <div class="fg">
          <label>قالب نمایش (Template)</label>
          <input class="fi" id="server-template-input" placeholder="مثلاً: [{name}][{prefix}][{protocol}]" style="width:100%" value="[{name}][{prefix}][{protocol}]">
          <span style="font-size:9px;color:var(--t3)">از <code>{name}</code>، <code>{prefix}</code>، <code>{protocol}</code> استفاده کنید</span>
        </div>
        <div class="cl"><i class="ti ti-info-circle"></i><span>پیش‌نمایش: <code id="server-format-preview">[CBeeNet][MyServer][Protocol]</code></span></div>
        <button class="btn btn-p" onclick="saveServerSettings()"><i class="ti ti-device-floppy"></i> ذخیره تنظیمات سرور</button>
        <div id="server-save-result" style="font-size:11px;color:var(--green-t);display:none">✓ ذخیره شد</div>
      </div>
    </div>
  </div>
  <!-- بخش تنظیمات دیگر (همان تغییر رمز) -->
  <div class="g2" style="margin-top:16px">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.0.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field"><label>رمز فعلی</label><input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی"><button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button></div>
        <div class="pw-field" style="margin-bottom:6px"><label>رمز جدید</label><input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)"><button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button></div>
        <div class="pw-strength" id="pw-strength-bar"><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div></div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs"><span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span><span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span><span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span></div>
        <div class="pw-field" style="margin-bottom:18px"><label>تکرار رمز جدید</label><input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید"><button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button></div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>
</main>

<script>
// ========== متغیرهای سراسری ==========
let isDark = localStorage.getItem('CBeeNet-theme') || 'dark-yellow';
let currentTheme = isDark;

// ========== توابع تم ==========
function applyTheme(theme){
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('CBeeNet-theme', theme);
  currentTheme = theme;
  document.getElementById('current-theme-display').textContent = theme;
  const isLight = theme.startsWith('light');
  const icon = isLight ? 'ti-moon' : 'ti-sun';
  const label = isLight ? 'تم تاریک' : 'تم روشن';
  document.getElementById('theme-icon').className = 'ti ' + icon;
  document.getElementById('theme-label').textContent = label;
  const mobIcon = document.getElementById('theme-mob-icon');
  if(mobIcon) mobIcon.className = 'ti ' + icon;
}

function setTheme(theme){
  applyTheme(theme);
  toast('تم به ' + theme + ' تغییر کرد', 'ok');
}

function toggleTheme(){
  const isLight = currentTheme.startsWith('light');
  const color = currentTheme.split('-')[1] || 'yellow';
  const newTheme = isLight ? 'dark-' + color : 'light-' + color;
  applyTheme(newTheme);
}

applyTheme(localStorage.getItem('CBeeNet-theme') || 'dark-yellow');

// ========== توابع کمکی ==========
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(protocols){
  if(!protocols || !protocols.length) protocols = ['vless-ws'];
  const labels = {
    'vless-ws': ['VLESS · WS', 'pc-ws'],
    'xhttp-packet-up': ['XHTTP · packet-up', 'pc-xhttp'],
    'xhttp-stream-up': ['XHTTP · stream-up', 'pc-xhttp'],
    'xhttp-stream-one': ['XHTTP ULTRA', 'pc-ultra']
  };
  return protocols.map(p => {
    const v = labels[p] || labels['vless-ws'];
    return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
  }).join('');
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}

// ========== توابع مدیریت پروتکل ==========
function toggleProtoBtn(el){ el.classList.toggle('active'); }
function getSelectedProtocols(){
  const btns = document.querySelectorAll('.proto-btn');
  const selected = [];
  btns.forEach(btn => { if(btn.classList.contains('active')) selected.push(btn.dataset.proto); });
  return selected.length ? selected : ['vless-ws'];
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setCount(val,el){
  document.getElementById('nl-count').value = val;
  document.querySelectorAll('.count-chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
document.addEventListener('DOMContentLoaded', function() {
  if(!document.getElementById('nl-count')) {
    const hidden = document.createElement('input');
    hidden.type = 'hidden';
    hidden.id = 'nl-count';
    hidden.value = 1;
    document.querySelector('.cp-body').appendChild(hidden);
  }
  // بارگذاری تنظیمات سرور از localStorage
  const savedServer = localStorage.getItem('CBeeNet-server-name') || 'CBeeNet';
  const savedPrefix = localStorage.getItem('CBeeNet-server-prefix') || '';
  const savedTemplate = localStorage.getItem('CBeeNet-server-template') || '[{name}][{prefix}][{protocol}]';
  document.getElementById('server-name-input').value = savedServer;
  document.getElementById('server-prefix-input').value = savedPrefix;
  document.getElementById('server-template-input').value = savedTemplate;
  updateServerFormatPreview();
});
function updateServerFormatPreview(){
  const name = document.getElementById('server-name-input').value.trim() || 'CBeeNet';
  const prefix = document.getElementById('server-prefix-input').value.trim() || '';
  const template = document.getElementById('server-template-input').value.trim() || '[{name}][{prefix}][{protocol}]';
  const preview = template
    .replace(/{name}/g, name)
    .replace(/{prefix}/g, prefix)
    .replace(/{protocol}/g, 'Protocol');
  document.getElementById('server-format-preview').textContent = preview;
}
document.getElementById('server-name-input').addEventListener('input', updateServerFormatPreview);
document.getElementById('server-prefix-input').addEventListener('input', updateServerFormatPreview);
document.getElementById('server-template-input').addEventListener('input', updateServerFormatPreview);
async function saveServerSettings(){
  const name = document.getElementById('server-name-input').value.trim() || 'CBeeNet';
  const prefix = document.getElementById('server-prefix-input').value.trim() || '';
  const template = document.getElementById('server-template-input').value.trim() || '[{name}][{prefix}][{protocol}]';
  try {
    const r = await authF('/api/settings/server', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ server_name: name, server_prefix: prefix, server_template: template })
    });
    const result = await r.json();
    if(result.ok){
      localStorage.setItem('CBeeNet-server-name', name);
      localStorage.setItem('CBeeNet-server-prefix', prefix);
      localStorage.setItem('CBeeNet-server-template', template);
      document.getElementById('server-save-result').style.display = 'block';
      setTimeout(() => document.getElementById('server-save-result').style.display = 'none', 3000);
      toast('تنظیمات سرور ذخیره شد ✓', 'ok');
    } else {
      toast('خطا در ذخیره تنظیمات', 'err');
    }
  } catch(e) {
    toast('خطا در ارتباط با سرور', 'err');
  }
}

// ========== ناوبری و سایدبار ==========
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}

// ========== اسپارک‌لاین‌ها ==========
const sparkData = { load: [], traffic: [], conns: [] };
const MAX_SPARK = 60;
let sparkLoadChart, sparkTrafficChart, sparkConnsChart;
let ch1, ch2, ch3;
function initSparklineCharts(){
  const accentColor = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#1677ff';
  const accentBg = getComputedStyle(document.documentElement).getPropertyValue('--accent-d').trim() || 'rgba(22,119,255,0.12)';
  const ctxLoad = document.getElementById('sparkLoad').getContext('2d');
  sparkLoadChart = new Chart(ctxLoad, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.3 }] },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false }, tooltip: { enabled: false } }, scales: { x: { display: false, grid: { display: false } }, y: { display: false, grid: { display: false }, min: 0, max: 100 } }, animation: { duration: 100 } }
  });
  const ctxTraffic = document.getElementById('sparkTraffic').getContext('2d');
  sparkTrafficChart = new Chart(ctxTraffic, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.3 }] },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false }, tooltip: { enabled: false } }, scales: { x: { display: false, grid: { display: false } }, y: { display: false, grid: { display: false }, min: 0 } }, animation: { duration: 100 } }
  });
  const ctxConns = document.getElementById('sparkConns').getContext('2d');
  sparkConnsChart = new Chart(ctxConns, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.3 }] },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false }, tooltip: { enabled: false } }, scales: { x: { display: false, grid: { display: false } }, y: { display: false, grid: { display: false }, min: 0 } }, animation: { duration: 100 } }
  });
}
function updateSparkline(chart, data, maxVal){
  if(!chart) return;
  if(data.length > MAX_SPARK) data.shift();
  const labels = data.map((_, i) => i);
  chart.data.labels = labels;
  chart.data.datasets[0].data = data;
  if(maxVal){
    chart.options.scales.y.max = maxVal;
  }
  chart.update('none');
}

// ========== دریافت داده‌ها ==========
let prevTraf = 0;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta = d.total_traffic_mb - prevTraf;
    const pct = Math.min(100, Math.max(0, Math.round((delta / 50) * 100 * 10) / 10));
    document.getElementById('bw-pct').textContent = pct + '%';
    document.getElementById('bw-bar').style.width = pct + '%';
    prevTraf = d.total_traffic_mb;
    sparkData.load.push(pct);
    document.getElementById('spark-load').innerHTML = pct + '<span class="unit">%</span>';
    updateSparkline(sparkLoadChart, sparkData.load, 100);
    const trafficVal = parseFloat(d.total_traffic_mb.toFixed(2));
    sparkData.traffic.push(trafficVal);
    document.getElementById('spark-traffic').innerHTML = trafficVal + '<span class="unit">MB</span>';
    const maxTraffic = Math.max(10, ...sparkData.traffic);
    updateSparkline(sparkTrafficChart, sparkData.traffic, maxTraffic * 1.2);
    const connsVal = d.active_connections || 0;
    sparkData.conns.push(connsVal);
    document.getElementById('spark-conns').textContent = connsVal;
    const maxConns = Math.max(5, ...sparkData.conns);
    updateSparkline(sparkConnsChart, sparkData.conns, maxConns * 1.2);
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    const curSub=nlSub.value;
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    if(curSub)nlSub.value=curSub;
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';
    // استفاده از تنظیمات سرور برای نمایش نام
    const serverName = localStorage.getItem('CBeeNet-server-name') || 'CBeeNet';
    const serverPrefix = localStorage.getItem('CBeeNet-server-prefix') || '';
    const serverTemplate = localStorage.getItem('CBeeNet-server-template') || '[{name}][{prefix}][{protocol}]';
    grid.innerHTML=links.map(l=>{
      const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
      const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
      const allowed=l.active&&!l.expired;
      const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
      return `<div class="cfg-card ${cardCls}">
        <div class="cfg-row">
          <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
          <div class="cfg-identity">
            <div class="cfg-label">${esc(l.label)}</div>
            <div class="cfg-sub-meta">
              <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
              <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col">
            <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
            <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-badges-col">
            ${protoBadge(l.protocols || ['vless-ws'])}
            ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
            <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>`;
    }).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocols = getSelectedProtocols();
  if(!protocols.length){toast('حداقل یک پروتکل انتخاب کنید','err');return}
  const count = parseInt(document.getElementById('nl-count').value) || 1;
  const body={label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocols,count};
  try{
    let r, d;
    if (count > 1) {
      r = await authF('/api/links/bulk', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      d = await r.json();
      toast(count+' کانفیگ ساخته شد ✓','ok');
      if (d.sub_url) navigator.clipboard.writeText(d.sub_url).catch(()=>{});
    } else {
      r = await authF('/api/links', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
      d = await r.json();
      if (d.sub_url) navigator.clipboard.writeText(d.sub_url).catch(()=>{});
      else navigator.clipboard.writeText(d.vless_link).catch(()=>{});
      toast('کانفیگ ساخته شد ✓','ok');
    }
    ['nl-label','nl-val','nl-exp','nl-note'].forEach(id=>document.getElementById(id).value='');
    document.querySelectorAll('.proto-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('.proto-btn[data-proto="vless-ws"]').classList.add('active');
    document.getElementById('nl-count').value = 1;
    document.querySelectorAll('.count-chip').forEach(c=>c.classList.remove('active'));
    document.querySelector('.count-chip').classList.add('active');
    loadLinks();
  } catch(e){ toast('خطا در ساخت','err'); }
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const body={label,note,limit_value:val||0,limit_unit:unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    const grid=document.getElementById('subs-grid');
    if(!subs.length){grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید</div></div>';return}
    grid.innerHTML=subs.map(s=>`
      <div class="sub-card">
        <div class="sub-card-top">
          <div class="sub-card-head-v2">
            <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
            <div class="sub-card-titles"><div class="sub-card-name-v2">${esc(s.name)}</div><div class="sub-card-desc-v2">${s.desc||'بدون توضیحات'}</div></div>
            <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}"><i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i></div>
          </div>
          <div class="sub-card-stats">
            <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
            <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
            <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
          </div>
        </div>
        <div class="sub-card-url-row"><span class="sub-card-url-text">${esc(s.public_url)}</span><button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i></button><button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')"><i class="ti ti-external-link"></i></button></div>
        <div class="sub-card-bottom">
          <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
          <button class="btn btn-sm btn-pur" onclick="copyAllSubLinks('${esc(s.sub_id)}')"><i class="ti ti-copy"></i> کپی همه</button>
          <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
          <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')"><i class="ti ti-trash"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
function filterSubs(q){q=q.trim().toLowerCase();if(!q){loadSubs();return}renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)))}
function renderSubsGrid(subs){/* مشابه loadSubs ولی با فیلتر */}

async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="padding:20px;text-align:center">در حال بارگذاری...</div>';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty">هنوز کانفیگی وجود ندارد</div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info"><div class="lrow-v2-name">${esc(l.label)}</div><div class="lrow-v2-meta">${fmtB(l.used_bytes)}</div></div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});renderLmodalList(lmodalLinks);}
function updateLmodalCount(){document.getElementById('lmodal-count').textContent=toFa(lmodalInSub.size)+' انتخاب شده';}
function filterLmodal(q){q=q.trim().toLowerCase();document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';});}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty">هنوز گروهی ندارید</div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div><div style="font-weight:700;font-size:13px">${esc(s.name)}</div><div style="font-size:10px;color:var(--accent)">${esc(s.sub_url)}</div><div style="font-size:10px;color:var(--t3)">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)}</div></div>
        <div style="display:flex;gap:5px"><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}')"><i class="ti ti-copy"></i> ساب</button><button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button></div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}
function parseBytesFmt(s){if(!s)return 0;const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);if(!m)return 0;const n=parseFloat(m[1]),u=m[2].toUpperCase();const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};return n*(mult[u]||0);}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){grid.innerHTML='';ce.style.display='block';document.getElementById('ch-traffic').textContent='—';document.getElementById('ch-avgdur').textContent='—';document.getElementById('ch-uniq').textContent='—';return;}
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id"><div class="conn-ip-v2">${esc(c.ip)}<button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}')"><i class="ti ti-copy"></i></button></div><div class="conn-label-v2">${esc(c.label)}</div></div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge([protoVal])}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">ترافیک</div><div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div></div></div>
            <div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-clock"></i></div><div><div class="conn-stat-text-label">مدت</div><div class="conn-stat-text-val">${dur}</div></div></div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
function refreshAll(){
  fetchStats();
  if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
  if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
  if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
  if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
  if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  toast('رفرش شد ✓','ok');
}
async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#1677ff','#4096ff','#0050b3','#003a8c'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c3=document.getElementById('ch3');
  if(c3){
    const ctx3 = c3.getContext('2d');
    const gradFill3 = makeGradient(ctx3, 'rgba(22,119,255,0.45)', 'rgba(22,119,255,0)');
    ch3 = new Chart(ctx3, {
      type: 'line',
      data: { labels: [], datasets: [{ label: 'مصرف', data: [], borderColor: 'var(--accent)', backgroundColor: gradFill3, fill: true, tension: 0.45, pointRadius: 0, borderWidth: 3 }] },
      options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false }, ticks: { color: '#6e7681', font: { size: 9 } } }, y: { grid: { color: 'rgba(22,119,255,0.05)' }, ticks: { color: '#6e7681', font: { size: 9 }, callback: v => v + ' MB' } } } }
    });
  }
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log');const p=document.createElement('p');const colors={ok:'#10b981',err:'#ef4444',info:'#8b949e',sent:'#1677ff'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل');ws.onerror=()=>wsLog('err','✗ خطا');ws.onmessage=m=>wsLog('info','دریافت '+m.data.length+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')')}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
async function copyAllSubLinks(subId){
  const r=await authF('/api/links');const d=await r.json();const links=d.links||[];const sub=allSubsRaw.find(s=>s.sub_id===subId);if(!sub){toast('گروه پیدا نشد','err');return}const subLinkIds=sub.link_ids||[];const urls=links.filter(l=>subLinkIds.includes(l.uuid)&&l.active&&!l.expired).map(l=>l.sub_url);if(!urls.length){toast('کانفیگ فعالی نیست','err');return}navigator.clipboard.writeText(urls.join('\n')).then(()=>toast(toFa(urls.length)+' لینک کپی شد ✓','ok'));
}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  initSparklineCharts();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  document.getElementById('sub-all-url')&&(document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all');
  fetchStats();loadLinks();loadSubs();
  setInterval(fetchStats,3000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});
</script>
</body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>CBee Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0d1117;--card:#161b22;--card-b:#30363d;--accent:#1677ff;--accent2:#4096ff;--t1:#f0f6fc;--t2:#8b949e;--t3:#6e7681;--radius:16px}}
body{{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}}
.wrap{{max-width:800px;width:100%}}
.brand{{font-size:28px;font-weight:900;text-align:center;margin-bottom:20px;color:var(--accent2)}}
.loading{{text-align:center;padding:40px;color:var(--t3)}}
.card{{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px}}
</style>
</head>
<body>
<div class="wrap"><div class="brand">CBee</div><div id="root" class="loading">در حال بارگذاری...</div></div>
<script>
const UUID_KEY='{uuid_key}';let savedPw='';
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json();}}
async function renderContent(d){{let html=`<div class="card"><h2 style="color:var(--accent2)">${{d.name}}</h2><p style="color:var(--t3)">${{d.desc||''}}</p><p>اتصالات فعال: ${{d.active_connections}}</p><p>کل مصرف: ${{d.total_used_fmt}}</p><hr style="margin:15px 0;border-color:var(--card-b)"><div>`;for(let l of d.links){{html+=`<div style="background:rgba(0,0,0,.2);border-radius:12px;padding:12px;margin-bottom:8px;border:1px solid var(--card-b)"><strong style="color:var(--accent2)">${{l.label}}</strong> <span style="color:var(--t3)">${{l.used_fmt}} / ${{l.limit_fmt}}</span><div style="font-size:10px;color:var(--t3)">${{l.vless_link.substring(0,60)}}…</div></div>`;}}html+=`</div></div>`;document.getElementById('root').innerHTML=html;}}
async function init(){{const data=await loadData();if(data.locked){{document.getElementById('root').innerHTML=`<div class="card" style="text-align:center"><h3 style="color:var(--accent2)">${{data.name}}</h3><p>این گروه با رمز محافظت شده است.</p><input type="password" id="pw" placeholder="رمز را وارد کنید" style="margin:10px;padding:8px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:white;width:200px"><br><button onclick="submitPw()" style="padding:8px 16px;background:var(--accent);border:none;border-radius:8px;cursor:pointer;color:#fff;font-weight:700">ورود</button></div>`;}}else{{renderContent(data);}}}}
async function submitPw(){{const pw=document.getElementById('pw').value;const data=await loadData(pw);if(data.locked){{alert('رمز اشتباه است');return;}}savedPw=pw;renderContent(data);}}
init();
</script>
</body></html>"""
