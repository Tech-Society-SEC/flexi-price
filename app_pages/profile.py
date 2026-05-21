import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.auth import require_auth, logout, get_user

st.set_page_config(page_title="Profile — Nexus Pricing", page_icon="👤", layout="wide")

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

require_auth()
user = get_user()

# ── Sidebar ──
with st.sidebar:
    st.markdown(f"""
    <div style="text-align:center; padding: 1rem 0 1.5rem;">
        <div style="background:linear-gradient(135deg,#6c63ff,#00d4ff);border-radius:14px;
                    width:48px;height:48px;margin:0 auto 10px;display:flex;
                    align-items:center;justify-content:center;font-size:24px;">⚡</div>
        <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;
                    background:linear-gradient(135deg,#6c63ff,#00d4ff);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text;">NEXUS PRICING</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/dashboard.py",  label="📊  Dashboard",       use_container_width=True)
    st.page_link("pages/prediction.py", label="🎯  Price Prediction", use_container_width=True)
    st.page_link("pages/analytics.py",  label="📈  Analytics",       use_container_width=True)
    st.page_link("pages/profile.py",    label="👤  Profile",         use_container_width=True)
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        logout()

# ── Page Header ──
st.markdown("""
<div style="margin-bottom:1.5rem;">
    <h1 style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;
               letter-spacing:-0.03em;margin:0;color:#f0f2ff;">👤 Profile & Settings</h1>
    <p style="color:#8b8fa8;margin:0.4rem 0 0;font-size:0.95rem;">
        Manage your account, preferences, and usage statistics
    </p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    # ── Profile Card ──
    total_preds = st.session_state.get("total_predictions", 0)
    st.markdown(f"""
    <div style="background:linear-gradient(145deg,#13151f,#1a1d2e);
                border:1px solid rgba(108,99,255,0.3);border-radius:20px;padding:2rem;
                text-align:center;margin-bottom:1.5rem;">
        <div style="width:80px;height:80px;background:linear-gradient(135deg,#6c63ff,#00d4ff);
                    border-radius:50%;margin:0 auto 1rem;display:flex;align-items:center;
                    justify-content:center;font-size:2.5rem;">👤</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:800;
                    color:#f0f2ff;margin-bottom:4px;">{user.get('name','User')}</div>
        <div style="color:#8b8fa8;font-size:0.88rem;margin-bottom:8px;">{user.get('user_email','')}</div>
        <div style="background:rgba(0,229,160,0.12);border:1px solid rgba(0,229,160,0.25);
                    border-radius:100px;padding:4px 16px;display:inline-block;
                    color:#00e5a0;font-size:0.8rem;font-weight:600;margin-bottom:1.5rem;">
            ● {user.get('plan','Pro')} Plan Active
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;text-align:center;">
            <div style="background:rgba(108,99,255,0.08);border-radius:12px;padding:1rem;">
                <div style="font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;
                            color:#6c63ff;">{total_preds}</div>
                <div style="color:#8b8fa8;font-size:0.75rem;">Predictions</div>
            </div>
            <div style="background:rgba(0,212,255,0.08);border-radius:12px;padding:1rem;">
                <div style="font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;
                            color:#00d4ff;">8</div>
                <div style="color:#8b8fa8;font-size:0.75rem;">Reports</div>
            </div>
        </div>
    </div>

    <div style="background:linear-gradient(145deg,#13151f,#1a1d2e);
                border:1px solid rgba(108,99,255,0.2);border-radius:16px;padding:1.5rem;
                margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif;font-weight:700;color:#f0f2ff;
                    margin-bottom:1rem;font-size:1rem;">🏢 Company Details</div>
        <div style="space-y:0.75rem;">
            {"".join([f'''
            <div style="display:flex;justify-content:space-between;padding:0.6rem 0;
                        border-bottom:1px solid rgba(255,255,255,0.05);">
                <span style="color:#8b8fa8;font-size:0.85rem;">{k}</span>
                <span style="color:#f0f2ff;font-size:0.85rem;font-weight:500;">{v}</span>
            </div>''' for k,v in [
                ("Company", user.get('company','—')),
                ("Role", user.get('role','—')),
                ("Plan", user.get('plan','Pro')),
                ("Member Since", user.get('joined','2024')),
                ("Email", st.session_state.get("user_email","—")),
            ]])}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Plan badge
    plan = user.get('plan', 'Pro')
    if plan == 'Pro':
        st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(108,99,255,0.2),rgba(0,212,255,0.15));
                    border:1px solid rgba(108,99,255,0.4);border-radius:14px;padding:1.2rem;
                    text-align:center;">
            <div style="font-size:1.5rem;margin-bottom:6px;">⚡</div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;color:#f0f2ff;margin-bottom:4px;">Pro Plan</div>
            <div style="color:#8b8fa8;font-size:0.8rem;">Unlimited predictions · SHAP · Analytics</div>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    # ── Settings Tabs ──
    s1, s2, s3 = st.tabs(["⚙️ Account Settings", "🎨 Appearance", "🔔 Notifications"])

    with s1:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        with st.form("account_form"):
            st.markdown("**Personal Information**")
            col_fn, col_ln = st.columns(2)
            name_parts = user.get('name', 'User Name').split()
            with col_fn:
                fname = st.text_input("First Name", value=name_parts[0] if name_parts else "")
            with col_ln:
                lname = st.text_input("Last Name", value=name_parts[-1] if len(name_parts) > 1 else "")

            email_val = st.text_input("Email", value=st.session_state.get("user_email",""))
            company_val = st.text_input("Company", value=user.get('company',''))
            role_val = st.text_input("Role / Title", value=user.get('role',''))

            st.markdown("**Business Settings**")
            biz_type = st.selectbox("Business Type", [
                "E-Commerce (Multi-category)",
                "E-Commerce (Single-category)",
                "Retail + Online",
                "D2C Brand",
                "Marketplace Seller",
            ])
            currency = st.selectbox("Default Currency", ["INR (₹)", "USD ($)", "EUR (€)", "GBP (£)"])
            pricing_strategy = st.selectbox("Default Pricing Strategy", [
                "Margin Maximization",
                "Volume / Market Share",
                "Competitive Parity",
                "Penetration Pricing",
                "Dynamic / AI-driven",
            ])

            st.markdown("**Security**")
            col_pw1, col_pw2 = st.columns(2)
            with col_pw1:
                st.text_input("New Password", type="password", placeholder="Leave blank to keep current")
            with col_pw2:
                st.text_input("Confirm Password", type="password", placeholder="Confirm new password")

            submitted = st.form_submit_button("💾 Save Changes", use_container_width=True)
            if submitted:
                st.success("✅ Profile updated successfully!")

    with s2:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        st.markdown("**Theme Preferences**")
        theme_choice = st.radio("Interface Theme", ["🌑 Dark (Default)", "🌓 Midnight", "🌙 Amoled Black"],
                                horizontal=True)

        st.markdown("**Accent Color**")
        accent_col1, accent_col2, accent_col3, accent_col4 = st.columns(4)
        with accent_col1:
            st.markdown("""<div style="height:40px;background:linear-gradient(135deg,#6c63ff,#00d4ff);
                           border-radius:10px;cursor:pointer;border:2px solid white;"></div>
                           <div style="text-align:center;font-size:0.75rem;color:#8b8fa8;margin-top:4px;">Nexus</div>""",
                        unsafe_allow_html=True)
        with accent_col2:
            st.markdown("""<div style="height:40px;background:linear-gradient(135deg,#00e5a0,#00d4ff);
                           border-radius:10px;cursor:pointer;"></div>
                           <div style="text-align:center;font-size:0.75rem;color:#8b8fa8;margin-top:4px;">Teal</div>""",
                        unsafe_allow_html=True)
        with accent_col3:
            st.markdown("""<div style="height:40px;background:linear-gradient(135deg,#ff7c4d,#ff4d8d);
                           border-radius:10px;cursor:pointer;"></div>
                           <div style="text-align:center;font-size:0.75rem;color:#8b8fa8;margin-top:4px;">Sunset</div>""",
                        unsafe_allow_html=True)
        with accent_col4:
            st.markdown("""<div style="height:40px;background:linear-gradient(135deg,#fff,#c8cadb);
                           border-radius:10px;cursor:pointer;"></div>
                           <div style="text-align:center;font-size:0.75rem;color:#8b8fa8;margin-top:4px;">Mono</div>""",
                        unsafe_allow_html=True)

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown("**Dashboard Layout**")
        layout_choice = st.radio("Default View", ["Expanded cards", "Compact view", "Data-dense"],
                                 horizontal=True)

        st.markdown("**Chart Preferences**")
        chart_theme = st.selectbox("Chart Color Scheme", ["Nexus Dark (Default)", "Ocean Blues", "Sunset", "Monochrome"])
        show_confidence = st.toggle("Always show confidence intervals", value=True)
        animate_charts = st.toggle("Enable chart animations", value=True)
        show_shap = st.toggle("Auto-show SHAP after prediction", value=False)

        if st.button("💾 Save Appearance", use_container_width=True):
            st.success("✅ Appearance preferences saved!")

    with s3:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        st.markdown("**Email Notifications**")
        n1 = st.toggle("Price opportunity alerts", value=True)
        n2 = st.toggle("Weekly analytics digest", value=True)
        n3 = st.toggle("Competitor price changes", value=False)
        n4 = st.toggle("Model retraining complete", value=True)
        n5 = st.toggle("Stock threshold warnings", value=False)

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown("**In-App Notifications**")
        n6 = st.toggle("Prediction complete banner", value=True)
        n7 = st.toggle("Market trend changes", value=True)
        n8 = st.toggle("Daily pricing summary", value=False)

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown("**Notification Schedule**")
        alert_time = st.selectbox("Daily digest time", ["07:00 AM", "09:00 AM", "12:00 PM", "06:00 PM"])
        timezone = st.selectbox("Timezone", ["IST (UTC+5:30)", "UTC", "EST (UTC-5)", "PST (UTC-8)"])

        if st.button("💾 Save Notification Settings", use_container_width=True):
            st.success("✅ Notification preferences saved!")

    # ── Usage Statistics ──
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown("""
    <h3 style="font-family:'Syne',sans-serif;font-weight:700;font-size:1.1rem;color:#f0f2ff;margin-bottom:1rem;">
        📊 Usage Statistics
    </h3>
    """, unsafe_allow_html=True)

    uc1, uc2, uc3, uc4 = st.columns(4)
    stats = [
        ("Predictions Run", str(st.session_state.get("total_predictions", 0)), "#6c63ff"),
        ("API Calls", "142", "#00d4ff"),
        ("Reports Generated", "8", "#00e5a0"),
        ("Avg Response Time", "0.34s", "#ff7c4d"),
    ]
    for col, (label, val, color) in zip([uc1,uc2,uc3,uc4], stats):
        with col:
            st.markdown(f"""
            <div style="background:rgba(19,21,31,0.9);border:1px solid {color}30;
                        border-radius:14px;padding:1.1rem;text-align:center;border-top:2px solid {color};">
                <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;color:{color};">{val}</div>
                <div style="color:#8b8fa8;font-size:0.75rem;margin-top:4px;">{label}</div>
            </div>""", unsafe_allow_html=True)
