---
target: mock-desafios.html
total_score: 26
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\solae\\Documents\\TPI\\mock-ui-tpi\\mock-desafios.html"
target_fingerprint: "sha256:7d5e7de79098cfde3d6f330afd3ca38ca77b4964cd3fb727efe85da186aa0e82"
target_path: "C:\\Users\\solae\\Documents\\TPI\\mock-ui-tpi\\mock-desafios.html"
timestamp: 2026-10-01T21-58-37Z
slug: mock-desafios-html
---
Method: dual-agent (A: a85274ae-8f7d-48cd-880c-1f5d3b674c1e · B: eef5ca91-cf4e-4698-bb5d-a4231b030553)

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Good; most operations give clear feedback |
| 2 | Match System / Real World | 3 | Mostly natural; but admin uses "DLQ" jargon |
| 3 | User Control and Freedom | 3 | Good control |
| 4 | Consistency and Standards | 3 | Mostly consistent |
| 5 | Error Prevention | 3 | Good prevention |
| 6 | Recognition Rather Than Recall | 3 | Good recognition |
| 7 | Flexibility and Efficiency | 2 | Rigid constraints (cannot pause time) |
| 8 | Aesthetic and Minimalist Design | 3 | Focused design |
| 9 | Error Recovery | 2 | No reassurance for technical drops |
| 10 | Help and Documentation | 1 | Missing help for complex workflows |
| **Total** | | **26/40** | **Acceptable** |

#### Design Specificity Verdict

**LLM assessment**: The design is highly specific and grounded in its product intent as a gamified learning platform. The "Arcade" theme, student HUD (lives, coins, streak), and retro typography give it a distinct, authored character rather than a generic template feel.
**Deterministic scan**: The detector found 20 items. 16 were false positives (cramped padding in scrollable wrappers and dialogs, and a decorative mockbar stripe). However, it correctly flagged real issues: 5 WCAG AA contrast violations on danger/accent badges, 1 undersized functional text (10px cohort badge), 1 layout-thrashing animation (`transition: width` on progress bars), and a "dark-glow" effect that, while thematic, could be sharpened to a hard-edged retro shadow.
**Visual overlays**: No reliable user-visible overlay is available (browser automation skipped).

#### Overall Impression
The gamified foundation is very strong and successfully establishes the dual Arcade/Normal worlds. However, it currently leans too hard into rigid game constraints without enough safety nets or contextual help for real-world academic use, and has some accessibility/performance gaps under the hood.

#### What's Working
1. **Thematic Consistency:** The gamification (lives, HUD, retro aesthetic) is deeply integrated into the structural layout and user flows.
2. **Reward Mechanisms:** The feedback loop on challenge completion effectively builds positive reinforcement.

#### Priority Issues

- **[P1] Rigid Challenge Constraints**:
  - **Why it matters**: "No podrás pausar el tiempo" is punitive and ignores real-world interruptions (e.g. lost connection).
  - **Fix**: Allow pausing with a penalty, or implement auto-save state recovery.
  - **Suggested command**: `/impeccable shape`
- **[P1] Accessibility & Contrast**:
  - **Why it matters**: 5 WCAG AA contrast failures (e.g. white text on red danger badges) and 10px functional text make the UI illegible for users with visual impairments.
  - **Fix**: Adjust `--accent-danger-fill` and purple accents to pass 4.5:1, and bump the cohort badge to 11px+.
  - **Suggested command**: `/impeccable audit`
- **[P2] Missing Help & Guidance**:
  - **Why it matters**: Complex workflows like configuring challenge rules lack contextual help.
  - **Fix**: Add inline tooltips or a global help link in the topbar.
  - **Suggested command**: `/impeccable clarify`
- **[P2] Technical Jargon in Admin**:
  - **Why it matters**: "DLQ" and "Dead Letter Queue" in the monitor screen may alienate non-technical professors.
  - **Fix**: Use plainer language like "Cola de errores" or "Eventos fallidos".
  - **Suggested command**: `/impeccable clarify`

#### Persona Red Flags

- **Jordan (First-Timer)**: May feel overwhelmed by the sudden introduction of lives, coins, and streaks without an initial onboarding or explanation of their purpose.
- **Casey (Mobile User)**: Wide tables in "Seguimiento" and "Mis Intentos" will likely require horizontal scrolling or break layout, making it difficult to compare metrics.
- **Sam (Accessibility-Dependent)**: Retro pixel fonts might scale poorly or become illegible for low-vision users. The "Paleta Arcade" dots rely solely on color without clear text labels for selection.

#### Minor Observations
- The "Simular error" checkbox in the mockbar is a nice touch for edge-case testing.
- The `transition: width` on progress bars should be swapped to `transform: scaleX` to avoid layout thrashing.
- The `dark-glow` zero-offset shadow in the arcade skin could be replaced with hard-edged retro offset shadows (`3px 3px 0 var(--accent-primary-fill)`) for a crisper 8-bit look.

#### Questions to Consider
- What if the gamification elements were progressively unlocked rather than overwhelming the user on day one?
- Does the heavy "Arcade" aesthetic risk distracting from the actual focus of reading and writing code?
