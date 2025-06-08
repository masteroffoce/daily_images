#!/usr/bin/env bash

xdg-open $( python scrape.py | python choose_holiday.py | python extract_search_terms.py | python api_get_adress.py  )
