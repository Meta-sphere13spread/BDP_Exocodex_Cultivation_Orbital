<!--
  GitHub repo top-level README for BDP Exocodex Cultivation Orbital.
  Drop this file at the repo root as 'README.md'.
  Pair it with the LICENSE file produced alongside this build.
-->

<p align="left">
  <a href="https://pypi.org/project/bdp-insight/0.1.1/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bdp-insight.svg?label=pypi"></a>
  <img alt="Python" src="https://img.shields.io/pypi/pyversions/bdp-insight.svg">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
  <img alt="Status" src="https://img.shields.io/badge/status-prototype-orange.svg">
  <a href="https://rapidapi.com/Metasphere13spread/api/bdp-insight-l2"><img alt="RapidAPI" src="https://img.shields.io/badge/RapidAPI-listing-blue.svg"></a>
</p>

# BDP Exocodex Cultivation Orbital / BDP-insight L2 HodgeConverter

**Mid-generation reasoning intervention probe for closed-source reasoning models.**
**Patch a chain-of-thought step, then observe what the model does next.**

**BDP Exocodex Cultivation Orbital / BDP-insight L2 HodgeConverter** is the public research and prototype release space for the BDP / Meta-13 line of runtime debugging, intervention-aware MRI, and LLM behavior analysis tools.

This repository currently publishes the first public BDP-insight prototype:

```text
BDP-insight L2 HodgeConverter v0.1.1
```

BDP-insight L2 HodgeConverter is a controlled output-prefix intervention prototype for LLM runtime debugging experiments.

It is **not** ordinary prompt rewriting. In the full debugger workflow the original user prompt remains unchanged. A local model begins generation, the debugger observes partial assistant output, a selected target span is sent to the server-bound Hodge kernel, and continuation resumes from the patched prefix.

It is also **not** hidden-state intervention (Pyvene / TransformerLens / nnsight require model weights). L2 operates on the **token surface**, so it works with closed-source models reachable only through their generation API.

This release is a prototype-level research and debugging tool.

---

## What's already validated (v0.1.1)

The current release ships with **29 documented experiments** preserved verbatim in an 11-sheet workbook:

| Aspect | Coverage |
|---|---|
| Test models | Qwen/Qwen2.5-0.5B-Instruct (baseline, 25 records) + Gemma4-4ae ~7B effective (cross-model compatibility, 4 records) |
| Input languages | Korean and English prompts both tested |
| Categories | arithmetic (11) · mid-value substitution (5) · reasoning (5) · word-problem math (4) · cross-model compat (4) |
| Documentation | 17-page User Guide PDF · 11-sheet Workbook · QUICK_START · API Hub description · CHANGELOG |

Cross-model evidence is consistent with the **Token-Surface Conversion Hypothesis (H1)** — an observational note (not a theorem) that the L2 intervention surface widens for models that emit more structured intermediate scaffolding (problem analysis -> setup -> equation -> computation -> answer). This is what makes reasoning models (o-series, Claude extended thinking, R1-style, QwQ-style) particularly amenable to token-surface intervention.

Full results, including 11 recommended public demo cases and the four Gemma cross-model records (EXP-GEMMA-01..04), are in the workbook under `BDP/BDP_L2_HodgeConverter_v0_1_1_Note/`.

---

## Current public prototype

### BDP-insight L2 HodgeConverter v0.1.1

The current public release lives here:

```text
BDP/
└── BDP_INSIGHT_v0_1_1_PUBLIC_UPLOAD_BUNDLE_v1/
    ├── dist/
    │   ├── bdp_insight-0.1.1-py3-none-any.whl
    │   └── bdp_insight-0.1.1.tar.gz
    ├── BDP_INSIGHT_v0_1_1_PUBLIC_RELEASE_CLEANUP_v1_1.zip
    ├── API_HUB_LISTING_v0_1_1.md
    ├── GITHUB_RELEASE_NOTES_v0_1_1.md
    ├── HUGGINGFACE_README_v0_1_1.md
    ├── CLEAN_IMPORT_TEST.py
    ├── UPLOAD_CHECKLIST_v0_1_1.md
    └── SHA256SUMS.txt
```

Additional public notes for the L2 HodgeConverter — including the full English user guide PDF, the 11-sheet experiment workbook, and the Korean reference appendix — are stored under:

```text
BDP/
└── BDP_L2_HodgeConverter_v0_1_1_Note/
    ├── README.md
    ├── QUICK_START.md
    ├── API_HUB_DESCRIPTION.md
    ├── CHANGELOG.md
    ├── BDP_L2_HodgeConverter_v0_1_1_User_Guide_EN.pdf       (17 pages)
    ├── BDP_L2_HodgeConverter_v0_1_1_User_Guide_EN.docx
    ├── BDP_L2_HodgeConverter_v0_1_1_Workbook_EN.xlsx        (11 sheets, 29 experiments)
    ├── assets/
    └── kr_appendix/
        └── User_Guide_KR.pdf
```

---

## API access

The BDP-insight L2 HodgeConverter API is available through RapidAPI:

```text
https://rapidapi.com/Metasphere13spread/api/bdp-insight-l2
```

Customers only need the standard RapidAPI client-side headers:

```text
X-RapidAPI-Key
X-RapidAPI-Host
```

