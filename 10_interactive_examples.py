import streamlit as st
import numpy as np
import plotly.graph_objects as go

MU_0 = 4 * np.pi * 1e-7
E_CHARGE = 1.6e-19
PROTON_MASS = 1.67e-27

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,#06d6a0,#ffd166);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
.given-box{background:rgba(17,138,178,.1);border:1px solid rgba(17,138,178,.25);border-radius:8px;padding:.6rem 1rem;margin:.5rem 0;font-family:'JetBrains Mono',monospace;font-size:.9rem;color:#118ab2;direction:ltr}
.find-box{background:rgba(255,209,102,.1);border:1px solid rgba(255,209,102,.25);border-radius:8px;padding:.6rem 1rem;margin:.5rem 0;font-family:'JetBrains Mono',monospace;font-size:.9rem;color:#ffd166;direction:ltr}
.solve-box{background:rgba(6,214,160,.08);border:1px solid rgba(6,214,160,.2);border-radius:10px;padding:1rem 1.2rem;margin:.8rem 0;font-family:'JetBrains Mono',monospace;font-size:.95rem;color:#06d6a0;direction:ltr;line-height:2}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">📋 أمثلة تفاعلية</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Interactive Examples with Step-by-Step Solutions</div>', unsafe_allow_html=True)

examples = [
    {
        "title": "مثال 1: المجال من سلك مستقيم",
        "life": "سلك نقل كهرباء يحمل تياراً كبيراً - ما مقدار المجال عند نقطة على بعد معين؟ هذا ما يحسبه المهندسون لتحديد مسافات الأمان.",
        "given": "I = 3 A, ra = 0.2 m, rb = 0.3 m",
        "find": "Ba = ? , Bb = ?",
        "steps": [
            ("Ba = μ₀ × I / (2π × ra)", f"= 4π×10⁻⁷ × 3 / (2π × 0.2)"),
            ("", f"= 3 × 10⁻⁶ T (داخل الصفحة ⊗)"),
            ("Bb = μ₀ × I / (2π × rb)", f"= 4π×10⁻⁷ × 3 / (2π × 0.3)"),
            ("", f"= 2 × 10⁻⁶ T (خارج الصفحة ⊙)"),
        ],
        "answer": "Ba = 3 × 10⁻⁶ T ⊗ , Bb = 2 × 10⁻⁶ T ⊙"
    },
    {
        "title": "مثال 2: المجال من ملف لولبي",
        "life": "ملف لولبي في مغناطيس الباب الإلكتروني - نحتاج معرفة التيار المطلوب لتوليد مجال معين.",
        "given": "B = 1.3 × 10⁻² T, n = 1400 turns/m",
        "find": "I = ?",
        "steps": [
            ("B = μ₀ × n × I", ""),
            ("I = B / (μ₀ × n)", f"= 1.3×10⁻² / (4π×10⁻⁷ × 1400)"),
            ("", f"= 7.4 A"),
        ],
        "answer": "I = 7.4 A"
    },
    {
        "title": "مثال 3: القوة بين موصلين متوازيين",
        "life": "في محطة كهربائية، سلكان يحملان تيارات كبيرة - القوة المتبادلة بينهما مهمة لتحديد المسافة الآمنة بينهما.",
        "given": "I₁ = 200 A, I₂ = 200 A, Fg/L = 0.2 N/m",
        "find": "r = ? (مسافة التوازن)",
        "steps": [
            ("Fg/L = FB/L", "0.2 = μ₀ × I₁ × I₂ / (2π × r)"),
            ("r = μ₀ × I₁ × I₂ / (2π × 0.2)", f"= 4π×10⁻⁷ × 200 × 200 / (2π × 0.2)"),
            ("", f"= 4 × 10⁻² m = 4 cm"),
        ],
        "answer": "r = 4 × 10⁻² m = 4 cm"
    },
    {
        "title": "مثال 4: مسار جسيم مشحون",
        "life": "في مطياف الكتلة، نحتاج معرفة نصف قطر مسار البروتون لفصله عن جسيمات أخرى.",
        "given": "Proton: m = 1.67×10⁻²⁷ kg, q = 1.6×10⁻¹⁹ C, v = 5×10⁶ m/s, B = 0.5 T",
        "find": "r = ? , T = ?",
        "steps": [
            ("r = mv / (qB)", f"= 1.67×10⁻²⁷ × 5×10⁶ / (1.6×10⁻¹⁹ × 0.5)"),
            ("", f"= 0.104 m = 10.4 cm"),
            ("T = 2πm / (qB)", f"= 2π × 1.67×10⁻²⁷ / (1.6×10⁻¹⁹ × 0.5)"),
            ("", f"= 1.31 × 10⁻⁷ s"),
        ],
        "answer": "r = 0.104 m , T = 1.31 × 10⁻⁷ s"
    },
    {
        "title": "مثال 5: مطياف الكتلة",
        "life": "فصل نظائر الكربون في مختبر تحليلي - أيهما يصل أولاً للكاشف؟",
        "given": "V = 1000 V, B = 0.1 T, ¹²C (m=1.99×10⁻²⁶ kg, q=6e) و ¹³C (m=2.16×10⁻²⁶ kg, q=6e)",
        "find": "r₁₂ = ? , r₁₃ = ?",
        "steps": [
            ("r = √(2mV/q) / B", ""),
            ("r₁₂ = √(2 × 1.99×10⁻²⁶ × 1000 / 6×1.6×10⁻¹⁹) / 0.1", "= 0.204 m"),
            ("r₁₃ = √(2 × 2.16×10⁻²⁶ × 1000 / 6×1.6×10⁻¹⁹) / 0.1", "= 0.213 m"),
        ],
        "answer": "r₁₂ = 0.204 m , r₁₃ = 0.213 m (¹³C أبعد لأنه أثقل)"
    },
    {
        "title": "مثال 6: القوة على موصل يحمل تياراً",
        "life": "ذراع روبوت صناعي يحمل تياراً في مجال مغناطيسي - ما القوة المؤثرة فيه؟",
        "given": "B = 0.8 T, I = 15 A, L = 0.4 m, θ = 90°",
        "find": "F = ?",
        "steps": [
            ("F = B × I × L × sinθ", "= 0.8 × 15 × 0.4 × sin(90°)"),
            ("", "= 0.8 × 15 × 0.4 × 1"),
            ("", "= 4.8 N (عمودية على كل من B و I)"),
        ],
        "answer": "F = 4.8 N"
    },
]

for idx, ex in enumerate(examples):
    with st.expander(f"📌 {ex['title']}", expanded=(idx == 0)):
        st.markdown(f"""<div class="life-example">{ex['life']}</div>""", unsafe_allow_html=True)

        col_g, col_f = st.columns(2)
        with col_g:
            st.markdown(f'<div class="given-box">📊 المعطيات:<br>{ex["given"]}</div>', unsafe_allow_html=True)
        with col_f:
            st.markdown(f'<div class="find-box">🎯 المطلوب:<br>{ex["find"]}</div>', unsafe_allow_html=True)

        # الحل خطوة بخطوة
        solve_html = '<div class="solve-box"><strong>الحل:</strong><br>'
        for step_title, step_val in ex['steps']:
            if step_title:
                solve_html += f'<br>{step_title}<br>'
            if step_val:
                solve_html += f'{step_val}<br>'
        solve_html += '</div>'
        st.markdown(solve_html, unsafe_allow_html=True)

        st.markdown(f"""<div class="formula-box" style="border-color:rgba(255,209,102,.4);">
        ✅ {ex['answer']}
        </div>""", unsafe_allow_html=True)

# مثال تفاعلي كامل مع رسم
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.3rem;font-weight:700;color:#ffd166;margin-bottom:1rem;">🎯 مثال تفاعلي: غيّر القيم وشاهد النتيجة فوراً</div>', unsafe_allow_html=True)

st.markdown("""<div class="life-example">
سلك مستقيم لا نهائي الطول يحمل تياراً كهربائياً. أوجد المجال المغناطيسي عند نقطتين على بعد مختلف عن السلك.
</div>""", unsafe_allow_html=True)

col_ix1, col_ix2, col_ix3 = st.columns([1, 1, 1.5])
with col_ix1:
    I_ix = st.slider("I (A)", 0.5, 20.0, 3.0, 0.5, key='ix_i')
    ra_ix = st.slider("ra (m)", 0.05, 0.5, 0.2, 0.01, key='ix_ra')
    Ba_ix = MU_0 * I_ix / (2 * np.pi * ra_ix)
    st.markdown(f"""<div class="formula-box" style="font-size:1rem;">
    Ba = {Ba_ix:.4e} T
    </div>""", unsafe_allow_html=True)

with col_ix2:
    rb_ix = st.slider("rb (m)", 0.05, 0.5, 0.3, 0.01, key='ix_rb')
    Bb_ix = MU_0 * I_ix / (2 * np.pi * rb_ix)
    st.markdown(f"""<div class="formula-box" style="font-size:1rem;">
    Bb = {Bb_ix:.4e} T
    </div>""", unsafe_allow_html=True)
    ratio = Ba_ix / Bb_ix if Bb_ix > 0 else 0
    st.markdown(f"""<div class="card" style="padding:.6rem;text-align:center;">
    <span style="color:#ffd166;font-weight:700;">Ba/Bb = rb/ra = {ratio:.2f}</span>
    </div>""", unsafe_allow_html=True)

with col_ix3:
    r_range = np.linspace(0.01, 0.5, 200)
    B_range = MU_0 * I_ix / (2 * np.pi * r_range)
    fig_ix = go.Figure()
    fig_ix.add_trace(go.Scatter(x=r_range*100, y=B_range*1e6, line=dict(color='#06d6a0', width=3)))
    fig_ix.add_scatter(x=[ra_ix*100], y=[Ba_ix*1e6], mode='markers+text',
                      marker=dict(size=12, color='#ef8354'), text='a', textposition='top center',
                      textfont=dict(color='#ef8354'))
    fig_ix.add_scatter(x=[rb_ix*100], y=[Bb_ix*1e6], mode='markers+text',
                      marker=dict(size=12, color='#118ab2'), text='b', textposition='top center',
                      textfont=dict(color='#118ab2'))
    fig_ix.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        font=dict(color='#9aa5b4', size=10), xaxis_title='r (cm)', yaxis_title='B (μT)',
        height=280, margin=dict(t=20, b=30, l=40, r=20))
    st.plotly_chart(fig_ix, use_container_width=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)