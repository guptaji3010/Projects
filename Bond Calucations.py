from fastapi import FastAPI
import uvicorn

# Import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()
print("Please select the following options for the required Calculation:\n"
    "1. Bond price sensitivity to interest rate change\n"
    "2. Yield Spread\n"
    "3. break-even yield\n"
    "4. Bond price\n"
    "5. Two-year spot rate\n"
    "6. Change in yield\n"
    "7. Bond value\n"
    "8. Dollar duration\n"
    "9. Duration gap\n"
    "10. Forward rate\n"
    "11. Forward rate agreement\n"
    "12. Forward rate\n"
    "13. Interest rate sensitivity\n"
    "14. Implied volatility\n"
    "15. Nominal spread\n"
    "16. Present value\n"
    "17. Price-yield\n"
    "18. Z-spread")

a=int(input("Enter the number for required Calculation: "))
if a==1:
    import BPSIR
    result = BPSIR.calculate_bond_price_sensitivity()
elif a==2:
    import Yield_Sprea
    result = Yield_Sprea.get_yield_spread()
elif a==3:
    import BEY
    result = BEY.calculate_break_even_yield()
elif a==4:
    import BPYS
    result = BPYS.calculate_bond_price()
elif a==5:
    import BSMForSR
    result = BSMForSR.calculate_two_year_spot_rate()
elif a==6:
    import BPYC
    result = BPYC.calculate_change_in_yield()
elif a==7:
    import BVDF
    result = BVDF.calculate_bond_value()
elif a==8:
    import DollarDuration
    result = DollarDuration.calculate_dollar_duration()
elif a==9:
    import DurationGap
    result = DurationGap.calculate_duration_gap()
elif a==10:
    import ForwardRate
    result = ForwardRate.calculate_forward_rate()
elif a==11:
    import FRA
    result = FRA.calculate_fra_payment()
elif a==12:
    import FRZCB
    result = FRZCB.calculate_forward_rate()
elif a==13:
    import IRSBP
    result = IRSBP.calculate_and_print_interest_sensitivity()
elif a==14:
    import IVBO
    result = IVBO.calculate_implied_volatility()
elif a==15:
    import N_Spread
    result = N_Spread.calculate_nominal_spread()
elif a==16:
    import PVFR
    result = PVFR.calculate_present_value()
elif a==17:
    import PYBEO
    result = PYBEO.calculate_price_yield()
elif a==18:
    import Z_Spread
    result = Z_Spread.calculate_z_spread()
else:
    print("Invalid Input")
# Define a route
@app.get("/")
async def read_root():

    # Return the result as a JSON response
    return {result}

# Run the application using Uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.5", port=8000)
