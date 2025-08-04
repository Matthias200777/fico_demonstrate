import streamlit as st
import random
from datetime import datetime

# App config
st.set_page_config(page_title="Financial Demo", layout="centered")

# Session state setup
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'history' not in st.session_state:
    st.session_state.history = []

# CSS styling (same as original)
st.markdown("""
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .demo-banner {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: #ff4444;
            color: white;
            text-align: center;
            padding: 10px;
            font-weight: bold;
            z-index: 1000;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
            width: 100%;
            max-width: 400px;
            margin-top: 60px;
        }

        .header {
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 24px;
            margin-bottom: 5px;
        }

        .header p {
            opacity: 0.9;
            font-size: 14px;
        }

        .content {
            padding: 30px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }

        .form-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .form-group input:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }

        .btn {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(52, 152, 219, 0.3);
        }

        .btn:disabled {
            background: #bdc3c7;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .dashboard {
            display: none;
        }

        .score-display {
            background: linear-gradient(135deg, #27ae60, #2ecc71);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }

        .score-number {
            font-size: 48px;
            font-weight: bold;
            margin: 10px 0;
        }

        .score-range {
            opacity: 0.9;
            font-size: 14px;
        }

        .user-info {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .disclaimer {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            font-size: 12px;
            line-height: 1.5;
        }

        .logout-btn {
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            margin-top: 20px;
        }

        .logout-btn:hover {
            box-shadow: 0 8px 20px rgba(231, 76, 60, 0.3);
        }

        .history {
            margin-top: 20px;
        }

        .history-item {
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Demo banner
st.markdown("""
<div class="demo-banner">
⚠️ DEMO WEBSITE - NOT REAL - FOR DEMONSTRATION PURPOSES ONLY ⚠️
</div>
""", unsafe_allow_html=True)

# Main container
with st.container():
    if not st.session_state.logged_in:
        # Login screen
        st.markdown("""
        <div class="header">
            <h1>Financial Services</h1>
            <p>Demo Portal</p>
        </div>
        <div class="disclaimer">
            <strong>DISCLAIMER:</strong> This is a mockup demonstration only.
        </div>
        """, unsafe_allow_html=True)

        with st.form("login"):
            username = st.text_input("Username", key="username")
            password = st.text_input("Password", type="password", key="password")
            if st.form_submit_button("Login to Demo"):
                if username == "loans@yourbank.com" and password == "12345":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Use: loans@yourbank.com / 12345")

    else:
        # Dashboard
        st.markdown("""
        <div class="header">
            <h1>Score Lookup</h1>
            <p>Demo Dashboard</p>
        </div>
        <div class="user-info">
            <strong>Logged in as:</strong> loans@yourbank.com (DEMO USER)
        </div>
        """, unsafe_allow_html=True)

        with st.form("score_gen"):
            ssn = st.text_input("SSN (XXX-XX-XXXX)", key="ssn", max_chars=11)
            if st.form_submit_button("Generate Demo Score"):
                if ssn and len(ssn) == 11 and ssn.count('-') == 2:
                    score = random.randint(300, 850)
                    masked_ssn = ssn[:7] + 'XXXX'
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    st.session_state.history.insert(0, {
                        'ssn': masked_ssn,
                        'score': score,
                        'timestamp': timestamp
                    })
                    st.session_state.last_score = score
                else:
                    st.warning("Enter valid SSN (XXX-XX-XXXX)")

        if 'last_score' in st.session_state:
            st.markdown(f"""
            <div class="score-display">
                <div>Demo Score</div>
                <div class="score-number">{st.session_state.last_score}</div>
                <div class="score-range">Range: 300-850 (SIMULATED)</div>
            </div>
            """, unsafe_allow_html=True)

        if st.session_state.history:
            st.markdown("<h3>Demo Lookup History</h3>", unsafe_allow_html=True)
            for item in st.session_state.history[:5]:
                st.markdown(f"""
                <div class="history-item">
                    <strong>SSN:</strong> {item['ssn']}<br>
                    <strong>Score:</strong> {item['score']}<br>
                    <strong>Time:</strong> {item['timestamp']}
                </div>
                """, unsafe_allow_html=True)

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()