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
.section-title{font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,#ffd166,#ef8354);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"💡 من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(255,209,102,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">🔬 مطياف الكتلة والسينكروترون</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Mass Spectrometer & Synchrotron Accelerator</div>', unsafe_allow_html=True)

tab_mass, tab_sync, tab_apps = st.tabs(["مطياف الكتلة", "مسرّع السينكروترون", "مجالات الاستخدام"])

with tab_mass:
    st.markdown("""<div class="life-example">
    مطياف الكتلة يشبه "الميزان الذري" - لكن بدلاً من وزن الأشياء، يفصل الذرات حسب كتلتها. 
    يُستخدم في الطب الشرعي لتحليل العينات، وفي الكيمياء لمعرفة تركيب المركبات، 
    وحتى في فحص doping في الألعاب الأولمبية!
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#ffd166;margin-bottom:1rem;">كيف يعمل مطياف الكتلة؟</div>
    <p style="color:#e8eaed;line-height:2.2;">
    <strong style="color:#06d6a0;">1. التأيين:</strong> تحويل الذرات إلى أيونات مشحونة<br>
    <strong style="color:#118ab2;">2. التسريع:</strong> تسريع الأيونات بفرق جهد V فتكتسب طاقة حركية<br>
    <strong style="color:#ef8354;">3. الانحراف:</strong> دخول المجال المغناطيسي حيث تنحرف في مسارات دائرية<br>
    <strong style="color:#7b2cbf;">4. الفصل:</strong> أيونات كتلة أكبر → مسار أكبر → تصل لنقاط مختلفة على الكاشف
    </p>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">qV = ½mv² &nbsp;&nbsp;→&nbsp;&nbsp; v = √(2qV/m)<br><br>r = mv/(qB) = √(2mV/q) / B</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-weight:700;color:#ffd166;margin-bottom:1rem;">⚙️ المحاكاة التفاعلية</div>', unsafe_allow_html=True)

    col_ms1, col_ms2 = st.columns([1, 1.5])
    with col_ms1:
        V_acc = st.slider("فرق الجهد V (V)", 100, 50000, 1000, 100, key='ms_v')
        B_ms = st.slider("المجال B (T)", 0.01, 1.0, 0.1, 0.01, key='ms_b')

        # ثلاثة نظائر
        isotopes = [
            ("¹²C", 12 * 1.66e-27, 6 * E_CHARGE, '#06d6a0'),
            ("¹³C", 13 * 1.66e-27, 6 * E_CHARGE, '#ef8354'),
            ("¹⁴C", 14 * 1.66e-27, 6 * E_CHARGE, '#7b2cbf'),
        ]

        for name, mass, charge, color in isotopes:
            r_iso = np.sqrt(2 * mass * V_acc / charge) / B_ms
            v_iso = np.sqrt(2 * charge * V_acc / mass)
            st.markdown(f"""<div class="card" style="padding:.6rem 1rem;border-left:3px solid {color};">
            <p style="color:{color};font-weight:700;font-size:.9rem;">{name}</p>
            <p style="direction:ltr;text-align:left;color:#9aa5b4;font-size:.8rem;">
            r = {r_iso*100:.2f} cm | v = {v_iso:.2e} m/s</p></div>""", unsafe_allow_html=True)

    with col_ms2:
        fig_ms = go.Figure()

        # منطقة التسريع
        fig_ms.add_shape(type='rect', x0=-0.5, y0=-0.3, x1=0.2, y1=0.3,
                         fillcolor='rgba(17,138,178,0.1)', line=dict(color='rgba(17,138,178,0.3)'))
        fig_ms.add_annotation(x=-0.15, y=0, text='Accelerator\nV', showarrow=False,
                              font=dict(color='#118ab2', size=10), xanchor='center')

        # منطقة المجال
        fig_ms.add_shape(type='rect', x0=0.2, y0=-0.5, x1=1.5, y1=0.5,
                         fillcolor='rgba(6,214,160,0.05)', line=dict(color='rgba(6,214,160,0.2)'))
        fig_ms.add_annotation(x=0.85, y=0.45, text='B ⊗', showarrow=False,
                              font=dict(color='#06d6a0', size=14))

        # كاشف
        fig_ms.add_shape(type='line', x0=1.5, y0=-0.5, x1=1.5, y1=0.5,
                         line=dict(color='rgba(255,209,102,0.5)', width=3))
        fig_ms.add_annotation(x=1.65, y=0, text='Detector', showarrow=False,
                              font=dict(color='#ffd166', size=10))

        # مسارات الأيونات
        for name, mass, charge, color in isotopes:
            r_iso = np.sqrt(2 * mass * V_acc / charge) / B_ms
            # تطبيع نصف القطر للعرض
            r_disp = r_iso * 100  # تحويل لـ cm
            r_norm = r_disp / max(r_disp, 0.01) * 0.4

            theta_arc = np.linspace(0, np.pi/2, 100)
            # مسار شبه دائري من نقطة الدخول
            x_arc = 0.2 + r_norm * (1 - np.cos(theta_arc))
            y_arc = r_norm * np.sin(theta_arc)

            fig_ms.add_trace(go.Scatter(x=x_arc, y=y_arc, mode='lines',
                                       line=dict(color=color, width=2.5), name=name))
            # نقطة الاصطدام
            fig_ms.add_trace(go.Scatter(x=[x_arc[-1]], y=[y_arc[-1]], mode='markers',
                                       marker=dict(size=8, color=color), showlegend=False))

        fig_ms.update_layout(
            plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
            xaxis=dict(showgrid=False, zeroline=False, range=[-0.6, 2.0]),
            yaxis=dict(showgrid=False, zeroline=False, range=[-0.6, 0.6], scaleanchor='x', scaleratio=1),
            height=450, margin=dict(t=20, b=20, l=20, r=20),
            legend=dict(bgcolor='rgba(26,34,54,0.8)', bordercolor='rgba(6,214,160,0.2)', font=dict(size=10))
        )
        st.plotly_chart(fig_ms, use_container_width=True)

    st.markdown("""<div class="info-box">
    <strong style="color:#118ab2;">📌 الاستنتاج:</strong> من العلاقة r = √(2mV/q) / B نلاحظ أن نصف القطر 
    يتناسب مع <strong style="color:#06d6a0;">الجذر التربيعي للكتلة</strong>. لذلك الذرات الأثقل تنحرف 
    في مسار أكبر وتصل لموقع مختلف على الكاشف - وهذا يسمح بفصل النظائر عن بعضها!
    </div>""", unsafe_allow_html=True)

with tab_sync:
    st.markdown("""<div class="life-example">
    تخيّل أنك تدفع طفلاً في الأرجوحة - كلما زادت سرعته، تحتاج أن تدفعه بتوقيت محدد لتطابق حركته.
    السينكروترون يعمل بنفس المبدأ لكن بدلاً من طفل، يدفع جسيمات مشحونة لتسريعها لسرعات قريبة من سرعة الضوء!
    أكبر مسرّع سينكروترون في العالم هو LHC في سويسرا - محيطه 27 كم!
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#ef8354;margin-bottom:1rem;">ما هو السينكروترون؟</div>
    <p style="color:#e8eaed;line-height:2.2;">
    السينكروترون هو <strong style="color:#ffd166;">مسرّع جسيمات حلقي</strong> يحافظ على الجسيمات في مسار دائري ثابت 
    نصف قطره باستخدام مغانط كهربائية. بينما تزداد سرعة الجسيمات (وطاقتها)، يُعدّل المجال المغناطيسي 
    ليبقى نصف القطر ثابتاً.
    </p>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="formula-box">r = mv/(qB) = const → B increases as v increases</div>', unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;">المكونات الرئيسية:</div>
    <ul style="color:#e8eaed;line-height:2.2;padding-right:1.5rem;">
        <li><strong style="color:#ef8354;">مغانط منحنية:</strong> تحافظ على المسار الدائري</li>
        <li><strong style="color:#118ab2;">تجاويف RF:</strong> تمنح الجسيمات طاقة إضافية في كل دورة</li>
        <li><strong style="color:#06d6a0;">مغانط تركيزية:</strong> تمنع الجسيمات من الانتشار</li>
        <li><strong style="color:#7b2cbf;">أنبوب فراغ:</strong> بيئة خالية من الهواء</li>
    </ul>
    </div>""", unsafe_allow_html=True)

    # رسم توضيحي للسينكروترون
    fig_sync = go.Figure()
    theta_ring = np.linspace(0, 2*np.pi, 200)
    R_ring = 1.0
    fig_sync.add_trace(go.Scatter(x=R_ring*np.cos(theta_ring), y=R_ring*np.sin(theta_ring),
                                  mode='lines', line=dict(color='#06d6a0', width=4), name='Beam path'))

    # مغانط في أماكن مختلفة
    n_magnets = 8
    for i in range(n_magnets):
        angle = 2*np.pi*i/n_magnets
        mx, my = R_ring*np.cos(angle), R_ring*np.sin(angle)
        if i % 2 == 0:
            fig_sync.add_shape(type='rect', x0=mx-0.08, y0=my-0.05, x1=mx+0.08, y1=my+0.05,
                              fillcolor='rgba(230,57,70,0.3)', line=dict(color='#e63946'))
        else:
            fig_sync.add_shape(type='rect', x0=mx-0.06, y0=my-0.04, x1=mx+0.06, y1=my+0.04,
                              fillcolor='rgba(17,138,178,0.3)', line=dict(color='#118ab2'))

    # جسيمات
    n_p = 12
    for i in range(n_p):
        a = 2*np.pi*i/n_p
        fig_sync.add_trace(go.Scatter(x=[R_ring*np.cos(a)], y=[R_ring*np.sin(a)],
                                     mode='markers', marker=dict(size=6, color='#ffd166'),
                                     showlegend=False))

    fig_sync.add_annotation(x=0, y=0, text='Synchrotron', showarrow=False,
                           font=dict(color='#9aa5b4', size=12))
    fig_sync.add_annotation(x=1.2, y=1.0, text='Bending\nMagnet', showarrow=False,
                           font=dict(color='#e63946', size=9))
    fig_sync.add_annotation(x=-1.3, y=0.8, text='RF\nCavity', showarrow=False,
                           font=dict(color='#118ab2', size=9))

    fig_sync.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-1.6, 1.6], scaleanchor='y', scaleratio=1),
        yaxis=dict(showgrid=False, zeroline=False, range=[-1.6, 1.6]),
        height=450, margin=dict(t=10, b=10, l=10, r=10)
    )
    st.plotly_chart(fig_sync, use_container_width=True)

with tab_apps:
    st.markdown('<div style="font-size:1.2rem;font-weight:700;color:#ffd166;margin-bottom:1.5rem;">مجالات الاستخدام</div>', unsafe_allow_html=True)

    applications = [
        ("🔬 الطب", "تصوير الأعضاء بـ PET scan، علاج الأورام بالبروتونات، إنتاج النظائر المشعة للتشخيص والعلاج. مسرّعات صغيرة تُستخدم مباشرة في المستشفيات لتدمير الخلايا السرطانية بدقة عالية.",
         "#ef8354"),
        ("⚛️ فيزياء الجسيمات", "اكتشاف الجسيمات الأولية مثل بوزون هيغز في LHC. فهم بنية المادة والقوى الأساسية في الكون. دراسة ظواهر ما بعد النموذج المعياري.",
         "#06d6a0"),
        ("🧬 علم المواد", "دراسة بنية البلورات والبروتينات بالأشعة السينكية من السينكروترون. تطوير مواد جديدة ذات خصائص فريدة. فهم سلوك المواد تحت ظروف قصوى.",
         "#118ab2"),
        ("🏭 الصناعة",        "فحص اللحامات والأنابيب بالأشعة السينكية. تعقيم الأدوات الطبية. تحسين عمليات التصنيع. فحص جودة أشباه الموصلات.",
         "#7b2cbf"),
        ("🌍 علوم البيئة", "دراسة التلوث الجوي وتحليل الجسيمات الدقيقة. مراقبة تغير المناخ عبر تحليل عينات الجليد. تطوير تقنيات معالجة النفايات المشعة.",
         "#ffd166"),
        ("🔐 الأمن",        "كشف المواد الخطرة في المطارات والموانئ. تحليل العينات الجنائية. تطوير تقنيات مسح غير مزعجة.",
         "#e63946"),
    ]
    for title, desc, color in applications:
        st.markdown(f"""<div class="card" style="border-left:4px solid {color};">
        <div style="font-weight:700;color:{color};margin-bottom:.5rem;">{title}</div>
        <p style="color:#9aa5b4;line-height:1.9;font-size:.9rem;">{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)