# Makefile

build:
    docker build -t iris-classification-app .

run:
    docker run -d -p 5000:5000 iris-classification-app

push:
    git add .
    git commit -m "Initial project commit"
    git push origin main
