import streamlit as st
import numpy as np
import plotly.graph_objects as go

MU_0 = 4 * np.pi * 1e-7

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#06d6a0,#118ab2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem;font-size:.9rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">المجال المغناطيسي من الموصلات</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Magnetic Field of Current-Carrying Conductors</div>', unsafe_allow_html=True)

tab_wire, tab_coil, tab_solenoid, tab_hand = st.tabs(["سلك مستقيم", "ملف دائري", "ملف لولبي", "قاعدة اليد اليمنى"])

# ==================== سلك مستقيم ====================
with tab_wire:
    st.markdown("""<div class="life-example">
    عندما تقترب من خط نقل كهرباء عالي الجهد (التيارات الكبيرة)، يمكنك الشعور بتأثير المجال المغناطيسي 
    لو كنت تحمل بوصلة - وكلما ابتعدت عن السلك، يضعف المجال. هذا بالضبط ما يصفه القانون: B = μ₀I/(2πr)
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">B = μ₀ × I / (2π × r)</div>', unsafe_allow_html=True)

    col_ctrl, col_plot = st.columns([1, 1.5])
    with col_ctrl:
        I = st.slider("التيار I (A)", 0.5, 30.0, 5.0, 0.5)
        r_max = st.slider("أقصى مسافة للعرض (m)", 0.05, 0.5, 0.2, 0.01)
        direction = st.selectbox("اتجاه التيار", ["داخل الصفحة ⊗", "خارج الصفحة ⊙"])

        r_vals = np.linspace(0.01, r_max, 200)
        B_vals = MU_0 * I / (2 * np.pi * r_vals)

        st.markdown(f"""<div class="card">
        <p style="direction:ltr;text-align:left;color:#9aa5b4;font-size:.9rem;">
        at r = 0.05 m: B = {MU_0*I/(2*np.pi*0.05):.4e} T<br>
        at r = {r_max:.2f} m: B = {MU_0*I/(2*np.pi*r_max):.4e} T<br>
        Ratio: {MU_0*I/(2*np.pi*0.05) / (MU_0*I/(2*np.pi*r_max)):.1f}x
        </p></div>""", unsafe_allow_html=True)

    with col_plot:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=r_vals, y=B_vals * 1e6, line=dict(color='#06d6a0', width=3), name='B(r)'))
        fig.add_annotation(x=r_vals[len(r_vals)//4], y=B_vals[len(B_vals)//4]*1e6,
                           text='B ∝ 1/r', showarrow=True, arrowcolor='#ef8354',
                           font=dict(color='#ef8354', size=13))
        fig.update_layout(
            title=dict(text='B vs r (Straight Wire)', font=dict(color='#06d6a0', size=14)),
            plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
            font=dict(color='#9aa5b4'), xaxis_title='r (m)', yaxis_title='B (μT)',
            height=400, margin=dict(t=50, b=30, l=50, r=20),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)')
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">خطوط المجال المغناطيسي حول السلك:</div>', unsafe_allow_html=True)

    fig2 = go.Figure()
    colors_circle = ['#06d6a0', '#118ab2', '#ef8354', '#7b2cbf', '#e63946', '#ffd166']
    radii = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18]
    t = np.linspace(0, 2*np.pi, 100)

    for i, rad in enumerate(radii):
        if rad <= r_max:
            fig2.add_trace(go.Scatter(x=rad*np.cos(t), y=rad*np.sin(t),
                                      mode='lines', line=dict(color=colors_circle[i%len(colors_circle)], width=2),
                                      showlegend=False))
            for angle in [0, np.pi/2, np.pi, 3*np.pi/2]:
                if direction == "داخل الصفحة ⊗":
                    dx = -np.sin(angle) * 0.015
                    dy = np.cos(angle) * 0.015
                else:
                    dx = np.sin(angle) * 0.015
                    dy = -np.cos(angle) * 0.015
                fig2.add_annotation(x=rad*np.cos(angle), y=rad*np.sin(angle),
                                    ax=rad*np.cos(angle)+dx, ay=rad*np.sin(angle)+dy,
                                    showarrow=True, arrowhead=2, arrowsize=1.2,
                                    arrowcolor=colors_circle[i%len(colors_circle)])

    if direction == "داخل الصفحة ⊗":
        fig2.add_annotation(x=0, y=0, text='⊗', showarrow=False, font=dict(size=30, color='#e63946'))
    else:
        fig2.add_annotation(x=0, y=0, text='⊙', showarrow=False, font=dict(size=30, color='#06d6a0'))

    fig2.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, scaleanchor='y', scaleratio=1, range=[-r_max*1.2, r_max*1.2]),
        yaxis=dict(showgrid=False, zeroline=False, range=[-r_max*1.2, r_max*1.2]),
        height=450, margin=dict(t=10, b=10, l=10, r=10)
    )
    st.plotly_chart(fig2, use_container_width=True)

# ==================== ملف دائري ====================
with tab_coil:
    st.markdown("""<div class="life-example">
    المغانط الكهربائية المستخدمة في الأجهزة الطبية مثل جهاز MRI تحتوي على ملفات دائرية ضخمة 
    تحمل تيارات كهربائية كبيرة لتوليد مجال مغناطيسي قوي جداً. المحرك الكهربائي في غسالة الملابس 
    يحتوي أيضاً على ملفات دائرية.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">B = μ₀ × I × N / (2 × R)</div>', unsafe_allow_html=True)

    col_c1, col_c2 = st.columns([1, 1.5])
    with col_c1:
        I_coil = st.slider("التيار I (A)", 0.5, 20.0, 5.0, 0.5, key='coil_i')
        N_coil = st.slider("عدد اللفات N", 1, 100, 10, 1, key='coil_n')
        R_coil = st.slider("نصف القطر R (m)", 0.01, 0.5, 0.1, 0.01, key='coil_r')

        B_coil = MU_0 * I_coil * N_coil / (2 * R_coil)
        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        B = {B_coil:.4e} T
        </div>""", unsafe_allow_html=True)

    with col_c2:
        fig_c = go.Figure()
        theta_c = np.linspace(0, 2*np.pi, 200)
        fig_c.add_trace(go.Scatter(x=R_coil*np.cos(theta_c), y=R_coil*np.sin(theta_c),
                                   mode='lines', line=dict(color='#06d6a0', width=4), name='Coil'))
        arrow_angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
        for a in arrow_angles:
            dx = -np.sin(a) * 0.03
            dy = np.cos(a) * 0.03
            fig_c.add_annotation(x=R_coil*np.cos(a), y=R_coil*np.sin(a),
                                ax=R_coil*np.cos(a)+dx, ay=R_coil*np.sin(a)+dy,
                                showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='#ffd166')
        fig_c.add_annotation(x=0, y=0, text='B ⊙', showarrow=False, font=dict(size=18, color='#ef8354'))
        for mult in [0.3, 0.6]:
            fig_c.add_trace(go.Scatter(x=mult*R_coil*np.cos(theta_c), y=mult*R_coil*np.sin(theta_c),
                                       mode='lines', line=dict(color='rgba(6,214,160,0.3)', width=1, dash='dot'), showlegend=False))
        lim = R_coil * 1.5
        fig_c.update_layout(
            plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
            xaxis=dict(showgrid=False, zeroline=False, range=[-lim, lim], scaleanchor='y', scaleratio=1),
            yaxis=dict(showgrid=False, zeroline=False, range=[-lim, lim]),
            height=400, margin=dict(t=10, b=10, l=10, r=10)
        )
        st.plotly_chart(fig_c, use_container_width=True)

# ==================== ملف لولبي ====================
with tab_solenoid:
    st.markdown("""<div class="life-example">
    الملف اللولبي هو أساس عمل العديد من الأجهزة: الصمامات الكهربائية في الغسالات، أقفال الأبواب الإلكترونية، 
    وحتى الحلقات الكهربائية في إشارات المرور. كلها تعتمد على توليد مجال مغناطيسي منتظم داخل الملف اللولبي.
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">B = μ₀ × I × n &nbsp;&nbsp; (where n = N / l)</div>', unsafe_allow_html=True)

    col_s1, col_s2 = st.columns([1, 1.5])
    with col_s1:
        I_sol = st.slider("التيار I (A)", 0.5, 15.0, 5.0, 0.5, key="sol_i")
        N_sol = st.slider("عدد اللفات الكلي N", 50, 5000, 1400, 50, key="sol_n")
        l_sol = st.slider("الطول l (m)", 0.1, 2.0, 1.0, 0.05, key="sol_l")

        n_sol = N_sol / l_sol
        B_sol = MU_0 * I_sol * n_sol

        st.markdown(f"""<div class="card">
        <p style="direction:ltr;text-align:left;color:#9aa5b4;font-size:.9rem;">
        n = N/l = {N_sol}/{l_sol:.2f} = {n_sol:.1f} turns/m<br>
        B = {B_sol:.4e} T = {B_sol*1e3:.4f} mT
        </p></div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        B = {B_sol:.4e} T
        </div>""", unsafe_allow_html=True)

    with col_s2:
        fig_s = go.Figure()
        R_sol_vis = 0.15
        n_vis = min(N_sol, 30)
        coil_positions = np.linspace(-l_sol/2, l_sol/2, int(n_vis))

        for i, pos in enumerate(coil_positions):
            alpha = 0.3 + 0.7 * (i / max(len(coil_positions)-1, 1))
            theta_vis = np.linspace(0, 2*np.pi, 60)
            fig_s.add_trace(go.Scatter(
                x=pos * np.ones_like(theta_vis) + 0.01 * np.cos(theta_vis),
                y=R_sol_vis * np.sin(theta_vis),
                mode="lines",
                line=dict(color=f"rgba(6,214,160,{alpha})", width=1.5),
                showlegend=False
            ))

        for y_off in [-0.08, 0, 0.08]:
            fig_s.add_trace(go.Scatter(
                x=[-l_sol/2*0.9, l_sol/2*0.9], y=[y_off, y_off],
                mode="lines", line=dict(color="#ef8354", width=2), showlegend=False
            ))
            fig_s.add_annotation(
                x=l_sol/2*0.85, y=y_off, ax=l_sol/2*0.95, ay=y_off,
                showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor="#ef8354"
            )

        fig_s.add_annotation(
            x=l_sol/2+0.05, y=0, text="N", showarrow=False,
            font=dict(size=20, color="#e63946")
        )
        fig_s.add_annotation(
            x=-l_sol/2-0.08, y=0, text="S", showarrow=False,
            font=dict(size=20, color="#118ab2")
        )

        fig_s.update_layout(
            plot_bgcolor="rgba(10,14,26,0.8)",
            paper_bgcolor="rgba(10,14,26,0.8)",
            xaxis=dict(showgrid=False, zeroline=False, range=[-l_sol/2-0.2, l_sol/2+0.2]),
            yaxis=dict(showgrid=False, zeroline=False, range=[-0.3, 0.3], scaleanchor="x", scaleratio=3),
            height=400, margin=dict(t=10, b=10, l=10, r=10)
        )
        st.plotly_chart(fig_s, use_container_width=True)

# ==================== قاعدة اليد اليمنى ====================
with tab_hand:
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;"> قاعدة اليد اليمنى:</strong> تُستخدم لتحديد اتجاه المجال المغناطيسي. 
    يشير الإبهام إلى اتجاه التيار، وتُلفّ الأصابع حَوْل الموصل فيشير اتجاه دورانها إلى اتجاه المجال المغناطيسي.
    </div>""", unsafe_allow_html=True)

    hand_type = st.selectbox("اختر نوع الموصل", [
        "موصل مستقيم (الإبهام ـ اتجاه التيار)",
        "ملف دائري (الأصابع ـ اتجاه التيار، الإبهام ـ اتجاه B)",
        "ملف لولبي (الأصابع ـ اتجاه التيار، الإبهام ـ اتجاه B)"
    ])

    thumb_label = "I (تيار)" if "مستقيم" in hand_type else "B (مجال)"
    curl_label = "B (مجال)" if "مستقيم" in hand_type else "I (تيار)"

    st.markdown(f"""<div style="text-align:center;margin:1.5rem 0;">
    <svg width="320" height="340" viewBox="0 0 320 340" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <style>
                @keyframes thumbPulse {{ 0%, 100% {{ transform: rotate(-30deg); }} 50% {{ transform: rotate(-38deg); }} }}
                @keyframes fingerWave {{ 0%, 100% {{ transform: rotate(0deg); }} 50% {{ transform: rotate(8deg); }} }}
                @keyframes arrowSpin {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
                .thumb {{ animation: thumbPulse 2s ease-in-out infinite; transform-origin: 100px 169px; }}
                .f1 {{ animation: fingerWave 2.5s ease-in-out infinite; transform-origin: 103px 142px; }}
                .f2 {{ animation: fingerWave 2.5s ease-in-out 0.2s infinite; transform-origin: 126px 139px; }}
                .f3 {{ animation: fingerWave 2.5s ease-in-out 0.4s infinite; transform-origin: 148px 141px; }}
                .f4 {{ animation: fingerWave 2.5s ease-in-out 0.6s infinite; transform-origin: 170px 146px; }}
                .spin-arrow {{ animation: arrowSpin 4s linear infinite; transform-origin: 160px 200px; }}
            </style>
        </defs>
        <ellipse cx="160" cy="200" rx="68" ry="88" fill="rgba(6,214,160,0.1)" stroke="#06d6a0" stroke-width="2"/>
        <g class="thumb">
            <rect x="80" y="160" width="45" height="18" rx="9" fill="rgba(239,131,84,0.3)" stroke="#ef8354" stroke-width="2"/>
            <polygon points="78,162 65,150 82,155" fill="#ef8354"/>
        </g>
        <text x="40" y="155" fill="#ef8354" font-size="13" font-weight="bold">{thumb_label}</text>
        <g class="f1"><rect x="95" y="115" width="16" height="55" rx="8" fill="rgba(6,214,160,0.25)" stroke="#06d6a0" stroke-width="1.5"/></g>
        <g class="f2"><rect x="118" y="108" width="16" height="62" rx="8" fill="rgba(6,214,160,0.25)" stroke="#06d6a0" stroke-width="1.5"/></g>
        <g class="f3"><rect x="140" y="113" width="16" height="57" rx="8" fill="rgba(6,214,160,0.25)" stroke="#06d6a0" stroke-width="1.5"/></g>
        <g class="f4"><rect x="162" y="122" width="15" height="48" rx="7" fill="rgba(6,214,160,0.25)" stroke="#06d6a0" stroke-width="1.5"/></g>
        <g class="spin-arrow">
            <path d="M 215 150 A 65 65 0 0 1 215 250" fill="none" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="6,3"/>
            <polygon points="215,250 224,238 208,242" fill="#ffd166"/>
        </g>
        <text x="225" y="205" fill="#ffd166" font-size="13" font-weight="bold">{curl_label}</text>
        <rect x="130" y="278" width="60" height="45" rx="10" fill="rgba(6,214,160,0.08)" stroke="rgba(6,214,160,0.25)" stroke-width="1.5"/>
        <text x="135" y="305" fill="rgba(6,214,160,0.4)" font-size="9">Right Hand</text>
    </svg>
    </div>""", unsafe_allow_html=True)

    if "مستقيم" in hand_type:
        st.markdown("""<div class="card">
        <p style="color:#e8eaed;line-height:2.2;">
        <strong style="color:#ef8354;">الإبهام</strong> - يشير إلى اتجاه التيار الكهربائي في الموصل<br>
        <strong style="color:#06d6a0;">الأصابع الأربعة</strong> - تلف حول الموصل، اتجاه دورانها = اتجاه المجال المغناطيسي<br>
        <strong style="color:#ffd166;">النتيجة:</strong> خطوط المجال تشكل دوائر متحدة المركز حول الموصل
        </p></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="card">
        <p style="color:#e8eaed;line-height:2.2;">
        <strong style="color:#06d6a0;">الأصابع الأربعة</strong> - تشير إلى اتجاه التيار في اللفات<br>
        <strong style="color:#ef8354;">الإبهام</strong> - يشير إلى اتجاه المجال المغناطيسي (نحو القطب الشمالي)<br>
        <strong style="color:#ffd166;">النتيجة:</strong> المجال داخل الملف يكون منتظما ومتوازيا
        </p></div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)