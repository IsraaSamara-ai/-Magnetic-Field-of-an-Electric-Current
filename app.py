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
[data-testid="stPageLink-NavLink"] {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.5)) !important;
    border: 1px solid rgba(6,214,160,0.1) !important;
    border-radius: 14px !important;
    padding: 1rem 1.2rem !important;
    transition: all 0.3s ease !important;
    margin-bottom: 0.5rem !important;
}
[data-testid="stPageLink-NavLink"]:hover {
    border-color: rgba(6,214,160,0.4) !important;
    box-shadow: 0 0 20px rgba(6,214,160,0.3), 0 8px 30px rgba(0,0,0,0.4) !important;
    transform: translateY(-2px) !important;
}
</style>
"""
st.markdown(MAIN_CSS, unsafe_allow_html=True)

MU_0 = 4 * np.pi * 1e-7

st.markdown('<div class="section-title">المجال المغناطيسي الناشئ عن تيار كهربائي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Magnetic Field of an Electric Current</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:var(--text-secondary); margin-bottom:2.5rem; font-size:0.95rem;">فيزياء الصف الثاني عشر - الجزء الثاني 2025</div>', unsafe_allow_html=True)

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
st.markdown('<div style="font-size:1.3rem; font-weight:700; color:var(--text-primary); margin-bottom:1.2rem; text-align:center;">استكشف الأقسام</div>', unsafe_allow_html=True)

sections = [
    ("pages/01_biot_savart.py", "🔬 قانون بيو-سافار", "تجربة تفاعلية لاكتشاف العلاقة الرياضية وحساب المجال المغناطيسي"),
    ("pages/02_magnetic_field_conductors.py", "🧲 المجال من الموصلات", "المجال لموصل مستقيم وملف دائري وملف لولبي مع قاعدة اليد اليمنى"),
    ("pages/03_plasma_confinement.py", "🔥 احتواء البلازما", "كيف يحتوي المجال المغناطيسي البلازما في مفاعلات الاندماج النووي"),
    ("pages/04_parallel_conductors.py", "⚡ القوة بين موصلين", "تجربة تفاعلية واستنتاج العلاقة الرياضية للقوة المتبادلة"),
    ("pages/05_natural_magnetism.py", "🧭 المغناطيسية الطبيعية", "تفسير المغناطيسية الدائمة ومناطق المجال المغناطيسي"),
    ("pages/06_charged_particle_3d.py", "⚛️ جسيم مشحون 3D", "حركة جسيم مشحون في مجال مغناطيسي منتظم برسوم ثلاثية الأبعاد"),
    ("pages/07_mass_spectrometer_synchrotron.py", "🔬 مطياف الكتلة", "مطياف الكتلة ومسرع السينكروترون وتطبيقاتهما"),
    ("pages/08_force_on_conductor.py", "💪 القوة على موصل", "تأثير المجال المغناطيسي في موصل يحمل تيارا وتحديد اتجاه القوة"),
    ("pages/09_virtual_lab.py", "🧪 المختبر الافتراضي", "قياس وملاحظة واستنتاج والتوصل للعلاقات الرياضية"),
    ("pages/10_interactive_examples.py", "📋 أمثلة تفاعلية", "أمثلة من الحياة اليومية مع توضيح المعطيات والمطلوب"),
    ("pages/11_final_assessment.py", "✅ التقييم النهائي", "اختبار تفاعلي شامل لقياس فهمك لجميع مفاهيم الدرس"),
]

for i in range(0, len(sections), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(sections):
            page, title, desc = sections[idx]
            with col:
                st.page_link(page, label=f"**{title}**  \n{desc}", use_container_width=True)

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
