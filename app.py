import streamlit as st
import numpy as np

st.set_page_config(
    page_title="المجال المغناطيسي | Magnetic Fields Lab",
    page_icon="🧲",
    layout="wide",
    initial_sidebar_state="expanded"
)

MAIN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
:root {
    --bg-primary: #0a0e1a;
    --bg-secondary: #111827;
    --bg-card: #1a2236;
    --accent-cyan: #06d6a0;
    --accent-blue: #118ab2;
    --accent-orange: #ef8354;
    --accent-purple: #7b2cbf;
    --text-primary: #e8eaed;
    --text-secondary: #9aa5b4;
}
.stApp {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, #0d1321 100%);
    color: var(--text-primary);
    font-family: 'Cairo', sans-serif;
}
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1321 0%, #1a2236 100%);
    border-left: 1px solid rgba(6,214,160,0.2);
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] li {
    padding: 6px 8px !important;
    margin-bottom: 2px !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] li:hover {
    background: rgba(6,214,160,0.1) !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] li [data-testid="stSidebarNavLink"] {
    font-family: 'Cairo', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}
.section-title {
    font-size: 2rem; font-weight: 900;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; margin: 2rem 0 0.5rem;
}
.section-sub {
    font-size: 1rem; color: var(--text-secondary);
    text-align: center; margin-bottom: 2rem;
}
.card {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.8));
    border: 1px solid rgba(6,214,160,0.15);
    border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem;
    backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    transition: border-color 0.3s ease;
}
.card:hover { border-color: rgba(6,214,160,0.4); }
.formula-box {
    background: linear-gradient(135deg, rgba(6,214,160,0.08), rgba(17,138,178,0.08));
    border: 1px solid rgba(6,214,160,0.25); border-radius: 12px;
    padding: 1.2rem 1.8rem; margin: 1rem 0; text-align: center;
    font-family: 'JetBrains Mono', monospace; font-size: 1.25rem;
    color: var(--accent-cyan); direction: ltr;
}
.info-box {
    background: linear-gradient(135deg, rgba(17,138,178,0.12), rgba(123,44,191,0.08));
    border: 1px solid rgba(17,138,178,0.3); border-left: 4px solid var(--accent-blue);
    border-radius: 0 12px 12px 0; padding: 1rem 1.5rem; margin: 1rem 0;
}
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(6,214,160,0.3), transparent);
    margin: 2rem 0;
}
.author-badge {
    position: fixed; bottom: 15px; left: 50%; transform: translateX(-50%);
    background: linear-gradient(135deg, rgba(6,214,160,0.15), rgba(17,138,178,0.15));
    border: 1px solid rgba(6,214,160,0.3); border-radius: 30px;
    padding: 0.5rem 1.5rem; color: var(--accent-cyan);
    font-size: 0.85rem; font-weight: 600; z-index: 999;
}
.metric-card {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.6));
    border: 1px solid rgba(6,214,160,0.12); border-radius: 12px;
    padding: 1.2rem; text-align: center;
}
.metric-value {
    font-size: 1.8rem; font-weight: 900;
    font-family: 'JetBrains Mono', monospace; color: var(--accent-cyan);
}
.metric-label { font-size: 0.85rem; color: var(--text-secondary); margin-top: 0.3rem; }
.sidebar-hint {
    background: linear-gradient(135deg, rgba(6,214,160,0.1), rgba(17,138,178,0.08));
    border: 1px solid rgba(6,214,160,0.25); border-radius: 12px;
    padding: 1rem 1.5rem; text-align: center; margin-bottom: 2rem;
    animation: hintPulse 2s ease-in-out infinite;
}
@keyframes hintPulse {
    0%, 100% { box-shadow: 0 0 5px rgba(6,214,160,0.1); }
    50% { box-shadow: 0 0 20px rgba(6,214,160,0.3); }
}
.streamlit-expanderHeader {
    font-family: 'Cairo', sans-serif !important;
}
</style>
"""
st.markdown(MAIN_CSS, unsafe_allow_html=True)

MU_0 = 4 * np.pi * 1e-7

st.markdown('<div class="section-title">المجال المغناطيسي الناشئ عن تيار كهربائي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Magnetic Field of an Electric Current</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:var(--text-secondary); margin-bottom:1.5rem; font-size:0.95rem;">فيزياء الصف الثاني عشر - الجزء الثاني 2025</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-value">12</div><div class="metric-label">قسم تفاعلي</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-value">3D</div><div class="metric-label">رسوم متحركة ثلاثية الأبعاد</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-value">∞</div><div class="metric-label">تجارب غير محدودة</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-value">Lab</div><div class="metric-label">مختبر افتراضي</div></div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="sidebar-hint">
<span style="font-size:1.5rem;">👈</span>
<span style="color:var(--accent-cyan); font-weight:700;">اختر القسم من القائمة الجانبية</span>
<br><span style="color:var(--text-secondary); font-size:0.9rem;">اضغط على أي عنوان في القائمة اليسرى للانتقال</span>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="font-size:1.2rem; font-weight:700; color:var(--text-primary); margin-bottom:1rem; text-align:center;">محتويات الدرس</div>', unsafe_allow_html=True)

sections_info = [
    ("🔬", "قانون بيو-سافار", "تجربة تفاعلية لاكتشاف العلاقة الرياضية وحساب المجال المغناطيسي الجزئي والاشتقاق الرياضي", "#06d6a0"),
    ("🧲", "المجال من الموصلات", "المجال المغناطيسي لموصل مستقيم وطويل، وملف دائري، وملف لولبي مع قاعدة اليد اليمنى المتحركة", "#118ab2"),
    ("🔥", "احتواء البلازما", "كيف يمكن للمجال المغناطيسي أن يحتوي البلازما في مفاعلات الاندماج النووي مع رسوم متحركة", "#ef8354"),
    ("⚡", "القوة بين موصلين متوازيين", "تجربة تفاعلية لاستقصاء القوة المغناطيسية المتبادلة والتوصل رياضيا للعلاقة", "#7b2cbf"),
    ("🧭", "المغناطيسية الطبيعية", "تفسير كيف ينشأ المجال المغناطيسي في المغناطيس الدائم ومناطق المجال المغناطيسي", "#e63946"),
    ("⚛️", "جسيم مشحون 3D", "حركة جسيم مشحون في مجال مغناطيسي منتظم برسوم متحركة ثلاثية الأبعاد واشتقاق r و T", "#06d6a0"),
    ("🔬", "مطياف الكتلة والسينكروترون", "شرح مطياف الكتلة ومسارع السينكروترون برسوم 3D ومجالات استخدامهما", "#ffd166"),
    ("💪", "القوة على موصل يحمل تيارا", "تأثير القوة المغناطيسية في موصل موضوع في مجال منتظم وقاعدة فلمنغ لليد اليسرى", "#ef8354"),
    ("🧪", "المختبر الافتراضي", "مختبر افتراضي تفاعلي لاستقصاء القوة: القياس والملاحظة والاستنتاج والتوصل للعلاقات", "#118ab2"),
    ("📋", "أمثلة تفاعلية", "أمثلة من الحياة اليومية لتوضيح المفاهيم المعقدة مع حلول خطوة بخطوة", "#7b2cbf"),
    ("✅", "التقييم النهائي", "اختبار تفاعلي شامل من 10 أسئلة لقياس فهمك لجميع مفاهيم الدرس", "#06d6a0"),
]

for icon, title, desc, color in sections_info:
    st.markdown(f"""<div class="card" style="border-left:4px solid {color};">
    <div style="font-size:1.05rem; font-weight:700; color:{color}; margin-bottom:0.4rem;">{icon} {title}</div>
    <p style="color:var(--text-secondary); line-height:1.8; font-size:0.9rem; margin:0;">{desc}</p>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="card">
