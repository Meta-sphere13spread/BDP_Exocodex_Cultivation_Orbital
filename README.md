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

# BDP Exocodex Cultivation Orbital/BDP-insight L2 HodgeConverter

**BDP Exocodex Cultivation Orbital/BDP-insight L2 HodgeConverter** is the public research and prototype release space for the BDP / Meta-13 line of runtime debugging, intervention-aware MRI, and LLM behavior analysis tools.

This repository currently publishes the first public BDP-insight prototype:

```text
BDP-insight L2 HodgeConverter v0.1.1
```

BDP-insight L2 HodgeConverter is a controlled output-prefix intervention prototype for LLM runtime debugging experiments.

It is not ordinary prompt rewriting.
In the full debugger workflow the original user prompt remains unchanged. A local model begins generation, the debugger observes partial assistant output, a selected target span is sent to the server-bound Hodge kernel, and continuation resumes from the patched prefix.

This release is a prototype-level research and debugging tool.

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

Additional public notes for the L2 HodgeConverter are stored under:

```text
BDP/
└── BDP_L2_HodgeConverter_v0_1_1_Note/
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

The direct endpoint performs the prefix conversion only — it does not invoke a model. To see arithmetic answers re-derive (e.g. `2 + 4 = 6` → `2 + 9 = 11`), use the Python debugger workflow described below.

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

## Prototype scope

BDP-insight L2 HodgeConverter is designed for:

- Runtime intervention experiments
- Output-prefix patching tutorials
- Symbolic redirection experiments
- LLM debugging and observability prototypes
- Controlled intervention demonstrations
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

Add the following topics on the repo settings page so users can discover the project via GitHub search and topic browsing:

```text
llm  debugger  runtime-intervention  prototype  research
output-prefix  bdp-insight  meta-13  hodge-converter  rapidapi
```

