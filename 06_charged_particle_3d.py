import streamlit as st
import numpy as np
import plotly.graph_objects as go

E_CHARGE = 1.6e-19
PROTON_MASS = 1.67e-27
ELECTRON_MASS = 9.11e-31

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#7b2cbf,#06d6a0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(123,44,191,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">⚛️ حركة جسيم مشحون في مجال مغناطيسي 3D</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Charged Particle Motion in Uniform Magnetic Field</div>', unsafe_allow_html=True)

st.markdown("""<div class="life-example">
تخيّل أنك ترمي كرة في غرفة مليئة بالمروحة الدوارة - الكرة لن تسير في خط مستقيم بل ستنحرف وتدور.
هذا بالضبط ما يحدث للجسيمات المشحونة في المجال المغناطيسي: الإلكترونات في شاشة التلفزيون القديمة 
(شاشة CRT) كانت تُوجّه بمجال مغناطيسي لترسم الصورة على الشاشة!
</div>""", unsafe_allow_html=True)

tab_3d, tab_derive, tab_calc = st.tabs(["🌌 الرسم ثلاثي الأبعاد", "📝 الاشتقاق الرياضي", "🧮 آلة حاسبة"])

with tab_3d:
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">الفكرة:</strong> عندما يتحرك جسيم مشحون بسرعة عمودية على مجال مغناطيسي منتظم، 
    فإن القوة المغناطيسية تعمل كقوة مركزية تجعل الجسيم يتحرك في مسار دائري.
    </div>""", unsafe_allow_html=True)

    col_3d_ctrl, col_3d_viz = st.columns([1, 2])

    with col_3d_ctrl:
        particle = st.selectbox("نوع الجسيم", ["بروتون (+)", "إلكترون (-)", "ألفا (²⁺)"], key='p3d')
        B_3d = st.slider("المجال المغناطيسي B (T)", 0.001, 2.0, 0.1, 0.001, format="%.3f", key='b3d')
        v_3d = st.slider("السرعة v (×10⁶ m/s)", 0.1, 20.0, 5.0, 0.1, key='v3d')
        theta_3d = st.slider("زاوية السرعة مع B (degrees)", 0, 90, 90, 1, key='th3d')
        show_trail = st.checkbox("إظهار المسار الكامل", value=True)

        if particle == "بروتون (+)":
            m_p, q_p, color_p, name_p = PROTON_MASS, E_CHARGE, '#ef8354', 'Proton'
        elif particle == "إلكترون (-)":
            m_p, q_p, color_p, name_p = ELECTRON_MASS, E_CHARGE, '#118ab2', 'Electron'
        else:
            m_p, q_p, color_p, name_p = 4*PROTON_MASS, 2*E_CHARGE, '#7b2cbf', 'Alpha'

        v_val = v_3d * 1e6
        theta_rad = np.radians(theta_3d)
        v_perp = v_val * np.sin(theta_rad)
        v_par = v_val * np.cos(theta_rad)

        r_val = m_p * v_perp / (q_p * B_3d) if B_3d > 0 and v_perp > 0 else 0
        T_val = 2 * np.pi * m_p / (q_p * B_3d) if B_3d > 0 else 0
        f_val = 1 / T_val if T_val > 0 else 0

        st.markdown(f"""<div class="card" style="padding:.8rem;">
        <p style="direction:ltr;text-align:left;color:#9aa5b4;font-size:.85rem;">
        <strong style="color:{color_p};">{name_p}</strong><br>
        r = {r_val:.4e} m<br>
        T = {T_val:.4e} s<br>
        f = {f_val:.4e} Hz<br>
        v⊥ = {v_perp:.4e} m/s<br>
        v∥ = {v_par:.4e} m/s
        </p></div>""", unsafe_allow_html=True)

    with col_3d_viz:
        fig3d = go.Figure()

        # المجال المغناطيسي (أسهم في اتجاه z)
        field_x = [0, 0, 0, 0]
        field_y = [0, 0, 0, 0]
        field_z = [0, 0, 0, 0]
        field_dx = [0, 0, 0, 0]
        field_dy = [0, 0, 0, 0]
        field_dz = [1, 1, 1, 1]
        fig3d.add_trace(go.Cone(x=[0], y=[0], z=[0], u=[0], v=[0], w=[0.5],
                                colorscale=[[0,'#06d6a0'],[1,'#06d6a0']],
                                opacity=0.3, name='B field'))

        # مسار الجسيم
        if r_val > 0:
            if theta_3d == 90:
                # مسار دائري في مستوى xy
                t_path = np.linspace(0, 4*np.pi, 500)
                x_path = r_val * np.cos(t_path)
                y_path = r_val * np.sin(t_path)
                z_path = np.zeros_like(t_path)
            else:
                # مسار حلزوني
                t_path = np.linspace(0, 8*np.pi, 800)
                x_path = r_val * np.cos(t_path)
                y_path = r_val * np.sin(t_path)
                pitch = v_par * T_val
                z_path = pitch * t_path / (2*np.pi)

            # تطبيع للعرض
            scale = 1.0 / max(r_val, 1e-10)
            scale = min(scale, 1e10)
            x_disp = x_path * scale
            y_disp = y_path * scale
            z_disp = z_path * scale

            if show_trail:
                fig3d.add_trace(go.Scatter3d(x=x_disp, y=y_disp, z=z_disp,
                                             mode='lines', line=dict(color=color_p, width=2), opacity=0.6,
                                             name=f'{name_p} path'))

            # الجسيم الحالي
            fig3d.add_trace(go.Scatter3d(x=[x_disp[0]], y=[y_disp[0]], z=[z_disp[0]],
                                         mode='markers', marker=dict(size=10, color=color_p),
                                         name=name_p))

        # أسهم B
        for bx in [-0.5, 0.5]:
            for by in [-0.5, 0.5]:
                fig3d.add_trace(go.Scatter3d(
                    x=[bx, bx], y=[by, by], z=[-1, 1],
                    mode='lines', line=dict(color='rgba(6,214,160,0.2)', width=2, dash='dash'),
                    showlegend=False))
                fig3d.add_trace(go.Scatter3d(x=[bx], y=[by], z=[1], mode='text',
                                    text=['B'], textfont=dict(color='rgba(6,214,160,0.5)', size=10),
                                    showlegend=False))
        z_max = max(np.max(z_disp)*1.2, 2) if r_val > 0 else 2
        xy_max = max(np.max(np.abs(x_disp))*1.5, 1) if r_val > 0 else 1

        fig3d.update_layout(
            scene=dict(
                xaxis=dict(showgrid=False, zeroline=True, zerolinecolor='rgba(6,214,160,0.1)',
                           range=[-xy_max, xy_max], title='X'),
                yaxis=dict(showgrid=False, zeroline=True, zerolinecolor='rgba(6,214,160,0.1)',
                           range=[-xy_max, xy_max], title='Y'),
                zaxis=dict(showgrid=False, zeroline=True, zerolinecolor='rgba(6,214,160,0.1)',
                           range=[-0.5, z_max], title='Z (B direction)'),
                bgcolor='rgba(10,14,26,0.8)'
            ),
            paper_bgcolor='rgba(10,14,26,0.8)',
            font=dict(color='#9aa5b4', size=10),
            height=500, margin=dict(t=10, b=10, l=10, r=10),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)', font=dict(size=9))
        )
        st.plotly_chart(fig3d, use_container_width=True)

        if theta_3d < 90:
            st.markdown("""<div class="info-box">
            <strong style="color:#118ab2;">مسار حلزوني!</strong> عندما تكون السرعة مائلة على المجال المغناطيسي 
            (θ < 90°)، يتحرك الجسيم في مسار حلزوني: دائري في المستوى العمودي على B ومستقيم موازٍ لـ B.
            </div>""", unsafe_allow_html=True)

with tab_derive:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#7b2cbf;margin-bottom:1rem;">الاشتقاق الرياضي - القوة المغناطيسية ونصف القطر</div>
    </div>""", unsafe_allow_html=True)

    deriv = [
        ("القوة المغناطيسية على جسيم مشحون متحرك:", "F = q × v × B × sinθ"),
        ("عندما تكون السرعة عمودية على B (θ = 90°):", "F = q × v × B"),
        ("القوة المغناطيسية تعمل كقوة مركزية (لا تغير السرعة):", "F = m × v² / r"),
        ("بالتساوي:", "q × v × B = m × v² / r"),
        ("نحلل لنصف القطر r:", "r = m × v / (q × B)"),
        ("الدورة الزمنية T (لا تعتمد على السرعة!):", "T = 2π × r / v = 2π × m / (q × B)"),
        ("التردد الدائري f:", "f = 1/T = q × B / (2π × m)"),
    ]
    for i, (desc, formula) in enumerate(deriv):
        st.markdown(f"""<div style="background:rgba(123,44,191,.05);border:1px solid rgba(123,44,191,.15);border-radius:10px;padding:.8rem 1.2rem;margin:.5rem 0;display:flex;align-items:center;gap:.8rem;">
        <span style="background:linear-gradient(135deg,#7b2cbf,#06d6a0);color:#fff;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.85rem;">{i+1}</span>
        <div><div style="color:#e8eaed;font-size:.9rem;margin-bottom:.3rem;">{desc}</div>
        <div style="font-family:'JetBrains Mono',monospace;color:#06d6a0;font-size:1rem;direction:ltr;">{formula}</div></div></div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="formula-box" style="font-size:1.3rem;">F = qvB sinθ &nbsp;&nbsp;|&nbsp;&nbsp; r = mv / (qB) &nbsp;&nbsp;|&nbsp;&nbsp; T = 2πm / (qB)</div>', unsafe_allow_html=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">📌 ملاحظة مهمة جداً:</strong> الدورة الزمنية T والتردد f <strong style="color:#06d6a0;">لا يعتمدان على السرعة v</strong>!
    هذا يعني أن جميع الجسيمات من نفس النوع (نفس m و q) في نفس المجال B لها نفس الدوره الزمنية 
    بغض النظر عن سرعتها. الفرق فقط في نصف قطر المسار (الأسرع → مسار أكبر).
    </div>""", unsafe_allow_html=True)

