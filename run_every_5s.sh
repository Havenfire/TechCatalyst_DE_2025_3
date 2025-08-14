#!/bin/bash
source dev1/bin/activate
for i in {1..5}
do
    
    python /workspaces/TechCatalyst_DE_2025_3/cron.py
    sleep 5
done