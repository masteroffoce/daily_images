#!/usr/bin/env bash

xdg-open $(  echo $1 | python extract_search_terms.py | python api_get_adress.py  )
