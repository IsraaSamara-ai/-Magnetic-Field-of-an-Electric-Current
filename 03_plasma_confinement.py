import streamlit as st
import numpy as np
import plotly.graph_objects as go

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#06d6a0,#ef8354);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
@keyframes plasma-glow{0%,100%{filter:brightness(1) drop-shadow(0 0 8px rgba(255,100,50,0.5))}50%{filter:brightness(1.3) drop-shadow(0 0 20px rgba(255,100,50,0.8))}}
@keyframes field-rotate{from{stroke-dashoffset:0}to{stroke-dashoffset:-40}}
.plasma-anim{animation:plasma-glow 1.5s ease-in-out infinite}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">🔥 احتواء البلازما بالمجال المغناطيسي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Plasma Confinement by Magnetic Fields</div>', unsafe_allow_html=True)

st.markdown("""<div class="life-example">
تخيّل أن لديك قدراً يغلي بملايين الدرجات - أي مادة ستذوب فوراً! لكن الشمس تفعل هذا كل يوم.
    كيف تحتفظ الشمس بمادتها؟ الإجابة: الجاذبية. أما على الأرض فنحتاج بديلاً - والمجال المغناطيسي هو الحل!
    فكرة احتواء البلازما تشبه "حبس النار في قفص غير مرئي مصنوع من المجال المغناطيسي".
</div>""", unsafe_allow_html=True)

tab_explain, tab_anim, tab_tech = st.tabs(["الشرح العلمي", "الرسوم المتحركة", "التطبيقات التكنولوجية"])

