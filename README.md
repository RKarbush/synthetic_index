# Synthetic Index

- An external data provider sends information on the prices of financial securities, and these are stored on a database by an automatic process. Occasionally, the prices received correspond to a date that is already on the database; in these cases, it is assumed that the latest price is always the correct one. For the purposes of this exercise, you are free to simulate the reception of the data in any way you see fit.

- A synthetic index is an aggregate of some underlying securities; each security is assigned a weight in the index to get the price of the synthetic index for each date, which is calculated according to the formula:

𝑃𝑡 = 𝑃𝑡−1×(1 + 𝑅𝑡), where
𝑃𝑡: price of the index on date t
𝑃𝑡−1: price of the index on date t-1, with 𝑃0 = 100
𝑅𝑡: return of the index on date t, calculated as follows: 𝑛
𝑅 𝑡 = ∑ 𝑤 𝑖 × 𝑟 𝑖𝑡 , w h e r e : 𝑖=1
𝑤𝑖: weight of each underlying security
𝑟𝑖𝑡: return of each underlying security on date t, calculated as follows:
𝑃𝑖
 𝑟= 𝑡 −1,where:
 𝑃𝑖 𝑡−1
𝑖𝑡
𝑃𝑖𝑡: price of the underlying security i on date t
𝑃𝑖 : price of the underlying security i on date t-1 𝑡−1

- The performance of all synthetic indices should be always updated with the latest price; that means that the process should run as soon as a new price is received and perform the calculation.

- The price series of the securities involved typically span several decades.

- The calculation must be implemented in a way that allows both internal processes and third-party applications to have access to the price series.

# USAGE

- In order to use this Web App, download the repository and setup a python environment using virtualenv: https://docs.python.org/es/3/library/venv.html .
- Activate your virtual environment using source venv/bin/activate. (change venv by the name you gave to your virtualenv)
- Install requirements by running: $ pip install -r requirements.txt
- Run server: $ python3 manage.py runserver.

- You can find an xlsx as example in media/Data.xlsx

- If you see some migration warnings, run
 - $ python3 manage.py makemigrations
 - $ python3 manage.py migrate


If you find some problems or need some info, contact me at roman.karbushev@outlook.com
