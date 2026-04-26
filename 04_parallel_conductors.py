import streamlit as st
import numpy as np
import plotly.graph_objects as go

MU_0 = 4 * np.pi * 1e-7

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap);
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#06d6a0,#118ab2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">⚡ القوة المغناطيسية بين موصلين متوازيين</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Magnetic Force Between Two Parallel Conductors</div>', unsafe_allow_html=True)

tab_exp, tab_derive, tab_interactive = st.tabs(["🧪 التجربة", "📝 الاشتقاق الرياضي", "🎮 التفاعل"])

with tab_exp:
    st.markdown("""<div class="life-example">
    أسلاك نقل الكهرباء على الأعمدة توضع ببعد محدد عن بعضها - ليس فقط للأمان، بل لأن التيارات المتساوية 
    تجعلها "تتجاذب"! هذا بالضبط ما سنكتشفه في هذه التجربة. في المحطات الكهربائية الكبيرة، 
    يستخدم المهندسون هذه القوة لقياس التيار الكهربائي بدقة (جهاز الأميتر المزدوج).
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">المواد والأدوات:</div>
    <p style="color:#9aa5b4;line-height:2;font-size:.9rem;">
    مصدر طاقة DC منخفض القدرة - ورق مقاومة متغيرة - أسلاك توصيل - أسلاك نحاسية سميكة - 
    قطعة خشب - جهاز أميتر - شريطان من ورق الألمنيوم (18cm × 4cm) - مثقب
    </p></div>""", unsafe_allow_html=True)

    exp_steps = [
        "أثقب قطعة الخشب أربعة ثقوب رفيعة وأثبت فيها أربعة أسلاك نحاسية سميكة",
        "أقص شريطين من ورق الألمنيوم (18cm × 4cm) وأثبت طرفيهما على الأسلاك النحاسية",
        "أركب الدارة الكهربائية بحيث يحمل الموصلان تيارين بالاتجاه نفسه",
        "أشغّل مصدر الطاقة على تيار منخفض لمدة قصيرة وأراقب ما يحدث",
        "أعد التوصيل بحيث يحمل الموصلان تيارين باتجاهين متعاكسين وأكرر الملاحظة",
    ]
    for i, step in enumerate(exp_steps):
        st.markdown(f"""<div style="background:rgba(6,214,160,.05);border:1px solid rgba(6,214,160,.15);border-radius:10px;padding:.8rem 1.2rem;margin:.5rem 0;display:flex;align-items:center;gap:.8rem;">
        <span style="background:linear-gradient(135deg,#06d6a0,#118ab2);color:#0a0e1a;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.85rem;">{i+1}</span>
        <div style="color:#e8eaed;font-size:.95rem;">{step}</div></div>""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">الملاحظة:</div>', unsafe_allow_html=True)

    col_obs1, col_obs2 = st.columns(2)
    with col_obs1:
        st.markdown("""<div class="card" style="border-color:rgba(6,214,160,.4);">
        <div style="font-weight:700;color:#06d6a0;margin-bottom:.5rem;">تياران بنفس الاتجاه:</div>
        <p style="color:#e8eaed;font-size:.95rem;">الشريطان <strong style="color:#06d6a0;">يتقاربان</strong> (قوة تجاذب)</p>
        </div>""", unsafe_allow_html=True)
    with col_obs2:
        st.markdown("""<div class="card" style="border-color:rgba(230,57,70,.4);">
        <div style="font-weight:700;color:#e63946;margin-bottom:.5rem;">تياران باتجاهين متعاكسين:</div>
        <p style="color:#e8eaed;font-size:.95rem;">الشريطان <strong style="color:#e63946;">يتباعدان</strong> (قوة تنافر)</p>
        </div>""", unsafe_allow_html=True)

with tab_derive:
    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">الاشتقاق الرياضي</div>
    <p style="color:#e8eaed;line-height:2;">موصلان متوازيان لا نهائيا الطول يبعدان عن بعضهما مسافة r، يسري فيهما تياران I₁ و I₂</p>
    </div>""", unsafe_allow_html=True)

    deriv_steps = [
        ("الموصل الأول يولد مجالاً عند موقع الموصل الثاني:", "B₁ = μ₀ × I₁ / (2π × r)"),
        ("الموصل الثاني (طوله L) يتأثر بقوة في المجال B₁:", "F₁₂ = B₁ × I₂ × L"),
        ("بالتعويض عن B₁:", "F₁₂ = μ₀ × I₁ × I₂ × L / (2π × r)"),
        ("وبالمثل، القوة على الموصل الأول:", "F₂₁ = μ₀ × I₁ × I₂ × L / (2π × r)"),
        ("القوة لكل وحدة أطوال:", "F/L = μ₀ × I₁ × I₂ / (2π × r)"),
    ]
    for i, (desc, formula) in enumerate(deriv_steps):
        st.markdown(f"""<div style="background:rgba(6,214,160,.05);border:1px solid rgba(6,214,160,.15);border-radius:10px;padding:.8rem 1.2rem;margin:.5rem 0;display:flex;align-items:center;gap:.8rem;">
        <span style="background:linear-gradient(135deg,#06d6a0,#118ab2);color:#0a0e1a;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.85rem;">{i+1}</span>
        <div><div style="color:#e8eaed;font-size:.9rem;margin-bottom:.3rem;">{desc}</div>
        <div style="font-family:'JetBrains Mono',monospace;color:#06d6a0;font-size:1rem;direction:ltr;">{formula}</div></div></div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box" style="font-size:1.4rem;">F/L = μ₀ × I₁ × I₂ / (2π × r)</div>', unsafe_allow_html=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">حالة خاصة - انعدام المجال المحصل:</strong><br>
    <span style="color:#e8eaed;">عند نقطة بين السلكين، إذا كان التياران متعاكسين والنقطة عند مسافتين r₁ و r₂، 
    ينعدم المجال المحصل عندما: I₁/r₁ = I₂/r₂</span>
    </div>""", unsafe_allow_html=True)