with tab_explain:
    st.markdown("""<div class="card">
    <div style="font-size:1.2rem;font-weight:700;color:#ef8354;margin-bottom:1rem;">ما هي البلازما؟</div>
    <p style="color:#e8eaed;line-height:2.2;font-size:1rem;">
    البلازما هي الحالة الرابعة للمادة (بعد الصلب والسائل والغاز). تتكون عندما تُزال الإلكترونات من الذرات 
    عند درجات حرارة عالية جداً (ملايين الدرجات المئوية)، فتصبح المادة عبارة عن:
    </p>
    <ul style="color:#e8eaed;line-height:2;font-size:0.95rem;padding-right:1.5rem;">
        <li><strong style="color:#e63946;">أيونات موجبة</strong> - ذرات فقدت إلكتروناتها</li>
        <li><strong style="color:#118ab2;">إلكترونات سالبة</strong> - جسيمات حرة متحركة</li>
    </ul>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">لماذا نحتاج احتواء البلازما؟</strong><br><br>
    <span style="color:#e8eaed;line-height:2;">
    في مفاعلات الاندماج النووي (مثل مفاعل الطاقة المستقبلية)، نحتاج لدمج نوى الذرات معاً لإنتاج طاقة هائلة. 
    هذا يحتاج درجات حرارة تتجاوز <strong style="color:#ef8354;">100 مليون درجة مئوية</strong>. 
    لا يمكن احتواء البلازما في أي وعاء مادي لأنها ستصهره!
    </span>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-size:1.2rem;font-weight:700;color:#06d6a0;margin-bottom:1rem;">كيف يحتوي المجال المغناطيسي البلازما؟</div>
    <p style="color:#e8eaed;line-height:2.2;font-size:1rem;">
    لأن البلازما تتكون من <strong style="color:#ffd166;">جسيمات مشحونة متحركة</strong> (أيونات + إلكترونات)، 
    فإنها تتأثر بالقوة المغناطيسية عند وجود مجال مغناطيسي خارجي. هذه القوة تجعل الجسيمات:
    </p>
    </div>""", unsafe_allow_html=True)

    steps_plasma = [
        ("تتحرك في مسارات حلزونية", "بدلاً من Escape في خط مستقيم، تدور الجسيمات حول خطوط المجال المغناطيسي"),
        ("تبقى محتجزة", "القوة المغناطيسية F = qv×B تعمل كقوة مركزية تحافظ على الجسيمات داخل حيز محدد"),
        ("لا تلامس الجدران", "بما أن الجسيمات تدور ولا تصل للجدران، لا داعي لوعاء مادي يتحمل الحرارة"),
    ]
    for i, (title, desc) in enumerate(steps_plasma):
        st.markdown(f"""<div style="background:rgba(6,214,160,.05);border:1px solid rgba(6,214,160,.15);border-radius:10px;padding:.8rem 1.2rem;margin:.5rem 0;display:flex;align-items:center;gap:.8rem;">
        <span style="background:linear-gradient(135deg,#06d6a0,#118ab2);color:#0a0e1a;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.85rem;">{i+1}</span>
        <div><div style="color:#e8eaed;font-weight:600;font-size:.95rem;">{title}</div><div style="color:#9aa5b4;font-size:.85rem;">{desc}</div></div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">F = q × v × B × sinθ</div>', unsafe_allow_html=True)
    st.markdown("""<div class="card">
    <p style="color:#9aa5b4;font-size:.9rem;direction:ltr;text-align:left;">
    F = القوة المغناطيسية (N)<br>
    q = شحنة الجسيم (C)<br>
    v = سرعة الجسيم (m/s)<br>
    B = المجال المغناطيسي (T)<br>
    θ = الزاوية بين v و B
    </p></div>""", unsafe_allow_html=True)

with tab_anim:
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;text-align:center;">حركة الجسيمات المشحونة في المجال المغناطيسي</div>', unsafe_allow_html=True)

    B_conf = st.slider("قوة المجال المغناطيسي B (T)", 0.1, 5.0, 1.0, 0.1, key='plasma_b')
    v_conf = st.slider("سرعة الجسيم v (×10⁶ m/s)", 0.1, 10.0, 2.0, 0.1, key='plasma_v')
    show_electrons = st.checkbox("إظهار الإلكترونات (سالب)", value=True)
    show_ions = st.checkbox("إظهار الأيونات (موجب)", value=True)

    fig_p = go.Figure()

    if show_electrons:
        q_e = 1.6e-19
        m_e = 9.11e-31
        v_e = v_conf * 1e6
        r_e = m_e * v_e / (q_e * B_conf)
        theta_anim = np.linspace(0, 6*np.pi, 500)
        x_e = r_e * np.cos(theta_anim) * 1e3
        y_e = r_e * np.sin(theta_anim) * 1e3
        colors_e = np.sin(theta_anim * 2) * 0.5 + 0.5
        fig_p.add_trace(go.Scatter(x=x_e, y=y_e, mode='lines',
                                   line=dict(color='#118ab2', width=2), name='Electron path'))
        fig_p.add_trace(go.Scatter(x=[x_e[0]], y=[y_e[0]], mode='markers',
                                   marker=dict(size=12, color='#118ab2', symbol='circle'),
                                   name='e⁻'))
        st.markdown(f"""<div class="card" style="padding:.6rem 1rem;">
        <p style="color:#118ab2;font-size:.85rem;direction:ltr;text-align:left;">
        Electron: r = mv/(qB) = {r_e*1e3:.4f} mm, f = qB/(2πm) = {q_e*B_conf/(2*np.pi*m_e):.2e} Hz
        </p></div>""", unsafe_allow_html=True)

    if show_ions:
        q_i = 1.6e-19
        m_i = 1.67e-27
        v_i = v_conf * 1e6 * 0.1
        r_i = m_i * v_i / (q_i * B_conf)
        theta_anim_i = np.linspace(0, 4*np.pi, 500)
        x_i = r_i * np.cos(theta_anim_i) * 1e3
        y_i = r_i * np.sin(theta_anim_i) * 1e3
        fig_p.add_trace(go.Scatter(x=x_i, y=y_i, mode='lines',
                                   line=dict(color='#e63946', width=2), name='Ion path'))
        fig_p.add_trace(go.Scatter(x=[x_i[0]], y=[y_i[0]], mode='markers',
                                   marker=dict(size=14, color='#e63946', symbol='circle'),
                                   name='Ion⁺'))
        st.markdown(f"""<div class="card" style="padding:.6rem 1rem;">
        <p style="color:#e63946;font-size:.85rem;direction:ltr;text-align:left;">
        Ion: r = mv/(qB) = {r_i*1e3:.2f} mm, f = qB/(2πm) = {q_i*B_conf/(2*np.pi*m_i):.2e} Hz
        </p></div>""", unsafe_allow_html=True)

    # خطوط المجال
    fig_p.add_hline(y=0, line_dash='dot', line_color='rgba(6,214,160,0.3)')
    fig_p.add_annotation(x=0, y=0, text='B ⊙', showarrow=False, font=dict(size=16, color='#06d6a0'))

    fig_p.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, title='x (mm)'),
        yaxis=dict(showgrid=False, zeroline=False, title='y (mm)', scaleanchor='x', scaleratio=1),
        height=450, margin=dict(t=20, b=40, l=50, r=20),
        legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)', font=dict(size=10))
    )
    st.plotly_chart(fig_p, use_container_width=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">📌 ملاحظة مهمة:</strong> نصف قطر مسار الإلكترون أصغر بكثير من نصف قطر مسار الأيون 
    لأن كتلة الإلكترون أصغر بكثير. هذا يعني أن الإلكترونات تكون "محتجزة" بشكل أسرع من الأيونات.
    </div>""", unsafe_allow_html=True)

    # رسم توضيحي للاحتواء
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;text-align:center;">مقطع عرضي للاحتواء المغناطيسي (Tokamak)</div>', unsafe_allow_html=True)

    fig_tok = go.Figure()
    # الجدران
    wall_t = np.linspace(0, 2*np.pi, 100)
    R_wall = 1.0
    fig_tok.add_trace(go.Scatter(x=R_wall*np.cos(wall_t), y=R_wall*np.sin(wall_t),
                                 mode='lines', line=dict(color='rgba(255,255,255,0.3)', width=3),
                                 name='Reactor wall'))

    # المجال المغناطيسي - دوائر متحدة المركز
    for r_field in [0.2, 0.4, 0.6, 0.8]:
        fig_tok.add_trace(go.Scatter(x=r_field*np.cos(wall_t), y=r_field*np.sin(wall_t),
                                     mode='lines', line=dict(color='rgba(6,214,160,0.2)', width=1, dash='dot'),
                                     showlegend=False))

    # جسيمات البلازما
    np.random.seed(42)
    n_particles = 60
    r_parts = np.random.uniform(0.1, 0.7, n_particles)
    angles = np.random.uniform(0, 2*np.pi, n_particles)
    fig_tok.add_trace(go.Scatter(x=r_parts*np.cos(angles), y=r_parts*np.sin(angles),
                                 mode='markers',
                                 marker=dict(size=np.random.uniform(4, 10, n_particles),
                                            color=['#118ab2' if i % 3 != 0 else '#e63946' for i in range(n_particles)],
                                            opacity=0.7),
                                 name='Plasma particles', showlegend=False))

    fig_tok.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-1.3, 1.3], scaleanchor='y', scaleratio=1),
        yaxis=dict(showgrid=False, zeroline=False, range=[-1.3, 1.3]),
        height=450, margin=dict(t=10, b=10, l=10, r=10)
    )
    st.plotly_chart(fig_tok, use_container_width=True)

