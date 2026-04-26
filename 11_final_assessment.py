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
.section-title{font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,#06d6a0,#e63946);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center;margin:1.5rem 0 .5rem}
.section-sub{font-size:1rem;color:#9aa5b4;text-align:center;margin-bottom:2rem}
.card{background:linear-gradient(145deg,#1a2236,rgba(26,34,54,.8));border:1px solid rgba(6,214,160,.15);border-radius:16px;padding:1.5rem;margin-bottom:1.5rem}
.formula-box{background:linear-gradient(135deg,rgba(6,214,160,.08),rgba(17,138,178,.08));border:1px solid rgba(6,214,160,.25);border-radius:12px;padding:1.2rem 1.8rem;margin:1rem 0;text-align:center;font-family:'JetBrains Mono',monospace;font-size:1.25rem;color:#06d6a0;direction:ltr}
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(6,214,160,.3),transparent);margin:2rem 0}
.author-badge{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,rgba(6,214,160,.15),rgba(17,138,178,.15));border:1px solid rgba(6,214,160,.3);border-radius:30px;padding:.5rem 1.5rem;color:#06d6a0;font-size:.85rem;font-weight:600;z-index:999}
.correct{background:rgba(6,214,160,.1);border:1px solid rgba(6,214,160,.4);border-radius:10px;padding:1rem;margin:.5rem 0;}
.wrong{background:rgba(230,57,70,.1);border:1px solid rgba(230,57,70,.4);border-radius:10px;padding:1rem;margin:.5rem 0;}
.score-circle{width:150px;height:150px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;margin:0 auto 1.5rem;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<div class="section-title">✅ التقييم النهائي التفاعلي</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Final Interactive Assessment</div>', unsafe_allow_html=True)

if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

questions = [
    {
        "q": "ما مقدار المجال المغناطيسي عند نقطة تبعد 0.2 m عن سلك مستقيم لا نهائي يحمل تيار 5 A؟",
        "options": [
            "5 × 10⁻⁶ T",
            "2.5 × 10⁻⁵ T",
            "1 × 10⁻⁵ T",
            "5 × 10⁻⁵ T"
        ],
        "correct": 0,
        "explanation": "B = μ₀I/(2πr) = 4π×10⁻⁷ × 5 / (2π × 0.2) = 5 × 10⁻⁶ T"
    },
    {
        "q": "ماذا يحدث لالمجال المغناطيسي إذا ضُوعف عدد اللفات في ملف دائري مع بقاء باقي المتغيرات ثابتة؟",
        "options": [
            "يُضاعف",
            "يصبح أربع أضعاف",
            "ينصف",
            "لا يتغير"
        ],
        "correct": 0,
        "explanation": "من B = μ₀IN/(2R) نجد أن B ∝ N، فإذا ضُوعف N فإن B يُضاعف"
    },
    {
        "q": "موصلان متوازيان يحملان تيارين بالاتجاه نفسه، نوع القوة المتبادلة هو:",
        "options": [
            "تنافر",
            "تجاذب",
            "لا توجد قوة",
            "قوة دورانية"
        ],
        "correct": 1,
        "explanation": "التياران بنفس الاتجاه → المجال بينهما ضعيف → تجاذب (خطوط المجال تميل للإضافة من الخارج)"
    },
    {
        "q": "ما القوة المغناطيسية على موصل طوله 0.5 m يحمل تيار 4 A في مجال 0.3 T بزاوية 30°؟",
        "options": [
            "0.3 N",
            "0.6 N",
            "0.15 N",
            "0.52 N"
        ],
        "correct": 0,
        "explanation": "F = BIL sinθ = 0.3 × 4 × 0.5 × sin(30°) = 0.3 × 4 × 0.5 × 0.5 = 0.3 N"
    },
    {
        "q": "في مطياف الكتلة، إذا زادت كتلة الأيون مرتين مع ثبات V و B و q، فإن نصف القطر:",
        "options": [
            "يُضاعف",
            "يزداد √2 مرة",
            "يزداد 4 مرات",
            "لا يتغير"
        ],
        "correct": 1,
        "explanation": "r = √(2mV/q)/B → r ∝ √m → إذا زادت m مرتين، يزداد r بمعامل √2"
    },
    {
        "q": "لماذا لا يمكن احتواء البلازما في وعاء مادي؟",
        "options": [
            "لأن البلازما خفيفة جداً",
            "لأن درجة حرارتها المرتفعة جداً تصهر أي وعاء",
            "لأن البلازما غير مرئية",
            "لأن البلازما لا تتفاعل مع المادة"
        ],
        "correct": 1,
        "explanation": "البلازما في مفاعل الاندماج تتجاوز 100 مليون درجة مئوية، وهو ما يصهر أي مادة"
    },
    {
        "q": "ما اتجاه المجال المغناطيسي داخل ملف لولبي يحمل تياراً (باستخدام قاعدة اليد اليمنى)؟",
        "options": [
            "عكس اتجاه الأصابع",
            "نفس اتجاه الإبهام",
            "عمودي على الإبهام",
            "يعتمد على عدد اللفات فقط"
        ],
        "correct": 1,
        "explanation": "في قاعدة اليد اليمنى للملف اللولبي: الأصابع → اتجاه التيار، الإبهام → اتجاه المجال"
    },
    {
        "q": "ما الذي يفسر المغناطيسية الطبيعية (المغناطيس الدائم)؟",
        "options": [
            "تيار كهربائي يسري فيه",
            "ترتيب العزوم المغناطيسية الذرية في نفس الاتجاه",
            "وجود كهرباء ساكنة",
            "تفاعل كيميائي"
        ],
        "correct": 1,
        "explanation": "في المغناطيس الدائم، العزوم المغناطيسية الذرية مرتبة في نفس الاتجاه فتتراكم المجالات"
    },
    {
        "q": "نصف قطر مسار جسيم مشحون في مجال مغناطيسي لا يعتمد على:",
        "options": [
            "كتلة الجسيم",
            "سرعة الجسيم",
            "شحنة الجسيم",
            "الدورة الزمنية"
        ],
        "correct": 3,
        "explanation": "r = mv/(qB) يعتمد على m و v و q و B. أما T = 2πm/(qB) فلا يعتمد على v"
    },
    {
        "q": "في السينكروترون، لماذا يُعدّل المجال المغناطيسي مع زيادة سرعة الجسيمات؟",
        "options": [
            "لزيادة الطاقة",
            "للحفاظ على نصف قطر المسار ثابتاً",
            "لتقليل الحرارة",
            "لزيادة عدد الجسيمات"
        ],
        "correct": 1,
        "explanation": "r = mv/(qB) → للحفاظ على r ثابتاً مع زيادة v، يجب زيادة B بنفس النسبة"
    },
]

if not st.session_state.quiz_submitted:
    st.markdown(f"""<div class="card" style="text-align:center;">
    <p style="color:#ffd166;font-size:1.1rem;font-weight:700;">الأسئلة: {len(questions)} سؤال متعدد الخيارات</p>
    <p style="color:#9aa5b4;">اختر الإجابة الصحيحة ثم اضغط "تسليم" في نهاية الاختبار</p>
    </div>""", unsafe_allow_html=True)

    for i, q in enumerate(questions):
        st.markdown(f"""<div class="card">
        <div style="font-weight:700;color:#06d6a0;margin-bottom:.8rem;">السؤال {i+1}: {q['q']}</div>
        </div>""", unsafe_allow_html=True)

        selected = st.radio(
            f"اختر إجابة السؤال {i+1}",
            q['options'],
            index=None,
            key=f"q_{i}",
            format_func=lambda x: x,
            label_visibility="collapsed"
        )
        if selected is not None:
            st.session_state.quiz_answers[i] = q['options'].index(selected)

        if i < len(questions) - 1:
            st.markdown('<div class="divider" style="margin:1rem 0;"></div>', unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("📋 تسليم الإجابات", type="primary", use_container_width=True):
        st.session_state.quiz_submitted = True
        st.rerun()

else:
    # حساب النتيجة
    score = 0
    for i, q in enumerate(questions):
        if st.session_state.quiz_answers.get(i) == q['correct']:
            score += 1

    percentage = (score / len(questions)) * 100

    # لون النتيجة
    if percentage >= 80:
        score_color = '#06d6a0'
        grade = 'ممتاز 🌟'
    elif percentage >= 60:
        score_color = '#ffd166'
        grade = 'جيد جداً ⭐'
    elif percentage >= 40:
        score_color = '#ef8354'
        grade = 'مقبول'
    else:
        score_color = '#e63946'
        grade = 'يحتاج مراجعة 📚'

    st.markdown(f"""<div style="text-align:center;margin:2rem 0;">
    <div class="score-circle" style="background:linear-gradient(135deg,{score_color}22,{score_color}08);
    border:3px solid {score_color};">
    <div style="font-size:2.5rem;font-weight:900;color:{score_color};font-family:'JetBrains Mono',monospace;">
    {score}/{len(questions)}
    </div>
    <div style="font-size:1.2rem;color:{score_color};font-weight:700;">{grade}</div>
    <div style="font-size:.9rem;color:#9aa5b4;">{percentage:.0f}%</div>
    </div></div>""", unsafe_allow_html=True)

    # مراجعة الإجابات
    for i, q in enumerate(questions):
        user_ans = st.session_state.quiz_answers.get(i, None)
        is_correct = user_ans == q['correct']

        border_color = '#06d6a0' if is_correct else '#e63946'
        bg_class = 'correct' if is_correct else 'wrong'
        icon = '✅' if is_correct else '❌'

        st.markdown(f"""<div class="{bg_class}">
        <div style="font-weight:700;color:{border_color};margin-bottom:.5rem;">{icon} السؤال {i+1}: {q['q']}</div>
        <p style="color:#e8eaed;font-size:.9rem;margin-bottom:.3rem;">
        إجابتك: <strong style="color:{'#06d6a0' if is_correct else '#e63946'};">
        {q['options'][user_ans] if user_ans is not None else 'لم تجب'}</strong></p>
        <p style="color:#06d6a0;font-size:.9rem;margin-bottom:.3rem;">
        الإجابة الصحيحة: <strong>{q['options'][q['correct']]}</strong></p>
        <p style="color:#9aa5b4;font-size:.85rem;direction:ltr;text-align:left;font-family:'JetBrains Mono',monospace;">
        {q['explanation']}</p>
        </div>""", unsafe_allow_html=True)

    # رسم بياني للنتيجة
    fig_score = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': 'النسبة المئوية', 'font': {'color': '#9aa5b4', 'size': 14}},
        number={'suffix': '%', 'font': {'color': score_color, 'size': 40}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': '#9aa5b4', 'tickfont': {'size': 10}},
            'bar': {'color': score_color},
            'bgcolor': 'rgba(26,34,54,0.8)',
            'borderwidth': 0,
            'steps': [
                {'range': [0, 40], 'color': 'rgba(230,57,70,0.2)'},
                {'range': [40, 60], 'color': 'rgba(239,131,84,0.2)'},
                {'range': [60, 80], 'color': 'rgba(255,209,102,0.2)'},
                {'range': [80, 100], 'color': 'rgba(6,214,160,0.2)'},
            ],
            'threshold': {
                'line': {'color': score_color, 'width': 4},
                'thickness': 0.8,
                'value': percentage
            }
        }
    ))
    fig_score.update_layout(
        paper_bgcolor='rgba(10,14,26,0.8)',
        height=300, margin=dict(t=60, b=30, l=40, r=40)
    )
    st.plotly_chart(fig_score, use_container_width=True)

    if st.button("🔄 إعادة الاختبار", use_container_width=True):
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False
        st.rerun()

st.markdown('<div class="author-badge">إعداد: Israa Youssuf Samara</div>', unsafe_allow_html=True)