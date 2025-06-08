#!/usr/bin/env bash

curl $( python scrape.py | python choose_holiday.py | python extract_search_terms.py | python api_get_adress.py ) > ~/backgrounds/$(date +'%Y%m%d')