with tab_calc:
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">🧮 آلة حاسبة تفاعلية</div>', unsafe_allow_html=True)

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        calc_particle = st.selectbox("اختر الجسيم", [
            "بروتون (m=1.67×10⁻²⁷ kg, q=1.6×10⁻¹⁹ C)",
            "إلكترون (m=9.11×10⁻³¹ kg, q=1.6×10⁻¹⁹ C)",
            "ألفا (m=6.68×10⁻²⁷ kg, q=3.2×10⁻¹⁹ C)",
            "مخصص"
        ], key='calc_p')

        if "مخصص" not in calc_particle:
            if "بروتون" in calc_particle:
                m_c, q_c = PROTON_MASS, E_CHARGE
            elif "إلكترون" in calc_particle:
                m_c, q_c = ELECTRON_MASS, E_CHARGE
            else:
                m_c, q_c = 4*PROTON_MASS, 2*E_CHARGE
        else:
            m_c = st.number_input("الكتلة m (kg)", 1e-31, 1e-24, PROTON_MASS, format="%.2e", key='cm')
            q_c = st.number_input("الشحنة q (C)", 1e-21, 1e-16, E_CHARGE, format="%.2e", key='cq')

        B_c = st.number_input("المجال B (T)", 0.001, 10.0, 0.5, format="%.3f", key='cb')
        v_c = st.number_input("السرعة v (m/s)", 1e3, 1e8, 1e6, format="%.2e", key='cv')
        theta_c = st.slider("زاوية θ (degrees)", 0, 90, 90, key='cth')

    with col_c2:
        theta_c_rad = np.radians(theta_c)
        F_c = q_c * v_c * B_c * np.sin(theta_c_rad)
        r_c = m_c * v_c * np.sin(theta_c_rad) / (q_c * B_c) if (q_c * B_c) > 0 else 0
        T_c = 2 * np.pi * m_c / (q_c * B_c) if (q_c * B_c) > 0 else 0
        f_c = 1 / T_c if T_c > 0 else 0

        st.markdown(f"""<div class="formula-box" style="font-size:1.1rem;">
        F = {F_c:.4e} N<br><br>
        r = {r_c:.4e} m<br><br>
        T = {T_c:.4e} s<br><br>
        f = {f_c:.4e} Hz
        </div>""", unsafe_allow_html=True)

        if theta_c == 90:
            st.markdown("""<div class="card" style="border-color:rgba(6,214,160,.3);">
            <p style="color:#06d6a0;font-weight:700;">مسار دائري</p>
            <p style="color:#9aa5b4;">السرعة عمودية تماماً على المجال</p></div>""", unsafe_allow_html=True)
        elif theta_c > 0:
            st.markdown("""<div class="card" style="border-color:rgba(123,44,191,.3);">
            <p style="color:#7b2cbf;font-weight:700;">مسار حلزوني</p>
            <p style="color:#9aa5b4;">السرعة مائلة على المجال - حركة دائرية + انتقالية</p></div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)