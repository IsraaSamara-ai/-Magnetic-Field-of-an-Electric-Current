import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
.data-table{width:100%;border-collapse:collapse;margin:1rem 0;}
.data-table th{background:rgba(6,214,160,.15);color:#06d6a0;padding:.6rem .8rem;text-align:center;font-size:.85rem;border:1px solid rgba(6,214,160,.2);}
.data-table td{background:rgba(26,34,54,.5);color:#e8eaed;padding:.5rem .8rem;text-align:center;font-size:.85rem;border:1px solid rgba(6,214,160,.1);}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">🧪 المختبر الافتراضي التفاعلي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Virtual Lab: Magnetic Force on a Current-Carrying Conductor</div>', unsafe_allow_html=True)

st.markdown("""<div class="info-box">
<strong style="color:#118ab2;">🎯 هدف المختبر:</strong> استقصاء العوامل المؤثرة في القوة المغناطيسية المؤثرة في موصل يحمل تياراً 
كهربائياً موضوع في مجال مغناطيسي منتظم - القياس والملاحظة والاستنتاج والتوصل للعلاقات الرياضية.
</div>""", unsafe_allow_html=True)

# تخزين القياسات
if 'measurements' not in st.session_state:
    st.session_state.measurements = []

tab_setup, tab_exp1, tab_exp2, tab_exp3, tab_conclude = st.tabs([
    "⚙️ الإعداد", "📊 التجربة 1: F مع I", "📊 التجربة 2: F مع L", "📊 التجربة 3: F مع B", "📈 الاستنتاج"
])

with tab_setup:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">طريقة العمل:</div>
    <ol style="color:#e8eaed;line-height:2.5;padding-right:1.5rem;">
        <li>ثبّت القيم الثابتة في كل تجربة</li>
        <li>غيّر المتغير المستقل بزيادات منتظمة</li>
        <li>سجّل قراءة القوة في كل مرة (اضغط "سجّل القياس")</li>
        <li>انتقل للاستنتاج بعد إكمال التجارب الثلاث</li>
    </ol>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#ffd166;margin-bottom:1rem;">القيم الافتراضية للمختبر:</div>
    <p style="direction:ltr;text-align:left;color:#9aa5b4;line-height:2;">
    B = 0.50 T (مجال مغناطيسي منتظم)<br>
    I = 5.0 A (تيار كهربائي)<br>
    L = 0.30 m (طول الموصل)<br>
    θ = 90° (الموصل عمودي على المجال)
    </p></div>""", unsafe_allow_html=True)

    if st.button("🗑️ مسح جميع القياسات", type="secondary"):
        st.session_state.measurements = []
        st.rerun()

with tab_exp1:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#06d6a0;">التجربة 1: تأثير التيار على القوة</div>
    <p style="color:#9aa5b4;">ثبّت: B = 0.50 T, L = 0.30 m, θ = 90° | غيّر: I</p>
    </div>""", unsafe_allow_html=True)

    col_e1a, col_e1b = st.columns([1, 1.5])
    with col_e1a:
        B_e1 = 0.50
        L_e1 = 0.30
        I_e1 = st.slider("التيار I (A)", 0.5, 20.0, 5.0, 0.5, key='e1i')
        F_e1 = B_e1 * I_e1 * L_e1 * np.sin(np.radians(90))
        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        F = {F_e1:.4f} N
        </div>""", unsafe_allow_html=True)

        if st.button("📝 سجّل القياس", key='rec1', type="primary"):
            st.session_state.measurements.append({
                'exp': 1, 'I': I_e1, 'L': L_e1, 'B': B_e1, 'theta': 90, 'F': F_e1
            })
            st.success(f"تم تسجيل: I={I_e1}A, F={F_e1:.4f}N")

    with col_e1b:
        exp1_data = [m for m in st.session_state.measurements if m['exp'] == 1]
        if exp1_data:
            fig_e1 = go.Figure()
            Is = [m['I'] for m in exp1_data]
            Fs = [m['F'] for m in exp1_data]
            fig_e1.add_trace(go.Scatter(x=Is, y=Fs, mode='lines+markers',
                                        line=dict(color='#06d6a0', width=3),
                                        marker=dict(size=10, color='#ffd166')))
            fig_e1.update_layout(
                title=dict(text='F vs I (Exp 1)', font=dict(color='#06d6a0')),
                plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                font=dict(color='#9aa5b4'), xaxis_title='I (A)', yaxis_title='F (N)',
                height=350, margin=dict(t=40, b=30, l=50, r=20))
            st.plotly_chart(fig_e1, use_container_width=True)
        else:
            st.markdown('<div class="card" style="text-align:center;color:#9aa5b4;">سجّل قياسات لرؤية الرسم البياني</div>', unsafe_allow_html=True)

with tab_exp2:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#118ab2;">التجربة 2: تأثير الطول على القوة</div>
    <p style="color:#9aa5b4;">ثبّت: B = 0.50 T, I = 5.0 A, θ = 90° | غيّر: L</p>
    </div>""", unsafe_allow_html=True)

    col_e2a, col_e2b = st.columns([1, 1.5])
    with col_e2a:
        B_e2 = 0.50
        I_e2 = 5.0
        L_e2 = st.slider("الطول L (m)", 0.05, 1.0, 0.30, 0.05, key='e2l')
        F_e2 = B_e2 * I_e2 * L_e2
        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        F = {F_e2:.4f} N
        </div>""", unsafe_allow_html=True)

        if st.button("📝 سجّل القياس", key='rec2', type="primary"):
            st.session_state.measurements.append({
                'exp': 2, 'I': I_e2, 'L': L_e2, 'B': B_e2, 'theta': 90, 'F': F_e2
            })
            st.success(f"تم تسجيل: L={L_e2}m, F={F_e2:.4f}N")

    with col_e2b:
        exp2_data = [m for m in st.session_state.measurements if m['exp'] == 2]
        if exp2_data:
            fig_e2 = go.Figure()
            Ls = [m['L'] for m in exp2_data]
            Fs = [m['F'] for m in exp2_data]
            fig_e2.add_trace(go.Scatter(x=Ls, y=Fs, mode='lines+markers',
                                        line=dict(color='#118ab2', width=3),
                                        marker=dict(size=10, color='#ffd166')))
            fig_e2.update_layout(
                title=dict(text='F vs L (Exp 2)', font=dict(color='#118ab2')),
                plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                font=dict(color='#9aa5b4'), xaxis_title='L (m)', yaxis_title='F (N)',
                height=350, margin=dict(t=40, b=30, l=50, r=20))
            st.plotly_chart(fig_e2, use_container_width=True)
        else:
            st.markdown('<div class="card" style="text-align:center;color:#9aa5b4;">سجّل قياسات لرؤية الرسم البياني</div>', unsafe_allow_html=True)

with tab_exp3:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#ef8354;">التجربة 3: تأثير المجال على القوة</div>
    <p style="color:#9aa5b4;">ثبّت: I = 5.0 A, L = 0.30 m, θ = 90° | غيّر: B</p>
    </div>""", unsafe_allow_html=True)

    col_e3a, col_e3b = st.columns([1, 1.5])
    with col_e3a:
        I_e3 = 5.0
        L_e3 = 0.30
        B_e3 = st.slider("المجال B (T)", 0.05, 2.0, 0.50, 0.05, key='e3b')
        F_e3 = B_e3 * I_e3 * L_e3
        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        F = {F_e3:.4f} N
        </div>""", unsafe_allow_html=True)

        if st.button("📝 سجّل القياس", key='rec3', type="primary"):
            st.session_state.measurements.append({
                'exp': 3, 'I': I_e3, 'L': L_e3, 'B': B_e3, 'theta': 90, 'F': F_e3
            })
            st.success(f"تم تسجيل: B={B_e3}T, F={F_e3:.4f}N")

    with col_e3b:
        exp3_data = [m for m in st.session_state.measurements if m['exp'] == 3]
        if exp3_data:
            fig_e3 = go.Figure()
            Bs = [m['B'] for m in exp3_data]
            Fs = [m['F'] for m in exp3_data]
            fig_e3.add_trace(go.Scatter(x=Bs, y=Fs, mode='lines+markers',
                                        line=dict(color='#ef8354', width=3),
                                        marker=dict(size=10, color='#ffd166')))
            fig_e3.update_layout(
                title=dict(text='F vs B (Exp 3)', font=dict(color='#ef8354')),
                plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                font=dict(color='#9aa5b4'), xaxis_title='B (T)', yaxis_title='F (N)',
                height=350, margin=dict(t=40, b=30, l=50, r=20))
            st.plotly_chart(fig_e3, use_container_width=True)
        else:
            st.markdown('<div class="card" style="text-align:center;color:#9aa5b4;">سجّل قياسات لرؤية الرسم البياني</div>', unsafe_allow_html=True)

with tab_conclude:
    st.markdown('<div style="font-size:1.2rem;font-weight:700;color:#ffd166;margin-bottom:1rem;">📊 التحليل والاستنتاج</div>', unsafe_allow_html=True)

    if st.session_state.measurements:
        # جدول جميع القياسات
        st.markdown("""<table class="data-table">
        <thead><tr><th>التجربة</th><th>I (A)</th><th>L (m)</th><th>B (T)</th><th>F (N)</th></tr></thead><tbody>""", unsafe_allow_html=True)
        for m in st.session_state.measurements:
            st.markdown(f"""<tr><td>{m['exp']}</td><td>{m['I']:.1f}</td><td>{m['L']:.2f}</td><td>{m['B']:.2f}</td><td>{m['F']:.4f}</td></tr>""", unsafe_allow_html=True)
        st.markdown("</tbody></table>", unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        # استنتاجات
        st.markdown("""<div class="card">
        <div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">الاستنتاجات من الرسوم البيانية:</div>
        </div>""", unsafe_allow_html=True)

        conclusions = [
            ("تجربة 1 (F مع I):", "الرسم البياني خط مستقيم يمر بنقطة الأصل → F ∝ I", "#06d6a0"),
            ("تجربة 2 (F مع L):", "الرسم البياني خط مستقيم يمر بنقطة الأصل → F ∝ L", "#118ab2"),
            ("تجربة 3 (F مع B):", "الرسم البياني خط مستقيم يمر بنقطة الأصل → F ∝ B", "#ef8354"),
        ]
        for title, desc, color in conclusions:
            st.markdown(f"""<div class="card" style="border-left:4px solid {color};padding:1rem;">
            <div style="color:{color};font-weight:700;">{title}</div>
            <div style="color:#e8eaed;">{desc}</div></div>""", unsafe_allow_html=True)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown("""<div class="card" style="border-color:rgba(255,209,102,.4);">
        <div style="font-weight:700;color:#ffd166;font-size:1.2rem;margin-bottom:1rem;">🏆 النتيجة النهائية:</div>
        <p style="color:#e8eaed;line-height:2.2;">
        بدمج الاستنتاجات الثلاثة: <strong style="color:#06d6a0;">F ∝ I × L × B</strong><br>
        عند θ = 90° (الوضع العمودي): <strong style="color:#06d6a0;">F = B × I × L</strong><br>
        للزاوية العامة: <strong style="color:#06d6a0;">F = B × I × L × sinθ</strong>
        </p></div>""", unsafe_allow_html=True)

        st.markdown('<div class="formula-box" style="font-size:1.5rem;">F = B × I × L × sinθ</div>', unsafe_allow_html=True)
    else:
        st.markdown("""<div class="card" style="text-align:center;">
        <p style="color:#ffd166;font-size:1.1rem;">⚡ لم تسجّل أي قياسات بعد</p>
        <p style="color:#9aa5b4;">اذهب للتجارب 1 و 2 و 3 وسجّل عدة قياسات في كل منها، ثم عد للاستنتاج</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)