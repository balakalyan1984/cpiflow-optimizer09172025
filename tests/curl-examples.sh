#!/usr/bin/env bash
BASE="${BASE:-https://<your-serving-endpoint>}"
TOK="${TOK:-<oauth-token>}"


hdr=(-H "Authorization: Bearer $TOK" -H "Content-Type: application/json")


# greet
curl -sS -H "Authorization: Bearer $TOK" "$BASE/v2/greet" | jq .


# single analyze (artifact only)
curl -sS "${hdr[@]}" -d '{"artifact_name":"PaymentSync","top_k":4}' "$BASE/v2/analyze" | jq .


# many
curl -sS "${hdr[@]}" -d '{"artifact_names":["PaymentSync","DeliveryNote","OrderToCash"],"top_k":4}' "$BASE/v2/analyze_many" | jq .


# all (alpha)
curl -sS -H "Authorization: Bearer $TOK" "$BASE/v2/analyze_all?top_k=4&sort=alpha" | jq .


# predict with full features
curl -sS "${hdr[@]}" -d '{"instances":[{"ARTIFACT_NAME":"OrderToCash","ORIGIN_COMPONENT_NAME":"SOAP","LOG_LEVEL":"INFO"}]}' "$BASE/v2/predict" | jq .