No provider-side secrets are required in client code.

### Pricing

| Tier | Price | Quota |
|---|---|---|
| Basic | Free | 20 calls/month — exploration, smoke tests, reading the API shape |
| Pro | $25/month + 100 calls included, $0.30/call over | regular CoT ablation work, 2-3 experiments/month |
| Ultra | $0.25 per call, $200/day cap, no subscription | one-off bursts, paper-scale ablation without monthly commitment |

A typical academic ablation study uses 20-50 calls, well within Pro.

### Direct API smoke-test body

The Hodge conversion endpoint accepts:

```json
{
  "text":          "2 + 4 = 6",
  "replacement":   "9",
  "target_regex":  "(?<=\\+)\\s*\\d+",
  "mode":          "output"
}
```

The direct endpoint performs the prefix conversion only — it does not invoke a model. To see arithmetic answers re-derive (e.g. `2 + 4 = 6` -> `2 + 9 = 11`), use the Python debugger workflow described below.

---

## Python package

The public Python package is on PyPI:

```text
https://pypi.org/project/bdp-insight/0.1.1/
```

Install:

```bash
pip install bdp-insight==0.1.1
```

Hugging Face model examples:

```bash
pip install "bdp-insight[hf]==0.1.1"
```

Optional static Studio dashboard:

```bash
pip install "bdp-insight[hf,studio]==0.1.1"
```

---

## Quick start

After installation:

```bash
bdp-insight-smoke
```

For interactive local model testing:

```bash
bdp-insight-chat
```

Available console commands:

```text
bdp-insight-chat        Interactive chat + optional dashboards
bdp-insight-smoke       API Hub / Modal smoke test
bdp-insight-dashboard   Dynamic debugger dashboard
bdp-insight-static      Static Studio dashboard
```

Inside the interactive chat:

```text
/hodge 9 2 8 32
/max 256
/quit
```

---

## Minimal Python usage

```python
from bdp_insight.api import (
    BDPHodgeConfig,
    attach_hodge_debugger,
    queue_hodge_output_intervention,
)

config = BDPHodgeConfig(
    rapidapi_url="https://bdp-insight-l2.p.rapidapi.com/v1/hodge/convert",
    rapidapi_host="bdp-insight-l2.p.rapidapi.com",
    rapidapi_key="YOUR_RAPIDAPI_KEY",
)

model = attach_hodge_debugger(
    model=model,
    tokenizer=tokenizer,
    config=config,
    model_id="your-model",
    run_dir="results/bdp_hodge_run",
)

queue_hodge_output_intervention(
    run_dir="results/bdp_hodge_run",
    new_word="9",
    target_regex="2",
    wait_tokens=8,
    continuation_tokens=32,
)

# Then call model.generate(...) normally.
```

---

## Designed for

BDP-insight L2 HodgeConverter is designed for:

- **Chain-of-thought (CoT) faithfulness studies** — perturb a single step and measure downstream effect
- **Mid-generation intervention on reasoning models** (o-series, Claude extended thinking, R1-style, QwQ-style) reachable only through their generation API
- **Symbolic redirection and arithmetic-step perturbation** experiments
- **Sleeper-trigger and backdoor ablation** — patch a candidate trigger token and check whether suspicious behavior depends on it
- **Steering vector baselines** — compare hidden-state steering against token-surface intervention on the same task
- Runtime intervention experiments
- Output-prefix patching tutorials
- LLM debugging and observability prototypes
- BDP-insight / Meta-13 style dynamic debugger workflows

This release does not provide:

- No guaranteed reasoning correction
- No universal arithmetic improvement
- No full hidden-state control
- No proof of tensor causality
- No identical behavior across all models or languages

Behavior may vary depending on model, language, prompt format, response template, target regex, wait timing, and continuation length.

---

## Public links

- RapidAPI listing: <https://rapidapi.com/Metasphere13spread/api/bdp-insight-l2>
- PyPI package: <https://pypi.org/project/bdp-insight/0.1.1/>
- GitHub public bundle: <https://github.com/Meta-sphere13spread/BDP_Exocodex_Cultivation_Orbital/tree/main/BDP/BDP_INSIGHT_v0_1_1_PUBLIC_UPLOAD_BUNDLE_v1>
- Hugging Face public bundle: <https://huggingface.co/meta13sphere/BDP_Exocodex_Cultivation_Orbital/tree/main/BDP/BDP_INSIGHT_v0_1_1_PUBLIC_UPLOAD_BUNDLE_v1>

---

## License

This project is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for the full text. The same MIT license applies to both the GitHub and Hugging Face mirrors of this repository.

---

## Status

Current public release:

```text
BDP-insight L2 HodgeConverter v0.1.1
```

Status:

```text
Prototype L2 public release complete.
```

---

## GitHub topics (suggested)

Add the following topics on the repo settings page so users can discover the project via GitHub search and topic browsing. GitHub allows up to 20 topics; the list below is 19 entries that map to the same discoverability surface as the HuggingFace mirror's YAML tags.

```text
llm  debugger  runtime-intervention  output-prefix  mid-generation-intervention
chain-of-thought  cot-faithfulness  causal-probe  interpretability  reasoning-models
token-surface  prototype  research  bdp-insight  meta-13
hodge-converter  rapidapi  qwen  gemma
```
