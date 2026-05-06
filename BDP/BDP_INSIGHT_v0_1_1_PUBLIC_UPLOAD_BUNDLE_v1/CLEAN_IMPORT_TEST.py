from bdp_insight.api import BDPHodgeConfig, check_rapidapi_config, queue_hodge_output_intervention

config = BDPHodgeConfig(
    rapidapi_url="https://bdp-insight-l2.p.rapidapi.com/v1/hodge/convert",
    rapidapi_host="bdp-insight-l2.p.rapidapi.com",
    rapidapi_key="",
)

print(check_rapidapi_config(config))

cmd_path = queue_hodge_output_intervention(
    run_dir="results/import_test_run",
    new_word="9",
    target_regex="2",
    wait_tokens=8,
    continuation_tokens=32,
)

print("[OK] bdp_insight import works")
print("[queued]", cmd_path)
