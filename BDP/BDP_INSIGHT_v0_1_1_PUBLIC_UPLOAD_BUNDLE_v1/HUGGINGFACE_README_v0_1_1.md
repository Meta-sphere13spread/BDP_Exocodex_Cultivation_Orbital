---
title: BDP-insight L2 HodgeConverter v0.1.1
emoji: 🧪
colorFrom: blue
colorTo: cyan
sdk: static
pinned: false
license: mit
tags:
  - llm
  - interpretability
  - debugging
  - runtime-intervention
  - hodgeconverter
---

# BDP-insight L2 HodgeConverter v0.1.1

Public prototype package for controlled output-prefix intervention experiments.

This repository is intended as a public package/documentation mirror for API Hub users. The full debugger workflow runs locally with a Hugging Face causal language model and calls the API Hub / Modal server-bound Hodge kernel for the selected conversion step.

## Key point

This is not ordinary prompt rewriting. The original user prompt remains unchanged. The debugger observes partial assistant output, patches a selected target span through the server-bound Hodge kernel, and resumes continuation from the patched prefix.

## Quick Start

```bash
pip install -e ".[hf,studio]"
python example_run.py
python example_interactive.py
```

## Required API Hub values

Users need only:

```text
rapidapi_url
rapidapi_host
rapidapi_key
```

No provider-side secrets are required in client code.

## Prototype limitations

This release is observational and prototype-level. It does not guarantee reasoning correction, arithmetic correctness, hidden-state control, or tensor causality.
