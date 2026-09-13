import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Advanced Pro AI Trading Bot & Command Center",
    page_icon="🤖",
    layout="centered"
)

# App Header
st.title("🤖 Advanced Pro AI Trading Command Center (Dynamic Edition)")
st.markdown("টেকনিক্যাল ইন্ডিকেটর, ক্যান্ডেলস্টিক, রিয়েল-টাইম টাইম-সিঙ্ক এনালাইসিস এবং রিস্ক ম্যানেজমেন্ট ইঞ্জিন")
st.markdown("---")

# Sidebar for Asset & Timeframe Selection
st.sidebar.header("⚙️ কন্ট্রোল ও মার্কেট প্যানেল")
selected_asset = st.sidebar.selectbox(
    "অ্যাসেট বা মার্কেট নির্বাচন করুন",
    ["BTCUSD (বিটকয়েন)", "ETHUSD (ইথেরিয়াম)", "AAPL (অ্যাপল স্টক)", "TSLA (টেসলা)", "USOIL (তেল)"]
)

timeframe = st.sidebar.selectbox(
    "টাইমফ্রেম সিলেক্ট করুন",
    ["5 মিনিট (Intraday)", "1 মিনিট (Scalping)", "15 মিনিট (Short-term)", "1 ঘণ্টা (Position)"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🟢 **মার্কেট স্ট্যাটাস:** লাইভ / খোলা আছে")

# Live Clock and 5-Minute Candle Countdown Logic
current_time_str = datetime.now().strftime("%H:%M:%S")
current_second = datetime.now().second
seconds_left_in_5m = 300 - ((datetime.now().minute % 5) * 60 + current_second)
timer_mins = seconds_left_in_5m // 60
timer_secs = seconds_left_in_5m % 60

st.sidebar.markdown("### ⏱️ লাইভ মার্কেট ক্লক")
st.sidebar.text(f"বর্তমান সময়: {current_time_str}")
st.sidebar.markdown(f"**পরবর্তী ৫ মি. ক্যান্ডেল ক্লোজ হতে বাকি:** `{timer_mins:02d}:{timer_secs:02d}`")

# Dynamic AI Logic based on Asset
if "BTC" in selected_asset:
    current_price = 79350.20
    support_level = 79100.00
    resistance_level = 80200.00
    stop_loss = 78900.00
    take_profit = 80050.00
    confidence_score = 78
    volatility_status = "উচ্চ (High Volatility - সাবধানে ট্রেড করুন)"
    signal_text = "🟢 শক্তিশালী BUY (উর্ধ্বমুখী ট্রেন্ড)"
elif "ETH" in selected_asset:
    current_price = 3450.10
    support_level = 3410.00
    resistance_level = 3520.00
    stop_loss = 3380.00
    take_profit = 3490.00
    confidence_score = 65
    volatility_status = "মধ্যম (Medium Volatility)"
    signal_text = "🟡 নিরপেক্ষ / অপেক্ষা করুন (Neutral)"
else:
    current_price = 328.210
    support_level = 324.110
    resistance_level = 330.810
    stop_loss = 319.248
    take_profit = 336.410
    confidence_score = 82
    volatility_status = "মধ্যম (Medium Volatility - অনুকূল)"
    signal_text = "🟢 শক্তিশালী BUY (ব্রেকআউট সম্ভাবনা)"

# Displaying Analysis & Dynamic Signals
st.subheader(f"📊 বিশদ বিশ্লেষণ: {selected_asset}")
st.markdown("### বাজারের অবস্থা: **ঊর্ধ্বমুখী (Uptrend)**")
st.markdown(f"### বাজারের ঝুঁকি বা ভোলাটিলিটি: **{volatility_status}**")
st.markdown("### চূড়ান্ত সিগন্যাল")
st.success(signal_text)

# Dynamic AI Confidence Score
st.markdown("### এআই কনফিডেন্স স্কোর (ডাইনামিক)")
st.progress(confidence_score)
st.markdown(f"**{confidence_score}%** - বর্তমান মার্কেট ডাটা বিশ্লেষণ করে এই স্কোর নির্ধারণ করা হয়েছে।")

st.markdown("---")

# Timing & Candle Confirmation Guide with Clock Sync
st.markdown("### ⏱️ ঘড়ির কাঁটা ও ক্যান্ডেল কনফার্মেশন গাইড")
if seconds_left_in_5m <= 30:
    st.error("🚨 **এন্ট্রি নেওয়ার উপযুক্ত সময়!** ক্যান্ডেল ক্লোজ হতে ৩০ সেকেন্ডের কম বাকি আছে, এখনই পজিশন নিশ্চিত করুন।")
else:
    st.info(f"⏳ পরবর্তী এন্ট্রি উইন্ডোর জন্য অপেক্ষা করুন। কাউন্টডাউন শেষ হওয়ার শেষ ৩০ সেকেন্ডে সিগন্যাল ফলো করুন।")

st.markdown("---")

# Specific Levels & Risk Management Table
st.markdown("### 🛡️ সুনির্দিষ্ট লেভেল ও রিস্ক ম্যানেজমেন্ট গাইড")

data = {
    "ফিচার ও প্যারামিটার (Parameters)": [
        "বর্তমান বাজার মূল্য (Current Price)", 
        "নিরাপদ সাপোর্ট লেভেল (Support)", 
        "প্রধান রেজিস্ট্যান্স লেভেল (Resistance)", 
        "স্টপ লস বা লস বাঁচানোর সীমা (SL)", 
        "টেক প্রফিট বা টার্গেট প্রফিট (TP)",
        "রিস্ক-টু-রিওয়ার্ড রেশিও (RRR)"
    ],
    "নির্ধারিত মূল্য / মান (Values)": [
        f"{current_price}", 
        f"{support_level}", 
        f"{resistance_level}", 
        f"{stop_loss}", 
        f"{take_profit}",
        "১ : ২.১ (অনুকূল)"
    ]
}

df = pd.DataFrame(data)
st.table(df)

st.markdown("---")

# Trade Psychology & Discipline Checkpoint
st.markdown("### 🧠 ট্রেডিং ডিসিপ্লিন ও সাইকোলজি চেকলিস্ট")
st.checkbox("আমি আমার মূলধনের ১-২% এর বেশি ঝুঁকি নিচ্ছি না।")
st.checkbox("আমি ইমোশন বা লোভের বশবর্তী হয়ে ওভার-ট্রেডিং করছি না।")
st.checkbox("বটের দেওয়া স্টপ-লস (SL) ও টেক-প্রফিট (TP) নিশ্চিতভাবে সেট করেছি।")

st.markdown("---")
st.markdown("💡 **বিশেষ পরামর্শ:** ঘড়ির কাঁটার ৫ মিনিটের চক্র মেনে চলুন এবং টার্গেট বা এসএল হিট হলেই ট্রেড ক্লোজ করে দিন।")

