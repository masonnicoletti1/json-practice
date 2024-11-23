#!/bin/bash

DATA="aviation.json"
jq -r '.[].receiptTime' "$DATA" | head -n 6
