import streamlit as st
import numpy as np

# ==================== إعدادات الصفحة ====================
st.set_page_config(
    page_title="المجال المغناطيسي | Magnetic Fields Lab",
    page_icon="🧲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== التنسيقات CSS ====================
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
    --accent-red: #e63946;
    --text-primary: #e8eaed;
    --text-secondary: #9aa5b4;
    --glow-cyan: 0 0 20px rgba(6,214,160,0.3);
    --glow-blue: 0 0 20px rgba(17,138,178,0.3);
}

.stApp {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, #0d1321 100%);
    color: var(--text-primary);
    font-family: 'Cairo', sans-serif;
}

/* إخفاء العناصر الافتراضية */
#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1321 0%, #1a2236 100%);
    border-left: 1px solid rgba(6,214,160,0.2);
}

[data-testid="stSidebarNav"]::-webkit-scrollbar {
    width: 4px;
}
[data-testid="stSidebarNav"]::-webkit-scrollbar-thumb {
    background: var(--accent-cyan);
    border-radius: 4px;
}

.section-title {
    font-size: 2rem;
    font-weight: 900;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.section-subtitle {
    font-size: 1.1rem;
    color: var(--text-secondary);
    text-align: center;
    margin-bottom: 2rem;
}

.card {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.8));
    border: 1px solid rgba(6,214,160,0.15);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.card:hover {
    border-color: rgba(6,214,160,0.4);
    box-shadow: var(--glow-cyan);
    transform: translateY(-2px);
}

.formula-box {
    background: linear-gradient(135deg, rgba(6,214,160,0.08), rgba(17,138,178,0.08));
    border: 1px solid rgba(6,214,160,0.25);
    border-radius: 12px;
    padding: 1.2rem 1.8rem;
    margin: 1rem 0;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.25rem;
    color: var(--accent-cyan);
    direction: ltr;
}

.info-box {
    background: linear-gradient(135deg, rgba(17,138,178,0.12), rgba(123,44,191,0.08));
    border: 1px solid rgba(17,138,178,0.3);
    border-left: 4px solid var(--accent-blue);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.5rem;
    margin: 1rem 0;
}

.warning-box {
    background: linear-gradient(135deg, rgba(230,57,70,0.1), rgba(239,131,84,0.08));
    border: 1px solid rgba(230,57,70,0.3);
    border-left: 4px solid var(--accent-red);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.5rem;
    margin: 1rem 0;
}

.life-example {
    background: linear-gradient(135deg, rgba(239,131,84,0.1), rgba(230,57,70,0.05));
    border: 1px solid rgba(239,131,84,0.25);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
}

.life-example::before {
    content: "💡 من الحياة اليومية";
    display: block;
    font-weight: 700;
    color: var(--accent-orange);
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
}

.step-box {
    background: rgba(6,214,160,0.05);
    border: 1px solid rgba(6,214,160,0.15);
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    margin: 0.5rem 0;
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
}

.step-number {
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
    color: var(--bg-primary);
    font-weight: 700;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 0.85rem;
}

.author-badge {
    position: fixed;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, rgba(6,214,160,0.15), rgba(17,138,178,0.15));
    border: 1px solid rgba(6,214,160,0.3);
    border-radius: 30px;
    padding: 0.5rem 1.5rem;
    color: var(--accent-cyan);
    font-size: 0.85rem;
    font-weight: 600;
    backdrop-filter: blur(10px);
    z-index: 999;
    white-space: nowrap;
}

.hero-glow {
    position: absolute;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.15;
    pointer-events: none;
}

.metric-card {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.6));
    border: 1px solid rgba(6,214,160,0.12);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    transition: all 0.3s ease;
}

.metric-card:hover {
    border-color: var(--accent-cyan);
    box-shadow: var(--glow-cyan);
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 900;
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent-cyan);
}

.metric-label {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 0.3rem;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(6,214,160,0.3), transparent);
    margin: 2rem 0;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 5px rgba(6,214,160,0.2); }
    50% { box-shadow: 0 0 25px rgba(6,214,160,0.5); }
}

@keyframes rotate-slow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.float-anim {
    animation: float 3s ease-in-out infinite;
}

