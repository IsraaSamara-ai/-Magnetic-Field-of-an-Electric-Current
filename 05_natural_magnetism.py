import streamlit as st
import numpy as np
import plotly.graph_objects as go

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');
.stApp{background:linear-gradient(135deg,#0a0e1a,#111827 50%,#0d1321);color:#e8eaed;font-family:'Cairo',sans-serif}
#MainMenu,footer,header[data-testid="stHeader"]{visibility:hidden}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1321,#1a2236)}
.section-title{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#ef8354,#e63946);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.info-box{background:linear-gradient(135deg,rgba(17,138,178,.12),rgba(123,44,191,.08));border:1px solid rgba(17,138,178,.3);border-left:4px solid #118ab2;border-radius:0 12px 12px 0;padding:1rem 1.5rem;margin:1rem 0}
.life-example{background:linear-gradient(135deg,rgba(239,131,84,.1),rgba(230,57,70,.05));border:1px solid rgba(239,131,84,.25);border-radius:12px;padding:1.2rem 1.5rem;margin:1rem 0}
.life-example::before{content:"من الحياة اليومية";display:block;font-weight:700;color:#ef8354;margin-bottom:.5rem;font-size:.9rem}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(239,131,84,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
@keyframes atom-spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.atom-anim{animation:atom-spin 4s linear infinite}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">🧭 المغناطيسية الطبيعية</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Natural Magnetism</div>', unsafe_allow_html=True)

st.markdown("""<div class="life-example">
لماذا يلتصق مغناطيس الثلاجة بالثلاجة؟ ولماذا بوصلة الهاتف تعرف الشمال دائماً؟ 
الإجابة تكمن في كيفية ترتيب "المغانط الصغيرة" جداً داخل المادة. فكّر في الأمر مثل صف من الناس 
يمشون عشوائياً في كل اتجاه (مادة عادية) مقابل صف من الناس يمشون بنفس الاتجاه (مغناطيس)!
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="card">
<div style="font-size:1.2rem;font-weight:700;color:#ef8354;margin-bottom:1rem;">السؤال المحوري:</div>
<p style="color:#e8eaed;line-height:2;">
كيف لمغناطيس دائم لا يسري فيه تيار كهربائي أن يولّد مجالاً مغناطيسياً؟
</p>
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="info-box">
<strong style="color:#118ab2;">الإجابة:</strong> تتكون المادة من ذرات تتحرك فيها الإلكترونات حول النواة في مسارات مغلقة 
على شكل حلقات صغيرة جداً. كل حلقة تشكّل تياراً كهربائياً صغيراً يؤدي إلى نشوء مجال مغناطيسي، 
ولذلك يمكن اعتبار المادة وكأنها تتكون من عدد كبير من <strong style="color:#06d6a0;">المغانط الذرية الصغيرة</strong>.
</div>""", unsafe_allow_html=True)

# ======== محاكاة الإلكترون يدور حول النواة ========
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:1.1rem;font-weight:700;color:#06d6a0;margin-bottom:1rem;text-align:center;">الإلكترون يدور حول النواة = تيار كهربائي مجهري</div>', unsafe_allow_html=True)

st.markdown("""<div style="text-align:center;margin:1rem 0;">
<svg width="280" height="280" viewBox="0 0 280 280" xmlns="http://www.w3.org/2000/svg">
    <!-- مدار الإلكترون -->
    <ellipse cx="140" cy="140" rx="100" ry="100" fill="none" stroke="rgba(6,214,160,0.3)" stroke-width="1.5" stroke-dasharray="6,4"/>
    <!-- النواة -->
    <circle cx="140" cy="140" r="18" fill="rgba(230,57,70,0.3)" stroke="#e63946" stroke-width="2"/>
    <text x="140" y="145" text-anchor="middle" fill="#e63946" font-size="12" font-weight="bold">Nucleus</text>
    <!-- الإلكترون المتحرك -->
    <g class="atom-anim" style="transform-origin:140px 140px;">
        <circle cx="240" cy="140" r="8" fill="rgba(17,138,178,0.4)" stroke="#118ab2" stroke-width="2"/>
        <text x="240" y="144" text-anchor="middle" fill="#118ab2" font-size="9" font-weight="bold">e⁻</text>
    </g>
    <!-- سهم اتجاه الدوران -->
    <path d="M 230 65 A 90 90 0 0 1 250 150" fill="none" stroke="#ffd166" stroke-width="2"/>
    <polygon points="250,150 242,138 255,142" fill="#ffd166"/>
    <!-- تسميات -->
    <text x="140" y="270" text-anchor="middle" fill="#9aa5b4" font-size="11">الإلكترون يدور = تيار كهربائي دائري</text>
    <text x="140" y="30" text-anchor="middle" fill="#06d6a0" font-size="12" font-weight="bold">ينتج مجالاً مغناطيسياً</text>
    <!-- مجال مغناطيسي -->
    <line x1="140" y1="120" x2="140" y2="60" stroke="rgba(6,214,160,0.5)" stroke-width="1.5" marker-end="url(#arrowG)"/>
    <line x1="140" y1="160" x2="140" y2="220" stroke="rgba(6,214,160,0.5)" stroke-width="1.5" marker-end="url(#arrowG)"/>
    <defs>
        <marker id="arrowG" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="rgba(6,214,160,0.5)"/>
        </marker>
    </defs>
    <text x="150" y="55" fill="#06d6a0" font-size="10">B</text>
    <text x="150" y="225" fill="#06d6a0" font-size="10">B</text>
</svg>
</div>""", unsafe_allow_html=True)

tab_random, tab_aligned, tab_interactive = st.tabs(["عزوم عشوائية (غير مغناطيس)", "عزوم مرتبة (مغناطيس دائم)", "محاكاة تفاعلية"])

with tab_random:
    st.markdown("""<div class="card">
    <p style="color:#e8eaed;line-height:2;">
    عندما تتوزع العزوم المغناطيسية في الاتجاهات كافة بشكل <strong style="color:#e63946;">عشوائي</strong>، 
    فإن المجالات المغناطيسية الذرية <strong style="color:#e63946;">تلغي بعضها</strong> (محصلتها تساوي صفر).
    </p>
    </div>""", unsafe_allow_html=True)

    fig_rand = go.Figure()
    np.random.seed(10)
    n = 6
    for i in range(n):
        for j in range(n):
            angle = np.random.uniform(0, 2*np.pi)
            dx = 0.38 * np.cos(angle)
            dy = 0.38 * np.sin(angle)
            color = '#e63946' if (i+j) % 2 == 0 else '#118ab2'
            fig_rand.add_trace(go.Scatter(
                x=[i, i+dx], y=[j, j+dy],
                mode='lines+markers',
                line=dict(color=color, width=2),
                marker=dict(size=5, color=color),
                showlegend=False,
                hoverinfo='skip'
            ))
            # رمز X في النهاية (بوصلة مغناطيسية مصغرة)
            fig_rand.add_trace(go.Scatter(
                x=[i-dx*0.15], y=[j-dy*0.15],
                mode='markers', marker=dict(size=3, symbol='x', color=color),
                showlegend=False, hoverinfo='skip'
            ))

    fig_rand.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-0.5, n-0.5],
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        yaxis=dict(showgrid=False, zeroline=False, range=[-0.5, n-0.5],
                   scaleanchor='x', scaleratio=1,
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        height=420, margin=dict(t=40, b=20, l=20, r=20),
        title=dict(text='Net B = 0 (Random Magnetic Domains)', font=dict(color='#e63946', size=14)),
        annotations=[dict(x=n/2, y=-0.8, text='كل سهم يمثل مغناطيساً ذرياً → اتجاهات عشوائية → المحصلة = صفر',
                       showarrow=False, font=dict(color='#9aa5b4', size=11),
                       xref='x', yref='y')]
    )
    st.plotly_chart(fig_rand, use_container_width=True)

    st.markdown("""<div class="card" style="border-color:rgba(230,57,70,.3);">
    <p style="color:#e63946;font-weight:700;">المحصلة = صفر</p>
    <p style="color:#9aa5b4;">المجالات تلغي بعضها لأن الاتجاهات عشوائية - هذه هي حالة المادة العادية غير المغناطيسية</p>
    </div>""", unsafe_allow_html=True)

with tab_aligned:
    st.markdown("""<div class="card">
    <p style="color:#e8eaed;line-height:2;">
    عندما تترتب العزوم المغناطيسية في <strong style="color:#06d6a0;">نفس الاتجاه</strong>، 
    فإن محصلة المجالات المغناطيسية الذرية تؤدي إلى نشوء <strong style="color:#06d6a0;">مجال مغناطيسي</strong> 
    في الحيز المحيط بالمغناطيس.
    </p>
    </div>""", unsafe_allow_html=True)

    fig_align = go.Figure()
    n = 6
    for i in range(n):
        for j in range(n):
            fig_align.add_trace(go.Scatter(
                x=[i, i+0.38], y=[j, j],
                mode='lines+markers',
                line=dict(color='#06d6a0', width=2.5),
                marker=dict(size=5, color='#06d6a0'),
                showlegend=False, hoverinfo='skip'
            ))
            fig_align.add_trace(go.Scatter(
                x=[i+0.38*0.85], y=[j],
                mode='markers', marker=dict(size=3, symbol='x', color='#06d6a0'),
                showlegend=False, hoverinfo='skip'
            ))

    # خطوط المجال المحصّل
    field_y = np.linspace(-0.3, n-0.7, 30)
    for fy in field_y:
        fig_align.add_trace(go.Scatter(
            x=[-0.8, n+0.3], y=[fy, fy],
            mode='lines', line=dict(color='rgba(255,209,102,0.15)', width=1),
            showlegend=False, hoverinfo='skip'
        ))

    # أسهم المجال الكبيرة
    for yy in [1, 3, 4]:
        fig_align.add_annotation(x=n+0.1, y=yy, ax=n+0.5, ay=yy,
                                showarrow=True, arrowhead=2, arrowsize=1.5,
                                arrowcolor='#ffd166')

    fig_align.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-1.2, n+0.8],
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        yaxis=dict(showgrid=False, zeroline=False, range=[-0.8, n-0.5],
                   scaleanchor='x', scaleratio=1,
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        height=420, margin=dict(t=40, b=20, l=20, r=30),
        title=dict(text='Net B ≠ 0 (Aligned Magnetic Domains)', font=dict(color='#06d6a0', size=14)),
        annotations=[dict(x=n/2, y=-1.2, text='كل المغانط الذرية متفقة → مجال مغناطيسي قوي ← B',
                       showarrow=False, font=dict(color='#ffd166', size=11),
                       xref='x', yref='y')]
    )
    st.plotly_chart(fig_align, use_container_width=True)

    st.markdown("""<div class="card" style="border-color:rgba(6,214,160,.3);">
    <p style="color:#06d6a0;font-weight:700;">المحصلة ≠ صفر</p>
    <p style="color:#9aa5b4;">المجالات تتراكم لأن الاتجاهات متوافقة - هذه هي حالة المغناطيس الدائم</p>
    </div>""", unsafe_allow_html=True)

with tab_interactive:
    st.markdown('<div style="font-weight:700;color:#06d6a0;margin-bottom:1rem;text-align:center;">حرّك الشريط ولاحظ ترتيب المناطق المغناطيسية</div>', unsafe_allow_html=True)
    alignment = st.slider("درجة الترتيب (0 = عشوائي ، 100 = مرتب تماماً)", 0, 100, 50, 1)

    fig_int = go.Figure()
    np.random.seed(42)
    n = 6
    for i in range(n):
        for j in range(n):
            target_angle = 0
            random_angle = np.random.uniform(0, 2*np.pi)
            angle = random_angle * (1 - alignment/100) + target_angle * (alignment/100)
            dx = 0.38 * np.cos(angle)
            dy = 0.38 * np.sin(angle)

            greenness = alignment / 100
            r_c = int(230 * (1-greenness) + 6 * greenness)
            g_c = int(57 * (1-greenness) + 214 * greenness)
            b_c = int(70 * (1-greenness) + 160 * greenness)
            color = f'rgb({r_c},{g_c},{b_c})'

            fig_int.add_trace(go.Scatter(
                x=[i, i+dx], y=[j, j+dy],
                mode='lines+markers',
                line=dict(color=color, width=2),
                marker=dict(size=5, color=color),
                showlegend=False, hoverinfo='skip'
            ))

    B_net = alignment / 100
    bar_color = '#06d6a0' if alignment > 70 else '#ffd166' if alignment > 30 else '#e63946'

    fig_int.update_layout(
        plot_bgcolor='rgba(10,14,26,0.8)', paper_bgcolor='rgba(10,14,26,0.8)',
        xaxis=dict(showgrid=False, zeroline=False, range=[-0.5, n-0.5],
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        yaxis=dict(showgrid=False, zeroline=False, range=[-0.5, n-0.5],
                   scaleanchor='x', scaleratio=1,
                   tickmode='array', tickvals=list(range(n)), ticktext=['']*n),
        height=420, margin=dict(t=40, b=60, l=20, r=20),
        title=dict(text=f'Alignment: {alignment}% | Magnetic Strength proportional to {B_net:.2f}',
                   font=dict(color=bar_color, size=13)),
        annotations=[dict(x=n/2, y=-0.9, text=f'Magnitude of net B field',
                       showarrow=False, font=dict(color='#9aa5b4', size=11),
                       xref='x', yref='y')]
    )
    st.plotly_chart(fig_int, use_container_width=True)

    # شريط بصري للمجال المحصل
    st.markdown(f"""<div style="margin:1rem 0;">
    <div style="background:rgba(26,34,54,.8);border-radius:10px;overflow:hidden;border:1px solid rgba(6,214,160,.2);">
        <div style="background:linear-gradient(90deg,{bar_color},{bar_color}88);height:30px;width:{alignment}%;transition:width .3s;display:flex;align-items:center;justify-content:center;">
            <span style="color:#0a0e1a;font-weight:700;font-size:.85rem;">B = {B_net:.2f}</span>
        </div>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:.3rem;">
        <span style="color:#e63946;font-size:.75rem;">0 (عشوائي)</span>
        <span style="color:#06d6a0;font-size:.75rem;">1 (مرتب)</span>
    </div>
    </div>""", unsafe_allow_html=True)

    if alignment == 100:
        st.markdown("""<div class="card" style="border-color:rgba(6,214,160,.4);">
        <p style="color:#06d6a0;font-weight:700;">مغناطيس دائم!</p>
        <p style="color:#9aa5b4;">كل العزوم مرتبة ← مجال مغناطيسي أقصى ← المادة تصبح مغناطيساً دائماً</p>
        </div>""", unsafe_allow_html=True)
    elif alignment == 0:
        st.markdown("""<div class="card" style="border-color:rgba(230,57,70,.4);">
        <p style="color:#e63946;font-weight:700;">مادة عادية!</p>
        <p style="color:#9aa5b4;">العزوم عشوائية ← المجالات تلغي بعضها ← لا يوجد مجال مغناطيسي ظاهر</p>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)