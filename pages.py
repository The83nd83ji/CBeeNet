# pages.py - CBee Gateway v1.0.0 - Premium Dashboard with Fixed Login, Smart Alerts & Professional Chart
import json

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login · CBee</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
html, body { height:100%; overflow:hidden; }
body {
  font-family: 'Vazirmatn', 'Segoe UI', sans-serif;
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
  filter: blur(120px);
  z-index: 0;
  pointer-events: none;
  animation: floatOrb 22s ease-in-out infinite alternate;
}
.o1 { width: 450px; height: 450px; background: rgba(22,119,255,0.08); top: -180px; right: -100px; animation-delay: 0s; }
.o2 { width: 350px; height: 350px; background: rgba(22,119,255,0.05); bottom: -120px; left: -80px; animation-delay: 7s; }
.o3 { width: 280px; height: 280px; background: rgba(22,119,255,0.04); top: 45%; left: 55%; animation-delay: 3.5s; }
.o4 { width: 200px; height: 200px; background: rgba(22,119,255,0.03); bottom: 30%; right: 25%; animation-delay: 11s; }
@keyframes floatOrb {
  0% { transform: translate(0,0) scale(1); }
  33% { transform: translate(70px,-80px) scale(1.1); }
  66% { transform: translate(-50px,50px) scale(0.85); }
  100% { transform: translate(40px,-30px) scale(1.05); }
}
.wrap { position: relative; z-index: 10; width: 100%; max-width: 420px; }
.card {
  background: rgba(22,27,34,0.75);
  backdrop-filter: blur(32px);
  -webkit-backdrop-filter: blur(32px);
  border: 1px solid rgba(48,54,61,0.6);
  border-radius: 36px;
  padding: 42px 36px 36px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7), 0 0 100px rgba(22,119,255,0.04);
  position: relative;
  overflow: hidden;
}
.card::before {
  content: '';
  position: absolute;
  top: -100px;
  right: -100px;
  width: 260px;
  height: 260px;
  background: radial-gradient(circle, rgba(22,119,255,0.06), transparent 70%);
  pointer-events: none;
}
.brand {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 28px;
  position: relative;
  z-index: 1;
}
.brand-name {
  font-size: 44px;
  font-weight: 900;
  font-family: 'Vazirmatn', sans-serif;
  background: linear-gradient(135deg, #1677ff, #0050b3);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: -0.02em;
  text-shadow: 0 0 50px rgba(22,119,255,0.15);
}
.brand-sub {
  font-size: 10px;
  color: #8b949e;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  font-weight: 600;
  margin-top: 2px;
}
.lang-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 22px;
}
.lang-btn {
  background: transparent;
  border: 1px solid #30363d;
  color: #8b949e;
  padding: 5px 16px;
  border-radius: 24px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  font-family: inherit;
  transition: 0.25s;
}
.lang-btn:hover { border-color: #1677ff; color: #f0f6fc; }
.lang-btn.active { background: #1677ff; border-color: #1677ff; color: #fff; box-shadow: 0 4px 14px rgba(22,119,255,0.3); }
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
  margin-bottom: 26px;
  line-height: 1.7;
}
.err {
  display: none;
  background: rgba(239,68,68,0.12);
  border: 1px solid rgba(239,68,68,0.3);
  border-radius: 14px;
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
input[type="password"], input[type="text"] {
  width: 100%;
  padding: 14px 48px 14px 18px;
  border-radius: 16px;
  border: 1px solid #30363d;
  background: rgba(0,0,0,0.35);
  color: #f0f6fc;
  font-family: inherit;
  font-size: 14px;
  outline: none;
  transition: all 0.25s;
}
[dir="rtl"] input[type="password"], [dir="rtl"] input[type="text"] {
  padding: 14px 18px 14px 48px;
}
input[type="password"]:focus, input[type="text"]:focus {
  border-color: rgba(22,119,255,0.6);
  background: rgba(0,0,0,0.45);
  box-shadow: 0 0 0 5px rgba(22,119,255,0.07);
}
.ic {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: #8b949e;
  font-size: 18px;
  pointer-events: none;
  transition: 0.2s;
}
[dir="rtl"] .ic {
  right: auto;
  left: 16px;
}
input:focus + .ic { color: #1677ff; }
.btn {
  width: 100%;
  padding: 15px;
  border-radius: 16px;
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
  box-shadow: 0 6px 28px rgba(22,119,255,0.3);
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
.btn:hover { transform: translateY(-2px); box-shadow: 0 10px 40px rgba(22,119,255,0.45); }
.btn:active { transform: translateY(0) scale(0.98); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }
.btn span { position: relative; z-index: 1; display: flex; align-items: center; gap: 6px; }
.footer {
  margin-top: 26px;
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
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="orb o4"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-name">CBee</div>
      <div class="brand-sub">Gateway · v1.0.0</div>
    </div>
    <div class="lang-row">
      <button class="lang-btn active" data-lang="en" onclick="setLoginLang('en')">English</button>
      <button class="lang-btn" data-lang="fa" onclick="setLoginLang('fa')">فارسی</button>
    </div>
    <h1 id="login-title">Login to Panel</h1>
    <p class="sub" id="login-sub">Enter password to access the dashboard</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field">
        <label id="login-pw-label">Password</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="••••••••" autofocus required>
          <i class="ti ti-key ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn">
        <span><i class="ti ti-login-2"></i> <span id="login-btn-text">Login to Dashboard</span></span>
      </button>
    </form>
    <div class="footer">
      <a href="https://t.me/CBeeNet" target="_blank"><i class="ti ti-brand-telegram"></i> <span id="login-telegram">@CBeeNet</span></a>
    </div>
  </div>
</div>
<script>
const loginLang = {
  en: {
    title: 'Login to Panel',
    sub: 'Enter password to access the dashboard',
    pw_label: 'Password',
    pw_placeholder: '••••••••',
    btn_text: 'Login to Dashboard',
    telegram: '@CBeeNet',
    error_default: 'Wrong password'
  },
  fa: {
    title: 'ورود به پنل',
    sub: 'رمز عبور را برای دسترسی به داشبورد وارد کنید',
    pw_label: 'رمز عبور',
    pw_placeholder: '••••••••',
    btn_text: 'ورود به داشبورد',
    telegram: '@CBeeNet',
    error_default: 'رمز عبور اشتباه است'
  }
};
let currentLoginLang = localStorage.getItem('CBeeNet-login-lang') || 'en';
function applyLoginLang(lang){
  const dict = loginLang[lang] || loginLang.en;
  document.getElementById('login-title').textContent = dict.title;
  document.getElementById('login-sub').textContent = dict.sub;
  document.getElementById('login-pw-label').textContent = dict.pw_label;
  document.getElementById('pw').placeholder = dict.pw_placeholder;
  document.getElementById('login-btn-text').textContent = dict.btn_text;
  document.getElementById('login-telegram').textContent = dict.telegram;
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === 'fa' ? 'rtl' : 'ltr';
  document.getElementById('pw').dir = 'ltr';
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  localStorage.setItem('CBeeNet-login-lang', lang);
  currentLoginLang = lang;
}
function setLoginLang(lang){ applyLoginLang(lang); }
applyLoginLang(localStorage.getItem('CBeeNet-login-lang') || 'en');
document.getElementById('form').addEventListener('submit', async e => {
  e.preventDefault();
  const btn = document.getElementById('btn');
  const err = document.getElementById('err');
  const et = document.getElementById('err-text');
  err.classList.remove('show');
  btn.disabled = true;
  btn.querySelector('span').innerHTML = '<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> ' + (currentLoginLang === 'fa' ? 'در حال ورود...' : 'Logging in...');
  try {
    const r = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password: document.getElementById('pw').value })
    });
    if (!r.ok) {
      const d = await r.json().catch(() => ({}));
      const dict = loginLang[currentLoginLang] || loginLang.en;
      throw new Error(d.detail || dict.error_default);
    }
    location.href = '/CFOX';
  } catch (e) {
    et.textContent = e.message;
    err.classList.add('show');
    btn.disabled = false;
    const dict = loginLang[currentLoginLang] || loginLang.en;
    btn.querySelector('span').innerHTML = '<i class="ti ti-login-2"></i> ' + dict.btn_text;
  }
});
</script>
</body></html>"""

LANG = {
  "en": {
    "dashboard": "Dashboard", "dashboard_sub": "System Overview",
    "active_connections": "Active Connections", "total_traffic": "Total Traffic",
    "total_links": "Configs", "uptime": "Uptime",
    "since_start": "Since Start", "active": "Active", "inactive": "Inactive",
    "refresh": "Refresh", "traffic_trend": "Bandwidth Usage",
    "service_status": "Service Status", "top_connections": "Live Connections",
    "no_connections": "No connections", "server": "Server",
    "settings": "Settings", "language": "Language",
    "farsi": "Persian", "english": "English",
    "save": "Save", "cancel": "Cancel", "delete": "Delete",
    "edit": "Edit", "copy": "Copy", "created": "Created",
    "expires": "Expires", "unlimited": "Unlimited",
    "used": "Used", "of": "of", "daily": "Daily",
    "hourly": "Hourly", "bandwidth": "Bandwidth",
    "connections": "Connections", "protocol": "Protocol",
    "ip_address": "IP Address", "port": "Port",
    "upload": "Upload", "download": "Download",
    "duration": "Duration", "status": "Status",
    "online": "Online", "offline": "Offline",
    "total": "Total", "users": "Users",
    "protocols": "Protocols", "traffic_usage": "Traffic Usage",
    "links": "Configs", "sub_groups": "Sub Groups",
    "subscription": "Subscription", "security": "Security",
    "logs": "Activity Logs", "errors": "Errors",
    "test_websocket": "WebSocket Test",
    "dark_theme": "Dark Theme", "light_theme": "Light Theme",
    "prestige_theme": "Prestige Theme", "blue": "Blue",
    "red": "Red", "yellow": "Yellow",
    "current_theme": "Current Theme",
    "server_settings": "Server & Link Settings",
    "server_name": "Server Name", "server_prefix": "Link Prefix",
    "link_template": "Link Name Template",
    "template_vars": "Available Variables",
    "template_note": "If `{protocol}` is not in the template, the protocol will not be shown.",
    "change_password": "Change Password",
    "current_password": "Current Password", "new_password": "New Password",
    "confirm_password": "Confirm Password",
    "password_strength": "Password Strength",
    "min_chars": "At least 4 characters", "contains_number": "Contains number",
    "contains_case": "Uppercase/Lowercase",
    "weak": "Very Weak", "medium": "Medium", "strong": "Strong",
    "save_password": "Save New Password",
    "login": "Login", "logout": "Logout",
    "login_title": "Login to Panel",
    "login_sub": "Enter password to access the dashboard",
    "password": "Password", "login_button": "Login to Dashboard",
    "telegram_channel": "Telegram Channel",
    "panel": "Panel", "system": "System",
    "configs": "Configs", "sub_groups_short": "Sub Groups",
    "activity_logs": "Activity Logs",
    "config_id": "Config ID",
    "sub_group_expiry": "Sub Group & Expiry",
    "no_group": "No Group",
    "days": "Days",
    "traffic_quota": "Traffic Quota",
    "transport_protocols": "Transport Protocols",
    "bulk_count": "Bulk Count",
    "create_config": "Create Config",
    "no_configs": "No configs yet",
    "new_group": "New Group",
    "no_groups": "No groups yet",
    "create_group": "Create a new group to organize your configs",
    "single_sub": "Single Subscription (per config)",
    "full_sub": "Full Subscription (Admin)",
    "full_sub_desc": "Includes all active configs.",
    "group_sub_links": "Group Subscription Links",
    "loading": "Loading...",
    "traffic_analysis": "Bandwidth usage analysis & monitoring",
    "total_traffic_used": "Total Traffic Used",
    "hourly_average": "Hourly Average",
    "per_hour": "/h",
    "peak_usage": "Peak Usage",
    "peak_hour": "Peak Hour",
    "lowest_usage": "Lowest Usage",
    "live_connections": "Live Connections",
    "total_traffic_live": "Total Traffic",
    "avg_duration": "Avg Duration",
    "unique_ips": "Unique IPs",
    "connections_list": "Connections List",
    "auto_update": "Auto-update every 5s",
    "no_active_connections": "No active connections",
    "will_appear": "They will appear here as soon as clients connect",
    "encryption": "Encryption",
    "access_control": "Access Control",
    "hash": "Hash",
    "session": "Session",
    "active_inactive": "Active/Inactive",
    "expiry_date": "Expiry Date",
    "public_page_pw": "Public Page Password",
    "optional": "Optional",
    "activity_logs_full": "Complete event history",
    "no_logs": "No logs yet",
    "error_logs": "Error Logs",
    "websocket_test": "WebSocket Test",
    "ws_note": "Only registered and active UUIDs can connect.",
    "connect": "Connect", "disconnect": "Disconnect", "send": "Send",
    "waiting_ws": "Waiting for connection...",
    "change_theme": "Change Theme",
    "server_link_settings": "Server & Link Settings",
    "save_settings": "Save Settings",
    "saved": "Saved",
    "online_status": "Online",
    "version": "Version", "framework": "Framework",
    "platform": "Platform", "storage": "Storage",
    "change_password_title": "Change Password",
    "change_password_sub": "Choose a strong password and keep it safe",
    "current_pw": "Current Password", "new_pw": "New Password",
    "confirm_pw": "Confirm Password",
    "save_new_pw": "Save New Password",
    "min_4_chars": "At least 4 chars",
    "contains_num": "Contains number",
    "contains_case_letters": "Uppercase/Lowercase",
    "very_weak": "Very Weak", "medium_strength": "Medium",
    "strong_strength": "Strong",
    "logout_btn": "Logout", "telegram_btn": "Telegram Channel",
    "load": "Load", "connections_live": "Live Connections",
    "traffic_chart": "Traffic Chart",
    "protocol_distribution": "Protocol Distribution",
    "daily_usage": "Daily Usage",
    "active_conns_table": "Active Connections",
    "configs_management": "Configs Management",
    "sub_groups_management": "Sub Groups Management",
    "subscription_links": "Subscription Links",
    "traffic_monitor": "Traffic Monitor",
    "connections_monitor": "Connections Monitor",
    "security_settings": "Security Settings",
    "activity_logs_title": "Activity Logs",
    "error_logs_title": "Error Logs",
    "websocket_tester": "WebSocket Tester",
    "system_settings": "System Settings",
    "language_settings": "Language Settings",
    "theme_settings": "Theme Settings",
    "server_info": "Server Info",
    "password_change": "Password Change",
    "save_changes": "Save Changes",
    "cancel_changes": "Cancel",
    "live": "Live", "running_time": "Running Time",
    "manage_configs": "Manage Configs for",
    "select_configs": "Select configs to include in this group",
    "select_all": "Select All", "deselect_all": "Deselect All",
    "changes_apply": "Changes apply immediately",
    "new_group_title": "Create New Group",
    "new_group_sub": "Create a separate public page to manage configs",
    "group_name": "Group Name",
    "description_optional": "Description (optional)",
    "public_page_password": "Public Page Password (optional)",
    "public_page_info": "This group's public page will be accessible via a unique link.",
    "edit_config": "Edit Config",
    "quota_0_unlimited": "Quota (0 = unlimited)",
    "expiry_days": "Expiry (days from now, 0 = no change/unlimited)",
    "expiry_note": "To keep current expiry, leave expiry field as 0.",
    "random_uuid": "Random UUID · Choose quota, expiry and protocol",
    "uuid_note": "UUID is generated randomly · Only registered UUIDs can connect · Protocol cannot be changed after creation.",
    "each_group_public": "Each group has its own public page with its configs",
    "single_sub_desc": "Each config has its own subscription URL. Click the",
    "icon_on_card": "icon on the config card.",
    "full_sub_note": "This URL only works in the browser where you're logged in (requires session cookie).",
    "based_on_mb": "Based on MB per hour",
    "lang_note": "Default language is English. Page will refresh after change.",
    "groups": "Groups",
    "usage": "Usage", "average": "Average",
    "protocols_legend": "Protocols",
    "daily_legend": "Daily",
    "hourly_legend": "Hourly",
    "bandwidth_usage": "Bandwidth Usage",
    "smart_alerts": "Smart Alerts",
    "alerts_sub": "Important events & notifications",
    "priority": "Priority",
    "critical": "Critical",
    "warning": "Warning",
    "info": "Info",
    "dismiss": "Dismiss",
    "filter_all": "All",
    "filter_critical": "Critical",
    "filter_warning": "Warning",
    "filter_info": "Info",
    "alert_expiry": "Config expiring soon",
    "alert_quota": "Traffic quota exceeded 80%",
    "alert_errors": "Repeated connection errors",
    "alert_new_ip": "New IP connected",
    "no_alerts": "No alerts to show"
  },
  "fa": {
    "dashboard": "داشبورد", "dashboard_sub": "نمای کلی سیستم",
    "active_connections": "اتصالات فعال", "total_traffic": "کل ترافیک",
    "total_links": "کانفیگ‌ها", "uptime": "آپتایم",
    "since_start": "از راه‌اندازی", "active": "فعال", "inactive": "غیرفعال",
    "refresh": "رفرش", "traffic_trend": "مصرف پهنای باند",
    "service_status": "وضعیت سرویس", "top_connections": "اتصال‌های لحظه‌ای",
    "no_connections": "هیچ اتصالی", "server": "سرور",
    "settings": "تنظیمات", "language": "زبان",
    "farsi": "فارسی", "english": "انگلیسی",
    "save": "ذخیره", "cancel": "انصراف", "delete": "حذف",
    "edit": "ویرایش", "copy": "کپی", "created": "ساخته شده",
    "expires": "انقضا", "unlimited": "نامحدود",
    "used": "مصرف", "of": "از", "daily": "روزانه",
    "hourly": "ساعتی", "bandwidth": "پهنای باند",
    "connections": "اتصالات", "protocol": "پروتکل",
    "ip_address": "آدرس آی‌پی", "port": "پورت",
    "upload": "آپلود", "download": "دانلود",
    "duration": "مدت", "status": "وضعیت",
    "online": "آنلاین", "offline": "آفلاین",
    "total": "کل", "users": "کاربران",
    "protocols": "پروتکل‌ها", "traffic_usage": "مصرف ترافیک",
    "links": "کانفیگ‌ها", "sub_groups": "گروه‌های ساب",
    "subscription": "سابسکریپشن", "security": "امنیت",
    "logs": "لاگ فعالیت‌ها", "errors": "خطاها",
    "test_websocket": "تست WebSocket",
    "dark_theme": "تم تاریک", "light_theme": "تم روشن",
    "prestige_theme": "تم پرستیژ", "blue": "آبی",
    "red": "قرمز", "yellow": "زرد",
    "current_theme": "تم پیش‌فرض",
    "server_settings": "تنظیمات سرور و نام لینک‌ها",
    "server_name": "نام سرور", "server_prefix": "پیشوند لینک‌ها",
    "link_template": "قالب نام کانفیگ‌ها",
    "template_vars": "متغیرهای قابل استفاده",
    "template_note": "اگر `{protocol}` در قالب نباشد، پروتکل در نام نمایش داده نمی‌شود.",
    "change_password": "تغییر رمز عبور",
    "current_password": "رمز فعلی", "new_password": "رمز جدید",
    "confirm_password": "تکرار رمز جدید",
    "password_strength": "قدرت رمز",
    "min_chars": "حداقل ۴ کاراکتر", "contains_number": "شامل عدد",
    "contains_case": "حروف بزرگ/کوچک",
    "weak": "خیلی ضعیف", "medium": "متوسط", "strong": "قوی",
    "save_password": "ذخیره رمز جدید",
    "login": "ورود", "logout": "خروج",
    "login_title": "ورود به پنل",
    "login_sub": "رمز عبور را برای دسترسی به داشبورد وارد کنید",
    "password": "رمز عبور", "login_button": "ورود به داشبورد",
    "telegram_channel": "کانال تلگرام",
    "panel": "پنل", "system": "سیستم",
    "configs": "کانفیگ‌ها", "sub_groups_short": "گروه‌های ساب",
    "activity_logs": "لاگ فعالیت‌ها",
    "config_id": "شناسه کانفیگ",
    "sub_group_expiry": "گروه ساب و انقضا",
    "no_group": "بدون گروه",
    "days": "روز",
    "traffic_quota": "سهمیه ترافیک",
    "transport_protocols": "پروتکل‌های انتقال",
    "bulk_count": "تعداد ساخت هم‌زمان",
    "create_config": "ساخت کانفیگ",
    "no_configs": "هنوز کانفیگی وجود ندارد",
    "new_group": "گروه جدید",
    "no_groups": "هنوز گروهی وجود ندارد",
    "create_group": "یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید",
    "single_sub": "سابسکریپشن تکی (هر کانفیگ)",
    "full_sub": "سابسکریپشن کامل (ادمین)",
    "full_sub_desc": "شامل تمام کانفیگ‌های فعال.",
    "group_sub_links": "لینک سابسکریپشن گروه‌ها",
    "loading": "در حال بارگذاری...",
    "traffic_analysis": "تحلیل و مانیتورینگ مصرف پهنای باند",
    "total_traffic_used": "کل ترافیک مصرفی",
    "hourly_average": "میانگین ساعتی",
    "per_hour": "در ساعت",
    "peak_usage": "پیک مصرف",
    "peak_hour": "بالاترین ساعت",
    "lowest_usage": "کمترین مصرف",
    "live_connections": "اتصالات زنده",
    "total_traffic_live": "مجموع ترافیک لحظه‌ای",
    "avg_duration": "میانگین مدت اتصال",
    "unique_ips": "آی‌پی‌های یکتا",
    "connections_list": "لیست اتصالات",
    "auto_update": "بروزرسانی خودکار هر ۵ ثانیه",
    "no_active_connections": "هیچ اتصال فعالی نیست",
    "will_appear": "به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند",
    "encryption": "رمزنگاری",
    "access_control": "کنترل دسترسی",
    "hash": "هش رمز",
    "session": "سشن",
    "active_inactive": "فعال/غیرفعال",
    "expiry_date": "تاریخ انقضا",
    "public_page_pw": "رمز صفحه پابلیک",
    "optional": "اختیاری",
    "activity_logs_full": "تاریخچه‌ی کامل رخدادهای پنل",
    "no_logs": "هنوز لاگی ثبت نشده",
    "error_logs": "لاگ خطاها",
    "websocket_test": "تست WebSocket",
    "ws_note": "فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.",
    "connect": "اتصال", "disconnect": "قطع", "send": "ارسال",
    "waiting_ws": "منتظر اتصال...",
    "change_theme": "تغییر تم",
    "server_link_settings": "تنظیمات سرور و نام لینک‌ها",
    "save_settings": "ذخیره تنظیمات",
    "saved": "ذخیره شد",
    "online_status": "آنلاین",
    "version": "نسخه", "framework": "فریم‌ورک",
    "platform": "پلتفرم", "storage": "ذخیره‌سازی",
    "change_password_title": "تغییر رمز عبور",
    "change_password_sub": "رمز قوی انتخاب کنید و آن را جایی امن نگه دارید",
    "current_pw": "رمز فعلی", "new_pw": "رمز جدید",
    "confirm_pw": "تکرار رمز جدید",
    "save_new_pw": "ذخیره رمز جدید",
    "min_4_chars": "حداقل ۴ کاراکتر",
    "contains_num": "شامل عدد",
    "contains_case_letters": "حروف بزرگ/کوچک",
    "very_weak": "خیلی ضعیف", "medium_strength": "متوسط",
    "strong_strength": "قوی",
    "logout_btn": "خروج", "telegram_btn": "کانال تلگرام",
    "load": "بار نسبی", "connections_live": "اتصالات لحظه‌ای",
    "traffic_chart": "نمودار ترافیک",
    "protocol_distribution": "توزیع پروتکل",
    "daily_usage": "مصرف روزانه",
    "active_conns_table": "اتصالات فعال",
    "configs_management": "مدیریت کانفیگ‌ها",
    "sub_groups_management": "مدیریت گروه‌های ساب",
    "subscription_links": "لینک‌های سابسکریپشن",
    "traffic_monitor": "مانیتورینگ ترافیک",
    "connections_monitor": "مانیتورینگ اتصالات",
    "security_settings": "تنظیمات امنیتی",
    "activity_logs_title": "لاگ فعالیت‌ها",
    "error_logs_title": "لاگ خطاها",
    "websocket_tester": "تست WebSocket",
    "system_settings": "تنظیمات سیستم",
    "language_settings": "تنظیمات زبان",
    "theme_settings": "تنظیمات تم",
    "server_info": "اطلاعات سرور",
    "password_change": "تغییر رمز عبور",
    "save_changes": "ذخیره تغییرات",
    "cancel_changes": "انصراف",
    "live": "لحظه‌ای", "running_time": "مدت روشن بودن",
    "manage_configs": "مدیریت کانفیگ‌های",
    "select_configs": "کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید",
    "select_all": "انتخاب همه", "deselect_all": "لغو همه",
    "changes_apply": "تغییرات بلافاصله اعمال می‌شود",
    "new_group_title": "ساخت گروه جدید",
    "new_group_sub": "یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید",
    "group_name": "نام گروه",
    "description_optional": "توضیحات (اختیاری)",
    "public_page_password": "رمز صفحه پابلیک (اختیاری)",
    "public_page_info": "صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.",
    "edit_config": "ویرایش کانفیگ",
    "quota_0_unlimited": "سهمیه (0 = نامحدود)",
    "expiry_days": "انقضا (روز از الان، 0 = بدون تغییر/نامحدود)",
    "expiry_note": "برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.",
    "random_uuid": "UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن",
    "uuid_note": "UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.",
    "each_group_public": "هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد",
    "single_sub_desc": "هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون",
    "icon_on_card": "کلیک کنید.",
    "full_sub_note": "این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).",
    "based_on_mb": "بر اساس مگابایت در هر ساعت",
    "lang_note": "زبان پیش‌فرض انگلیسی است. پس از تغییر، صفحه رفرش می‌شود.",
    "groups": "گروه",
    "usage": "مصرف", "average": "میانگین",
    "protocols_legend": "پروتکل‌ها",
    "daily_legend": "روزانه",
    "hourly_legend": "ساعتی",
    "bandwidth_usage": "مصرف پهنای باند",
    "smart_alerts": "هشدارهای هوشمند",
    "alerts_sub": "رویدادها و اعلان‌های مهم",
    "priority": "اولویت",
    "critical": "بحرانی",
    "warning": "هشدار",
    "info": "اطلاعات",
    "dismiss": "رد کردن",
    "filter_all": "همه",
    "filter_critical": "بحرانی",
    "filter_warning": "هشدار",
    "filter_info": "اطلاعات",
    "alert_expiry": "انقضای نزدیک کانفیگ",
    "alert_quota": "مصرف ترافیک بیش از ۸۰٪",
    "alert_errors": "خطاهای مکرر اتصال",
    "alert_new_ip": "آی‌پی جدید متصل شد",
    "no_alerts": "هیچ هشداری وجود ندارد"
  }
}

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
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
  --font-family:'Vazirmatn','Segoe UI',sans-serif;
}
[data-theme="dark-blue"]{--accent:#1677ff;--accent2:#4096ff;--accent-d:rgba(22,119,255,0.12);--accent-glow:rgba(22,119,255,0.35);--card-bh:rgba(22,119,255,0.20);}
[data-theme="dark-red"]{--accent:#ef4444;--accent2:#f87171;--accent-d:rgba(239,68,68,0.12);--accent-glow:rgba(239,68,68,0.35);--card-bh:rgba(239,68,68,0.20);}
[data-theme="dark-yellow"]{--accent:#f59e0b;--accent2:#fbbf24;--accent-d:rgba(245,158,11,0.12);--accent-glow:rgba(245,158,11,0.35);--card-bh:rgba(245,158,11,0.20);}
[data-theme="dark-prestige"]{
  --bg:#0a0e17;
  --bg2:#111927;
  --bg3:#1a2438;
  --card:#111927;
  --card-b:#1e2d45;
  --card-bh:rgba(26,122,255,0.25);
  --accent:#1a7aff;
  --accent2:#4d94ff;
  --accent-d:rgba(26,122,255,0.15);
  --accent-glow:rgba(26,122,255,0.35);
  --green:#10b981;
  --green-bg:rgba(16,185,129,0.10);
  --green-t:#34d399;
  --red:#ef4444;
  --red-bg:rgba(239,68,68,0.10);
  --red-t:#f87171;
  --amber:#f59e0b;
  --amber-bg:rgba(245,158,11,0.10);
  --amber-t:#fbbf24;
  --purple:#8b5cf6;
  --purple-bg:rgba(139,92,246,0.10);
  --t1:#e8edf5;
  --t2:#8fa4c8;
  --t3:#5a7298;
  --shadow:0 8px 32px rgba(0,0,0,0.6);
}
[data-theme="light-blue"]{--bg:#f6f8fa;--bg2:#ffffff;--bg3:#eaeef2;--card:#ffffff;--card-b:#d0d7de;--card-bh:rgba(22,119,255,0.25);--accent:#1677ff;--accent2:#4096ff;--accent-d:rgba(22,119,255,0.08);--accent-glow:rgba(22,119,255,0.25);--t1:#24292f;--t2:#57606a;--t3:#8b949e;--shadow:0 8px 28px rgba(0,0,0,0.08);}
[data-theme="light-red"]{--bg:#f6f8fa;--bg2:#ffffff;--bg3:#eaeef2;--card:#ffffff;--card-b:#d0d7de;--card-bh:rgba(239,68,68,0.25);--accent:#ef4444;--accent2:#f87171;--accent-d:rgba(239,68,68,0.08);--accent-glow:rgba(239,68,68,0.25);--t1:#24292f;--t2:#57606a;--t3:#8b949e;--shadow:0 8px 28px rgba(0,0,0,0.08);}
[data-theme="light-yellow"]{--bg:#f6f8fa;--bg2:#ffffff;--bg3:#eaeef2;--card:#ffffff;--card-b:#d0d7de;--card-bh:rgba(245,158,11,0.25);--accent:#f59e0b;--accent2:#fbbf24;--accent-d:rgba(245,158,11,0.08);--accent-glow:rgba(245,158,11,0.25);--t1:#24292f;--t2:#57606a;--t3:#8b949e;--shadow:0 8px 28px rgba(0,0,0,0.08);}
html,body{height:100%}
body{font-family:var(--font-family);background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s,border-color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
[dir="ltr"] .sidebar{right:auto;left:0;border-left:none;border-right:1px solid var(--card-b)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-text{font-size:20px;font-weight:900;color:var(--t1);font-family:var(--font-family);letter-spacing:-0.02em}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
[dir="ltr"] .sb-close{left:auto;right:12px}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px;border-radius:8px}
[dir="ltr"] .nav-it{border-right:none;border-left:2px solid transparent}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
[dir="ltr"] .nav-it.on{border-right-color:transparent;border-left-color:var(--accent)}
.nav-badge{margin-right:auto;background:rgba(245,158,11,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
[dir="ltr"] .nav-badge{margin-right:0;margin-left:auto}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#1DA1F2,#0D8BD9);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-title{color:var(--t1);font-size:16px;font-weight:900;font-family:var(--font-family)}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
[dir="ltr"] .main{margin-right:0;margin-left:var(--sidebar-w)}
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
.dash-stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:22px}
.dash-stat-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:all .2s;position:relative;overflow:hidden}
.dash-stat-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.dash-stat-card .label{font-size:10.5px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:6px}
.dash-stat-card .value{font-size:28px;font-weight:800;color:var(--t1);margin-top:4px;letter-spacing:-.02em}
.dash-stat-card .sub{font-size:10px;color:var(--t2);margin-top:4px}
.dash-stat-card .icon{position:absolute;top:16px;left:16px;font-size:22px;color:var(--accent);opacity:.3}
[dir="ltr"] .dash-stat-card .icon{left:auto;right:16px}
.dash-sparkline-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:22px}
.dash-spark-card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px 18px 14px;transition:all .2s}
.dash-spark-card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.dash-spark-card .spark-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.dash-spark-card .spark-label{font-size:10.5px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:5px}
.dash-spark-card .spark-label i{font-size:14px;color:var(--accent)}
.dash-spark-card .spark-value{font-size:20px;font-weight:800;color:var(--t1);letter-spacing:-.02em;line-height:1.2}
.dash-spark-card .spark-value .unit{font-size:13px;font-weight:500;color:var(--t3);margin-right:3px}
.dash-spark-card .spark-chart{height:160px;position:relative;margin-top:2px}
.dash-spark-card .spark-chart canvas{width:100% !important;height:100% !important}
.dash-spark-card .spark-sub{font-size:9.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:4px}
.dash-spark-card .spark-sub .dot{width:5px;height:5px;border-radius:50%;display:inline-block;background:var(--accent)}
.chart-controls{display:flex;align-items:center;justify-content:space-between;margin-top:8px;gap:8px;flex-wrap:wrap}
.chart-controls .time-range{font-size:10.5px;color:var(--t2);font-weight:600;font-family:ui-monospace,monospace;background:var(--accent-d);padding:3px 10px;border-radius:6px;border:1px solid var(--card-b)}
.chart-controls .btn-group{display:flex;gap:4px}
.chart-controls .btn-group button{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);border-radius:6px;padding:3px 10px;font-size:10px;cursor:pointer;font-family:inherit;transition:.15s;font-weight:600}
.chart-controls .btn-group button:hover{background:var(--accent-d);color:var(--accent2);border-color:var(--accent)}
.chart-controls .btn-group button:active{transform:scale(.96)}
.dash-charts-second{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:22px}
.dash-small-chart{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px 18px}
.dash-small-chart .chart-title{font-size:11px;font-weight:600;color:var(--t2);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.dash-small-chart .chart-title i{color:var(--accent)}
.dash-small-chart .chart-wrap{height:120px;position:relative}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}
@media(max-width:1024px){.dash-stats-grid{grid-template-columns:1fr 1fr}.dash-charts-second{grid-template-columns:1fr 1fr}}
@media(max-width:768px){.dash-charts-second{grid-template-columns:1fr}.dash-sparkline-row{grid-template-columns:1fr}.dash-stats-grid{grid-template-columns:1fr}.main{padding:62px 12px 50px}.sidebar{transform:translateX(100%)}[dir="ltr"] .sidebar{transform:translateX(-100%)}.sidebar.open{transform:translateX(0)}.sb-close{display:flex}.main{margin-right:0;padding-top:70px}[dir="ltr"] .main{margin-left:0}.mob-top{display:flex}}
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
.btn-lang{background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);padding:5px 12px;font-size:11px;border-radius:7px;cursor:pointer;font-family:inherit;transition:.15s}
.btn-lang:hover{background:var(--accent-d);color:var(--t1)}
.btn-lang.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.card{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
[dir="ltr"] .ml-auto{margin-right:0;margin-left:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
@media(max-width:768px){.g2{grid-template-columns:1fr}}
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
@media(max-width:1050px){.sidebar{transform:translateX(100%)}.sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}.sb-close{display:flex}.main{margin-right:0;padding-top:70px}.mob-top{display:flex}}
@media(max-width:500px){.main{padding:62px 12px 50px}.sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--accent);border-radius:10px}
/* Smart Alerts Styles */
.alerts-wrap{display:flex;flex-direction:column;gap:16px}
.alerts-filters{display:flex;gap:8px;flex-wrap:wrap}
.alerts-filters .btn{font-size:10.5px;padding:4px 12px;border-radius:20px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.alerts-filters .btn:hover{background:var(--accent-d);color:var(--t1)}
.alerts-filters .btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.alert-item{display:flex;gap:12px;padding:12px 14px;background:var(--card);border:1px solid var(--card-b);border-radius:12px;align-items:flex-start;transition:.15s}
.alert-item:hover{border-color:var(--card-bh)}
.alert-item.critical{border-left:3px solid var(--red)}
.alert-item.warning{border-left:3px solid var(--amber)}
.alert-item.info{border-left:3px solid var(--accent)}
.alert-icon{font-size:18px;flex-shrink:0;margin-top:2px}
.alert-icon.critical{color:var(--red-t)}
.alert-icon.warning{color:var(--amber-t)}
.alert-icon.info{color:var(--accent2)}
.alert-body{flex:1;min-width:0}
.alert-title{font-size:12.5px;font-weight:700;color:var(--t1)}
.alert-desc{font-size:11px;color:var(--t3);margin-top:2px;line-height:1.6}
.alert-time{font-size:9.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:5px}
.alert-actions{display:flex;gap:6px;flex-shrink:0;align-items:center}
.alert-actions .btn{font-size:10px;padding:3px 8px;border-radius:6px}
.alert-actions .btn-dismiss{background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;font-family:inherit;transition:.15s}
.alert-actions .btn-dismiss:hover{background:var(--accent-d);color:var(--t1);border-color:var(--accent)}
.alerts-empty{text-align:center;padding:50px 20px;color:var(--t3)}
.alerts-empty i{font-size:40px;opacity:.3;display:block;margin-bottom:12px}
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
          <div class="lmodal-title-v2" data-lang="manage_configs">Manage Configs for <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2" data-lang="select_configs">Select configs to include in this group</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="Search configs..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> <span data-lang="select_all">Select All</span></button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> <span data-lang="deselect_all">Deselect All</span></button>
        <span class="lmodal-count" id="lmodal-count">0 selected</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">Loading...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> <span data-lang="changes_apply">Changes apply immediately</span></div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')"><span data-lang="close">Close</span></button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> <span data-lang="save">Save</span></button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title" data-lang="new_group_title">Create New Group</div>
      <div class="modal-v2-sub" data-lang="new_group_sub">Create a separate public page to manage configs</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> <span data-lang="group_name">Group Name</span></label>
        <input class="modal-v2-input" id="ns-name" placeholder="e.g. Telegram Channel">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> <span data-lang="description_optional">Description (optional)</span></label>
        <input class="modal-v2-input" id="ns-desc" placeholder="Short description of this group">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> <span data-lang="public_page_password">Public Page Password (optional)</span></label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="Leave empty = no password">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span data-lang="public_page_info">This group's public page will be accessible via a unique link.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6"><span data-lang="cancel">Cancel</span></button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> <span data-lang="create_group">Create Group</span></button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> <span data-lang="edit_config">Edit Config</span></div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label data-lang="title">Title</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label data-lang="quota_0_unlimited">Quota (0 = unlimited)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label data-lang="expiry_days">Expiry (days from now, 0 = no change/unlimited)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:16px"><label data-lang="note">Note</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="cl"><i class="ti ti-info-circle"></i><span data-lang="expiry_note">To keep current expiry, leave expiry field as 0.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')"><span data-lang="cancel">Cancel</span></button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> <span data-lang="save_changes">Save Changes</span></button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <span class="mob-title">CBee</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <span class="logo-text">CBee</span>
    <div style="font-size:10px;color:var(--t3);margin-top:1px">Gateway · v1.0.0</div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec" data-lang="panel">Panel</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> <span data-lang="dashboard">Dashboard</span></div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> <span data-lang="configs">Configs</span> <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> <span data-lang="sub_groups_short">Sub Groups</span> <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> <span data-lang="subscription">Subscription</span></div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> <span data-lang="traffic">Traffic</span></div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> <span data-lang="connections">Connections</span> <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-it" data-pg="alerts"><i class="ti ti-bell"></i> <span data-lang="smart_alerts">Smart Alerts</span> <span class="nav-badge" id="alerts-badge">0</span></div>
    <div class="nav-sec" data-lang="system">System</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> <span data-lang="security">Security</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> <span data-lang="activity_logs">Activity Logs</span></div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> <span data-lang="errors">Errors</span></div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> <span data-lang="test_websocket">WebSocket Test</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> <span data-lang="settings">Settings</span></div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label" data-lang="dark_theme">Dark Theme</span></button>
    <a class="tg-btn" href="https://t.me/CBeeNet" target="_blank" rel="noopener"><i class="ti ti-brand-telegram"></i> <span data-lang="telegram_btn">@CBeeNet</span></a>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> <span data-lang="logout_btn">Logout</span></button>
  </div>
</aside>
<main class="main">
<!-- صفحه داشبورد (Overview) -->
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> <span data-lang="dashboard">Dashboard</span></div><div class="tb-sub" id="last-upd">Loading...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> <span data-lang="active">Active</span></span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> <span data-lang="refresh">Refresh</span></button>
    </div>
  </div>
  <div class="dash-stats-grid" id="dash-stats">
    <div class="dash-stat-card">
      <i class="ti ti-plug-connected icon"></i>
      <div class="label" data-lang="active_connections">Active Connections</div>
      <div class="value" id="dash-conns">0</div>
      <div class="sub" data-lang="live">Live</div>
    </div>
    <div class="dash-stat-card">
      <i class="ti ti-database icon"></i>
      <div class="label" data-lang="total_traffic">Total Traffic</div>
      <div class="value" id="dash-traffic">0 <small style="font-size:14px;font-weight:400;">MB</small></div>
      <div class="sub" data-lang="since_start">Since Start</div>
    </div>
    <div class="dash-stat-card">
      <i class="ti ti-users icon"></i>
      <div class="label" data-lang="total_links">Configs</div>
      <div class="value" id="dash-links">0</div>
      <div class="sub" id="dash-links-sub">Active / Total</div>
    </div>
    <div class="dash-stat-card">
      <i class="ti ti-clock icon"></i>
      <div class="label" data-lang="uptime">Uptime</div>
      <div class="value" id="dash-uptime">00:00:00</div>
      <div class="sub" data-lang="running_time">Running Time</div>
    </div>
  </div>
  <!-- سه نمودار حرفه‌ای با کنترل بازه زمانی -->
  <div class="dash-sparkline-row">
    <div class="dash-spark-card">
      <div class="spark-top">
        <span class="spark-label"><i class="ti ti-gauge"></i> <span data-lang="load">Load</span></span>
        <span class="spark-value" id="spark-load">0<span class="unit">%</span></span>
      </div>
      <div class="spark-chart"><canvas id="sparkLoad"></canvas></div>
      <div class="chart-controls">
        <div class="btn-group">
          <button onclick="shiftTime('load', -1)" title="1 min back"><i class="ti ti-chevron-left"></i></button>
          <button onclick="shiftTime('load', 1)" title="1 min forward"><i class="ti ti-chevron-right"></i></button>
        </div>
        <span class="time-range" id="load-range">--:-- – --:--</span>
        <button class="btn-sm btn-g" onclick="resetTime('load')" style="font-size:9px;padding:2px 8px">Reset</button>
      </div>
    </div>
    <div class="dash-spark-card">
      <div class="spark-top">
        <span class="spark-label"><i class="ti ti-database"></i> <span data-lang="total_traffic">Total Traffic</span></span>
        <span class="spark-value" id="spark-traffic">0<span class="unit">MB</span></span>
      </div>
      <div class="spark-chart"><canvas id="sparkTraffic"></canvas></div>
      <div class="chart-controls">
        <div class="btn-group">
          <button onclick="shiftTime('traffic', -1)"><i class="ti ti-chevron-left"></i></button>
          <button onclick="shiftTime('traffic', 1)"><i class="ti ti-chevron-right"></i></button>
        </div>
        <span class="time-range" id="traffic-range">--:-- – --:--</span>
        <button class="btn-sm btn-g" onclick="resetTime('traffic')" style="font-size:9px;padding:2px 8px">Reset</button>
      </div>
    </div>
    <div class="dash-spark-card">
      <div class="spark-top">
        <span class="spark-label"><i class="ti ti-plug-connected"></i> <span data-lang="connections_live">Live Connections</span></span>
        <span class="spark-value" id="spark-conns">0</span>
      </div>
      <div class="spark-chart"><canvas id="sparkConns"></canvas></div>
      <div class="chart-controls">
        <div class="btn-group">
          <button onclick="shiftTime('conns', -1)"><i class="ti ti-chevron-left"></i></button>
          <button onclick="shiftTime('conns', 1)"><i class="ti ti-chevron-right"></i></button>
        </div>
        <span class="time-range" id="conns-range">--:-- – --:--</span>
        <button class="btn-sm btn-g" onclick="resetTime('conns')" style="font-size:9px;padding:2px 8px">Reset</button>
      </div>
    </div>
  </div>
  <!-- دو نمودار کوچک اضافی (پروتکل‌ها و میانگین ساعتی) -->
  <div class="dash-charts-second">
    <div class="dash-small-chart">
      <div class="chart-title"><i class="ti ti-chart-bar"></i> <span data-lang="protocol_distribution">Protocol Distribution</span></div>
      <div class="chart-wrap"><canvas id="dashProtoChart"></canvas></div>
    </div>
    <div class="dash-small-chart">
      <div class="chart-title"><i class="ti ti-arrow-up-right"></i> <span data-lang="hourly_average">Hourly Avg</span></div>
      <div class="chart-wrap"><canvas id="dashHourlyChart"></canvas></div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">CBee Gateway v1.0.0 · 2026 · Railway</span>
    <a class="df-link" href="https://t.me/CBeeNet" target="_blank"><i class="ti ti-brand-telegram"></i> t.me/CBeeNet</a>
  </div>
</section>

<!-- صفحه Configs -->
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> <span data-lang="configs">Configs</span></div><div class="tb-sub" data-lang="configs_management">Create and manage configs with quota, expiry and grouping</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">0 <span data-lang="configs">Configs</span></span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title" data-lang="create_config">Create New Config</div>
        <div class="cp-head-sub" data-lang="random_uuid">Random UUID · Choose quota, expiry and protocol</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> <span data-lang="config_id">Config ID</span></div>
          <input class="cp-input-full" id="nl-label" placeholder="e.g. User Ali">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="Note (optional)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> <span data-lang="sub_group_expiry">Sub Group & Expiry</span></div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— <span data-lang="no_group">No Group</span> —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="Expiry (days) · 0 = unlimited">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)" data-lang="unlimited">Unlimited</span>
            <span class="chip" onclick="setExpiry(7,this)">7 <span data-lang="days">Days</span></span>
            <span class="chip active" onclick="setExpiry(30,this)">30 <span data-lang="days">Days</span></span>
            <span class="chip" onclick="setExpiry(90,this)">90 <span data-lang="days">Days</span></span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> <span data-lang="traffic_quota">Traffic Quota</span></div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = unlimited">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)" data-lang="unlimited">Unlimited</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">500 MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">1 GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">5 GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">10 GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">50 GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> <span data-lang="transport_protocols">Transport Protocols</span></div>
        <div class="proto-group" id="proto-group">
          <button class="proto-btn active" data-proto="vless-ws" onclick="toggleProtoBtn(this)">VLESS / WS <span class="proto-badge">WebSocket</span></button>
          <button class="proto-btn" data-proto="xhttp-packet-up" onclick="toggleProtoBtn(this)">XHTTP · packet-up <span class="proto-badge">Siz10</span></button>
          <button class="proto-btn" data-proto="xhttp-stream-up" onclick="toggleProtoBtn(this)">XHTTP · stream-up <span class="proto-badge">Siz10</span></button>
        </div>
        <div style="margin-top:12px;display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--accent-d);border-radius:10px;border:1px solid var(--card-b)">
          <span style="font-size:12px;font-weight:700;color:var(--t2)"><i class="ti ti-layers-intersect"></i> <span data-lang="bulk_count">Bulk Count</span></span>
          <div class="count-chips">
            <span class="count-chip active" onclick="setCount(1,this)">1</span>
            <span class="count-chip" onclick="setCount(5,this)">5</span>
            <span class="count-chip" onclick="setCount(10,this)">10</span>
            <span class="count-chip" onclick="setCount(50,this)">50</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> <span data-lang="uuid_note">UUID is generated randomly · Only registered UUIDs can connect · Protocol cannot be changed after creation.</span></div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> <span data-lang="create_config">Create Config</span></button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p data-lang="no_configs">No configs yet</p></div>
</section>

<!-- صفحه Sub Groups -->
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> <span data-lang="sub_groups_short">Sub Groups</span></div><div class="tb-sub" data-lang="each_group_public">Each group has its own public page with its configs</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">0 <span data-lang="groups">Groups</span></span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> <span data-lang="new_group">New Group</span></button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="Search groups..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title" data-lang="no_groups">No groups yet</div><div class="subs-empty-v2-sub" data-lang="create_group">Create a new group to organize your configs</div></div>
  </div>
</section>

<!-- صفحه Subscription -->
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> <span data-lang="subscription">Subscription</span></div><div class="tb-sub" data-lang="subscription_links">Subscription links for v2ray apps</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> <span data-lang="single_sub">Single Subscription (per config)</span></div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px"><span data-lang="single_sub_desc">Each config has its own subscription URL. Click the</span> <i class="ti ti-rss"></i> <span data-lang="icon_on_card">icon on the config card.</span></p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> <span data-lang="full_sub">Full Subscription (Admin)</span></div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px" data-lang="full_sub_desc">Includes all active configs.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">Loading...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span data-lang="full_sub_note">This URL only works in the browser where you're logged in (requires session cookie).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> <span data-lang="group_sub_links">Group Subscription Links</span></div>
    <div id="sub-groups-list" data-lang="loading">Loading...</div>
  </div>
</section>

<!-- صفحه Traffic (بخش ترافیک با نمودار بزرگ) -->
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> <span data-lang="traffic">Traffic</span></div><div class="tb-sub" data-lang="traffic_analysis">Bandwidth usage analysis & monitoring</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> <span data-lang="refresh">Refresh</span></button></div>
  </div>
  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> <span data-lang="total_traffic_used">Total Traffic Used</span></div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label" data-lang="hourly_average">Hourly Average</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB <span data-lang="per_hour">/h</span></div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label" data-lang="peak_usage">Peak Usage</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time" data-lang="peak_hour">Peak Hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label" data-lang="lowest_usage">Lowest Usage</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB <span data-lang="per_hour">/h</span></div></div>
    </div>
  </div>
  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> <span data-lang="traffic_trend">Traffic Usage Trend</span></div>
        <div class="traf-chart-sub" data-lang="based_on_mb">Based on MB per hour</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> <span data-lang="usage">Usage</span></div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> <span data-lang="average">Average</span></div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>

<!-- صفحه Connections -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> <span data-lang="connections">Connections</span></div><div class="tb-sub" data-lang="connections_monitor">Live IP and traffic monitoring per connection</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> <span data-lang="refresh">Refresh</span></button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div><div class="conn-hero-label" data-lang="live_connections">Live Connections</div><div class="conn-hero-val" id="ch-count">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-transfer"></i></div><div class="conn-hero-label" data-lang="total_traffic_live">Total Traffic</div><div class="conn-hero-val" id="ch-traffic">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-clock"></i></div><div class="conn-hero-label" data-lang="avg_duration">Avg Duration</div><div class="conn-hero-val" id="ch-avgdur">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div><div class="conn-hero-label" data-lang="unique_ips">Unique IPs</div><div class="conn-hero-val" id="ch-uniq">—</div></div>
  </div>
  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> <span data-lang="connections_list">Connections List</span></div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> <span data-lang="auto_update">Auto-update every 5s</span></div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title" data-lang="no_active_connections">No active connections</div>
    <div class="conn-empty-v2-sub" data-lang="will_appear">They will appear here as soon as clients connect</div>
  </div>
</section>

<!-- صفحه Alerts -->
<section class="pg" id="pg-alerts">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-bell"></i> <span data-lang="smart_alerts">Smart Alerts</span></div><div class="tb-sub" data-lang="alerts_sub">Important events & notifications</div></div>
    <div class="tb-right"><span class="badge bg-red" id="alerts-count-badge">0</span><button class="btn btn-p btn-sm" onclick="loadAlerts()"><i class="ti ti-refresh"></i> <span data-lang="refresh">Refresh</span></button></div>
  </div>
  <div class="alerts-wrap">
    <div class="alerts-filters">
      <button class="btn active" data-filter="all" onclick="filterAlerts('all',this)"><span data-lang="filter_all">All</span></button>
      <button class="btn" data-filter="critical" onclick="filterAlerts('critical',this)"><span data-lang="filter_critical">Critical</span></button>
      <button class="btn" data-filter="warning" onclick="filterAlerts('warning',this)"><span data-lang="filter_warning">Warning</span></button>
      <button class="btn" data-filter="info" onclick="filterAlerts('info',this)"><span data-lang="filter_info">Info</span></button>
    </div>
    <div id="alerts-list"></div>
  </div>
</section>

<!-- صفحه Security -->
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> <span data-lang="security">Security</span></div></div></div>
  <div class="g2">
    <div class="card"><div class="card-title"><i class="ti ti-lock"></i> <span data-lang="encryption">Encryption</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="active">Active</span> (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> <span data-lang="protocols">Protocols</span></span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> <span data-lang="hash">Hash</span></span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> <span data-lang="session">Session</span></span><span class="sr-v">HttpOnly · 7 <span data-lang="days">Days</span></span></div>
    </div>
    <div class="card"><div class="card-title"><i class="ti ti-shield-check"></i> <span data-lang="access_control">Access Control</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="active">Active</span></span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> <span data-lang="active_inactive">Active/Inactive</span></span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="active">Active</span></span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> <span data-lang="traffic_quota">Traffic Quota</span></span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="active">Active</span></span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> <span data-lang="expiry_date">Expiry Date</span></span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="active">Active</span></span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> <span data-lang="public_page_pw">Public Page Password</span></span><span class="sr-v" style="color:var(--green-t)">● <span data-lang="optional">Optional</span></span></div>
    </div>
  </div>
</section>

<!-- صفحه Activity Logs -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> <span data-lang="activity_logs">Activity Logs</span></div><div class="tb-sub" data-lang="activity_logs_full">Complete event history</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p data-lang="no_logs">No logs yet</p></div></div>
</section>

<!-- صفحه Errors -->
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> <span data-lang="errors">Errors</span></div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">0</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> <span data-lang="error_logs">Error Logs</span></div><div id="errs-full">—</div></div>
</section>

<!-- صفحه WebSocket Test -->
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> <span data-lang="websocket_test">WebSocket Test</span></div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span data-lang="ws_note">Only registered and active UUIDs can connect.</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID</label><input class="fi" id="ws-uuid" placeholder="Active config UUID" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> <span data-lang="connect">Connect</span></button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> <span data-lang="disconnect">Disconnect</span></button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="Test message..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> <span data-lang="send">Send</span></button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)" data-lang="waiting_ws">Waiting for connection...</p>
    </div>
  </div>
</section>

<!-- صفحه Settings -->
<section class="pg" id="pg-settings">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-settings"></i> <span data-lang="settings">Settings</span></div><div class="tb-sub" data-lang="system_settings">System configuration</div></div>
    <div class="tb-right"><span class="badge bg-blue">v1.0.0</span></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-palette"></i> <span data-lang="theme_settings">Theme Settings</span></div>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div>
          <label style="font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px" data-lang="dark_theme">Dark Theme</label>
          <div style="display:flex;gap:10px;flex-wrap:wrap" id="dark-themes">
            <button class="btn btn-p theme-btn-select" data-theme="dark-blue" style="background:#1677ff;color:#fff;box-shadow:0 2px 8px rgba(22,119,255,0.4)" onclick="setTheme('dark-blue')"><i class="ti ti-circle"></i> <span data-lang="blue">Blue</span></button>
            <button class="btn btn-p theme-btn-select" data-theme="dark-red" style="background:#ef4444;color:#fff;box-shadow:0 2px 8px rgba(239,68,68,0.4)" onclick="setTheme('dark-red')"><i class="ti ti-circle"></i> <span data-lang="red">Red</span></button>
            <button class="btn btn-p theme-btn-select" data-theme="dark-yellow" style="background:#f59e0b;color:#000;box-shadow:0 2px 8px rgba(245,158,11,0.4)" onclick="setTheme('dark-yellow')"><i class="ti ti-circle"></i> <span data-lang="yellow">Yellow</span></button>
            <button class="btn btn-p theme-btn-select" data-theme="dark-prestige" style="background:linear-gradient(135deg,#1a7aff,#4d94ff);color:#fff;box-shadow:0 2px 8px rgba(26,122,255,0.4)" onclick="setTheme('dark-prestige')"><i class="ti ti-circle"></i> <span data-lang="prestige_theme">Prestige</span></button>
          </div>
        </div>
        <div>
          <label style="font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px" data-lang="light_theme">Light Theme</label>
          <div style="display:flex;gap:10px;flex-wrap:wrap" id="light-themes">
            <button class="btn btn-p theme-btn-select" data-theme="light-blue" style="background:#1677ff;color:#fff;box-shadow:0 2px 8px rgba(22,119,255,0.3)" onclick="setTheme('light-blue')"><i class="ti ti-circle"></i> <span data-lang="blue">Blue</span></button>
            <button class="btn btn-p theme-btn-select" data-theme="light-red" style="background:#ef4444;color:#fff;box-shadow:0 2px 8px rgba(239,68,68,0.3)" onclick="setTheme('light-red')"><i class="ti ti-circle"></i> <span data-lang="red">Red</span></button>
            <button class="btn btn-p theme-btn-select" data-theme="light-yellow" style="background:#f59e0b;color:#000;box-shadow:0 2px 8px rgba(245,158,11,0.3)" onclick="setTheme('light-yellow')"><i class="ti ti-circle"></i> <span data-lang="yellow">Yellow</span></button>
          </div>
        </div>
        <div class="cl"><i class="ti ti-info-circle"></i><span data-lang="current_theme">Current Theme</span>: <strong id="current-theme-display">dark-prestige</strong></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-language"></i> <span data-lang="language_settings">Language Settings</span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap" id="lang-buttons">
        <button class="btn-lang" data-lang-code="en" onclick="setLanguage('en')">English</button>
        <button class="btn-lang" data-lang-code="fa" onclick="setLanguage('fa')">فارسی</button>
      </div>
      <div class="cl" style="margin-top:12px"><i class="ti ti-info-circle"></i><span data-lang="lang_note">Default language is English. Page will refresh after change.</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-server-2"></i> <span data-lang="server_link_settings">Server & Link Settings</span></div>
      <div style="display:flex;flex-direction:column;gap:12px">
        <div class="fg">
          <label data-lang="server_name">Server Name</label>
          <input class="fi" id="server-name-input" placeholder="e.g. CBeeNet" style="width:100%">
        </div>
        <div class="fg">
          <label data-lang="server_prefix">Link Prefix</label>
          <input class="fi" id="server-prefix-input" placeholder="e.g. MyServer" style="width:100%">
        </div>
        <div class="fg">
          <label data-lang="link_template">Link Name Template</label>
          <input class="fi" id="link-name-template" placeholder="e.g. {server}-{label}" style="width:100%">
          <div style="font-size:9.5px;color:var(--t3);margin-top:4px;display:flex;flex-wrap:wrap;gap:6px">
            <span style="background:var(--accent-d);padding:2px 8px;border-radius:4px">{server}</span>
            <span style="background:var(--accent-d);padding:2px 8px;border-radius:4px">{prefix}</span>
            <span style="background:var(--accent-d);padding:2px 8px;border-radius:4px">{label}</span>
            <span style="background:var(--accent-d);padding:2px 8px;border-radius:4px">{protocol}</span>
          </div>
        </div>
        <div class="cl"><i class="ti ti-info-circle"></i><span data-lang="template_note">If `{protocol}` is not in the template, the protocol will not be shown.</span></div>
        <button class="btn btn-p" onclick="saveServerSettings()"><i class="ti ti-device-floppy"></i> <span data-lang="save_settings">Save Settings</span></button>
        <div id="server-save-result" style="font-size:11px;color:var(--green-t);display:none">✓ <span data-lang="saved">Saved</span></div>
      </div>
    </div>
  </div>
  <div class="g2" style="margin-top:16px">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> <span data-lang="online_status">Online</span> · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label" data-lang="port">Port</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label" data-lang="version">Version</div><div class="srv-tile-val">v1.0.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label" data-lang="framework">Framework</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label" data-lang="platform">Platform</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label" data-lang="storage">Storage</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title" data-lang="change_password_title">Change Password</div>
          <div class="pw-hero-sub" data-lang="change_password_sub">Choose a strong password and keep it safe</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field"><label data-lang="current_pw">Current Password</label><input class="pw-input" type="password" id="cp-cur" placeholder="Current password"><button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button></div>
        <div class="pw-field" style="margin-bottom:6px"><label data-lang="new_pw">New Password</label><input class="pw-input" type="password" id="cp-new" placeholder="Min 4 characters" oninput="checkPwStrength(this.value)"><button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button></div>
        <div class="pw-strength" id="pw-strength-bar"><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div></div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> <span data-lang="password_strength">Password Strength</span></div>
        <div class="pw-reqs"><span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> <span data-lang="min_4_chars">At least 4 chars</span></span><span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> <span data-lang="contains_num">Contains number</span></span><span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> <span data-lang="contains_case_letters">Uppercase/Lowercase</span></span></div>
        <div class="pw-field" style="margin-bottom:18px"><label data-lang="confirm_pw">Confirm Password</label><input class="pw-input" type="password" id="cp-cf" placeholder="Confirm new password"><button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button></div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> <span data-lang="save_new_pw">Save New Password</span></button>
      </div>
    </div>
  </div>
</section>
</main>
<script>
const LANG_DICT = {
  "en": {
    "dashboard":"Dashboard","dashboard_sub":"System Overview","active_connections":"Active Connections","total_traffic":"Total Traffic","total_links":"Configs","uptime":"Uptime","since_start":"Since Start","active":"Active","inactive":"Inactive","refresh":"Refresh","traffic_trend":"Bandwidth Usage","service_status":"Service Status","top_connections":"Live Connections","no_connections":"No connections","server":"Server","settings":"Settings","language":"Language","farsi":"Persian","english":"English","save":"Save","cancel":"Cancel","delete":"Delete","edit":"Edit","copy":"Copy","created":"Created","expires":"Expires","unlimited":"Unlimited","used":"Used","of":"of","daily":"Daily","hourly":"Hourly","bandwidth":"Bandwidth","connections":"Connections","protocol":"Protocol","ip_address":"IP Address","port":"Port","upload":"Upload","download":"Download","duration":"Duration","status":"Status","online":"Online","offline":"Offline","total":"Total","users":"Users","protocols":"Protocols","traffic_usage":"Traffic Usage","links":"Configs","sub_groups":"Sub Groups","subscription":"Subscription","security":"Security","logs":"Activity Logs","errors":"Errors","test_websocket":"WebSocket Test","dark_theme":"Dark Theme","light_theme":"Light Theme","prestige_theme":"Prestige Theme","blue":"Blue","red":"Red","yellow":"Yellow","current_theme":"Current Theme","server_settings":"Server & Link Settings","server_name":"Server Name","server_prefix":"Link Prefix","link_template":"Link Name Template","template_vars":"Available Variables","template_note":"If `{protocol}` is not in the template, the protocol will not be shown.","change_password":"Change Password","current_password":"Current Password","new_password":"New Password","confirm_password":"Confirm Password","password_strength":"Password Strength","min_chars":"At least 4 characters","contains_number":"Contains number","contains_case":"Uppercase/Lowercase","weak":"Very Weak","medium":"Medium","strong":"Strong","save_password":"Save New Password","login":"Login","logout":"Logout","login_title":"Login to Panel","login_sub":"Enter password to access the dashboard","password":"Password","login_button":"Login to Dashboard","telegram_channel":"Telegram Channel","panel":"Panel","system":"System","configs":"Configs","sub_groups_short":"Sub Groups","activity_logs":"Activity Logs","config_id":"Config ID","sub_group_expiry":"Sub Group & Expiry","no_group":"No Group","days":"Days","traffic_quota":"Traffic Quota","transport_protocols":"Transport Protocols","bulk_count":"Bulk Count","create_config":"Create Config","no_configs":"No configs yet","new_group":"New Group","no_groups":"No groups yet","create_group":"Create a new group to organize your configs","single_sub":"Single Subscription (per config)","full_sub":"Full Subscription (Admin)","full_sub_desc":"Includes all active configs.","group_sub_links":"Group Subscription Links","loading":"Loading...","traffic_analysis":"Bandwidth usage analysis & monitoring","total_traffic_used":"Total Traffic Used","hourly_average":"Hourly Average","per_hour":"/h","peak_usage":"Peak Usage","peak_hour":"Peak Hour","lowest_usage":"Lowest Usage","live_connections":"Live Connections","total_traffic_live":"Total Traffic","avg_duration":"Avg Duration","unique_ips":"Unique IPs","connections_list":"Connections List","auto_update":"Auto-update every 5s","no_active_connections":"No active connections","will_appear":"They will appear here as soon as clients connect","encryption":"Encryption","access_control":"Access Control","hash":"Hash","session":"Session","active_inactive":"Active/Inactive","expiry_date":"Expiry Date","public_page_pw":"Public Page Password","optional":"Optional","activity_logs_full":"Complete event history","no_logs":"No logs yet","error_logs":"Error Logs","websocket_test":"WebSocket Test","ws_note":"Only registered and active UUIDs can connect.","connect":"Connect","disconnect":"Disconnect","send":"Send","waiting_ws":"Waiting for connection...","change_theme":"Change Theme","server_link_settings":"Server & Link Settings","save_settings":"Save Settings","saved":"Saved","online_status":"Online","version":"Version","framework":"Framework","platform":"Platform","storage":"Storage","change_password_title":"Change Password","change_password_sub":"Choose a strong password and keep it safe","current_pw":"Current Password","new_pw":"New Password","confirm_pw":"Confirm Password","save_new_pw":"Save New Password","min_4_chars":"At least 4 chars","contains_num":"Contains number","contains_case_letters":"Uppercase/Lowercase","very_weak":"Very Weak","medium_strength":"Medium","strong_strength":"Strong","logout_btn":"Logout","telegram_btn":"Telegram Channel","load":"Load","connections_live":"Live Connections","traffic_chart":"Traffic Chart","protocol_distribution":"Protocol Distribution","daily_usage":"Daily Usage","active_conns_table":"Active Connections","configs_management":"Configs Management","sub_groups_management":"Sub Groups Management","subscription_links":"Subscription Links","traffic_monitor":"Traffic Monitor","connections_monitor":"Connections Monitor","security_settings":"Security Settings","activity_logs_title":"Activity Logs","error_logs_title":"Error Logs","websocket_tester":"WebSocket Tester","system_settings":"System Settings","language_settings":"Language Settings","theme_settings":"Theme Settings","server_info":"Server Info","password_change":"Password Change","save_changes":"Save Changes","cancel_changes":"Cancel","live":"Live","running_time":"Running Time","manage_configs":"Manage Configs for","select_configs":"Select configs to include in this group","select_all":"Select All","deselect_all":"Deselect All","changes_apply":"Changes apply immediately","new_group_title":"Create New Group","new_group_sub":"Create a separate public page to manage configs","group_name":"Group Name","description_optional":"Description (optional)","public_page_password":"Public Page Password (optional)","public_page_info":"This group's public page will be accessible via a unique link.","edit_config":"Edit Config","quota_0_unlimited":"Quota (0 = unlimited)","expiry_days":"Expiry (days from now, 0 = no change/unlimited)","expiry_note":"To keep current expiry, leave expiry field as 0.","random_uuid":"Random UUID · Choose quota, expiry and protocol","uuid_note":"UUID is generated randomly · Only registered UUIDs can connect · Protocol cannot be changed after creation.","each_group_public":"Each group has its own public page with its configs","single_sub_desc":"Each config has its own subscription URL. Click the","icon_on_card":"icon on the config card.","full_sub_note":"This URL only works in the browser where you're logged in (requires session cookie).","based_on_mb":"Based on MB per hour","lang_note":"Default language is English. Page will refresh after change.","groups":"Groups","usage":"Usage","average":"Average","protocols_legend":"Protocols","daily_legend":"Daily","hourly_legend":"Hourly","bandwidth_usage":"Bandwidth Usage","smart_alerts":"Smart Alerts","alerts_sub":"Important events & notifications","priority":"Priority","critical":"Critical","warning":"Warning","info":"Info","dismiss":"Dismiss","filter_all":"All","filter_critical":"Critical","filter_warning":"Warning","filter_info":"Info","alert_expiry":"Config expiring soon","alert_quota":"Traffic quota exceeded 80%","alert_errors":"Repeated connection errors","alert_new_ip":"New IP connected","no_alerts":"No alerts to show"
  },
  "fa": {
    "dashboard":"داشبورد","dashboard_sub":"نمای کلی سیستم","active_connections":"اتصالات فعال","total_traffic":"کل ترافیک","total_links":"کانفیگ‌ها","uptime":"آپتایم","since_start":"از راه‌اندازی","active":"فعال","inactive":"غیرفعال","refresh":"رفرش","traffic_trend":"مصرف پهنای باند","service_status":"وضعیت سرویس","top_connections":"اتصال‌های لحظه‌ای","no_connections":"هیچ اتصالی","server":"سرور","settings":"تنظیمات","language":"زبان","farsi":"فارسی","english":"انگلیسی","save":"ذخیره","cancel":"انصراف","delete":"حذف","edit":"ویرایش","copy":"کپی","created":"ساخته شده","expires":"انقضا","unlimited":"نامحدود","used":"مصرف","of":"از","daily":"روزانه","hourly":"ساعتی","bandwidth":"پهنای باند","connections":"اتصالات","protocol":"پروتکل","ip_address":"آدرس آی‌پی","port":"پورت","upload":"آپلود","download":"دانلود","duration":"مدت","status":"وضعیت","online":"آنلاین","offline":"آفلاین","total":"کل","users":"کاربران","protocols":"پروتکل‌ها","traffic_usage":"مصرف ترافیک","links":"کانفیگ‌ها","sub_groups":"گروه‌های ساب","subscription":"سابسکریپشن","security":"امنیت","logs":"لاگ فعالیت‌ها","errors":"خطاها","test_websocket":"تست WebSocket","dark_theme":"تم تاریک","light_theme":"تم روشن","prestige_theme":"تم پرستیژ","blue":"آبی","red":"قرمز","yellow":"زرد","current_theme":"تم پیش‌فرض","server_settings":"تنظیمات سرور و نام لینک‌ها","server_name":"نام سرور","server_prefix":"پیشوند لینک‌ها","link_template":"قالب نام کانفیگ‌ها","template_vars":"متغیرهای قابل استفاده","template_note":"اگر `{protocol}` در قالب نباشد، پروتکل در نام نمایش داده نمی‌شود.","change_password":"تغییر رمز عبور","current_password":"رمز فعلی","new_password":"رمز جدید","confirm_password":"تکرار رمز جدید","password_strength":"قدرت رمز","min_chars":"حداقل ۴ کاراکتر","contains_number":"شامل عدد","contains_case":"حروف بزرگ/کوچک","weak":"خیلی ضعیف","medium":"متوسط","strong":"قوی","save_password":"ذخیره رمز جدید","login":"ورود","logout":"خروج","login_title":"ورود به پنل","login_sub":"رمز عبور را برای دسترسی به داشبورد وارد کنید","password":"رمز عبور","login_button":"ورود به داشبورد","telegram_channel":"کانال تلگرام","panel":"پنل","system":"سیستم","configs":"کانفیگ‌ها","sub_groups_short":"گروه‌های ساب","activity_logs":"لاگ فعالیت‌ها","config_id":"شناسه کانفیگ","sub_group_expiry":"گروه ساب و انقضا","no_group":"بدون گروه","days":"روز","traffic_quota":"سهمیه ترافیک","transport_protocols":"پروتکل‌های انتقال","bulk_count":"تعداد ساخت هم‌زمان","create_config":"ساخت کانفیگ","no_configs":"هنوز کانفیگی وجود ندارد","new_group":"گروه جدید","no_groups":"هنوز گروهی وجود ندارد","create_group":"یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید","single_sub":"سابسکریپشن تکی (هر کانفیگ)","full_sub":"سابسکریپشن کامل (ادمین)","full_sub_desc":"شامل تمام کانفیگ‌های فعال.","group_sub_links":"لینک سابسکریپشن گروه‌ها","loading":"در حال بارگذاری...","traffic_analysis":"تحلیل و مانیتورینگ مصرف پهنای باند","total_traffic_used":"کل ترافیک مصرفی","hourly_average":"میانگین ساعتی","per_hour":"در ساعت","peak_usage":"پیک مصرف","peak_hour":"بالاترین ساعت","lowest_usage":"کمترین مصرف","live_connections":"اتصالات زنده","total_traffic_live":"مجموع ترافیک لحظه‌ای","avg_duration":"میانگین مدت اتصال","unique_ips":"آی‌پی‌های یکتا","connections_list":"لیست اتصالات","auto_update":"بروزرسانی خودکار هر ۵ ثانیه","no_active_connections":"هیچ اتصال فعالی نیست","will_appear":"به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند","encryption":"رمزنگاری","access_control":"کنترل دسترسی","hash":"هش رمز","session":"سشن","active_inactive":"فعال/غیرفعال","expiry_date":"تاریخ انقضا","public_page_pw":"رمز صفحه پابلیک","optional":"اختیاری","activity_logs_full":"تاریخچه‌ی کامل رخدادهای پنل","no_logs":"هنوز لاگی ثبت نشده","error_logs":"لاگ خطاها","websocket_test":"تست WebSocket","ws_note":"فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند.","connect":"اتصال","disconnect":"قطع","send":"ارسال","waiting_ws":"منتظر اتصال...","change_theme":"تغییر تم","server_link_settings":"تنظیمات سرور و نام لینک‌ها","save_settings":"ذخیره تنظیمات","saved":"ذخیره شد","online_status":"آنلاین","version":"نسخه","framework":"فریم‌ورک","platform":"پلتفرم","storage":"ذخیره‌سازی","change_password_title":"تغییر رمز عبور","change_password_sub":"رمز قوی انتخاب کنید و آن را جایی امن نگه دارید","current_pw":"رمز فعلی","new_pw":"رمز جدید","confirm_pw":"تکرار رمز جدید","save_new_pw":"ذخیره رمز جدید","min_4_chars":"حداقل ۴ کاراکتر","contains_num":"شامل عدد","contains_case_letters":"حروف بزرگ/کوچک","very_weak":"خیلی ضعیف","medium_strength":"متوسط","strong_strength":"قوی","logout_btn":"خروج","telegram_btn":"کانال تلگرام","load":"بار نسبی","connections_live":"اتصالات لحظه‌ای","traffic_chart":"نمودار ترافیک","protocol_distribution":"توزیع پروتکل","daily_usage":"مصرف روزانه","active_conns_table":"اتصالات فعال","configs_management":"مدیریت کانفیگ‌ها","sub_groups_management":"مدیریت گروه‌های ساب","subscription_links":"لینک‌های سابسکریپشن","traffic_monitor":"مانیتورینگ ترافیک","connections_monitor":"مانیتورینگ اتصالات","security_settings":"تنظیمات امنیتی","activity_logs_title":"لاگ فعالیت‌ها","error_logs_title":"لاگ خطاها","websocket_tester":"تست WebSocket","system_settings":"تنظیمات سیستم","language_settings":"تنظیمات زبان","theme_settings":"تنظیمات تم","server_info":"اطلاعات سرور","password_change":"تغییر رمز عبور","save_changes":"ذخیره تغییرات","cancel_changes":"انصراف","live":"لحظه‌ای","running_time":"مدت روشن بودن","manage_configs":"مدیریت کانفیگ‌های","select_configs":"کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید","select_all":"انتخاب همه","deselect_all":"لغو همه","changes_apply":"تغییرات بلافاصله اعمال می‌شود","new_group_title":"ساخت گروه جدید","new_group_sub":"یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید","group_name":"نام گروه","description_optional":"توضیحات (اختیاری)","public_page_password":"رمز صفحه پابلیک (اختیاری)","public_page_info":"صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.","edit_config":"ویرایش کانفیگ","quota_0_unlimited":"سهمیه (0 = نامحدود)","expiry_days":"انقضا (روز از الان، 0 = بدون تغییر/نامحدود)","expiry_note":"برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.","random_uuid":"UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن","uuid_note":"UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.","each_group_public":"هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد","single_sub_desc":"هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون","icon_on_card":"کلیک کنید.","full_sub_note":"این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).","based_on_mb":"بر اساس مگابایت در هر ساعت","lang_note":"زبان پیش‌فرض انگلیسی است. پس از تغییر، صفحه رفرش می‌شود.","groups":"گروه","usage":"مصرف","average":"میانگین","protocols_legend":"پروتکل‌ها","daily_legend":"روزانه","hourly_legend":"ساعتی","bandwidth_usage":"مصرف پهنای باند","smart_alerts":"هشدارهای هوشمند","alerts_sub":"رویدادها و اعلان‌های مهم","priority":"اولویت","critical":"بحرانی","warning":"هشدار","info":"اطلاعات","dismiss":"رد کردن","filter_all":"همه","filter_critical":"بحرانی","filter_warning":"هشدار","filter_info":"اطلاعات","alert_expiry":"انقضای نزدیک کانفیگ","alert_quota":"مصرف ترافیک بیش از ۸۰٪","alert_errors":"خطاهای مکرر اتصال","alert_new_ip":"آی‌پی جدید متصل شد","no_alerts":"هیچ هشداری وجود ندارد"
  }
};
let currentLang = localStorage.getItem('CBeeNet-lang') || 'en';
let currentTheme = localStorage.getItem('CBeeNet-theme') || 'dark-prestige';
let alertsData = [];
let currentAlertFilter = 'all';

// ========== Language & Theme ==========
function setLanguage(lang){
  currentLang = lang;
  localStorage.setItem('CBeeNet-lang', lang);
  applyLanguage();
  document.querySelectorAll('.btn-lang').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.langCode === lang);
  });
  toast('Language changed to ' + (lang === 'fa' ? 'فارسی' : 'English'), 'ok');
}
function applyLanguage(){
  const dict = LANG_DICT[currentLang] || LANG_DICT['en'];
  document.documentElement.dir = currentLang === 'fa' ? 'rtl' : 'ltr';
  document.documentElement.lang = currentLang;
  document.querySelectorAll('[data-lang]').forEach(el => {
    const key = el.getAttribute('data-lang');
    if(dict[key] !== undefined) el.textContent = dict[key];
  });
  document.querySelectorAll('[data-lang-placeholder]').forEach(el => {
    const key = el.getAttribute('data-lang-placeholder');
    if(dict[key] !== undefined) el.placeholder = dict[key];
  });
}
function applyTheme(theme){
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('CBeeNet-theme', theme);
  currentTheme = theme;
  document.getElementById('current-theme-display').textContent = theme;
  document.querySelectorAll('.theme-btn-select').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.theme === theme);
    btn.style.outline = btn.dataset.theme === theme ? '2px solid var(--accent)' : 'none';
    btn.style.outlineOffset = btn.dataset.theme === theme ? '2px' : '0';
  });
  const isLight = theme.startsWith('light');
  const icon = isLight ? 'ti-moon' : 'ti-sun';
  const labelKey = isLight ? 'light_theme' : 'dark_theme';
  const dict = LANG_DICT[currentLang] || LANG_DICT['en'];
  document.getElementById('theme-icon').className = 'ti ' + icon;
  document.getElementById('theme-label').textContent = dict[labelKey] || (isLight ? 'Light Theme' : 'Dark Theme');
  document.getElementById('theme-mob-icon').className = 'ti ' + icon;
}
function setTheme(theme){ applyTheme(theme); toast('Theme changed to ' + theme, 'ok'); }
function toggleTheme(){
  const isLight = currentTheme.startsWith('light');
  const color = currentTheme.split('-')[1] || 'prestige';
  const newTheme = isLight ? 'dark-' + color : 'light-' + color;
  const finalTheme = newTheme === 'dark-prestige' ? 'dark-prestige' : newTheme;
  applyTheme(finalTheme);
}
function toast(msg, type=''){
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2400);
}
function fmtB(b){ if(!b || b === 0) return '0 B'; if(b < 1024) return b + ' B'; if(b < 1024**2) return (b/1024).toFixed(1) + ' KB'; if(b < 1024**3) return (b/1024**2).toFixed(2) + ' MB'; return (b/1024**3).toFixed(2) + ' GB'; }
function toFa(n){ return String(n).replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[d]); }
function esc(s){ return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function daysLeft(exp){ if(!exp) return null; return Math.ceil((new Date(exp) - Date.now()) / 864e5); }
function expChip(exp, expired){
  if(expired) return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(!exp) return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> Unlimited</span>';
  const d = daysLeft(exp);
  if(d <= 0) return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(d <= 3) return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${d} days left</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${d} days left</span>`;
}
function protoBadge(protocols){
  if(!protocols || !protocols.length) protocols = ['vless-ws'];
  const labels = { 'vless-ws': ['VLESS · WS', 'pc-ws'], 'xhttp-packet-up': ['XHTTP · packet-up', 'pc-xhttp'], 'xhttp-stream-up': ['XHTTP · stream-up', 'pc-xhttp'], 'xhttp-stream-one': ['XHTTP ULTRA', 'pc-ultra'] };
  return protocols.map(p => { const v = labels[p] || labels['vless-ws']; return `<span class="proto-chip ${v[1]}">${v[0]}</span>`; }).join('');
}
async function checkAuth(){
  try{ const r = await fetch('/api/me'); const d = await r.json(); if(!d.authenticated) location.href = '/login'; }catch(e){ location.href = '/login'; }
}
async function logout(){ try{ await fetch('/api/logout', {method:'POST'}); }catch(e){} location.href = '/login'; }
document.getElementById('logout-btn').addEventListener('click', logout);
async function authF(url, opts={}){ const r = await fetch(url, opts); if(r.status === 401){ location.href = '/login'; throw new Error('unauthorized'); } return r; }
function toggleProtoBtn(el){ el.classList.toggle('active'); }
function getSelectedProtocols(){
  const btns = document.querySelectorAll('.proto-btn');
  const selected = [];
  btns.forEach(btn => { if(btn.classList.contains('active')) selected.push(btn.dataset.proto); });
  return selected.length ? selected : ['vless-ws'];
}
function setQuota(val, unit, el){
  document.getElementById('nl-val').value = val === 0 ? '' : val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days, el){
  document.getElementById('nl-exp').value = days === 0 ? '' : days;
  document.querySelectorAll('#exp-chips .chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
function setCount(val, el){
  document.getElementById('nl-count').value = val;
  document.querySelectorAll('.count-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
async function loadServerSettings(){
  try {
    const r = await authF('/api/settings/server');
    const data = await r.json();
    document.getElementById('server-name-input').value = data.server_name || 'CBeeNet';
    document.getElementById('server-prefix-input').value = data.server_prefix || '';
    document.getElementById('link-name-template').value = data.link_template || '{server}-{label}';
    localStorage.setItem('CBeeNet-server-name', data.server_name || 'CBeeNet');
    localStorage.setItem('CBeeNet-server-prefix', data.server_prefix || '');
    localStorage.setItem('CBeeNet-link-template', data.link_template || '{server}-{label}');
  } catch(e) { console.warn('Could not load server settings:', e); }
}
async function saveServerSettings(){
  const name = document.getElementById('server-name-input').value.trim() || 'CBeeNet';
  const prefix = document.getElementById('server-prefix-input').value.trim() || '';
  const template = document.getElementById('link-name-template').value.trim() || '{server}-{label}';
  try {
    const r = await authF('/api/settings/server', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ server_name: name, server_prefix: prefix, link_template: template })
    });
    const result = await r.json();
    if(result.ok){
      localStorage.setItem('CBeeNet-server-name', name);
      localStorage.setItem('CBeeNet-server-prefix', prefix);
      localStorage.setItem('CBeeNet-link-template', template);
      document.getElementById('server-save-result').style.display = 'block';
      setTimeout(() => document.getElementById('server-save-result').style.display = 'none', 3000);
      toast('Settings saved ✓', 'ok');
      loadLinks();
    } else {
      toast('Error saving settings', 'err');
    }
  } catch(e) { toast('Server connection error', 'err'); }
}
function formatLinkName(label, protocol){
  const template = localStorage.getItem('CBeeNet-link-template') || '{server}-{label}';
  const server = localStorage.getItem('CBeeNet-server-name') || 'CBeeNet';
  const prefix = localStorage.getItem('CBeeNet-server-prefix') || '';
  let result = template;
  result = result.replace(/{server}/g, server);
  result = result.replace(/{prefix}/g, prefix);
  result = result.replace(/{label}/g, label);
  if(template.includes('{protocol}')){
    const protoMap = { 'vless-ws': 'VLESS-WS', 'xhttp-packet-up': 'XHTTP-packet', 'xhttp-stream-up': 'XHTTP-stream', 'xhttp-stream-one': 'XHTTP-ultra' };
    result = result.replace(/{protocol}/g, protoMap[protocol] || protocol);
  }
  return result;
}
const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb(){ sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb(){ sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
document.getElementById('close-sb').addEventListener('click', closeSb);
overlay.addEventListener('click', closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  const loaders = {links: loadLinks, connections: loadConns, errors: loadErrs, subscriptions: loadSubsPage, subgroups: loadSubs, logs: loadActivity, alerts: loadAlerts};
  if(loaders[name]) loaders[name]();
  closeSb();
  window.scrollTo({top: 0, behavior: 'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el => el.addEventListener('click', () => navTo(el.dataset.pg)));
function openModal(id){ document.getElementById(id).classList.add('open'); }
function closeModal(id){ document.getElementById(id).classList.remove('open'); }

// ========== Sparkline Charts with Time Control ==========
let sparkLoadChart, sparkTrafficChart, sparkConnsChart;
const MAX_POINTS = 200; // ~ 16 minutes (5s interval)
let sparkData = { load: [], traffic: [], conns: [] };
let sparkTime = { load: [], traffic: [], conns: [] }; // store timestamps (Date objects)
let sparkWindow = { load: { start: 0, end: MAX_POINTS }, traffic: { start: 0, end: MAX_POINTS }, conns: { start: 0, end: MAX_POINTS } };

function initSparklineCharts(){
  const accentColor = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#1a7aff';
  const accentBg = getComputedStyle(document.documentElement).getPropertyValue('--accent-d').trim() || 'rgba(26,122,255,0.12)';
  const textColor = getComputedStyle(document.documentElement).getPropertyValue('--t3').trim() || '#5a7298';
  const gridColor = getComputedStyle(document.documentElement).getPropertyValue('--card-b').trim() || '#1e2d45';
  
  const commonOpts = (label, unit='') => ({
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: 'rgba(0,0,0,0.8)',
        borderColor: accentColor,
        borderWidth: 1,
        titleColor: '#fff',
        bodyColor: '#fff',
        cornerRadius: 6,
        callbacks: {
          label: function(context) {
            const val = context.parsed.y;
            return val.toFixed(1) + (unit ? ' ' + unit : '');
          }
        }
      }
    },
    scales: {
      x: { display: true, grid: { color: gridColor, drawBorder: false }, ticks: { color: textColor, font: { size: 8, family: 'Vazirmatn, sans-serif' }, maxTicksLimit: 6, callback: function(value, index, ticks) { if(this.getLabelForValue) { const label = this.getLabelForValue(value); if(label) return label; } return ''; } } },
      y: { display: true, grid: { color: gridColor, drawBorder: false }, ticks: { color: textColor, font: { size: 8, family: 'Vazirmatn, sans-serif' } }, beginAtZero: true }
    },
    animation: { duration: 300 }
  });

  const ctxLoad = document.getElementById('sparkLoad').getContext('2d');
  sparkLoadChart = new Chart(ctxLoad, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.4 }] },
    options: { ...commonOpts('Load', '%'), scales: { ...commonOpts('Load', '%').scales, y: { ...commonOpts('Load', '%').scales.y, max: 100 } } }
  });
  const ctxTraffic = document.getElementById('sparkTraffic').getContext('2d');
  sparkTrafficChart = new Chart(ctxTraffic, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.4 }] },
    options: { ...commonOpts('Traffic', 'MB'), scales: { ...commonOpts('Traffic', 'MB').scales, y: { ...commonOpts('Traffic', 'MB').scales.y, beginAtZero: true } } }
  });
  const ctxConns = document.getElementById('sparkConns').getContext('2d');
  sparkConnsChart = new Chart(ctxConns, {
    type: 'line',
    data: { labels: [], datasets: [{ data: [], borderColor: accentColor, backgroundColor: accentBg, borderWidth: 2, pointRadius: 0, fill: true, tension: 0.4 }] },
    options: { ...commonOpts('Connections', ''), scales: { ...commonOpts('Connections', '').scales, y: { ...commonOpts('Connections', '').scales.y, stepSize: 1, beginAtZero: true } } }
  });

  // Set initial window to last 5 minutes worth of points (approx 60 points)
  sparkWindow.load.start = Math.max(0, sparkData.load.length - 60);
  sparkWindow.load.end = sparkData.load.length;
  sparkWindow.traffic.start = Math.max(0, sparkData.traffic.length - 60);
  sparkWindow.traffic.end = sparkData.traffic.length;
  sparkWindow.conns.start = Math.max(0, sparkData.conns.length - 60);
  sparkWindow.conns.end = sparkData.conns.length;
  updateSparklineAll();
}

function shiftTime(type, direction) {
  const step = 12; // ~1 minute (5s * 12 = 60s)
  const w = sparkWindow[type];
  const dataLen = sparkData[type].length;
  let newStart = w.start + direction * step;
  let newEnd = w.end + direction * step;
  if (newStart < 0) { newStart = 0; newEnd = Math.min(dataLen, newStart + (w.end - w.start)); }
  if (newEnd > dataLen) { newEnd = dataLen; newStart = Math.max(0, newEnd - (w.end - w.start)); }
  if (newEnd - newStart < 2) return; // keep at least 2 points
  w.start = newStart;
  w.end = newEnd;
  updateSparklineChart(type);
  updateRangeLabel(type);
}

function resetTime(type) {
  const w = sparkWindow[type];
  const dataLen = sparkData[type].length;
  w.start = Math.max(0, dataLen - 60);
  w.end = dataLen;
  updateSparklineChart(type);
  updateRangeLabel(type);
}

function updateRangeLabel(type) {
  const w = sparkWindow[type];
  const times = sparkTime[type];
  const el = document.getElementById(type + '-range');
  if (!el || times.length === 0) return;
  const startIdx = Math.max(0, Math.min(w.start, times.length-1));
  const endIdx = Math.max(0, Math.min(w.end-1, times.length-1));
  if (startIdx >= times.length || endIdx < 0) { el.textContent = '--:-- – --:--'; return; }
  const startTime = times[startIdx];
  const endTime = times[endIdx];
  const fmt = (d) => d ? d.toLocaleTimeString('en-US', {hour:'2-digit', minute:'2-digit'}) : '--:--';
  el.textContent = fmt(startTime) + ' – ' + fmt(endTime);
}

function updateSparklineChart(type) {
  const w = sparkWindow[type];
  const dataArr = sparkData[type];
  const timeArr = sparkTime[type];
  const sliced = dataArr.slice(w.start, w.end);
  const times = timeArr.slice(w.start, w.end);
  let chart;
  if (type === 'load') chart = sparkLoadChart;
  else if (type === 'traffic') chart = sparkTrafficChart;
  else if (type === 'conns') chart = sparkConnsChart;
  if (!chart) return;
  chart.data.labels = times.map(d => d ? d.toLocaleTimeString('en-US', {hour:'2-digit', minute:'2-digit'}) : '');
  chart.data.datasets[0].data = sliced;
  // Auto-scale y for traffic/conns
  if (type === 'traffic') {
    const max = Math.max(10, ...sliced, 1) * 1.2;
    chart.options.scales.y.max = Math.ceil(max);
  } else if (type === 'conns') {
    const max = Math.max(5, ...sliced, 1) * 1.2;
    chart.options.scales.y.max = Math.ceil(max);
  } else {
    chart.options.scales.y.max = 100;
  }
  chart.update('none');
}

function updateSparklineAll() {
  updateSparklineChart('load');
  updateSparklineChart('traffic');
  updateSparklineChart('conns');
  updateRangeLabel('load');
  updateRangeLabel('traffic');
  updateRangeLabel('conns');
}

// Add new data point to a specific metric
function addSparkDataPoint(type, value, time) {
  sparkData[type].push(value);
  sparkTime[type].push(time || new Date());
  if (sparkData[type].length > MAX_POINTS) {
    sparkData[type].shift();
    sparkTime[type].shift();
  }
  // Auto-advance window if at end (default behavior)
  const w = sparkWindow[type];
  if (w.end === sparkData[type].length - 1) {
    w.start = Math.max(0, w.start + 1);
    w.end = sparkData[type].length;
  } else {
    // if user scrolled back, keep window fixed
  }
  // If window end is at the end, we keep it at end
  if (w.end === sparkData[type].length - 1 && w.start < w.end) {
    // keep it
  }
  // Update chart only if this type is visible
  updateSparklineChart(type);
  updateRangeLabel(type);
}

// ========== Other Charts (Protocol & Hourly) ==========
let dashProtoChart = null, dashHourlyChart = null;
function initCharts(){
  const accentColor = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#1a7aff';
  const purpleColor = getComputedStyle(document.documentElement).getPropertyValue('--purple').trim() || '#8b5cf6';
  const greenColor = getComputedStyle(document.documentElement).getPropertyValue('--green-t').trim() || '#34d399';
  const amberColor = getComputedStyle(document.documentElement).getPropertyValue('--amber-t').trim() || '#fbbf24';
  const textColor = getComputedStyle(document.documentElement).getPropertyValue('--t3').trim() || '#5a7298';
  const gridColor = getComputedStyle(document.documentElement).getPropertyValue('--card-b').trim() || '#1e2d45';
  
  const ctxProto = document.getElementById('dashProtoChart').getContext('2d');
  dashProtoChart = new Chart(ctxProto, {
    type: 'bar',
    data: { labels: ['VLESS/WS', 'XHTTP-packet', 'XHTTP-stream'], datasets: [{ data: [0, 0, 0], backgroundColor: ['rgba(26, 122, 255, 0.8)', 'rgba(139, 92, 246, 0.8)', 'rgba(52, 211, 153, 0.8)'], borderColor: [accentColor, purpleColor, greenColor], borderWidth: 2, borderRadius: 6, barPercentage: 0.6 }] },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { backgroundColor: 'rgba(11, 17, 29, 0.9)', borderColor: accentColor, borderWidth: 1, titleColor: '#fff', bodyColor: '#fff', cornerRadius: 8, padding: 10, callbacks: { label: function(context){ return context.parsed.y + ' configs'; } } } },
      scales: { x: { grid: { display: false }, ticks: { color: textColor, font: { size: 9, family: 'Vazirmatn, sans-serif' } } }, y: { grid: { color: gridColor, drawBorder: false }, ticks: { color: textColor, font: { size: 9, family: 'Vazirmatn, sans-serif' }, stepSize: 1 } } },
      animation: { duration: 400, easing: 'easeOutQuart' }
    }
  });
  const ctxHourly = document.getElementById('dashHourlyChart').getContext('2d');
  dashHourlyChart = new Chart(ctxHourly, {
    type: 'line',
    data: { labels: ['00', '04', '08', '12', '16', '20'], datasets: [{ data: [0, 0, 0, 0, 0, 0], borderColor: amberColor, backgroundColor: 'rgba(251, 191, 36, 0.1)', borderWidth: 2, pointRadius: 0, pointHoverRadius: 5, pointHoverBorderWidth: 2, pointHoverBorderColor: '#fff', fill: true, tension: 0.3 }] },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { backgroundColor: 'rgba(11, 17, 29, 0.9)', borderColor: amberColor, borderWidth: 1, titleColor: '#fff', bodyColor: '#fff', cornerRadius: 8, padding: 10, callbacks: { label: function(context){ return context.parsed.y + ' MB'; } } } },
      scales: { x: { grid: { display: false }, ticks: { color: textColor, font: { size: 8, family: 'Vazirmatn, sans-serif' } } }, y: { grid: { color: gridColor, drawBorder: false }, ticks: { color: textColor, font: { size: 8, family: 'Vazirmatn, sans-serif' }, callback: function(value) { return value + ' MB'; } } } },
      animation: { duration: 400, easing: 'easeOutQuart' }
    }
  });
}
function updateCharts(statsData, linksData){
  if(dashProtoChart && linksData){
    const protoCounts = { 'vless-ws': 0, 'xhttp-packet-up': 0, 'xhttp-stream-up': 0 };
    linksData.forEach(l => {
      const protos = l.protocols || ['vless-ws'];
      protos.forEach(p => { if(protoCounts[p] !== undefined) protoCounts[p]++; });
    });
    const counts = [protoCounts['vless-ws'], protoCounts['xhttp-packet-up'], protoCounts['xhttp-stream-up']];
    dashProtoChart.data.datasets[0].data = counts;
    dashProtoChart.update('none');
  }
  if(dashHourlyChart && statsData){
    const hourly = statsData.hourly || {};
    const labels = Object.keys(hourly).sort();
    const data = labels.map(h => (hourly[h] || 0) / (1024 * 1024));
    let slicedLabels = labels.slice(0, 6);
    let slicedData = data.slice(0, 6);
    while(slicedLabels.length < 6){ slicedLabels.push('—'); slicedData.push(0); }
    dashHourlyChart.data.labels = slicedLabels;
    dashHourlyChart.data.datasets[0].data = slicedData;
    dashHourlyChart.update('none');
  }
}

// ========== fetchStats with sparkline updates ==========
let prevTraf = 0;
let allLinksList = [];
async function fetchStats(){
  try{
    const connResp = await authF('/api/connections');
    const connData = await connResp.json();
    const conns = connData.connections || [];
    const uniqueIps = new Set(conns.map(c => c.ip));
    const activeCount = uniqueIps.size;
    document.getElementById('dash-conns').textContent = activeCount;
    
    const statsResp = await authF('/stats');
    const d = await statsResp.json();
    document.getElementById('dash-traffic').innerHTML = (d.total_traffic_mb || 0).toFixed(1) + ' <small style="font-size:14px;font-weight:400;">MB</small>';
    document.getElementById('dash-links').textContent = d.links_count || 0;
    document.getElementById('dash-links-sub').textContent = (d.active_links || 0) + ' / ' + (d.links_count || 0);
    document.getElementById('dash-uptime').textContent = d.uptime || '00:00:00';
    document.getElementById('uptime-badge').textContent = 'Railway · ' + (d.uptime || '00:00:00');
    document.getElementById('last-upd').textContent = 'Last update: ' + new Date().toLocaleTimeString();

    // Update sparklines
    const now = new Date();
    // Load (delta percent)
    const delta = d.total_traffic_mb - prevTraf;
    const pct = Math.min(100, Math.max(0, Math.round((delta / 50) * 100 * 10) / 10));
    prevTraf = d.total_traffic_mb;
    addSparkDataPoint('load', pct, now);
    document.getElementById('spark-load').innerHTML = pct + '<span class="unit">%</span>';

    // Traffic (total MB)
    const trafficVal = parseFloat(d.total_traffic_mb.toFixed(2));
    addSparkDataPoint('traffic', trafficVal, now);
    document.getElementById('spark-traffic').innerHTML = trafficVal + '<span class="unit">MB</span>';

    // Connections
    addSparkDataPoint('conns', activeCount, now);
    document.getElementById('spark-conns').textContent = activeCount;

    // Update other charts
    updateCharts(d, allLinksList);
  } catch(e){ console.error('fetchStats error:', e); }
}

// ========== loadLinks (with allSubsList) ==========
async function loadLinks(){
  try{
    const [lr, sr] = await Promise.all([authF('/api/links'), authF('/api/subs')]);
    const {links = []} = await lr.json();
    const {subs = []} = await sr.json();
    allLinksList = links;
    allSubsList = subs;
    const nlSub = document.getElementById('nl-sub');
    const curSub = nlSub.value;
    nlSub.innerHTML = '<option value="">— No Group —</option>' + subs.map(s => `<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    if(curSub) nlSub.value = curSub;
    document.getElementById('links-nb').textContent = links.length;
    document.getElementById('links-pg-cnt').textContent = links.length + ' Configs';
    const grid = document.getElementById('links-grid');
    const empty = document.getElementById('links-empty');
    if(!links.length){ grid.innerHTML = ''; empty.style.display = 'block'; return; }
    empty.style.display = 'none';
    grid.innerHTML = links.map(l => {
      const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
      const bc = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--accent)';
      const allowed = l.active && !l.expired;
      const cardCls = !l.active ? 'is-off' : (l.expired ? 'is-exp' : '');
      const proto = (l.protocols && l.protocols[0]) || 'vless-ws';
      const protoLabel = proto === 'vless-ws' ? 'VLESS-WS' : proto.replace('xhttp-', '').toUpperCase();
      const displayLabel = formatLinkName(l.label, protoLabel);
      return `<div class="cfg-card ${cardCls}">
        <div class="cfg-row">
          <span class="cfg-status-dot ${allowed ? 'pulse' : ''}"></span>
          <div class="cfg-identity">
            <div class="cfg-label">${esc(displayLabel)}</div>
            <div class="cfg-sub-meta">
              <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID copied','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
              <span>${new Date(l.created_at).toLocaleDateString()}</span>
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col">
            <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
            <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>of ${lim}</span></div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-exp-col">${expChip(l.expires_at, l.expired)}</div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-badges-col">
            ${protoBadge(l.protocols || ['vless-ws'])}
            ${l.sub_id && allSubsList.find(s => s.sub_id === l.sub_id) ? `<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s => s.sub_id === l.sub_id).name)}</span>` : ''}
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="tog${allowed ? ' on' : ''}" onclick="toggleActive('${l.uuid}', ${!l.active})" title="Toggle"></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('Link copied','ok'))" title="Copy"><i class="ti ti-copy"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub copied','ok'))" title="Sub"><i class="ti ti-rss"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
            <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="Edit"><i class="ti ti-edit"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="Reset"><i class="ti ti-rotate"></i></button>
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="Delete"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>`;
    }).join('');
    const stats = await authF('/stats').then(r => r.json());
    updateCharts(stats, links);
  } catch(e){ console.error(e); }
}

// ========== createLink, openEditLink, saveEditLink, toggleActive, resetUsage, deleteLink, showQR ==========
async function createLink(){
  const label = document.getElementById('nl-label').value.trim() || 'New Config';
  const val = document.getElementById('nl-val').value;
  const unit = document.getElementById('nl-unit').value;
  const exp = document.getElementById('nl-exp').value;
  const note = document.getElementById('nl-note').value.trim();
  const sub_id = document.getElementById('nl-sub').value || null;
  const protocols = getSelectedProtocols();
  if(!protocols.length){ toast('Select at least one protocol', 'err'); return; }
  const count = parseInt(document.getElementById('nl-count').value) || 1;
  const body = { label, limit_value: val || 0, limit_unit: unit, expires_days: exp || 0, note, sub_id, protocols, count };
  try{
    let r, d;
    if(count > 1){
      r = await authF('/api/links/bulk', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      d = await r.json();
      toast(count + ' configs created ✓', 'ok');
    } else {
      r = await authF('/api/links', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      d = await r.json();
      toast('Config created ✓', 'ok');
    }
    document.getElementById('nl-label').value = '';
    document.getElementById('nl-val').value = '';
    document.getElementById('nl-exp').value = '';
    document.getElementById('nl-note').value = '';
    document.querySelectorAll('.proto-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelector('.proto-btn[data-proto="vless-ws"]').classList.add('active');
    document.getElementById('nl-count').value = 1;
    document.querySelectorAll('.count-chip').forEach(c => c.classList.remove('active'));
    document.querySelector('.count-chip').classList.add('active');
    loadLinks();
  } catch(e){ toast('Error creating config', 'err'); }
}
function openEditLink(uuid){
  const l = allLinksList.find(x => x.uuid === uuid);
  if(!l) return;
  document.getElementById('el-uuid').value = uuid;
  document.getElementById('el-label').value = l.label;
  document.getElementById('el-note').value = l.note || '';
  if(l.limit_bytes === 0){ document.getElementById('el-val').value = ''; document.getElementById('el-unit').value = 'GB'; }
  else { document.getElementById('el-val').value = (l.limit_bytes / 1024 / 1024).toFixed(0); document.getElementById('el-unit').value = 'MB'; }
  document.getElementById('el-exp').value = '';
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid = document.getElementById('el-uuid').value;
  const label = document.getElementById('el-label').value.trim();
  const note = document.getElementById('el-note').value.trim();
  const val = document.getElementById('el-val').value;
  const unit = document.getElementById('el-unit').value;
  const exp = document.getElementById('el-exp').value;
  const body = { label, note, limit_value: val || 0, limit_unit: unit };
  if(exp && Number(exp) > 0) body.expires_days = Number(exp);
  try{
    const r = await authF('/api/links/' + uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    if(!r.ok) throw new Error();
    closeModal('modal-edit-link');
    toast('Config updated ✓', 'ok');
    loadLinks();
  } catch(e){ toast('Error updating config', 'err'); }
}
async function toggleActive(uuid, newState){
  try{ const r = await authF('/api/links/' + uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ active: newState }) }); if(!r.ok) throw new Error(); toast(newState ? 'Activated ✓' : 'Deactivated', 'ok'); loadLinks(); } catch(e){ toast('Error', 'err'); }
}
async function resetUsage(uuid){
  try{ const r = await authF('/api/links/' + uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ reset_usage: true }) }); if(!r.ok) throw new Error(); toast('Usage reset ✓', 'ok'); loadLinks(); } catch(e){ toast('Error', 'err'); }
}
async function deleteLink(uuid){
  if(!confirm('Delete this config?')) return;
  try{ const r = await authF('/api/links/' + uuid, { method: 'DELETE' }); if(!r.ok) throw new Error(); toast('Deleted ✓', 'ok'); loadLinks(); } catch(e){ toast('Error', 'err'); }
}
function showQR(link){ window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=' + encodeURIComponent(link), '_blank'); }

// ========== Sub Groups (loadSubs, filterSubs, createSub, deleteSub, openSubLinks, etc.) ==========
let allSubsList = [];
async function loadSubs(){
  try{
    const r = await authF('/api/subs');
    const d = await r.json();
    const subs = d.subs || [];
    allSubsRaw = subs;
    document.getElementById('subs-nb').textContent = subs.length;
    document.getElementById('subs-pg-cnt').textContent = subs.length + ' Groups';
    const grid = document.getElementById('subs-grid');
    if(!subs.length){ grid.innerHTML = '<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title" data-lang="no_groups">No groups yet</div><div class="subs-empty-v2-sub" data-lang="create_group">Create a new group to organize your configs</div></div>'; return; }
    grid.innerHTML = subs.map(s => `
      <div class="sub-card">
        <div class="sub-card-top">
          <div class="sub-card-head-v2">
            <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
            <div class="sub-card-titles"><div class="sub-card-name-v2">${esc(s.name)}</div><div class="sub-card-desc-v2">${s.desc || 'No description'}</div></div>
            <div class="sub-card-lock-badge ${s.has_password ? 'locked' : 'open'}"><i class="ti ${s.has_password ? 'ti-lock' : 'ti-lock-open'}"></i></div>
          </div>
          <div class="sub-card-stats">
            <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label" data-lang="configs">Configs</div></div>
            <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label" data-lang="active">Active</div></div>
            <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label" data-lang="usage">Usage</div></div>
          </div>
        </div>
        <div class="sub-card-url-row"><span class="sub-card-url-text">${esc(s.public_url)}</span><button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-copy"></i></button><button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')"><i class="ti ti-external-link"></i></button></div>
        <div class="sub-card-bottom">
          <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> <span data-lang="configs">Configs</span></button>
          <button class="btn btn-sm btn-pur" onclick="copyAllSubLinks('${esc(s.sub_id)}')"><i class="ti ti-copy"></i> <span data-lang="copy">Copy All</span></button>
          <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
          <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')"><i class="ti ti-trash"></i></button>
        </div>
      </div>
    `).join('');
  } catch(e){ console.error(e); }
}
function filterSubs(q){ q = q.trim().toLowerCase(); if(!q){ loadSubs(); return; } const filtered = allSubsRaw.filter(s => s.name.toLowerCase().includes(q) || (s.desc || '').toLowerCase().includes(q)); const grid = document.getElementById('subs-grid'); if(!filtered.length){ grid.innerHTML = '<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups found</div></div>'; return; } grid.innerHTML = filtered.map(s => `
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles"><div class="sub-card-name-v2">${esc(s.name)}</div><div class="sub-card-desc-v2">${s.desc || 'No description'}</div></div>
          <div class="sub-card-lock-badge ${s.has_password ? 'locked' : 'open'}"><i class="ti ${s.has_password ? 'ti-lock' : 'ti-lock-open'}"></i></div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">Configs</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">Active</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">Usage</div></div>
        </div>
      </div>
      <div class="sub-card-url-row"><span class="sub-card-url-text">${esc(s.public_url)}</span><button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-copy"></i></button><button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')"><i class="ti ti-external-link"></i></button></div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> Configs</button>
        <button class="btn btn-sm btn-pur" onclick="copyAllSubLinks('${esc(s.sub_id)}')"><i class="ti ti-copy"></i> Copy All</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join(''); }
async function createSub(){
  const name = document.getElementById('ns-name').value.trim() || 'New Group';
  const desc = document.getElementById('ns-desc').value.trim();
  const pw = document.getElementById('ns-pw').value;
  try{
    const r = await authF('/api/subs', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name, desc, password: pw }) });
    if(!r.ok) throw new Error('failed');
    document.getElementById('ns-name').value = '';
    document.getElementById('ns-desc').value = '';
    document.getElementById('ns-pw').value = '';
    closeModal('modal-create-sub');
    toast('Group created ✓', 'ok');
    loadSubs();
  } catch(e){ toast('Error creating group', 'err'); }
}
async function deleteSub(sub_id){
  if(!confirm('Delete this group?')) return;
  try{ const r = await authF('/api/subs/' + sub_id, { method: 'DELETE' }); if(!r.ok) throw new Error(); toast('Group deleted ✓', 'ok'); loadSubs(); loadLinks(); } catch(e){ toast('Error', 'err'); }
}
let lmodalLinks = [], lmodalInSub = new Set(), currentSubId = '';
async function openSubLinks(sub_id, name){
  currentSubId = sub_id;
  document.getElementById('modal-sub-name').textContent = name;
  document.getElementById('modal-links-body').innerHTML = '<div style="padding:20px;text-align:center">Loading...</div>';
  openModal('modal-links');
  try{
    const [lr, sr] = await Promise.all([authF('/api/links'), authF('/api/subs')]);
    const {links = []} = await lr.json();
    const {subs = []} = await sr.json();
    const thisSub = subs.find(s => s.sub_id === sub_id);
    lmodalInSub = new Set(thisSub?.link_ids || []);
    lmodalLinks = links;
    renderLmodalList(links);
  } catch(e){ toast('Error loading', 'err'); }
}
function renderLmodalList(links){
  const body = document.getElementById('modal-links-body');
  if(!links.length){ body.innerHTML = '<div class="empty">No configs</div>'; updateLmodalCount(); return; }
  body.innerHTML = links.map(l => {
    const checked = lmodalInSub.has(l.uuid);
    const on = l.active && !l.expired;
    return `<div class="lrow-v2 ${checked ? 'checked' : ''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}', this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info"><div class="lrow-v2-name">${esc(l.label)}</div><div class="lrow-v2-meta">${fmtB(l.used_bytes)}</div></div>
      <span class="lrow-v2-status ${on ? 'on' : 'off'}">${on ? 'Active' : 'Inactive'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid, el){ if(lmodalInSub.has(uuid)){ lmodalInSub.delete(uuid); el.classList.remove('checked'); } else { lmodalInSub.add(uuid); el.classList.add('checked'); } updateLmodalCount(); }
function lmodalSelectAll(state){ lmodalLinks.forEach(l => { if(state) lmodalInSub.add(l.uuid); else lmodalInSub.delete(l.uuid); }); renderLmodalList(lmodalLinks); }
function updateLmodalCount(){ document.getElementById('lmodal-count').textContent = lmodalInSub.size + ' selected'; }
function filterLmodal(q){ q = q.trim().toLowerCase(); document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row => { row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none'; }); }
async function saveSubLinks(){
  if(!currentSubId) return;
  const link_ids = [...lmodalInSub];
  try{
    const r = await authF('/api/subs/' + currentSubId, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ link_ids }) });
    if(!r.ok) throw new Error();
    await Promise.all(lmodalLinks.map(l => authF('/api/links/' + l.uuid, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sub_id: lmodalInSub.has(l.uuid) ? currentSubId : null }) })));
    closeModal('modal-links');
    toast('Group configs saved ✓', 'ok');
    loadSubs();
    loadLinks();
  } catch(e){ toast('Error saving', 'err'); }
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent = location.protocol + '//' + location.host + '/sub-all';
  try{
    const r = await authF('/api/subs');
    const d = await r.json();
    const subs = d.subs || [];
    const el = document.getElementById('sub-groups-list');
    if(!subs.length){ el.innerHTML = '<div class="empty">No groups yet</div>'; return; }
    el.innerHTML = subs.map(s => `
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div><div style="font-weight:700;font-size:13px">${esc(s.name)}</div><div style="font-size:10px;color:var(--accent)">${esc(s.sub_url)}</div><div style="font-size:10px;color:var(--t3)">${toFa(s.links_count)} configs · ${esc(s.total_used_fmt)}</div></div>
        <div style="display:flex;gap:5px"><button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}')"><i class="ti ti-copy"></i> Sub</button><button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button></div>
      </div>
    `).join('');
  } catch(e){}
}
function cpSubAll(){ navigator.clipboard.writeText(location.protocol + '//' + location.host + '/sub-all').then(() => toast('Copied ✓', 'ok')); }
async function copyAllSubLinks(subId){
  const r = await authF('/api/links');
  const d = await r.json();
  const links = d.links || [];
  const sub = allSubsRaw.find(s => s.sub_id === subId);
  if(!sub){ toast('Group not found', 'err'); return; }
  const subLinkIds = sub.link_ids || [];
  const urls = links.filter(l => subLinkIds.includes(l.uuid) && l.active && !l.expired).map(l => l.sub_url);
  if(!urls.length){ toast('No active configs', 'err'); return; }
  navigator.clipboard.writeText(urls.join('\n')).then(() => toast(urls.length + ' links copied ✓', 'ok'));
}

// ========== Connections, Activity, Errors, WebSocket ==========
async function loadConns(){
  try{
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const ce = document.getElementById('conns-empty');
    document.getElementById('ch-count').textContent = toFa(d.count);
    const conns = d.connections || [];
    if(!d.count){ grid.innerHTML = ''; ce.style.display = 'block'; document.getElementById('ch-traffic').textContent = '—'; document.getElementById('ch-avgdur').textContent = '—'; document.getElementById('ch-uniq').textContent = '—'; return; }
    ce.style.display = 'none';
    const totalBytes = conns.reduce((s, c) => s + parseBytesFmt(c.bytes_fmt), 0);
    document.getElementById('ch-traffic').textContent = fmtB(totalBytes);
    const uniqIps = new Set(conns.map(c => c.ip)).size;
    document.getElementById('ch-uniq').textContent = toFa(uniqIps);
    const durs = conns.map(c => c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0);
    const avgSec = durs.length ? Math.floor(durs.reduce((a,b) => a+b, 0) / durs.length) : 0;
    document.getElementById('ch-avgdur').textContent = avgSec < 60 ? avgSec + 's' : avgSec < 3600 ? Math.floor(avgSec/60) + 'm' : Math.floor(avgSec/3600) + 'h';
    const maxDur = Math.max(...durs, 1);
    grid.innerHTML = conns.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + 's' : secs < 3600 ? Math.floor(secs/60) + 'm' : Math.floor(secs/3600) + 'h';
      const durPct = Math.min(100, Math.round((secs / maxDur) * 100));
      const protoVal = c.transport === 'vless-ws' ? 'vless-ws' : (c.transport || '').replace('xhttp-', 'xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id"><div class="conn-ip-v2">${esc(c.ip)}<button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}')"><i class="ti ti-copy"></i></button></div><div class="conn-label-v2">${esc(c.label)}</div></div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> Live</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge([protoVal])}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-text-label">Traffic</div><div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div></div></div>
            <div class="conn-stat-box"><div class="conn-stat-icon time"><i class="ti ti-clock"></i></div><div><div class="conn-stat-text-label">Duration</div><div class="conn-stat-text-val">${dur}</div></div></div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  } catch(e){ console.error(e); }
}
function parseBytesFmt(s){ if(!s) return 0; const m = String(s).match(/([\d.]+)\s*([A-Za-z]+)/); if(!m) return 0; const n = parseFloat(m[1]), u = m[2].toUpperCase(); const mult = { B:1, KB:1024, MB:1024**2, GB:1024**3, TB:1024**4 }; return n * (mult[u] || 0); }
async function loadActivity(){
  try{
    const r = await authF('/api/activity');
    const d = await r.json();
    const logs = (d.logs || []).slice().reverse();
    const el = document.getElementById('logs-list');
    const em = document.getElementById('logs-empty');
    if(!logs.length){ el.innerHTML = ''; em.style.display = 'block'; return; }
    em.style.display = 'none';
    const icMap = { ok: 'ti-circle-check', err: 'ti-circle-x', warn: 'ti-alert-triangle', info: 'ti-info-circle' };
    const kindFa = { link: 'Config', sub: 'Group', auth: 'Login', connection: 'Connection', system: 'System' };
    el.innerHTML = logs.map(l => `
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level] || 'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString()} <span class="log-kind">${kindFa[l.kind] || l.kind}</span></div>
        </div>
      </div>
    `).join('');
  } catch(e){ console.error(e); }
}
async function loadErrs(){
  try{ const r = await authF('/stats'); const d = await r.json(); renderErrs(d.recent_errors || []); } catch(e){}
}
function renderErrs(errs){
  const el = document.getElementById('errs-full');
  if(!el) return;
  if(!errs.length){ el.innerHTML = '<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> No errors</div>'; return; }
  el.innerHTML = errs.slice().reverse().map(e => `<div class="erow"><div class="etime"><i class="ti ti-clock"></i> ${new Date(e.time).toLocaleString()}</div><div class="emsg">${esc(e.error)}${e.url ? ' — ' + esc(e.url) : ''}</div></div>`).join('');
}
let ws = null;
function wsLog(c, m){
  const l = document.getElementById('ws-log');
  const p = document.createElement('p');
  const colors = { ok: '#10b981', err: '#ef4444', info: '#8b949e', sent: '#1677ff' };
  p.style.color = colors[c] || '#fff';
  p.textContent = '[' + new Date().toLocaleTimeString() + '] ' + m;
  l.appendChild(p);
  l.scrollTop = l.scrollHeight;
}
function wsConn(){
  const u = document.getElementById('ws-uuid').value.trim();
  if(!u){ toast('Enter UUID', 'err'); return; }
  const url = (location.protocol === 'https:' ? 'wss' : 'ws') + '://' + location.host + '/ws/' + u;
  wsLog('info', 'Connecting: ' + url);
  ws = new WebSocket(url);
  ws.onopen = () => wsLog('ok', '✓ Connected');
  ws.onerror = () => wsLog('err', '✗ Error');
  ws.onmessage = m => wsLog('info', 'Received ' + m.data.length + ' bytes');
  ws.onclose = e => wsLog('err', 'Disconnected (' + e.code + ')');
}
function wsSend(){
  const m = document.getElementById('ws-msg').value;
  if(!m || !ws || ws.readyState !== 1) return;
  ws.send(m);
  wsLog('sent', 'Sent: ' + m);
  document.getElementById('ws-msg').value = '';
}
function wsDisc(){ if(ws) ws.close(); }

// ========== Change Password ==========
async function changePw(){
  const cur = document.getElementById('cp-cur').value;
  const nw = document.getElementById('cp-new').value;
  const cf = document.getElementById('cp-cf').value;
  if(!cur || !nw || !cf){ toast('Fill all fields', 'err'); return; }
  if(nw.length < 4){ toast('Min 4 characters', 'err'); return; }
  if(nw !== cf){ toast('Passwords do not match', 'err'); return; }
  try{
    const r = await authF('/api/change-password', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ current_password: cur, new_password: nw }) });
    const d = await r.json().catch(() => ({}));
    if(!r.ok) throw new Error(d.detail || 'Error');
    toast('Password changed ✓', 'ok');
    document.getElementById('cp-cur').value = '';
    document.getElementById('cp-new').value = '';
    document.getElementById('cp-cf').value = '';
  } catch(e){ toast('✗ ' + e.message, 'err'); }
}
function togglePwField(id, btn){
  const inp = document.getElementById(id);
  const icon = btn.querySelector('i');
  const toText = inp.type === 'password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti ' + (toText ? 'ti-eye-off' : 'ti-eye');
}
function checkPwStrength(val){
  const segs = document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label = document.getElementById('pw-strength-label');
  const reqLen = document.getElementById('req-len');
  const reqNum = document.getElementById('req-num');
  const reqCase = document.getElementById('req-case');
  const hasLen = val.length >= 4;
  const hasNum = /\d/.test(val);
  const hasCase = /[a-z]/.test(val) && /[A-Z]/.test(val);
  const hasLong = val.length >= 8;
  reqLen.classList.toggle('met', hasLen);
  reqNum.classList.toggle('met', hasNum);
  reqCase.classList.toggle('met', hasCase);
  let score = 0; if(hasLen) score++; if(hasNum) score++; if(hasCase) score++; if(hasLong) score++;
  const colors = ['#1677ff', '#4096ff', '#0050b3', '#003a8c'];
  const labels = ['Very Weak', 'Weak', 'Medium', 'Strong'];
  segs.forEach((s, i) => { s.style.background = i < score ? colors[Math.max(0, score-1)] : 'rgba(100,116,139,.2)'; });
  if(val.length === 0){ label.innerHTML = '<i class="ti ti-shield"></i> Password Strength'; return; }
  label.innerHTML = `<i class="ti ti-shield-check" style="color:${colors[Math.max(0, score-1)]}"></i> ${labels[Math.max(0, score-1)]}`;
}

// ========== Smart Alerts ==========
function generateAlertsFromData(stats, links){
  const alerts = [];
  links.forEach(l => {
    if(l.expires_at && !l.expired){
      const d = daysLeft(l.expires_at);
      if(d !== null && d <= 3){
        alerts.push({
          id: 'exp-' + l.uuid,
          priority: d <= 1 ? 'critical' : 'warning',
          icon: 'ti ti-calendar-x',
          titleKey: 'alert_expiry',
          title: 'Config expiring soon',
          description: `"${l.label}" expires in ${d} day${d>1?'s':''}`,
          time: new Date().toISOString(),
          link: '/CFOX#pg-links',
          dismissable: true
        });
      }
    }
    if(l.limit_bytes > 0){
      const pct = l.used_bytes / l.limit_bytes * 100;
      if(pct > 80){
        alerts.push({
          id: 'quota-' + l.uuid,
          priority: pct > 95 ? 'critical' : 'warning',
          icon: 'ti ti-gauge',
          titleKey: 'alert_quota',
          title: 'Traffic quota exceeded 80%',
          description: `"${l.label}" used ${fmtB(l.used_bytes)} of ${fmtB(l.limit_bytes)} (${Math.round(pct)}%)`,
          time: new Date().toISOString(),
          link: '/CFOX#pg-links',
          dismissable: true
        });
      }
    }
  });
  const recentErrors = stats.recent_errors || [];
  const fiveMinAgo = Date.now() - 300000;
  const recent = recentErrors.filter(e => new Date(e.time).getTime() > fiveMinAgo);
  if(recent.length >= 3){
    alerts.push({
      id: 'errors-' + Date.now(),
      priority: 'critical',
      icon: 'ti ti-alert-triangle',
      titleKey: 'alert_errors',
      title: 'Repeated connection errors',
      description: `${recent.length} errors in the last 5 minutes. Check logs.`,
      time: new Date().toISOString(),
      link: '/CFOX#pg-errors',
      dismissable: true
    });
  }
  const connCount = stats.active_connections || 0;
  if(connCount > 0){
    const lastAlert = alertsData.find(a => a.id && a.id.startsWith('newip-'));
    if(!lastAlert || (new Date() - new Date(lastAlert.time) > 3600000)){
      alerts.push({
        id: 'newip-' + Date.now(),
        priority: 'info',
        icon: 'ti ti-user-plus',
        titleKey: 'alert_new_ip',
        title: 'New IP connected',
        description: `A new connection was established from a different IP.`,
        time: new Date().toISOString(),
        link: '/CFOX#pg-connections',
        dismissable: true
      });
    }
  }
  return alerts;
}
async function loadAlerts(){
  try{
    const r = await authF('/stats');
    const stats = await r.json();
    const linksResp = await authF('/api/links');
    const {links = []} = await linksResp.json();
    const newAlerts = generateAlertsFromData(stats, links);
    const dismissedIds = alertsData.filter(a => a.dismissed).map(a => a.id);
    alertsData = newAlerts.map(a => ({
      ...a,
      dismissed: dismissedIds.includes(a.id)
    }));
    renderAlerts(currentAlertFilter);
    document.getElementById('alerts-badge').textContent = alertsData.filter(a => !a.dismissed).length;
    document.getElementById('alerts-count-badge').textContent = alertsData.filter(a => !a.dismissed).length;
  } catch(e){ console.error('Alerts load error:', e); }
}
function renderAlerts(filter){
  const list = document.getElementById('alerts-list');
  const filtered = alertsData.filter(a => !a.dismissed && (filter === 'all' || a.priority === filter));
  if(!filtered.length){
    list.innerHTML = `<div class="alerts-empty"><i class="ti ti-bell-off"></i><span data-lang="no_alerts">No alerts to show</span></div>`;
    return;
  }
  const dict = LANG_DICT[currentLang] || LANG_DICT['en'];
  list.innerHTML = filtered.map(a => `
    <div class="alert-item ${a.priority}">
      <div class="alert-icon ${a.priority}"><i class="${a.icon}"></i></div>
      <div class="alert-body">
        <div class="alert-title">${dict[a.titleKey] || a.title}</div>
        <div class="alert-desc">${a.description}</div>
        <div class="alert-time"><i class="ti ti-clock"></i> ${new Date(a.time).toLocaleString()}</div>
      </div>
      <div class="alert-actions">
        ${a.link ? `<a href="${a.link}" class="btn btn-sm btn-g"><i class="ti ti-eye"></i></a>` : ''}
        ${a.dismissable ? `<button class="btn btn-sm btn-dismiss" onclick="dismissAlert('${a.id}')"><i class="ti ti-x"></i> <span data-lang="dismiss">Dismiss</span></button>` : ''}
      </div>
    </div>
  `).join('');
}
function filterAlerts(filter, btn){
  currentAlertFilter = filter;
  document.querySelectorAll('.alerts-filters .btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderAlerts(filter);
}
function dismissAlert(id){
  const alert = alertsData.find(a => a.id === id);
  if(alert) alert.dismissed = true;
  renderAlerts(currentAlertFilter);
  document.getElementById('alerts-badge').textContent = alertsData.filter(a => !a.dismissed).length;
  document.getElementById('alerts-count-badge').textContent = alertsData.filter(a => !a.dismissed).length;
}
setInterval(() => {
  if(document.getElementById('pg-alerts')?.classList.contains('on')){
    loadAlerts();
  }
}, 30000);

// ========== Refresh All ==========
function refreshAll(){
  fetchStats();
  if(document.getElementById('pg-links').classList.contains('on')) loadLinks();
  if(document.getElementById('pg-subgroups').classList.contains('on')) loadSubs();
  if(document.getElementById('pg-subscriptions').classList.contains('on')) loadSubsPage();
  if(document.getElementById('pg-connections').classList.contains('on')) loadConns();
  if(document.getElementById('pg-logs').classList.contains('on')) loadActivity();
  if(document.getElementById('pg-alerts').classList.contains('on')) loadAlerts();
  toast('Refreshed ✓', 'ok');
}

// ========== DOM Ready ==========
document.addEventListener('DOMContentLoaded', async () => {
  await checkAuth();
  applyLanguage();
  document.querySelectorAll('.btn-lang').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.langCode === currentLang);
  });
  applyTheme(currentTheme);
  initSparklineCharts();
  initCharts();
  document.getElementById('set-host').textContent = location.host;
  document.getElementById('sub-all-url').textContent = location.protocol + '//' + location.host + '/sub-all';
  await loadServerSettings();
  fetchStats();
  loadLinks();
  loadSubs();
  loadSubsPage();
  setInterval(fetchStats, 5000);
  setInterval(() => {
    if(document.getElementById('pg-connections').classList.contains('on')) loadConns();
    if(document.getElementById('pg-logs').classList.contains('on')) loadActivity();
  }, 10000);
});
document.addEventListener('DOMContentLoaded', function() {
  if(!document.getElementById('nl-count')) {
    const hidden = document.createElement('input');
    hidden.type = 'hidden';
    hidden.id = 'nl-count';
    hidden.value = 1;
    document.querySelector('.cp-body').appendChild(hidden);
  }
});
</script>
</body></html>"""

def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>CBee Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#0d1117;--card:#161b22;--card-b:#30363d;--accent:#1677ff;--accent2:#4096ff;--t1:#f0f6fc;--t2:#8b949e;--t3:#6e7681;--radius:16px}}
body{{font-family:'Vazirmatn','Segoe UI',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}}
.wrap{{max-width:800px;width:100%}}
.brand{{font-size:28px;font-weight:900;text-align:center;margin-bottom:20px;color:var(--accent2)}}
.loading{{text-align:center;padding:40px;color:var(--t3)}}
.card{{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:20px}}
</style>
</head>
<body>
<div class="wrap"><div class="brand">CBee</div><div id="root" class="loading">Loading...</div></div>
<script>
const UUID_KEY='{uuid_key}';let savedPw='';
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json();}}
async function renderContent(d){{let html=`<div class="card"><h2 style="color:var(--accent2)">${{d.name}}</h2><p style="color:var(--t3)">${{d.desc||''}}</p><p>Active connections: ${{d.active_connections}}</p><p>Total usage: ${{d.total_used_fmt}}</p><hr style="margin:15px 0;border-color:var(--card-b)"><div>`;for(let l of d.links){{html+=`<div style="background:rgba(0,0,0,.2);border-radius:12px;padding:12px;margin-bottom:8px;border:1px solid var(--card-b)"><strong style="color:var(--accent2)">${{l.label}}</strong> <span style="color:var(--t3)">${{l.used_fmt}} / ${{l.limit_fmt}}</span><div style="font-size:10px;color:var(--t3)">${{l.vless_link.substring(0,60)}}…</div></div>`;}}html+=`</div></div>`;document.getElementById('root').innerHTML=html;}}
async function init(){{const data=await loadData();if(data.locked){{document.getElementById('root').innerHTML=`<div class="card" style="text-align:center"><h3 style="color:var(--accent2)">${{data.name}}</h3><p>This group is password protected.</p><input type="password" id="pw" placeholder="Enter password" style="margin:10px;padding:8px;border-radius:8px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:white;width:200px"><br><button onclick="submitPw()" style="padding:8px 16px;background:var(--accent);border:none;border-radius:8px;cursor:pointer;color:#fff;font-weight:700">Login</button></div>`;}}else{{renderContent(data);}}}}
async function submitPw(){{const pw=document.getElementById('pw').value;const data=await loadData(pw);if(data.locked){{alert('Wrong password');return;}}savedPw=pw;renderContent(data);}}
init();
</script>
</body></html>"""
