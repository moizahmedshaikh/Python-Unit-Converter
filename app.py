import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversions = {
        'Meter': 1,
        'Kilometer': 0.001,
        'Centimeter': 100,
        'Millimeter': 1000,
        'Inch': 39.3701,
        'Foot': 3.28084,
        'Yard': 1.09361,
        'Mile': 0.000621371
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1e6,
        'Pound': 2.20462,
        'Ounce': 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'Liter': 1,
        'Milliliter': 1000,
        'Gallon (US)': 0.264172,
        'Gallon (UK)': 0.219969,
        'Quart': 1.05669,
        'Pint': 2.11338,
        'Fluid Ounce': 33.814
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_time(value, from_unit, to_unit):
    conversions = {
        'Second': 1,
        'Minute': 1/60,
        'Hour': 1/3600,
        'Day': 1/86400
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_area(value, from_unit, to_unit):
    conversions = {
        'Square Meter': 1,
        'Square Kilometer': 0.000001,
        'Square Mile': 0.0000003861,
        'Square Yard': 1.19599,
        'Square Foot': 10.7639,
        'Acre': 0.000247105
    }
    return value * conversions[to_unit] / conversions[from_unit]

st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔄", layout="wide")

st.sidebar.title("🔧 Unit Converter")
st.sidebar.markdown("**Fast & Accurate Unit Conversion in Seconds!**")

unit_type = st.sidebar.radio("Select Conversion Type", [
    "📏 Length Converter",
    "⚖️ Weight Converter",
    "🌡️ Temperature Converter",
    "💧 Liquid Converter",
    "⏳ Time Converter",
    "📐 Area Converter"
])

if unit_type == "📏 Length Converter":
    units = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Foot', 'Yard', 'Mile']
    convert_function = convert_length
elif unit_type == "⚖️ Weight Converter":
    units = ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce']
    convert_function = convert_weight
elif unit_type == "🌡️ Temperature Converter":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    convert_function = convert_temperature
elif unit_type == "💧 Liquid Converter":
    units = ['Liter', 'Milliliter', 'Gallon (US)', 'Gallon (UK)', 'Quart', 'Pint', 'Fluid Ounce']
    convert_function = convert_volume
elif unit_type == "⏳ Time Converter":
    units = ['Second', 'Minute', 'Hour', 'Day']
    convert_function = convert_time
elif unit_type == "📐 Area Converter":
    units = ['Square Meter', 'Square Kilometer', 'Square Mile', 'Square Yard', 'Square Foot', 'Acre']
    convert_function = convert_area

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2; font-size: 42px; font-weight: bold;'>
        🔄 Ultimate Unit Converter
    </h1>
    <h3 style='text-align: center; color: #555; font-size: 20px;'>
        Convert Length, Weight, Temperature, Volume, Time & Area Instantly 🚀
    </h3>
    <hr style='border: 2px solid #4A90E2;'>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    value = st.number_input("Enter Value", value=1.0, step=0.1, format="%.2f")
    from_unit = st.selectbox("From", units)
with col3:
    to_unit = st.selectbox("To", units)
    converted_value = ""
    if st.button("Convert Now 🚀"):
        converted_value = convert_function(value, from_unit, to_unit)
        st.success(f"🎯 Converted Value: {converted_value:.4f} {to_unit}")

st.markdown("""
    <style>
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #357ABD;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("---")
st.markdown("<p style='text-align: center;'>🌍 Made By Moiz Ahmed Shaikh</p>", unsafe_allow_html=True)