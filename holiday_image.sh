#!/usr/bin/env bash

LANG=en_us_88591
xdg-open $( python scrape.py $(date +'%B_%d') | python choose_holiday.py | python extract_search_terms.py | python api_get_adress.py  )
