# Release Upload Checklist — BDP-insight v0.1.1

## Local validation

```bash
python tools/check_release_ready.py
python example_run.py
python example_interactive.py
python -m build
```

## Import validation from another folder

```python
from bdp_insight.api import BDPHodgeConfig, check_rapidapi_config

config = BDPHodgeConfig(
    rapidapi_url="https://bdp-insight-l2.p.rapidapi.com/v1/hodge/convert",
    rapidapi_host="bdp-insight-l2.p.rapidapi.com",
    rapidapi_key="YOUR_RAPIDAPI_KEY",
)

print(check_rapidapi_config(config))
```

## API Hub

- [ ] Short description pasted
- [ ] Long description pasted
- [ ] `POST /v1/hodge/convert` documented with `text/replacement/target_regex/mode`
- [ ] Do not describe direct endpoint as remote full-model generation
- [ ] Customer-facing docs mention only X-RapidAPI-Key and X-RapidAPI-Host
- [ ] Provider-side secrets are not shown in customer docs
- [ ] Health check `/health` succeeds
- [ ] Pricing/quota restored from test values

## GitHub

- [ ] Upload source package or repository contents
- [ ] Add release tag `v0.1.1`
- [ ] Attach wheel/sdist if desired
- [ ] README matches current package
- [ ] No generated results, keys, provider secrets, or server kernel files

## Hugging Face

- [ ] Use `HUGGINGFACE_README_v0_1_1.md` as repo README
- [ ] Upload public docs/package only
- [ ] Do not upload raw secrets, server kernel, generated results, or private test logs

## PyPI/TestPyPI later

- [ ] Verify clean venv install
- [ ] Verify wheel install from `dist/*.whl`
- [ ] Consider TestPyPI first
