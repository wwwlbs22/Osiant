# Osiant
# Number → Information (Termux / Linux) — Hindi

Yeh project aapko ek number dekar uss number se judi information (name, address, father name, mother name) dikhane, naya record add karne, update karne aur list karne ki suvidha deta hai. Do tarike se chal sakta hai: CLI aur Web UI (Flask).

Requirements
- Python 3
- (Web UI ke liye) Flask

Install (Termux)
1. Termux open karein:
   - `pkg update && pkg upgrade`
   - `pkg install python git`
2. Optional (pip upgrade): `pip install --upgrade pip`

Clone / copy files
- Agar GitHub repo bana liya hai: `git clone https://github.com/<your-user>/<your-repo>.git`
- Ya sidha files ko ek folder me rakhein.

Python environment setup
- (Optional) Virtual environment:
  - `python3 -m venv venv`
  - `source venv/bin/activate`
- Install dependencies:
  - `pip install -r requirements.txt`

CLI Usage
- Lookup: `python3 main.py 101`
- Add new: `python3 main.py --add`
- Update: `python3 main.py --update 101`
- List: `python3 main.py --list`
- Interactive mode: `python3 main.py` (phir prompt par number daalein)

Make CLI executable:
- `chmod +x main.py`
- `./main.py 101`

Web UI (Flask)
- Start server: `python3 app.py`
- Default: http://127.0.0.1:5000
- Termux: `export FLASK_APP=app.py && python3 app.py` (same)
- Web UI features: search by number, add, update, list

Data storage
- Saara data local file `data.json` me store hota hai (simple JSON).

GitHub push quick steps (agar aap local se push karoge)
1. `git init`
2. `git add .`
3. `git commit -m "Initial commit"`
4. Create repo on GitHub (web UI) — phir:
   - `git remote add origin https://github.com/<your-user>/<your-repo>.git`
   - `git branch -M main`
   - `git push -u origin main`

Privacy note
- Real personal data bina permission ke store/share na karein. Yeh example educational purpose ke liye hai.
