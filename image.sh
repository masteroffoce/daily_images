#!/usr/bin/env bash

xdg-open $(  echo $1 | python ollama.py | python pixabay.py  )
