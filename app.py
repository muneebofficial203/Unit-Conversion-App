import streamlit as st

st.title("🌎 Unit Convertor App By Muneeb")
st.write("🚀 Fast unit conversion for everyone! Creating the project for Quarter 3!")

def convert_unit(value, unit_from, unit_to, category):
    # Temperature conversions require formulas
    if category == "Temperature":
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            return (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            return (value - 32) * 5/9
        elif unit_from == "Celsius" and unit_to == "Kelvin":
            return value + 273.15
        elif unit_from == "Kelvin" and unit_to == "Celsius":
            return value - 273.15
        elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return "Invalid conversion, Try Again!😑"

    # Time conversions: using multiplication factors
    elif category == "Time":
        conversion = {
            "second_minute": 1/60,
            "minute_second": 60,
            "minute_hour": 1/60,
            "hour_minute": 60,
            "hour_day": 1/24,
            "day_hour": 24,
        }
        key = f"{unit_from}_{unit_to}"
        if key in conversion:
            return value * conversion[key]
        else:
            return "Invalid conversion, Try Again!😑"

    # Weight conversions
    elif category == "Weight":
        conversion = {
            "gram_kilogram": 0.001,
            "kilogram_gram": 1000,
            "kilogram_pound": 2.20462,
            "pound_kilogram": 1/2.20462,
        }
        key = f"{unit_from}_{unit_to}"
        if key in conversion:
            return value * conversion[key]
        else:
            return "Invalid conversion, Try Again!😑"
    
    # Length conversions as default example
    else:
        conversion = {
            "meter_kilometer": 0.001,
            "kilometer_meter": 1000,
        }
        key = f"{unit_from}_{unit_to}"
        if key in conversion:
            return value * conversion[key]
        else:
            return "Invalid conversion, Try Again!😑"

# Select the conversion category
category = st.selectbox("Select Category:", ["Length", "Time", "Temperature", "Weight"])

value = st.number_input("Enter the Value:")

# Based on the selected category, display different unit options
if category == "Length":
    unit_from = st.selectbox("Convert From:", ["meter", "kilometer"])
    unit_to   = st.selectbox("Convert To:", ["meter", "kilometer"])
elif category == "Time":
    unit_from = st.selectbox("Convert From:", ["second", "minute", "hour", "day"])
    unit_to   = st.selectbox("Convert To:", ["second", "minute", "hour", "day"])
elif category == "Temperature":
    unit_from = st.selectbox("Convert From:", ["Celsius", "Fahrenheit", "Kelvin"])
    unit_to   = st.selectbox("Convert To:", ["Celsius", "Fahrenheit", "Kelvin"])
elif category == "Weight":
    unit_from = st.selectbox("Convert From:", ["gram", "kilogram", "pound"])
    unit_to   = st.selectbox("Convert To:", ["gram", "kilogram", "pound"])

if st.button("Click me for Conversion 😊"):
    result = convert_unit(value, unit_from, unit_to, category)
    if isinstance(result, str):
        st.write(result)
    else:
        st.write(f"Congratulations! Your converted value: {result} 😍")
