import datetime
import streamlit as st



st.title('T-Bill Return')

d1 = st.date_input("Acquire Date", datetime.date.today())
d2 = st.date_input("Maturity Date", datetime.date.today())
price = st.number_input("Unit Cost")

if(price > 0 and price < 100 and d2 > d1):

    ndays = (d2 - d1).days
    yld = (100.0 - price )/ price
    ret = yld * 365 / ndays
    st.write(f'The return is {round(ret*100,2)}%, {ndays} days, yield = {yld}')


st.title('Option Return')
st_price = st.number_input("Strike Price")
opt_price = st.number_input("Option Price")
exp_date = st.date_input("Expire Date", datetime.date.today())

if(st_price!=0 and opt_price!=0 and exp_date>datetime.date.today()):

    ndays = (exp_date-datetime.date.today()).days
    yld = opt_price / st_price
    ret = yld * 365 / ndays
    st.write(f'The return is {round(ret*100,2)}%, {ndays} days, yield = {yld}')
