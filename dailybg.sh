#!/usr/bin/env bash

LANG=en_us_88591
curl $( python scrape.py $(date -d "+$1 day" +'%B_%d') | python choose_holiday.py | python extract_search_terms.py | python api_get_adress.py ) > ~/backgrounds/$(date -d "+$1 day" +'%Y%m%d')
