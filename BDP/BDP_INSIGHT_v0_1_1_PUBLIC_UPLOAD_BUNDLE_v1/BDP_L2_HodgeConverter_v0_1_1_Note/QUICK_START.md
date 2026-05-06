# Quick Start

`BDP-insight-L2` HodgeConverter — two entry points.

> ⚠ Behavior varies BY MODEL and BY INPUT LANGUAGE. Reproduce in your environment.

This API exposes the **server-side Hodge conversion** component. There are two ways to use it:

- **Section A — Direct API Hub smoke test.** A single HTTP call to the Hodge conversion endpoint. This is what runs against the API Hub *Test Endpoint* button. It does **not** invoke a model — it just performs the prefix-level conversion.
- **Section B — Python debugger integration.** A local model produces a partial output, the debugger watches for the target, calls this API to produce the patched prefix, and resumes generation. The arithmetic answer changes downstream (e.g. `2 + 4 = 6` → `2 + 9 = 11`) only in this flow.

---

## A. Direct API Hub smoke test

Use this to verify connectivity and to learn the request/response shape.

### Headers

```http
X-RapidAPI-Key:  <your customer key>
X-RapidAPI-Host: <listed host>
Content-Type:    application/json
```

### Request body

```json
{
  "text":          "2 + 4 = 6",
  "replacement":   "9",
  "target_regex":  "(?<=\\+)\\s*\\d+",
  "mode":          "output"
}
```

### Field reference

| Field          | Type   | Purpose                                                              |
|----------------|--------|----------------------------------------------------------------------|
| `text`         | string | The partial output (or any string) to convert                        |
| `replacement`  | string | The value that overwrites the matched span                           |
| `target_regex` | string | Regex that pinpoints which span of `text` to patch                   |
| `mode`         | string | `output` for output-prefix intervention (the public L2 path)         |

### Expected conceptual result

```
input  text:  2 + 4 = 6
output text:  2 + 9 = 6
```

Or, with a shorter input that does not pre-state an answer:

```json
{
  "text":          "2 + 4",
  "replacement":   "9",
  "target_regex":  "(?<=\\+)\\s*\\d+",
  "mode":          "output"
}
```

```
input  text:  2 + 4
output text:  2 + 9
```

**Important:** the direct endpoint performs the prefix conversion only. It does not run a downstream model, and therefore the arithmetic answer is not re-derived here. To see the answer change (e.g. `... = 11`), use the Python debugger workflow in Section B.

---

## B. Python debugger integration

This is the full output-prefix intervention loop. A local model is invoked; the debugger calls this API mid-generation to obtain a patched prefix, then resumes the model from the patched prefix.

### Conceptual flow

```
user prompt  (sent to local model — NOT to this API)
  -> model begins generation
  -> partial assistant output appears
  -> debugger watches target_regex on the partial output
  -> debugger calls THIS API to convert the matched span
  -> local debugger resumes generation from the patched prefix
  -> final continuation reflects the mutated prefix
```

### Debugger-side configuration

| Field                  | Value                            | Where it goes                                       |
|------------------------|----------------------------------|-----------------------------------------------------|
| user prompt            | `"What is 2 + 4?"` etc.          | Local model only (not sent to this API)             |
| `new_word`             | `"9"`                            | Passed by the debugger as `replacement` to this API |
| `target_regex`         | `(?<=\+)\s*\d+`                | Used both client-side (watch) and as the API field  |
| `wait_tokens`          | `16`                             | Debugger-only: tokens to wait until target appears  |
| `continuation_tokens`  | `32`                             | Debugger-only: tokens generated after the patch     |

### Pseudocode

```python
# Local debugger pseudocode — illustrative only
queue_hodge_output_intervention(
    new_word="9",
    target_regex=r"(?<=\+)\s*\d+",
    wait_tokens=16,
    continuation_tokens=32,
)
# Internally, when target_regex matches the partial output,
# the debugger sends {text, replacement, target_regex, mode}
# to the Hodge conversion API and resumes the local model
# from the patched prefix.
```

### Expected outcome (debugger flow)

```
partial output:   2 + 4 = 6
after patch:      2 + 9 = 11   (continuation re-derives the answer)
```

The original prompt is not modified. Only the matched span (`4` after `+`) is replaced. The continuation re-derives downstream values from the mutated prefix — this is what makes the final answer change.

---

## 5-stage decision (do not evaluate by final answer alone)

1. **target detection** — did the regex match the partial output?
2. **server patch** — did the Hodge kernel return a patched prefix?
3. **prefix mutation** — did the assistant prefix actually change?
4. **continuation effect** — did the continuation track the mutation?
5. **final answer** — is the final result coherent given the patch?

## Common pitfalls

- **Wrong endpoint expectation** — the direct API Hub endpoint converts the prefix; it does not run a model. To see the arithmetic answer change, use the Python debugger flow.
- **Target not exposed** — model emits only the answer. Use formula-guided wording in the user prompt (debugger flow only).
- **Evaluating only final answer** — apply the 5-stage decomposition.
- **Template pressure** — natural-language templates may reorder operands (see EXP-A02 / A03).
- **Breakpoint too early** — small `wait_tokens` cuts mid-phrase (debugger flow only).
- **Result-token stale tail** — without target-first breakpoint the old answer persists (debugger flow only).
- **Pre-existing distribution clash** — `replacement` / `new_word` equal to a common token can cause re-orderings.

## Customer credentials

Customers only need `X-RapidAPI-Key` and `X-RapidAPI-Host`. No provider-side secrets are required in client code.

## Where to go next

- `BDP_L2_HodgeConverter_v0_1_1_Workbook_EN.xlsx` → `Quick_Start` and `Regex_Recipes` sheets.
- `BDP_L2_HodgeConverter_v0_1_1_User_Guide_EN.pdf` → §4 Quick Start, §6 Key success cases, §11 Cross-model compatibility.
- `API_HUB_DESCRIPTION.md` → text suitable for the API Hub listing field.