.pulse-anim {
    animation: pulse-glow 2s ease-in-out infinite;
}

.nav-card {
    background: linear-gradient(145deg, var(--bg-card), rgba(26,34,54,0.5));
    border: 1px solid rgba(6,214,160,0.1);
    border-radius: 14px;
    padding: 1.5rem;
    cursor: pointer;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
    display: block;
}

.nav-card:hover {
    border-color: var(--accent-cyan);
    box-shadow: var(--glow-cyan), 0 8px 30px rgba(0,0,0,0.4);
    transform: translateY(-4px) scale(1.01);
}

.nav-card-icon {
    font-size: 2.5rem;
    margin-bottom: 0.8rem;
}

.nav-card-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
}

.nav-card-desc {
    font-size: 0.82rem;
    color: var(--text-secondary);
    line-height: 1.5;
}

.plotly-chart .js-plotly-plot {
    border-radius: 12px !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: rgba(26,34,54,0.5);
    border-radius: 12px;
    padding: 4px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    font-family: 'Cairo', sans-serif;
    font-weight: 600;
    color: var(--text-secondary);
    transition: all 0.3s;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue)) !important;
    color: var(--bg-primary) !important;
}

.stSlider > div > div > div {
    background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue)) !important;
}

.stSelectbox > div > div {
    background: var(--bg-card) !important;
    border-color: rgba(6,214,160,0.2) !important;
    color: var(--text-primary) !important;
}

h1, h2, h3 {
    font-family: 'Cairo', sans-serif !important;
}
</style>
"""

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ==================== الثوابت الفيزيائية ====================
MU_0 = 4 * np.pi * 1e-7  # النفاذية المغناطيسية للفراغ T.m/A
E_CHARGE = 1.6e-19  # شحنة الإلكترون C
PROTON_MASS = 1.67e-27  # كتلة البروتون kg
ELECTRON_MASS = 9.11e-31  # كتلة الإلكترون kg

# ==================== محتوى الصفحة الرئيسية ====================

# تأثيرات الإضاءة الخلفية
st.markdown("""
<div style="position:relative; overflow:hidden; min-height:100vh;">
    <div class="hero-glow" style="top:-100px; right:-50px; background:var(--accent-cyan);"></div>
    <div class="hero-glow" style="bottom:100px; left:-80px; background:var(--accent-blue);"></div>
    <div class="hero-glow" style="top:40%; right:20%; background:var(--accent-purple); opacity:0.08;"></div>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<div class="section-title" style="font-size:2.8rem; margin-top:2rem;">المجال المغناطيسي الناشئ عن تيّار كهربائي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle" style="font-size:1.3rem;">Magnetic Field of an Electric Current</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; color:var(--text-secondary); margin-bottom:2.5rem; font-size:0.95rem;">فيزياء الصف الثاني عشر - الجزء الثاني 2025</div>', unsafe_allow_html=True)

# بطاقات الإحصائيات
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class="metric-card pulse-anim">
        <div class="metric-value">12</div>
        <div class="metric-label">قسم تفاعلي</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="metric-card pulse-anim" style="animation-delay:0.3s;">
        <div class="metric-value">3D</div>
        <div class="metric-label">رسوم متحركة ثلاثية الأبعاد</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="metric-card pulse-anim" style="animation-delay:0.6s;">
        <div class="metric-value">∞</div>
        <div class="metric-label">تجارب غير محدودة</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="metric-card pulse-anim" style="animation-delay:0.9s;">
        <div class="metric-value">Lab</div>
        <div class="metric-label">مختبر افتراضي</div>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# شبكة التنقل
st.markdown('<div style="font-size:1.3rem; font-weight:700; color:var(--text-primary); margin-bottom:1.2rem; text-align:center;">🔧 استكشف الأقسام</div>', unsafe_allow_html=True)

