import re

html_path = r"c:\Users\solae\Documents\TPI\mock-ui-tpi\tpi-redesign.html"
css_path = r"c:\Users\solae\Documents\TPI\mock-ui-tpi\css\tokens.css"

html_content = open(html_path, "r", encoding="utf-8").read()

# CSS append content
css_append = """
/* --- Gamer / Arcade (Dark) · Paleta Candy --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='candy'] {
  --bg-app:#121212; --bg-surface:#1a1a1a; --bg-surface-alt:#242424;
  --border-subtle:#333333; --border-highlight:#ff5bbd;
  --text-primary:#ffffff; --text-muted:#a0a0a0;
  --accent-primary:#2de2e6; --accent-primary-fill:#2de2e6; --on-accent-primary:#1a1a1a;
  --accent-secondary:#7c4dff; --accent-secondary-fill:#7c4dff; --on-accent-secondary:#ffffff;
  --accent-gold:#fff0a6; --accent-gold-fill:#fff0a6; --on-accent-gold:#1a1a1a;
  --accent-danger:#ff5bbd; --accent-danger-fill:#ff5bbd; --on-accent-danger:#1a1a1a;
  --accent-success:#2de2e6; --accent-success-fill:#2de2e6; --on-accent-success:#1a1a1a;
  --focus-glow:rgba(45,226,230,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Moody --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='moody'] {
  --bg-app:#050814; --bg-surface:#0b1026; --bg-surface-alt:#161d36;
  --border-subtle:#2b2d42; --border-highlight:#00f5d4;
  --text-primary:#f0f4f8; --text-muted:#8a94a6;
  --accent-primary:#00f5d4; --accent-primary-fill:#00f5d4; --on-accent-primary:#050814;
  --accent-secondary:#9b5de5; --accent-secondary-fill:#9b5de5; --on-accent-secondary:#ffffff;
  --accent-gold:#f15bb5; --accent-gold-fill:#f15bb5; --on-accent-gold:#ffffff;
  --accent-danger:#f15bb5; --accent-danger-fill:#f15bb5; --on-accent-danger:#ffffff;
  --accent-success:#00f5d4; --accent-success-fill:#00f5d4; --on-accent-success:#050814;
  --focus-glow:rgba(0,245,212,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Sunset --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='sunset'] {
  --bg-app:#060a12; --bg-surface:#0b1320; --bg-surface-alt:#162238;
  --border-subtle:#2a3b5c; --border-highlight:#ff9f1c;
  --text-primary:#fdfefe; --text-muted:#9ba4b5;
  --accent-primary:#ff9f1c; --accent-primary-fill:#ff9f1c; --on-accent-primary:#060a12;
  --accent-secondary:#845ec2; --accent-secondary-fill:#845ec2; --on-accent-secondary:#ffffff;
  --accent-gold:#ff9f1c; --accent-gold-fill:#ff9f1c; --on-accent-gold:#060a12;
  --accent-danger:#ff4d6d; --accent-danger-fill:#ff4d6d; --on-accent-danger:#ffffff;
  --accent-success:#2ec4b6; --accent-success-fill:#2ec4b6; --on-accent-success:#060a12;
  --focus-glow:rgba(255,159,28,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Esports --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='esports'] {
  --bg-app:#1f202f; --bg-surface:#2b2d42; --bg-surface-alt:#3f4259;
  --border-subtle:#8d99ae; --border-highlight:#ef233c;
  --text-primary:#edf2f4; --text-muted:#8d99ae;
  --accent-primary:#ef233c; --accent-primary-fill:#ef233c; --on-accent-primary:#ffffff;
  --accent-secondary:#ffb703; --accent-secondary-fill:#ffb703; --on-accent-secondary:#2b2d42;
  --accent-gold:#ffb703; --accent-gold-fill:#ffb703; --on-accent-gold:#2b2d42;
  --accent-danger:#ef233c; --accent-danger-fill:#ef233c; --on-accent-danger:#ffffff;
  --accent-success:#ffb703; --accent-success-fill:#ffb703; --on-accent-success:#2b2d42;
  --focus-glow:rgba(239,35,60,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Sci-fi --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='scifi'] {
  --bg-app:#060d14; --bg-surface:#0d1b2a; --bg-surface-alt:#1b263b;
  --border-subtle:#2c3e50; --border-highlight:#41ead4;
  --text-primary:#e9ecef; --text-muted:#7d8b99;
  --accent-primary:#41ead4; --accent-primary-fill:#41ead4; --on-accent-primary:#060d14;
  --accent-secondary:#c7f9cc; --accent-secondary-fill:#c7f9cc; --on-accent-secondary:#060d14;
  --accent-gold:#c7f9cc; --accent-gold-fill:#c7f9cc; --on-accent-gold:#060d14;
  --accent-danger:#41ead4; --accent-danger-fill:#41ead4; --on-accent-danger:#060d14;
  --accent-success:#41ead4; --accent-success-fill:#41ead4; --on-accent-success:#060d14;
  --focus-glow:rgba(65,234,212,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Flashy --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='flashy'] {
  --bg-app:#050716; --bg-surface:#0b0f2b; --bg-surface-alt:#161b40;
  --border-subtle:#2b86c5; --border-highlight:#ff3cac;
  --text-primary:#ffffff; --text-muted:#8b92b3;
  --accent-primary:#ff3cac; --accent-primary-fill:#ff3cac; --on-accent-primary:#ffffff;
  --accent-secondary:#2b86c5; --accent-secondary-fill:#2b86c5; --on-accent-secondary:#ffffff;
  --accent-gold:#f9f871; --accent-gold-fill:#f9f871; --on-accent-gold:#050716;
  --accent-danger:#ff3cac; --accent-danger-fill:#ff3cac; --on-accent-danger:#ffffff;
  --accent-success:#2b86c5; --accent-success-fill:#2b86c5; --on-accent-success:#ffffff;
  --focus-glow:rgba(255,60,172,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Mystical --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='mystical'] {
  --bg-app:#131429; --bg-surface:#1f2041; --bg-surface-alt:#2f3061;
  --border-subtle:#4b3f72; --border-highlight:#ffc857;
  --text-primary:#e6e8e6; --text-muted:#9293b0;
  --accent-primary:#ffc857; --accent-primary-fill:#ffc857; --on-accent-primary:#131429;
  --accent-secondary:#119da4; --accent-secondary-fill:#119da4; --on-accent-secondary:#131429;
  --accent-gold:#ffc857; --accent-gold-fill:#ffc857; --on-accent-gold:#131429;
  --accent-danger:#4b3f72; --accent-danger-fill:#4b3f72; --on-accent-danger:#ffffff;
  --accent-success:#119da4; --accent-success-fill:#119da4; --on-accent-success:#131429;
  --focus-glow:rgba(255,200,87,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* --- Gamer / Arcade (Dark) · Paleta Urban --- */
:root[data-theme='dark'][data-skin='gamer'][data-palette='urban'] {
  --bg-app:#040710; --bg-surface:#0a0f1f; --bg-surface-alt:#121c36;
  --border-subtle:#1f3c88; --border-highlight:#00bbf9;
  --text-primary:#fef9ef; --text-muted:#8195b8;
  --accent-primary:#00bbf9; --accent-primary-fill:#00bbf9; --on-accent-primary:#040710;
  --accent-secondary:#f15bb5; --accent-secondary-fill:#f15bb5; --on-accent-secondary:#040710;
  --accent-gold:#00bbf9; --accent-gold-fill:#00bbf9; --on-accent-gold:#040710;
  --accent-danger:#f15bb5; --accent-danger-fill:#f15bb5; --on-accent-danger:#040710;
  --accent-success:#00bbf9; --accent-success-fill:#00bbf9; --on-accent-success:#040710;
  --focus-glow:rgba(0,187,249,.55);
  --radius-control:4px; --border-width:2px; --press-y:-2px;
}

/* Dot style override */
.palette-dots { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; background: transparent; padding: 0 !important; }
.palette-dots button {
  width: 28px; height: 28px; border-radius: 50%; border: 2px solid var(--border-subtle, #333);
  cursor: pointer; padding: 0; 
  background: linear-gradient(135deg, var(--c1) 50%, var(--c2) 50%);
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  flex: none; font-size: 0; color: transparent;
}
.palette-dots button:hover { transform: scale(1.1); border-color: #fff; }
.palette-dots button[aria-pressed="true"] {
  border-color: #fff;
  transform: scale(1.15);
  box-shadow: 0 0 0 2px var(--bg-surface), 0 0 0 4px var(--c1);
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + css_append)

new_dots_html = """  <div class="palette-dots" role="group" aria-label="Paleta Arcade">
    <button data-palette-btn="electric" style="--c1:#00e5ff; --c2:#a855f7;" aria-pressed="true" title="Cian Eléctrico y Oro (Recomendada)">⚡ Cian Eléctrico</button>
    <button data-palette-btn="neon" style="--c1:#f275dc; --c2:#29c9e0;" aria-pressed="false" title="Magenta Original (Vaporwave)">🌸 Magenta Original</button>
    <button data-palette-btn="latenight" style="--c1:#4ef3c9; --c2:#ff2e88;" aria-pressed="false" title="Late Night (Alto Contraste)">🌃 Late Night</button>
    <button data-palette-btn="candy" style="--c1:#2de2e6; --c2:#ff5bbd;" aria-pressed="false" title="Candy Bright (Playful & Pop)">Candy Bright</button>
    <button data-palette-btn="moody" style="--c1:#00f5d4; --c2:#9b5de5;" aria-pressed="false" title="Moody Cyber (Adventurous)">Moody Cyber</button>
    <button data-palette-btn="sunset" style="--c1:#ff9f1c; --c2:#ff4d6d;" aria-pressed="false" title="Sunset Sprint (Energetic)">Sunset Sprint</button>
    <button data-palette-btn="esports" style="--c1:#ef233c; --c2:#ffb703;" aria-pressed="false" title="Esports (Intense & Competitive)">Esports</button>
    <button data-palette-btn="scifi" style="--c1:#41ead4; --c2:#c7f9cc;" aria-pressed="false" title="Sci-Fi (Cool & Clean)">Sci-Fi</button>
    <button data-palette-btn="flashy" style="--c1:#ff3cac; --c2:#2b86c5;" aria-pressed="false" title="Flashy (Futuristic)">Flashy</button>
    <button data-palette-btn="mystical" style="--c1:#ffc857; --c2:#119da4;" aria-pressed="false" title="Mystical (Story-driven)">Mystical</button>
    <button data-palette-btn="urban" style="--c1:#00bbf9; --c2:#f15bb5;" aria-pressed="false" title="Urban (Neon-lit)">Urban</button>
  </div>"""

# Replace in Mockbar
old_mockbar_regex = r'<div class="seg" role="group" aria-label="Paleta Arcade">.*?</div>'
html_content = re.sub(old_mockbar_regex, new_dots_html, html_content, count=1, flags=re.DOTALL)

# Replace in Account menu
old_account_regex = r'<div class="seg sm" role="group" aria-label="Paleta Arcade">.*?</div>'
html_content = re.sub(old_account_regex, new_dots_html.replace('class="palette-dots"', 'class="palette-dots sm"'), html_content, count=1, flags=re.DOTALL)


with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
