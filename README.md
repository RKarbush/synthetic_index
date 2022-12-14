# Synthetic Index

- An external data provider sends information on the prices of financial securities, and these are stored on a database by an automatic process. Occasionally, the prices received correspond to a date that is already on the database; in these cases, it is assumed that the latest price is always the correct one. For the purposes of this exercise, you are free to simulate the reception of the data in any way you see fit.

- A synthetic index is an aggregate of some underlying securities; each security is assigned a weight in the index to get the price of the synthetic index for each date, which is calculated according to the formula:

๐๐ก = ๐๐กโ1ร(1 + ๐๐ก), where
๐๐ก: price of the index on date t
๐๐กโ1: price of the index on date t-1, with ๐0 = 100
๐๐ก: return of the index on date t, calculated as follows: ๐
๐ ๐ก = โ ๐ค ๐ ร ๐ ๐๐ก , w h e r e : ๐=1
๐ค๐: weight of each underlying security
๐๐๐ก: return of each underlying security on date t, calculated as follows:
๐๐
 ๐= ๐ก โ1,where:
 ๐๐ ๐กโ1
๐๐ก
๐๐๐ก: price of the underlying security i on date t
๐๐ : price of the underlying security i on date t-1 ๐กโ1

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
