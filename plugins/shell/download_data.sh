#!/bin/bash
api_key=$@

curl -X 'GET' \
  'https://open.api.nexon.com/maplestory/v1/ranking/overall?date=2024-12-10&page=1' \
  -H 'accept: application/json' \
  -H "x-nxopen-api-key: ${api_key}"