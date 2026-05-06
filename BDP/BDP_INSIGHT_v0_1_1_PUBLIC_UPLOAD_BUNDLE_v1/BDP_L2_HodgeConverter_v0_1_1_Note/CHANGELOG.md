# Changelog

All notable changes to the `BDP-insight-L2` HodgeConverter public package.
Round labels (R1 / R2 / R3 / R4 / R5) are kept here only — public titles use `v0.1.1 Public Prototype — English Edition`. 

## API Hub deployment polish (R5) — 2026-05-06

Final pre-deployment polish. No experiment data, EXP IDs, avoid-claim wording, KR appendix, or workbook content was changed.

**Changed**
- `QUICK_START.md` rewritten as two clearly separated sections:
  - **Section A — Direct API Hub smoke test** with the actual Hodge conversion endpoint body shape: `text` / `replacement` / `target_regex` / `mode`.
  - **Section B — Python debugger integration** keeps the `prompt` / `new_word` / `target_regex` / `wait_tokens` / `continuation_tokens` debugger configuration — these belong to the local debugger, not to the direct API.
- Public-facing customer documentation no longer mentions `X-RapidAPI-Proxy-Secret` at all. The `README.md` credential section now reads simply: customers only need `X-RapidAPI-Key` and `X-RapidAPI-Host`; no provider-side secrets are required in client code.
- `API_HUB_DESCRIPTION.md` Short and Long descriptions updated to the API-Hub-ready wording. Added a `Direct API example (smoke test)` block with the correct schema and expected conceptual results (`2 + 4 = 6` → `2 + 9 = 6`, and the shorter `2 + 4` → `2 + 9` variant).
- Build verification (`build_zip_en.py`) tightened: customer-facing docs (`README.md`, `QUICK_START.md`, `API_HUB_DESCRIPTION.md`) MUST contain zero occurrences of `X-RapidAPI-Proxy-Secret`. Build fails otherwise.

**Preserved (no regression)**
- All 29 experiment IDs unchanged.
- All four avoid-claim phrases still prohibited.
- KR appendix unchanged.
- User Guide PDF/DOCX, Workbook, logo, all unchanged.

## English Edition (R4) — 2026-05-06

English-only public package for API Hub / GitHub distribution.

**Added**
- English-only `README.md`, `User_Guide_EN.pdf` / `.docx`, `Workbook_EN.xlsx` (11 sheets).
- `QUICK_START.md`, `API_HUB_DESCRIPTION.md`, this `CHANGELOG.md`.
- User Guide §3.2 *API credentials — customer vs provider* (provider-only marker; this internal-facing section remains in the User Guide PDF for future internal/provider documentation).
- `kr_appendix/User_Guide_KR.pdf` — Korean reference PDF as appendix only.

**Changed**
- Public title is now `v0.1.1 Public Prototype — English Edition`. Round labels removed from titles.
- Token-Surface Conversion Hypothesis (H1) wording softened: the hypothesis concerns the *share* of reasoning that surfaces as tokens, not parameter count. The phrasing 'larger model = wider surface' is replaced with 'more structured intermediate output exposes a wider intervention surface'.

**Preserved (no regression)**
- All 29 experiment IDs (EXP-A01 … EXP-D05, EXP-B03-R1, EXP-GEMMA-01 … 04).
- All four avoid-claim phrases remain prohibited.
- Korean experiment Before/After cells preserved verbatim (raw experiment data).

## Cross-model update (R3 internal) — 2026-05-05

Bilingual (KR/EN) update with logo and API Hub listing. Internal-only intermediate state.
- Added `BDP-insight-L2` API name throughout.
- Added bilingual headers and inline English translations.
- Added IMPORTANT NOTICE box and API Hub Listing box on the cover.
- Added BDP-insight whitebox MRI logo on cover and README.

## Cross-model update (R2 internal) — 2026-05-05

Cross-model compatibility records.
- Added 4 Gemma4-4ae records (EXP-GEMMA-01 … 04).
- New `Cross_Model_Compat` workbook sheet.
- Added behavior classes 7.1–7.4 (cross-model observational).
- Stated Token-Surface Conversion as a hypothesis.
- 5 new glossary entries.

## Initial release (R1 internal) — 2026-05-05

Initial public-prototype packaging.
- 25 Qwen experiments preserved verbatim.
- 10-sheet Korean workbook + 12-section Korean User Guide PDF.
- HOW_IT_WAS_PREPARED documentation.
