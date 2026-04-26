import streamlit as st
import numpy as np
import plotly.graph_objects as go

MU_0 = 4 * np.pi * 1e-7

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp { background: linear-gradient(135deg, #0a0e1a 0%, #111827 50%, #0d1321 100%); color: #e8eaed; font-family: 'Cairo', sans-serif; }
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d1321 0%, #1a2236 100%); }
.section-title { font-size: 2rem; font-weight: 900; background: linear-gradient(135deg, #06d6a0, #118ab2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin: 1.5rem 0 0.5rem; }
.section-sub { font-size: 1rem; color: #9aa5b4; text-align: center; margin-bottom: 2rem; }
.card { background: linear-gradient(145deg, #1a2236, rgba(26,34,54,0.8)); border: 1px solid rgba(6,214,160,0.15); border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem; }
.formula-box { background: linear-gradient(135deg, rgba(6,214,160,0.08), rgba(17,138,178,0.08)); border: 1px solid rgba(6,214,160,0.25); border-radius: 12px; padding: 1.2rem 1.8rem; margin: 1rem 0; text-align: center; font-family: 'JetBrains Mono', monospace; font-size: 1.25rem; color: #06d6a0; direction: ltr; }
.info-box { background: linear-gradient(135deg, rgba(17,138,178,0.12), rgba(123,44,191,0.08)); border: 1px solid rgba(17,138,178,0.3); border-left: 4px solid #118ab2; border-radius: 0 12px 12px 0; padding: 1rem 1.5rem; margin: 1rem 0; }
.life-example { background: linear-gradient(135deg, rgba(239,131,84,0.1), rgba(230,57,70,0.05)); border: 1px solid rgba(239,131,84,0.25); border-radius: 12px; padding: 1.2rem 1.5rem; margin: 1rem 0; }
.life-example::before { content: "💡 من الحياة اليومية"; display: block; font-weight: 700; color: #ef8354; margin-bottom: 0.5rem; }
.step-box { background: rgba(6,214,160,0.05); border: 1px solid rgba(6,214,160,0.15); border-radius: 10px; padding: 0.8rem 1.2rem; margin: 0.5rem 0; }
.divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(6,214,160,0.3), transparent); margin: 2rem 0; }
.author-badge { position: fixed; bottom: 15px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, rgba(6,214,160,0.15), rgba(17,138,178,0.15)); border: 1px solid rgba(6,214,160,0.3); border-radius: 30px; padding: 0.5rem 1.5rem; color: #06d6a0; font-size: 0.85rem; font-weight: 600; z-index: 999; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">🔬 قانون بيو-سافار</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">The Biot-Savart Law - Interactive Experiment</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📖 الشرح النظري", "🧪 التجربة التفاعلية", "📊 الاشتقاق الرياضي"])

with tab1:
    st.markdown("""<div class="card">
    <p style="color:#e8eaed; line-height:2; font-size:1rem;">
    تعلّمْتَ أنّ المغناطيس يولِّد حَوْلَه مجالًا مغناطيسيًّا، لكنّ الاستخدام العمليّ والتطبيقات التكنولوجيّة 
    في الغالب تعتمد على <strong style="color:#06d6a0;">المغناطيس الكهربائيّ</strong>؛ إذ يمكنُ توليد مجالٍ مغناطيسيٍّ 
    بتمرير تيّار كهربائيٍّ في مُوصل.
    </p>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">تجربة أورستد:</strong> عندما أورستد لاحظ انحراف إبرة بوصلة وضعت أسفل سلك يمر فيه تيار كهربائي، 
    وفسر ذلك بتولّد مجال مغناطيسي حول السلك أدى إلى انحراف إبرة البوصلة. كانت هذه التجربة البداية لاكتشاف العلاقة بين الكهرباء والمغناطيسية.
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="life-example">
    تخيّل أنك تضع بوصلة هاتفك بالقرب من سلك توصيل كبير يحمل تياراً كهربائياً - ستلاحظ أن اتجاه البوصلة يتغير! 
    هذا بالضبط ما اكتشفه أورستد. نفس المبدأ يجعل المحولات الكهربائية في شاحن هاتفك تعمل.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#06d6a0; margin:1.5rem 0 0.8rem;">القانون الرياضي:</div>', unsafe_allow_html=True)

    st.markdown("""<div class="formula-box">
    dB = (μ₀ / 4π) × (I × dL × sinθ) / r²
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <p style="color:#9aa5b4; line-height:2; font-size:0.95rem; direction:ltr; text-align:left;">
    <strong style="color:#06d6a0;">dB</strong> = مقدار المجال المغناطيسي الجزئي عند النقطة P<br>
    <strong style="color:#06d6a0;">μ₀</strong> = 4π × 10⁻⁷ T.m/A (النفاذية المغناطيسية للفراغ)<br>
    <strong style="color:#06d6a0;">I</strong> = مقدار التيار الكهربائي المار في الموصل (A)<br>
    <strong style="color:#06d6a0;">dL</strong> = طول القطعة الصغيرة من الموصل (m)<br>
    <strong style="color:#06d6a0;">r</strong> = المسافة من القطعة dL إلى النقطة P (m)<br>
    <strong style="color:#06d6a0;">θ</strong> = الزاوية بين متجه الطول dL والمتجه الممتد من dL إلى النقطة P
    </p>
    </div>""", unsafe_allow_html=True)

with tab2:
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">🎯 الهدف:</strong> استكشف كيف تتغير قيمة dB عند تغيير التيار والمسافة والزاوية. 
    لاحظ العلاقة بين كل متغير والمجال المغناطيسي الناتج.
    </div>""", unsafe_allow_html=True)

    col_sliders, col_viz = st.columns([1, 1.5])

    with col_sliders:
        st.markdown('<div style="font-weight:700; color:#06d6a0; margin-bottom:1rem;">⚙️ تغيير المتغيرات</div>', unsafe_allow_html=True)

        I = st.slider("التيار الكهربائي I (A)", 0.1, 20.0, 5.0, 0.1)
        dL = st.slider("طول القطعة dL (m)", 0.001, 0.1, 0.01, 0.001, format="%.3f")
        r = st.slider("المسافة r (m)", 0.01, 1.0, 0.1, 0.01, format="%.2f")
        theta_deg = st.slider("الزاوية θ (degrees)", 0, 180, 90, 1)

        theta_rad = np.radians(theta_deg)
        dB = (MU_0 / (4 * np.pi)) * (I * dL * np.sin(theta_rad)) / (r ** 2)

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        dB = {dB:.4e} T
        </div>""", unsafe_allow_html=True)

        # تتبع القيم
        st.markdown(f"""<div class="card">
        <p style="color:#9aa5b4; font-size:0.9rem; direction:ltr; text-align:left;">
        μ₀ = {MU_0:.4e} T.m/A<br>
        I = {I:.1f} A<br>
        dL = {dL:.3f} m<br>
        r = {r:.2f} m<br>
        sin({theta_deg}°) = {np.sin(theta_rad):.4f}
        </p>
        </div>""", unsafe_allow_html=True)

    with col_viz:
        # رسم تخيلي لقانون بيو-سافار
        fig = go.Figure()

        # الموصل
        wire_x = [0, 0.5 * np.cos(theta_rad)]
        wire_y = [0, 0.5 * np.sin(theta_rad)]
        fig.add_trace(go.Scatter(x=wire_x, y=wire_y, mode='lines+markers',
                                 line=dict(color='#06d6a0', width=4), marker=dict(size=8, color='#06d6a0'),
                                 name='dL'))

        # متجه r
        fig.add_trace(go.Scatter(x=[0, r], y=[0, 0], mode='lines+markers',
                                 line=dict(color='#ef8354', width=3, dash='dash'),
                                 marker=dict(size=8, color='#ef8354'), name='r'))

        # النقطة P
        fig.add_trace(go.Scatter(x=[r], y=[0], mode='markers+text',
                                 marker=dict(size=14, color='#e63946'),
                                 text='P', textposition='top center',
                                 textfont=dict(color='#e63946', size=16), name='Point P'))

        # زاوية theta
        arc_theta = np.linspace(0, theta_rad, 50)
        arc_r = 0.15
        fig.add_trace(go.Scatter(x=arc_r * np.cos(arc_theta), y=arc_r * np.sin(arc_theta),
                                 mode='lines', line=dict(color='#7b2cbf', width=2),
                                 showlegend=False))

        # dB - اتجاه عمودي على المستوى
        dB_scale = min(dB * 1e5, 0.4)
        fig.add_trace(go.Scatter(x=[r, r], y=[0, dB_scale], mode='lines+markers',
                                 line=dict(color='#ffd166', width=3),
                                 marker=dict(size=10, color='#ffd166'),
                                 name='dB (⊙ out of plane)'))

        # دائرة المجال حول P
        circle_t = np.linspace(0, 2 * np.pi, 100)
        cr = 0.08
        fig.add_trace(go.Scatter(x=r + cr * np.cos(circle_t), y=cr * np.sin(circle_t),
                                 mode='lines', line=dict(color='#06d6a0', width=1, dash='dot'),
                                 showlegend=False))

        fig.update_layout(
            plot_bgcolor='rgba(10,14,26,0.8)',
            paper_bgcolor='rgba(10,14,26,0.8)',
            font=dict(color='#e8eaed', family='Cairo'),
            xaxis=dict(showgrid=False, zeroline=True, zerolinecolor='rgba(6,214,160,0.2)',
                       range=[-0.2, r + 0.3]),
            yaxis=dict(showgrid=False, zeroline=True, zerolinecolor='rgba(6,214,160,0.2)',
                       range=[-0.3, 0.5]),
            height=450, margin=dict(t=30, b=30, l=30, r=30),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)',
                        font=dict(size=11))
        )
        st.plotly_chart(fig, use_container_width=True)

        # ملاحظات
        if theta_deg == 0 or theta_deg == 180:
            st.markdown("""<div class="card" style="border-color:rgba(230,57,70,0.4);">
            <p style="color:#e63946; font-weight:700;">⚠️ لاحظ!</p>
            <p style="color:#9aa5b4;">عندما θ = 0° أو θ = 180° فإن sinθ = 0 وبالتالي dB = 0.<br>
            هذا يعني أن المجال المغناطيسي ينعدم عند النقاط الواقعة على امتداد الموصل.</p>
            </div>""", unsafe_allow_html=True)
        elif theta_deg == 90:
            st.markdown("""<div class="card" style="border-color:rgba(6,214,160,0.4);">
            <p style="color:#06d6a0; font-weight:700;">✅ أقصى مجال!</p>
            <p style="color:#9aa5b4;">عند θ = 90° (الوضع العمودي) يكون المجال المغناطيسي أكبر ما يمكن لأن sin(90°) = 1</p>
            </div>""", unsafe_allow_html=True)

    # رسم علاقة dB مع كل متغير
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#06d6a0; margin-bottom:1rem;">📈 العلاقات البيانية</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        I_vals = np.linspace(0.1, 20, 100)
        dB_I = (MU_0 / (4 * np.pi)) * (I_vals * dL * np.sin(theta_rad)) / (r ** 2)
        fig1 = go.Figure(go.Scatter(x=I_vals, y=dB_I, line=dict(color='#06d6a0', width=2.5)))
        fig1.update_layout(title=dict(text='dB vs I', font=dict(color='#06d6a0')),
                           plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                           font=dict(color='#9aa5b4', size=10),
                           xaxis_title='I (A)', yaxis_title='dB (T)', height=280, margin=dict(t=40,b=30,l=40,r=20))
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        r_vals = np.linspace(0.01, 1, 100)
        dB_r = (MU_0 / (4 * np.pi)) * (I * dL * np.sin(theta_rad)) / (r_vals ** 2)
        fig2 = go.Figure(go.Scatter(x=r_vals, y=dB_r, line=dict(color='#ef8354', width=2.5)))
        fig2.update_layout(title=dict(text='dB vs r', font=dict(color='#ef8354')),
                           plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                           font=dict(color='#9aa5b4', size=10),
                           xaxis_title='r (m)', yaxis_title='dB (T)', height=280, margin=dict(t=40,b=30,l=40,r=20))
        st.plotly_chart(fig2, use_container_width=True)

    with c3:
        th_vals = np.linspace(0, 180, 200)
        dB_th = (MU_0 / (4 * np.pi)) * (I * dL * np.sin(np.radians(th_vals))) / (r ** 2)
        fig3 = go.Figure(go.Scatter(x=th_vals, y=dB_th, line=dict(color='#7b2cbf', width=2.5)))
        fig3.add_vline(x=theta_deg, line_dash='dash', line_color='#ffd166')
        fig3.update_layout(title=dict(text='dB vs θ', font=dict(color='#7b2cbf')),
                           plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
                           font=dict(color='#9aa5b4', size=10),
                           xaxis_title='θ (degrees)', yaxis_title='dB (T)', height=280, margin=dict(t=40,b=30,l=40,r=20))
        st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.markdown("""<div class="card">
    <div style="font-size:1.1rem; font-weight:700; color:#06d6a0; margin-bottom:1rem;">📝 الاشتقاق الرياضي للمجال من موصل مستقيم لا نهائي</div>
    <p style="color:#e8eaed; line-height:2.2; font-size:0.95rem; direction:rtl;">
    لنحسب المجال المغناطيسي عند نقطة P تبعد مسافة <span style="color:#06d6a0; direction:ltr; display:inline;">r</span> عمودياً عن موصل مستقيم لا نهائي الطول يسري فيه تيار <span style="color:#06d6a0; direction:ltr; display:inline;">I</span>:
    </p>
    </div>""", unsafe_allow_html=True)

    steps = [
        ("نبدأ من قانون بيو-سافار:", "dB = (μ₀ / 4π) × (I × dL × sinθ) / r²"),
        ("بالنسبة لموصل مستقيم، الزاوية θ بين dL وr تساوي 90° دائماً:", "sinθ = 1 → dB = (μ₀ / 4π) × (I × dL) / r²"),
        ("نستبدل المتغيرات: dL = r × dθ / sinθ و r = a / sinθ (حيث a المسافة العمودية):", "dB = (μ₀ × I × sinθ × dθ) / (4π × a)"),
        ("نجمع بالتكامل من θ = 0 إلى θ = π:", "B = ∫₀ᵖ (μ₀ × I × sinθ) / (4π × a) dθ"),
        ("نتيجة التكامل:", "B = (μ₀ × I) / (4π × a) × [-cosθ]₀ᵖ = (μ₀ × I) / (4π × a) × [1-(-1)]"),
        ("النتيجة النهائية:", "B = μ₀ × I / (2π × r)"),
    ]

    for i, (desc, formula) in enumerate(steps):
        st.markdown(f"""<div class="step-box">
        <div style="display:flex; align-items:center; gap:0.8rem;">
            <span style="background:linear-gradient(135deg,#06d6a0,#118ab2); color:#0a0e1a; font-weight:700; 
            width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; 
            flex-shrink:0; font-size:0.85rem;">{i+1}</span>
            <div>
                <div style="color:#e8eaed; font-size:0.9rem; margin-bottom:0.4rem;">{desc}</div>
                <div style="font-family:'JetBrains Mono',monospace; color:#06d6a0; font-size:1rem; direction:ltr;">{formula}</div>
            </div>
        </div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.1rem; font-weight:700; color:#06d6a0; margin-bottom:0.8rem;">📋 الاستنتاجات من القانون:</div>', unsafe_allow_html=True)

    conclusions = [
        "المجال المغناطيسي يتناسب طردياً مع التيار الكهربائي I",
        "المجال المغناطيسي يتناسب عكسياً مع المسافة r من الموصل",
        "المجال ثابت عند جميع النقاط الواقعة على محيط دائرة نصف قطرها r",
        "المجال ينعدم عند النقاط الواقعة على امتداد الموصل (θ = 0° أو 180°)",
        "النفاذية المغناطيسية μ₀ تحدد قابلية الوسط لتدفق خطوط المجال",
    ]
    for c in conclusions:
        st.markdown(f"""<div class="card" style="padding:0.8rem 1.2rem; margin:0.3rem 0;">
        <p style="color:#e8eaed; font-size:0.9rem;">✦ {c}</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)