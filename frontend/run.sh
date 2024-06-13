#!/bin/bash

cd /home/millankumar/code/ProjectArise/frontend
npm i
npm run build
npm run preview -- --port 3002 --host