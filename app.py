import streamlit as st


# Set up
st.title("🌟 Unit Converter 🌟")


# Custom CSS for Styling
st.markdown("""
    <style>
        /* Background color */
        .stApp {
            background-color:rgb(53, 90, 71);
        }

        /* Top navigation bar color */
        header[data-testid="stHeader"] {
            background-color:rgb(52, 74, 49); 
        }

        @media (prefers-color-scheme: light) {
            /* background color */
            .stApp {
                background-color:rgb(184, 211, 152);
            }

            /* Top navigation bar color */
            header[data-testid="stHeader"] {
                background-color:rgb(184, 211, 152); 
            }

            .stAlert {
                background-color: rgb(162, 201, 111);
            }
        }
    </style>
""", unsafe_allow_html=True)


# Conversion Types
conversion_type = st.selectbox("Select Conversion Type:", [
    "Length", "Weight (Mass)", "Temperature", "Time", "Speed (Velocity)", "Area", "Volume", 
    "Acceleration", "Force", "Pressure", "Energy", "Power", "Electric Current", 
    "Charge", "Voltage", "Resistance", "Frequency", "Density", "Amount of Substance", "Luminous Intensity"
])


# Input Field
value = st.number_input("Enter Value:", format="%.4f")


# Conversion Dictionary
unit_dict = {
    "Length": {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, 
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    },
    "Weight (Mass)": {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274, "Tons": 0.001
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Time": {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
    },
    "Speed (Velocity)": {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384
    },
    "Area": {
        "Square meters": 1, "Square kilometers": 0.000001, "Square centimeters": 10000, 
        "Square inches": 1550.0031, "Square feet": 10.7639, "Acres": 0.000247105
    },
    "Volume": {
        "Cubic meters": 1, "Liters": 1000, "Milliliters": 1000000, "Cubic inches": 61023.7, 
        "Cubic feet": 35.3147, "Gallons": 264.172
    },
    "Acceleration": {
        "Meters per second²": 1, "Kilometers per hour²": 12960, "Feet per second²": 3.28084, "G-force": 0.101972
    },
    "Force": {
        "Newtons": 1, "Kilonewtons": 0.001, "Pound-force": 0.224809, "Dynes": 100000
    },
    "Pressure": {
        "Pascals": 1, "Kilopascals": 0.001, "Bars": 0.00001, "Atmospheres": 0.00000986923, "PSI": 0.000145038
    },
    "Energy": {
        "Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilowatt-hours": 0.000000277778, "Electronvolts": 6.242e+18
    },
    "Power": {
        "Watts": 1, "Kilowatts": 0.001, "Horsepower": 0.00134102, "BTU per hour": 3.41214
    },
    "Electric Current": {
        "Amperes": 1, "Milliamperes": 1000, "Kiloamperes": 0.001
    },
    "Charge": {
        "Coulombs": 1, "MilliCoulombs": 1000, "MicroCoulombs": 1000000
    },
    "Voltage": {
        "Volts": 1, "Millivolts": 1000, "Kilovolts": 0.001
    },
    "Resistance": {
        "Ohms": 1, "Milliohms": 1000, "Kiloohms": 0.001, "Megaohms": 0.000001
    },
    "Frequency": {
        "Hertz": 1, "Kilohertz": 0.001, "Megahertz": 0.000001, "Gigahertz": 0.000000001
    },
    "Density": {
        "Kilograms per cubic meter": 1, "Grams per cubic centimeter": 0.001, "Pounds per cubic foot": 0.06242796
    },
    "Amount of Substance": {
        "Moles": 1, "Millimoles": 1000
    },
    "Luminous Intensity": {
        "Candelas": 1, "Lumens": 12.57
    }
}


# Dropdowns for Units
from_unit = st.selectbox("From:", list(unit_dict[conversion_type].keys()))
to_unit = st.selectbox("To:", list(unit_dict[conversion_type].keys()))


# Conversion Logic
def convert(value, from_unit, to_unit):
    if conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit case
    else:
        return value * (unit_dict[conversion_type][to_unit] / unit_dict[conversion_type][from_unit])


# Convert Button
if st.button("Convert"):
    result = convert(value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.4f} {to_unit}")


# Footer
st.success(f"Thank you for using this app! 💖")
st.success(f"Made by Palwasha 💗✨ ")

