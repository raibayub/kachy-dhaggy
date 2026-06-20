import re

file_path = "Kachy Dhaagy.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace :root
new_root = """    :root {
      --bg-primary: #FAFAFA;
      --bg-secondary: #F4F4F5;
      --gold: #C5A059;
      --gold-soft: #D3B579;
      --text: #121212;
      --muted: #6B7280;
      --card-bg: rgba(255, 255, 255, 0.8);
      --glass-border: rgba(0, 0, 0, 0.08);
      --shadow-lux: 0 20px 40px rgba(0, 0, 0, 0.06);
      --ease: cubic-bezier(.22, 1, .36, 1);
      --nav-bg: rgba(250, 250, 250, 0.85);
      --nav-scrolled: rgba(250, 250, 250, 0.98);
      --overlay-gradient: linear-gradient(180deg, transparent 35%, rgba(18, 18, 18, 0.85) 100%);
      --text-overlay: #FFFFFF;
    }

    [data-theme="dark"] {
      --bg-primary: #0a0a0a;
      --bg-secondary: #121212;
      --gold: #D4AF37;
      --gold-soft: #E8CE7B;
      --text: #F8FAFC;
      --muted: #94A3B8;
      --card-bg: rgba(255, 255, 255, 0.03);
      --glass-border: rgba(255, 255, 255, 0.08);
      --shadow-lux: 0 20px 60px rgba(0, 0, 0, 0.4);
      --nav-bg: rgba(10, 10, 10, 0.7);
      --nav-scrolled: rgba(10, 10, 10, 0.98);
      --overlay-gradient: linear-gradient(180deg, transparent 35%, rgba(10, 10, 10, 0.95) 100%);
      --text-overlay: #FFFFFF;
    }"""
content = re.sub(r':root\s*\{[^}]*\}', new_root, content)

# 2. Update Nav Backgrounds
content = re.sub(r'background:\s*rgba\(11,\s*18,\s*32,\s*0\.55\);', 'background: var(--nav-bg);', content)
content = re.sub(r'background:\s*rgba\(11,\s*18,\s*32,\s*0\.85\);', 'background: var(--nav-scrolled);', content)

# 3. Update Nav Toggle button style in JS
content = re.sub(r"menu\.style\.cssText = 'display:flex;flex-direction:column;position:fixed;top:68px;left:0;right:0;background:rgba\(11,18,32,0\.97\);",
                 "menu.style.cssText = 'display:flex;flex-direction:column;position:fixed;top:68px;left:0;right:0;background:var(--nav-scrolled);", content)

# 4. Add Theme Toggle to Nav HTML
nav_html_old = """    <a href="#bestsellers" class="nav-cta">Shop Now</a>
    <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>"""
nav_html_new = """    <div style="display:flex; align-items:center; gap:20px;">
      <button id="theme-toggle" aria-label="Toggle Theme" style="background:none; border:none; cursor:pointer; color:var(--text); font-size:1.2rem; transition: transform 0.3s ease;">
        <svg id="theme-icon-moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        <svg id="theme-icon-sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
      </button>
      <a href="#bestsellers" class="nav-cta">Shop Now</a>
      <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>"""
content = content.replace(nav_html_old, nav_html_new)

# 5. Overlays (Use var(--overlay-gradient) and var(--text-overlay))
content = re.sub(r'background:\s*linear-gradient\(180deg,\s*transparent\s*35%,\s*rgba\(11,\s*18,\s*32,\s*0\.95\)\s*100%\);', 'background: var(--overlay-gradient);', content)
content = re.sub(r'background:\s*linear-gradient\(180deg,\s*transparent\s*50%,\s*rgba\(11,\s*18,\s*32,\s*0\.9\)\s*100%\);', 'background: var(--overlay-gradient);', content)
content = content.replace('.collection-label h3 {\n      font-size: 1.9rem;\n      color: var(--text);\n      margin-bottom: 14px;\n    }', '.collection-label h3 {\n      font-size: 1.9rem;\n      color: var(--text-overlay);\n      margin-bottom: 14px;\n    }')
content = content.replace('color: var(--gold-soft);', 'color: var(--text-overlay);') # for look-overlay span and hero eyebrow
# let's be careful with hero eyebrow
content = content.replace('.hero-eyebrow {\n      font-size: 0.72rem;\n      letter-spacing: 6px;\n      text-transform: uppercase;\n      color: var(--text-overlay);', '.hero-eyebrow {\n      font-size: 0.72rem;\n      letter-spacing: 6px;\n      text-transform: uppercase;\n      color: var(--gold);')

content = content.replace('color: var(--text-overlay);\n      font-weight: 600;\n      opacity: 0;\n      transform: translateY(8px);\n      transition: all 0.4s var(--ease);\n    }', 'color: var(--text-overlay);\n      font-weight: 600;\n      opacity: 0;\n      transform: translateY(8px);\n      transition: all 0.4s var(--ease);\n    }')


# 6. Refine Hero BG
new_hero_bg = """    .hero-bg {
      position: absolute;
      inset: 0;
      background: var(--bg-primary);
      background-image: radial-gradient(circle at 70% 30%, rgba(197, 160, 89, 0.05) 0%, transparent 50%);
      transform: scale(1.05);
      animation: heroZoom 20s ease-out forwards;
    }"""
content = re.sub(r'\.hero-bg\s*\{[^}]*\}', new_hero_bg, content)


# 7. Add JS for Theme Toggling
js_add = """
    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    const iconMoon = document.getElementById('theme-icon-moon');
    const iconSun = document.getElementById('theme-icon-sun');

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      iconMoon.style.display = 'none';
      iconSun.style.display = 'block';
    } else {
      iconMoon.style.display = 'block';
      iconSun.style.display = 'none';
    }

    themeToggle.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        iconMoon.style.display = 'block';
        iconSun.style.display = 'none';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        iconMoon.style.display = 'none';
        iconSun.style.display = 'block';
      }
      themeToggle.style.transform = 'scale(0.9)';
      setTimeout(() => themeToggle.style.transform = 'scale(1)', 150);
    });
"""
content = content.replace('// Sticky navbar state', js_add + '\n    // Sticky navbar state')

# 8. Minor Text color adjustments in forms and other inputs
content = re.sub(r'color:\s*rgba\(148,\s*163,\s*184,\s*0\.45\);', 'color: var(--muted); opacity: 0.6;', content)
content = re.sub(r'color:\s*rgba\(148,\s*163,\s*184,\s*0\.4\);', 'color: var(--muted); opacity: 0.6;', content)

# Fix quick view button background to use nav-bg
content = re.sub(r'background:\s*rgba\(11,\s*18,\s*32,\s*0\.85\);', 'background: var(--nav-scrolled);', content)

# ensure scroll indicator uses var(--text)
content = content.replace('background: var(--text);', 'background: var(--text);')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
