import streamlit as st
import numpy as np
import plotly.graph_objects as go

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,#e63946,#ef8354);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(230,57,70,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">💪 القوة المغناطيسية على موصل يحمل تياراً</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Magnetic Force on a Current-Carrying Conductor</div>', unsafe_allow_html=True)

st.markdown("""<div class="life-example">
لماذا يتحرك المحرك الكهربائي؟ عندما يمر تيار في ملف داخل المحرك، يتولد مجال مغناطيسي يتفاعل مع مجال المغناطيس الدائم 
فتنشأ قوة تدور الملف. نفس المبدأ يجعل مروحة السقف تدور والمكبس الكهربائي يعمل وحتى مكبر الصوت في هاتفك يصدر صوتاً!
</div>""", unsafe_allow_html=True)

st.markdown('<div class="formula-box">F = B × I × L × sinθ</div>', unsafe_allow_html=True)

st.markdown("""<div class="card">
<p style="direction:ltr;text-align:left;color:#9aa5b4;line-height:2;font-size:.95rem;">
<strong style="color:#06d6a0;">F</strong> = القوة المغناطيسية (N)<br>
<strong style="color:#06d6a0;">B</strong> = المجال المغناطيسي المنتظم (T)<br>
<strong style="color:#06d6a0;">I</strong> = التيار الكهربائي (A)<br>
<strong style="color:#06d6a0;">L</strong> = طول الموصل في المجال (m)<br>
<strong style="color:#06d6a0;">θ</strong> = الزاوية بين اتجاه التيار واتجاه المجال
</p></div>""", unsafe_allow_html=True)

tab_rule, tab_anim, tab_interactive = st.tabs(["قاعدة اليد اليسرى", "الرسوم المتحركة", "تجربة تفاعلية"])

