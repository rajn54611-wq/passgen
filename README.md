Passgen

A simple password generator and strength checker written in Python. No extra packages needed.

Features

•Cryptographically secure passwords (uses Python's secrets module)
•Strength rating (Weak, Medium, Strong, Very Strong) with entropy in bits
•Improvement tips for weak passwords
•Interactive menu or command-line options

Install

git clone https://github.com/rajn54611-wq/passgen.git
cd passgen

Usage 
Inetractive menu:

python passgen.py

Command line:

python passgen.py -l 20             # 20-character password
python passgen.py -l 12 -c 5        # five 12-character passwords
python passgen.py --no-symbols      # letters and digits only
python passgen.py -k "MyPass123"    # check a password's strength 

Options

Option           Description
-l, --length     Password length (8-128, default 16)

-c, --count      Number of passwords

--no-symbols     Exclude symbols

--no-digits      Exclude digits

--no-upper       Exclude uppercase

-k, --check      Check the strength of a password

License
MIT
