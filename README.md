# weather_man

Virtual Environment

sudo apt update
sudo apt install python3-venv
rm -rf .env
python3 -m venv .env
ls -l .env/bin
source .env/bin/activate

python src/main.py weatherfiles -e 2004
python src/main.py weatherfiles -c 2004/6
python src/main.py weatherfiles -a 2004/6