with tab_rule:
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">قاعدة اليد اليسرى (فلمنغ):</strong> تُستخدم لتحديد اتجاه القوة المغناطيسية على موصل يحمل تياراً
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align:center;margin:1.5rem 0;">
    <svg width="350" height="320" viewBox="0 0 350 320" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="175" cy="170" rx="65" ry="85" fill="rgba(230,57,70,0.12)" stroke="#e63946" stroke-width="2"/>
        <rect x="245" y="158" width="50" height="16" rx="8" fill="rgba(255,209,102,0.3)" stroke="#ffd166" stroke-width="2"/>
        <polygon points="295,162 310,158 310,174" fill="#ffd166"/>
        <text x="310" y="170" fill="#ffd166" font-size="13" font-weight="bold">F</text>
        <rect x="120" y="80" width="16" height="60" rx="8" fill="rgba(6,214,160,0.25)" stroke="#06d6a0" stroke-width="1.5" transform="rotate(-10,128,110)"/>
        <polygon points="122,80 118,62 138,65" fill="#06d6a0"/>
        <text x="80" y="55" fill="#06d6a0" font-size="13" font-weight="bold">B</text>
        <rect x="145" y="82" width="16" height="65" rx="8" fill="rgba(17,138,178,0.25)" stroke="#118ab2" stroke-width="1.5" transform="rotate(5,153,114)"/>
        <polygon points="150,82 155,60 168,65" fill="#118ab2"/>
        <text x="155" y="48" fill="#118ab2" font-size="13" font-weight="bold">I</text>
        <rect x="140" y="245" width="55" height="40" rx="10" fill="rgba(230,57,70,0.08)" stroke="rgba(230,57,70,0.3)" stroke-width="1.5"/>
        <text x="142" y="270" fill="rgba(230,57,70,0.5)" font-size="9">Left Hand</text>
        <text x="50" y="200" fill="#ffd166" font-size="11">Thumb = F</text>
        <text x="50" y="220" fill="#06d6a0" font-size="11">Index = B</text>
        <text x="50" y="240" fill="#118ab2" font-size="11">Middle = I</text>
    </svg>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <p style="color:#e8eaed;line-height:2.2;">
    <strong style="color:#ffd166;">الإبهام</strong> ← اتجاه القوة المغناطيسية F<br>
    <strong style="color:#06d6a0;">السبابة</strong> ← اتجاه المجال المغناطيسي B<br>
    <strong style="color:#118ab2;">الوسطى</strong> ← اتجاه التيار الكهربائي I<br><br>
    <strong style="color:#e63946;">ملاحظة:</strong> نستخدم اليد <strong>اليسرى</strong> هنا (عكس اليد اليمنى للمجال)، 
    لأننا نحدد اتجاه <strong>القوة</strong> وليس اتجاه <strong>المجال</strong>.
    </p></div>""", unsafe_allow_html=True)

with tab_anim:
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">الرسوم المتحركة التوضيحية</div>', unsafe_allow_html=True)

    theta_demo = st.slider("زاوية θ بين التيار والمجال", 0, 180, 90, 1, key='force_th')
    theta_rad = np.radians(theta_demo)

    fig_fa = go.Figure()

    for y in [-0.3, 0, 0.3]:
        fig_fa.add_annotation(x=-0.8, y=y, ax=-0.3, ay=y,
                             showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='#06d6a0')
    fig_fa.add_annotation(x=-0.8, y=0.5, text='B →', showarrow=False,
                         font=dict(color='#06d6a0', size=14, weight=700))

    wire_end_x = 0.5 * np.cos(theta_rad)
    wire_end_y = 0.5 * np.sin(theta_rad)
    fig_fa.add_trace(go.Scatter(x=[0, wire_end_x], y=[0, wire_end_y],
                                mode='lines+markers', line=dict(color='#118ab2', width=5),
                                marker=dict(size=8, color='#118ab2'), name='Conductor (I)'))

    fig_fa.add_annotation(x=wire_end_x/2+0.1, y=wire_end_y/2+0.1,
                         text='I', showarrow=False, font=dict(color='#118ab2', size=16, weight=700))

    F_scale = np.sin(theta_rad)
    if F_scale > 0.01:
        fig_fa.add_annotation(x=0, y=0, ax=0, ay=F_scale*0.4,
                             showarrow=True, arrowhead=3, arrowsize=2, arrowcolor='#ffd166')
        fig_fa.add_annotation(x=0.08, y=F_scale*0.3, text='F',
                             showarrow=False, font=dict(color='#ffd166', size=14, weight=700))
    else:
        fig_fa.add_annotation(x=0.1, y=0, text='F = 0',
                             showarrow=False, font=dict(color='#e63946', size=14, weight=700))

    arc_t = np.linspace(0, theta_rad, 50)
    fig_fa.add_trace(go.Scatter(x=0.2*np.cos(arc_t), y=0.2*np.sin(arc_t),
                                mode='lines', line=dict(color='#7b2cbf', width=2), showlegend=False))
    fig_fa.add_annotation(x=0.25*np.cos(theta_rad/2), y=0.25*np.sin(theta_rad/2),
                         text=f'theta={theta_demo}', showarrow=False,
                         font=dict(color='#7b2cbf', size=12))

    fig_fa.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-1, 1], scaleanchor='y', scaleratio=1),
        yaxis=dict(showgrid=False, zeroline=False, range=[-0.7, 0.7]),
        height=400, margin=dict(t=20, b=20, l=20, r=20)
    )
    st.plotly_chart(fig_fa, use_container_width=True)

    if theta_demo == 0 or theta_demo == 180:
        st.markdown("""<div class="card" style="border-color:rgba(230,57,70,.4);">
        <p style="color:#e63946;font-weight:700;">F = 0!</p>
        <p style="color:#9aa5b4;">عندما يكون الموصل موازياً للمجال لا تنشأ قوة مغناطيسية</p></div>""", unsafe_allow_html=True)
    elif theta_demo == 90:
        st.markdown("""<div class="card" style="border-color:rgba(6,214,160,.4);">
        <p style="color:#06d6a0;font-weight:700;">F = BIL (maximum force)!</p>
        <p style="color:#9aa5b4;">عندما يكون الموصل عمودياً على المجال تكون القوة أكبر ما يمكن</p></div>""", unsafe_allow_html=True)

with tab_interactive:
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">Change values and observe</div>', unsafe_allow_html=True)

    col_f1, col_f2 = st.columns([1, 1.5])
    with col_f1:
        B_f = st.slider("B (T)", 0.01, 2.0, 0.5, 0.01, key='fb')
        I_f = st.slider("I (A)", 0.1, 30.0, 5.0, 0.1, key='fi')
        L_f = st.slider("L (m)", 0.05, 2.0, 0.3, 0.05, key='fl')
        theta_f = st.slider("theta (degrees)", 0, 180, 90, 1, key='fth')

        F_val = B_f * I_f * L_f * np.sin(np.radians(theta_f))

        st.markdown(f"""<div class="formula-box" style="font-size:1.2rem;">
        F = {F_val:.4e} N
        </div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="card" style="padding:.8rem;">
        <p style="direction:ltr;text-align:left;color:#9aa5b4;font-size:.85rem;">
        F = {B_f} x {I_f} x {L_f} x sin({theta_f})<br>
        = {B_f} x {I_f} x {L_f} x {np.sin(np.radians(theta_f)):.4f}<br>
        = {F_val:.4e} N
        </p></div>""", unsafe_allow_html=True)

    with col_f2:
        th_range = np.linspace(0, 180, 200)
        F_range = B_f * I_f * L_f * np.sin(np.radians(th_range))

        fig_fi = go.Figure()
        fig_fi.add_trace(go.Scatter(x=th_range, y=F_range*1e3, line=dict(color='#06d6a0', width=3), name='F(theta)'))
        fig_fi.add_scatter(x=[theta_f], y=[F_val*1e3], mode='markers',
                          marker=dict(size=12, color='#ffd166'), name='Current theta')
        fig_fi.add_vline(x=theta_f, line_dash='dash', line_color='rgba(255,209,102,0.3)')

        fig_fi.update_layout(
            title=dict(text='F vs theta', font=dict(color='#06d6a0')),
            plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
            font=dict(color='#9aa5b4'), xaxis_title='theta (degrees)', yaxis_title='F (mN)',
            height=350, margin=dict(t=40, b=30, l=50, r=20),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)', font=dict(size=9))
        )
        st.plotly_chart(fig_fi, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    fig_f3d = go.Figure()

    fig_f3d.add_trace(go.Scatter3d(x=[0,1], y=[0,0], z=[0,0], mode='lines',
                                   line=dict(color='#06d6a0', width=4), name='B'))
    fig_f3d.add_trace(go.Scatter3d(x=[1.1], y=[0], z=[0], mode='text',
                                   text=['B'], textfont=dict(color='#06d6a0', size=14),
                                   showlegend=False))

    fig_f3d.add_trace(go.Scatter3d(x=[0,0], y=[0,0.8], z=[0,0], mode='lines',
                                   line=dict(color='#118ab2', width=4), name='I'))
    fig_f3d.add_trace(go.Scatter3d(x=[0], y=[0.9], z=[0], mode='text',
                                   text=['I'], textfont=dict(color='#118ab2', size=14),
                                   showlegend=False))

    fig_f3d.add_trace(go.Scatter3d(x=[0,0], y=[0,0], z=[0,0.6], mode='lines',
                                   line=dict(color='#ffd166', width=4), name='F'))
    fig_f3d.add_trace(go.Scatter3d(x=[0], y=[0], z=[0.7], mode='text',
                                   text=['F'], textfont=dict(color='#ffd166', size=14),
                                   showlegend=False))

    fig_f3d.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers',
                                   marker=dict(size=8, color='white'), showlegend=False))

    fig_f3d.update_layout(
        scene=dict(xaxis=dict(showgrid=False, range=[-0.2,1.3]),
                   yaxis=dict(showgrid=False, range=[-0.2,1.1]),
                   zaxis=dict(showgrid=False, range=[-0.2,0.9]),
                   bgcolor='rgba(10,14,26,0.8)'),
        paper_bgcolor='rgba(10,14,26,0.8)', height=350, margin=dict(t=10, b=10, l=10, r=10),
        legend=dict(bgcolor='rgba(26,34,54,0.8)', font=dict(size=9))
    )
    st.plotly_chart(fig_f3d, use_container_width=True)
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">F = IL x B</strong> - القوة عمودية دائماً على كل من التيار والمجال
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)