<div style="font-size:1.2rem; font-weight:700; color:var(--accent-cyan); margin-bottom:1rem;">الفكرة الرئيسة</div>
<p style="color:var(--text-secondary); line-height:1.9; font-size:1rem;">
يمكن توليد مجال مغناطيسي بتمرير تيار كهربائي في موصل، ويُحسب المجال المغناطيسي الذي يولّده موصل يحمل تياراً كهربائياً باستخدام علاقات رياضية تعتمد على عوامل، منها شكل الموصل الذي يحمل التيار ومقداره والمسافة عنه.
</p>
</div>""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""<div class="card">
    <div style="font-size:1rem; font-weight:700; color:var(--accent-blue); margin-bottom:0.8rem;">نواتج التعلم</div>
    <ul style="color:var(--text-secondary); line-height:2; font-size:0.9rem; padding-right:1.2rem;">
        <li>أستنتج العوامل التي يعتمد عليها المجال المغناطيسي الناشئ عن تيار في موصل</li>
        <li>أحسب المجال المغناطيسي لموصل مستقيم وملف دائري وملف لولبي</li>
        <li>أصف خطوط المجال المغناطيسي لكل حالة</li>
        <li>أستنتج العلاقات الرياضية للقوة المغناطيسية</li>
        <li>أوضح تطبيقات المجال المغناطيسي في التكنولوجيا</li>
    </ul>
    </div>""", unsafe_allow_html=True)

with col_b:
    st.markdown("""<div class="card">
    <div style="font-size:1rem; font-weight:700; color:var(--accent-orange); margin-bottom:0.8rem;">المفاهيم والمصطلحات</div>
    <ul style="color:var(--text-secondary); line-height:2; font-size:0.9rem; padding-right:1.2rem;">
        <li><strong>Magnetic Permeability</strong> - النفاذية المغناطيسية</li>
        <li><strong>Solenoid</strong> - ملف لولبي</li>
        <li><strong>Magnetic Domains</strong> - مناطق مغناطيسية</li>
        <li><strong>Biot-Savart Law</strong> - قانون بيو-سافار</li>
        <li><strong>Mass Spectrometer</strong> - مطياف الكتلة</li>
        <li><strong>Synchrotron</strong> - مسرع السينكروترون</li>
    </ul>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)