sections = [
    ("🔬", "قانون بيو-سافار", "تجربة تفاعلية لاكتشاف العلاقة الرياضية وحساب المجال المغناطيسي الجزئي", "01_biot_savart"),
    ("🧲", "المجال من الموصلات", "المجال المغناطيسي لموصل مستقيم وملف دائري وملف لولبي مع قاعدة اليد اليمنى المتحركة", "02_magnetic_field_conductors"),
    ("🔥", "احتواء البلازما", "كيف يحتوي المجال المغناطيسي البلازما في مفاعلات الاندماج النووي", "03_plasma_confinement"),
    ("⚡", "القوة بين موصلين متوازيين", "تجربة تفاعلية واستنتاج العلاقة الرياضية للقوة المتبادلة", "04_parallel_conductors"),
    ("🧭", "المغناطيسية الطبيعية", "تفسير المغناطيسية الدائمة ومناطق المجال المغناطيسي", "05_natural_magnetism"),
    ("⚛️", "جسيم مشحون 3D", "حركة جسيم مشحون في مجال مغناطيسي منتظم برسوم ثلاثية الأبعاد", "06_charged_particle_3d"),
    ("🔬", "مطياف الكتلة والسينكروترون", "تطبيقات حديثة للمجال المغناطيسي في الفيزياء والتكنولوجيا", "07_mass_spectrometer_synchrotron"),
    ("💪", "القوة على موصل يحمل تياراً", "تأثير المجال المغناطيسي في موصل يحمل تياراً وتحديد اتجاه القوة", "08_force_on_conductor"),
    ("🧪", "المختبر الافتراضي", "قياس وملاحظة واستنتاج والتوصل للعلاقات الرياضية بالتجربة", "09_virtual_lab"),
    ("📋", "أمثلة تفاعلية", "أمثلة من الحياة اليومية مع توضيح المعطيات والمطلوب", "10_interactive_examples"),
    ("✅", "التقييم النهائي", "اختبار تفاعلي شامل لقياس فهمك لجميع مفاهيم الدرس", "11_final_assessment"),
]

# عرض البطاقات في شبكة
for i in range(0, len(sections), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(sections):
            icon, title, desc, page = sections[idx]
            with col:
                st.markdown(f"""
                <a href="/{page}" class="nav-card">
                    <div class="nav-card-icon float-anim" style="animation-delay:{idx*0.15}s;">{icon}</div>
                    <div class="nav-card-title">{title}</div>
                    <div class="nav-card-desc">{desc}</div>
                </a>
                """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# محتوى تعريفي
st.markdown("""<div class="card">
<div style="font-size:1.2rem; font-weight:700; color:var(--accent-cyan); margin-bottom:1rem;">📖 الفكرة الرئيسة</div>
<p style="color:var(--text-secondary); line-height:1.9; font-size:1rem;">
يمكن توليد مجال مغناطيسي بتمرير تيار كهربائي في موصل، ويُحسب المجال المغناطيسي الذي يولّده موصل يحمل تياراً كهربائياً باستخدام علاقات رياضية تعتمد على عوامل، منها شكل الموصل الذي يحمل التيار ومقداره والمسافة عنه.
</p>
</div>""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""<div class="card">
    <div style="font-size:1rem; font-weight:700; color:var(--accent-blue); margin-bottom:0.8rem;">🎯 نواتج التعلم</div>
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
    <div style="font-size:1rem; font-weight:700; color:var(--accent-orange); margin-bottom:0.8rem;">📝 المفاهيم والمصطلحات</div>
    <ul style="color:var(--text-secondary); line-height:2; font-size:0.9rem; padding-right:1.2rem;">
        <li><strong>Magnetic Permeability</strong> - النفاذية المغناطيسية</li>
        <li><strong>Solenoid</strong> - ملف لولبي</li>
        <li><strong>Magnetic Domains</strong> - مناطق مغناطيسية</li>
        <li><strong>Biot-Savart Law</strong> - قانون بيو-سافار</li>
        <li><strong>Mass Spectrometer</strong> - مطياف الكتلة</li>
        <li><strong>Synchrotron</strong> - مسرّع السينكروترون</li>
    </ul>
    </div>""", unsafe_allow_html=True)

# إغلاق الحاوية وتوقيع المؤلفة
st.markdown("""
</div>
<div class="author-badge">إعداد: Israa Youssuf Samara</div>
""", unsafe_allow_html=True)