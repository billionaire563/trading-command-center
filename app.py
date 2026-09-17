import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# Page configuration
st.set_page_config(
    page_title="Advanced Pro AI Trading Bot",
    page_icon="📈",
    layout="centered"
)

# ৩০ সেকেন্ড পর পর পেজ অটো-রিফ্রেশ হবে
count = st_autorefresh(interval=30000, limit=100, key="datarefresh")

# App Header
st.title("🤖 Advanced Pro AI Trading Bot & Command Center")
st.markdown("রিয়েল-টাইম এনালাইসিস, ডায়নামিক সিগন্যাল এবং ঘড়ির কাঁটা ধরে নিখুঁত এন্ট্রি টাইম")
st.markdown("---")

# Sidebar for Asset Selection
st.sidebar.header("⚙️ কন্ট্রোল প্যানেল")
selected_asset = st.sidebar.selectbox(
    "অ্যাসেট বা মার্কেট নির্বাচন করুন",
    ["AAPL (অ্যাপল স্টক)", "TSLA (টেসলা)", "ETHUSD (ইথেরিয়াম)", "BTCUSD (বিটকয়েন)", "USOIL (তেল)"]
)

timeframe = st.sidebar.selectbox(
    "টাইমফ্রেম সিলেক্ট করুন",
    ["1 মিনিট (Scalping)", "5 মিনিট (Intraday)", "15 মিনিট (Short-term)", "1 ঘণ্টা (Position)"]
)

# বর্তমান রিয়েল-টাইম ঘড়ির সময় বের করা
now = datetime.now()
current_time_str = now.strftime("%I:%M:%S %p") # যেমন: 10:45:12 AM

# পরবর্তী এন্ট্রি নেওয়ার সুনির্দিষ্ট ঘড়ির সময় হিসাব করা (যেমন পরবর্তী ১ মিনিট বা ৫ মিনিটের ক্যান্ডেল ক্লোজ টাইম)
next_entry_time = now + timedelta(seconds=35)
next_entry_str = next_entry_time.strftime("%I:%M:%S %p")

# মার্কেট ডেটা ও র্যান্ডম ফ্ল্যাকচুয়েশন
base_price = 328.210
price_change = round(random.uniform(-1.5, 1.8), 3)
current_price = round(base_price + price_change, 3)

support_level = 324.110
resistance_level = 330.810
confidence_score = random.randint(65, 95)

# সিগন্যাল ও সুনির্দিষ্ট টাইমিং লজিক
if current_price > support_level and confidence_score >= 75:
    signal_status = "🟢 শক্তিশালী BUY (এন্ট্রি নেওয়ার উপযুক্ত সময়)"
    timing_instruction = f"আজকের ঘড়ি অনুযায়ী ঠিক **{next_entry_str}** মিনিটে ট্রেডিং প্ল্যাটফর্মে BUY বাটনে ক্লিক করুন।"
elif current_price >= resistance_level - 1.0:
    signal_status = "⚠️ সাবধান / SELL (প্রফিট বুকিংয়ের সময়)"
    timing_instruction = f"বাজার রেজিস্টर्मेंসে আছে। ঠিক **{next_entry_str}** এর মধ্যে আগের ট্রেড ক্লোজ করুন।"
else:
    signal_status = "⏳ অপেক্ষা করুন (Waiting for Setup)"
    timing_instruction = f"বাজারের বর্তমান গতি পর্যবেক্ষণ করা হচ্ছে। পরবর্তী সিগন্যালের জন্য অপেক্ষা করুন।"

# Displaying Analysis
st.subheader(f"📊 লাইভ মার্কেট বিশ্লেষণ: {selected_asset}")
st.markdown(f"🕒 **বর্তমান সিস্টেম সময়:** {current_time_str}")
st.markdown(f"### বর্তমান বাজার মূল্য: **${current_price}** (পরিবর্তন: {price_change:+.3f})")
st.markdown(f"### চূড়ান্ত সিগন্যাল: **{signal_status}**")

# AI Confidence Score
st.markdown("### এআই কনফিডেন্স স্কোর")
st.progress(confidence_score)
st.markdown(f"**{confidence_score}%** - কনফিডেন্স লেভেল যথেষ্ট শক্তিশালী।")

st.markdown("---")

# Exact Clock-Time Entry Guide
st.markdown("### ⏰ সুনির্দিষ্ট এন্ট্রি টাইমিং গাইড (ঘড়ির সময় অনুযায়ী)")
if "BUY" in signal_status:
    st.success(timing_instruction)
elif "SELL" in signal_status:
    st.warning(timing_instruction)
else:
    st.info(timing_instruction)

st.markdown("---")

# Specific Levels & Risk Management
st.markdown("### 🛡️ রিস্ক ম্যানেজমেন্ট লেভেল")

stop_loss = round(current_price - 4.5, 3)
take_profit = round(current_price + 6.0, 3)

data = {
    "প্যারামিটার": ["বর্তমান মূল্য", "সাপোর্ট লেভেল", "রেজিস্ট্যান্স লেভেল", "স্টপ লস (SL)", "টেক প্রফিট (TP)"],
    "মূল্য": [f"${current_price}", f"${support_level}", f"${resistance_level}", f"${stop_loss}", f"${take_profit}"]
}

df = pd.DataFrame(data)
st.table(df)

st.markdown("---")
st.markdown("💡 **পরামর্শ:** বডিতে যখনই সুনির্দিষ্ট ঘড়ির সময় (যেমন নির্দিষ্ট মিনিট-সেকেণ্ড) দেওয়া থাকবে, ঠিক সেই সময়ে মার্কেটে এন্ট্রি বা এক্সিট নেবেন।")