with tab_interactive:
    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">🎮 غيّر القيم ولاحظ النتائج!</strong> - اختر اتجاه التيارات وشاهد نوع القوة وخطوط المجال
    </div>""", unsafe_allow_html=True)

    col_p1, col_p2 = st.columns([1, 1.5])
    with col_p1:
        I1 = st.slider("I₁ (A)", 0.5, 50.0, 10.0, 0.5, key='par_i1')
        I2 = st.slider("I₂ (A)", 0.5, 50.0, 10.0, 0.5, key='par_i2')
        r_par = st.slider("المسافة r (m)", 0.01, 0.5, 0.1, 0.01, key='par_r')
        L_par = st.slider("الطول L (m)", 0.1, 2.0, 1.0, 0.1, key='par_l')

        same_dir = st.checkbox("التياران بنفس الاتجاه", value=True)

        F_per_L = MU_0 * I1 * I2 / (2 * np.pi * r_par)
        F_total = F_per_L * L_par
        force_type = "تجاذب ←→" if same_dir else "تنافر →←"

        st.markdown(f"""<div class="formula-box" style="font-size:1rem;">
        F/L = {F_per_L:.4e} N/m<br>
        F = {F_total:.4e} N<br>
        <span style="color:#{'06d6a0' if same_dir else '#e63946'};">نوع القوة: {force_type}</span>
        </div>""", unsafe_allow_html=True)

    with col_p2:
        fig_par = go.Figure()
        half_r = r_par / 2

        # خطوط المجال المحصل
        y_line = np.linspace(-L_par/2, L_par/2, 50)
        t_circle = np.linspace(0, 2*np.pi, 100)

        # المجال من الموصل 1
        for rad in [0.03, 0.06, 0.09]:
            if rad < half_r:
                fig_par.add_trace(go.Scatter(
                    x=-half_r + rad*np.cos(t_circle), y=rad*np.sin(t_circle)*0.3,
                    mode='lines', line=dict(color='rgba(6,214,160,0.25)', width=1, dash='dot'),
                    showlegend=False))

        # المجال من الموصل 2
        for rad in [0.03, 0.06, 0.09]:
            if rad < half_r:
                fig_par.add_trace(go.Scatter(
                    x=half_r + rad*np.cos(t_circle), y=rad*np.sin(t_circle)*0.3,
                    mode='lines', line=dict(color='rgba(239,131,84,0.25)', width=1, dash='dot'),
                    showlegend=False))

        # الموصلات
        fig_par.add_trace(go.Scatter(x=[-half_r]*2, y=[-L_par/2, L_par/2],
                                     mode='lines', line=dict(color='#06d6a0', width=6),
                                     name=f'I₁ = {I1} A'))
        fig_par.add_trace(go.Scatter(x=[half_r]*2, y=[-L_par/2, L_par/2],
                                     mode='lines', line=dict(color='#ef8354', width=6),
                                     name=f'I₂ = {I2} A'))

        # أسهم القوة
        if same_dir:
            fig_par.add_annotation(x=-half_r, y=0, ax=-half_r+0.02, ay=0,
                                   showarrow=True, arrowhead=2, arrowsize=2, arrowcolor='#ffd166')
            fig_par.add_annotation(x=half_r, y=0, ax=half_r-0.02, ay=0,
                                   showarrow=True, arrowhead=2, arrowsize=2, arrowcolor='#ffd166')
        else:
            fig_par.add_annotation(x=-half_r, y=0, ax=-half_r-0.02, ay=0,
                                   showarrow=True, arrowhead=2, arrowsize=2, arrowcolor='#e63946')
            fig_par.add_annotation(x=half_r, y=0, ax=half_r+0.02, ay=0,
                                   showarrow=True, arrowhead=2, arrowsize=2, arrowcolor='#e63946')

        # تسميات
        fig_par.add_annotation(x=-half_r, y=L_par/2+0.05, text=f'I₁={I1}A',
                              showarrow=False, font=dict(color='#06d6a0', size=12))
        fig_par.add_annotation(x=half_r, y=L_par/2+0.05, text=f'I₂={I2}A',
                              showarrow=False, font=dict(color='#ef8354', size=12))

        force_color = '#06d6a0' if same_dir else '#e63946'
        fig_par.add_annotation(x=0, y=-L_par/2-0.1, text=force_type,
                              showarrow=False, font=dict(color=force_color, size=14, weight=700))

        fig_par.update_layout(
            plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
            xaxis=dict(showgrid=False, zeroline=False, range=[-half_r*2, half_r*2]),
            yaxis=dict(showgrid=False, zeroline=False, range=[-L_par/2-0.2, L_par/2+0.15]),
            height=400, margin=dict(t=20, b=30, l=20, r=20),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)', font=dict(size=10))
        )
        st.plotly_chart(fig_par, use_container_width=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)