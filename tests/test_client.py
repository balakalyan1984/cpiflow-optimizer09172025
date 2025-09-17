import os, requests, json


BASE = os.environ.get("BASE", "https://<your-serving-endpoint>")
TOK = os.environ.get("TOK", "<oauth-token>")
H = {"Authorization": f"Bearer {TOK}", "Content-Type": "application/json"}


print("/v2/greet =>", requests.get(f"{BASE}/v2/greet", headers={"Authorization": H["Authorization"]}).status_code)


r = requests.post(f"{BASE}/v2/analyze", headers=H, data=json.dumps({"artifact_name":"PaymentSync","top_k":4}))
print("/v2/analyze =>", r.status_code, r.text[:200])


r = requests.post(f"{BASE}/v2/analyze_many", headers=H, data=json.dumps({
"artifact_names":["PaymentSync","DeliveryNote","OrderToCash"],
"top_k":4
}))
print("/v2/analyze_many =>", r.status_code, r.text[:200])


r = requests.get(f"{BASE}/v2/analyze_all?top_k=4&sort=alpha", headers={"Authorization": H["Authorization"]})
print("/v2/analyze_all =>", r.status_code, r.text[:200])


r = requests.post(f"{BASE}/v2/predict", headers=H, data=json.dumps({
"instances":[{"ARTIFACT_NAME":"OrderToCash","ORIGIN_COMPONENT_NAME":"SOAP","LOG_LEVEL":"INFO"}]
}))
print("/v2/predict =>", r.status_code, r.text[:200])