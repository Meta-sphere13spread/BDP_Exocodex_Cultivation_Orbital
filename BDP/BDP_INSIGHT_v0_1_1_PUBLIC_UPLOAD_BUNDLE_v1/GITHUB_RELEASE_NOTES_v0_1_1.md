# GitHub Release Notes — BDP-insight L2 HodgeConverter v0.1.1

## Release

`v0.1.1` public prototype.

## What is included

- Python-first integration API: `bdp_insight.api`
- Root-level minimal example: `example_run.py`
- Interactive example with optional dashboards: `example_interactive.py`
- API Hub / Modal direct smoke test: `examples/example_direct_api.py`
- Optional Gemma-style compatibility example: `examples/example_gemma.py`
- Dynamic debugger dashboard launcher
- Static Studio / IRS-DCE capture support
- Release readiness checker: `tools/check_release_ready.py`

## Core claim

BDP-insight L2 HodgeConverter is a controlled output-prefix intervention prototype. It is not ordinary prompt rewriting. The original user prompt remains unchanged; the debugger observes partial assistant output, sends a selected target span to the server-bound Hodge kernel, and resumes continuation from the patched prefix.

## Caveats

- Prototype-level research/debugging tool.
- Not guaranteed reasoning correction.
- Not universal arithmetic improvement.
- Not proof of tensor causality.
- Results depend on model, language, prompt format, target regex, wait timing, and continuation length.

## Install

```bash
pip install -e .
pip install -e ".[hf,studio]"
```

## Quick Start

```bash
python example_run.py
python example_interactive.py
```

## Release checks

```bash
python tools/check_release_ready.py
```