with tab_tech:
    st.markdown("""<div class="card">
    <div style="font-size:1.2rem;font-weight:700;color:#ef8354;margin-bottom:1rem;">التطبيقات التكنولوجية</div>
    </div>""", unsafe_allow_html=True)

    apps = [
        ("مفاعلات الاندماج النووي (Tokamak)", 
         "أكبر مشروع هو ITER في فرنسا - مفاعل ضخم يستخدم مجالات مغناطيسية قوية جداً لاحتواء بلازما بدرجة حرارة 150 مليون درجة. الهدف: إنتاج طاقة نظيفة وغير محدودة من الاندماج النووي نفسه الذي يحدث في الشمس.",
         "#ef8354"),
        ("معالجة النفايات النووية",
         "يمكن استخدام البلازما المحتجزة مغناطيسياً لتدمير النفايات النووية الخطرة وتحويلها إلى مواد أقل خطورة.",
         "#e63946"),
        ("تصنيع أشباه الموصلات",
         "البلازما المحتجزة تُستخدم في عملية النقش (Etching) لصنع رقائق الإلكترونيات الدقيقة جداً في الهواتف والحاسوب.",
         "#06d6a0"),
        ("محركات الدفع الفضائي",
         "محركات البلازما الأيونية في المركبات الفضائية تستخدم مجالات مغناطيسية لتوجيه البلازمة وإنتاج الدفع.",
         "#118ab2"),
    ]
    for title, desc, color in apps:
        st.markdown(f"""<div class="card" style="border-left:4px solid {color};">
        <div style="font-weight:700;color:{color};margin-bottom:.5rem;font-size:1rem;">{title}</div>
        <p style="color:#9aa5b4;line-height:1.9;font-size:.9rem;">{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)