# API Hub Listing — BDP-insight L2 HodgeConverter v0.1.1

## Short Description

Controlled output-prefix intervention API for LLM runtime debugging experiments. Prototype-level, observational, not guaranteed reasoning correction.

## Long Description

BDP-insight L2 HodgeConverter exposes a controlled output-prefix intervention path for LLM runtime debugging experiments.

The original user prompt is not rewritten. In the full debugger workflow, a local model begins generation, the debugger observes partial assistant output, a selected target span is sent to the server-bound Hodge kernel, and continuation resumes from the patched prefix.

This API endpoint provides the server-side Hodge conversion component used by that workflow. It is designed for HodgeConverter tutorial reproduction, symbolic redirection experiments, runtime intervention testing, and BDP-insight / Meta-13 debugger prototype analysis.

The prototype is not Qwen-specific. Qwen is used as the baseline public test model, while Gemma-style structured outputs show that models exposing more intermediate scaffolding can provide a wider intervention surface. This is an observational compatibility note, not a guarantee.

This system does not provide guaranteed reasoning correction, universal arithmetic improvement, full hidden-state control, or proof of tensor causality. Behavior varies by model, language, prompt format, target regex, wait timing, and continuation length. Users should reproduce experiments in their own environment.

Privacy notice: prompt/token observations or partial generated output may be transmitted to the paid server-bound kernel for runtime patch preparation. Do not submit secrets, credentials, personal data, private datasets, or confidential production prompts. BDP does not intentionally persist raw prompts or generated text; request payloads are discarded after the operation. Operational logs should be limited to request IDs, timestamps, status, usage counters, lengths, hashes, and plan metadata.

Customers only need X-RapidAPI-Key and X-RapidAPI-Host. No provider-side secrets are required in client code.

## Endpoint

```text
POST /v1/hodge/convert
```

## Direct API Smoke Test Body

```json
{
  "text": "2 + 4 = 6",
  "replacement": "9",
  "target_regex": "(?<=\\+)\\s*\\d+",
  "mode": "output"
}
```

## Python Debugger Workflow

The direct endpoint is a Hodge conversion component. The full output-prefix debugger workflow is demonstrated in the public Python package:

```bash
pip install -e ".[hf,studio]"
python example_run.py
python example_interactive.py
```

## Recommended Tags

```text
llm
debugging
interpretability
runtime-intervention
hodgeconverter
output-prefix
research-prototype
```
