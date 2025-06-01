import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="المدرسة الآمنة", layout="wide")

st.logo("logo.png")

#st.sidebar.markdown("Sidebar content")
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cairo&display=swap" rel="stylesheet">
    <style>
       *{
             font-family: "Cairo", sans-serif !important;
            font-style: normal;
       }
        html, body, [class*="css"] {
           font-family: "Cairo", sans-serif !important;
            font-style: normal;
            direction: rtl;
            text-align: right;
        }
        .question {
            font-size: 20px !important;
            font-weight: bold;
        }
        .custom-box {
            background-color: #fff;
            border: 2px solid #d32f2f;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        [data-testid="stHeadingWithActionElements"] h1 {
            color: rgb(211, 47, 47);
            font-size: 48px;
            text-align: center;
            border: 11px solid #fe3a3a;
            border-radius: 27px;
            box-shadow: aquamarine;
            box-shadow: 10px 10px 2px 0px rgba(0, 0, 0, 0.25);
            margin-bottom: 3.6rem;
            }

             [data-testid="stHeadingWithActionElements"] h3{
                margin-bottom: 1.6rem;
                    font-size: 34px;
            }
            [data-testid="stMarkdownContainer"] {
                width: 100%
            }
            [data-testid="stSidebarHeader"] img{
            height: 6rem;
            border: 1px solid red;
            border-radius: 10px;
            width: 100%;
         }
         
         /* Styles pour la sidebar */
         .css-1d391kg {
            background-color: #f8f9fa !important;
         }
         
         [data-testid="stSidebar"] {
            background: linear-gradient(145deg, #ffffff 0%, #f5f5f5 100%) !important;
            border-right: 3px solid #d32f2f !important;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1) !important;
         }
         
         [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(145deg, #ffffff 0%, #f5f5f5 100%) !important;
            padding-top: 2rem !important;
         }
         
         /* Style pour le titre de la sidebar */
         [data-testid="stSidebar"] .css-17eq0hr {
            background-color: #d32f2f !important;
            color: white !important;
            padding: 15px !important;
            border-radius: 10px !important;
            margin-bottom: 20px !important;
            text-align: center !important;
            font-weight: bold !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important;
         }
         
         /* Style pour les boutons radio de la sidebar */
         [data-testid="stSidebar"] .stRadio > div {
            background-color: white !important;
            padding: 15px !important;
            border-radius: 12px !important;
            border: 2px solid #e0e0e0 !important;
            margin-bottom: 10px !important;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
            transition: all 0.3s ease !important;
         }
         
         [data-testid="stSidebar"] .stRadio > div:hover {
            border-color: #d32f2f !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15) !important;
         }
         
         /* Style pour les labels des boutons radio */
         [data-testid="stSidebar"] .stRadio label {
            font-size: 16px !important;
            font-weight: 600 !important;
            color: #333 !important;
            display: flex !important;
            align-items: center !important;
            padding: 8px 0 !important;
         }
         
         /* Style pour l'option sélectionnée */
         [data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div {
                background-color: #d32f2f !important;
                color: white !important;
                padding: 10px;
                border-radius: 10px;
                margin-right: 1rem;
         }
         
         [data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div label {
            color: white !important;
         }
         
         /* Style pour les icônes dans la sidebar */
         [data-testid="stSidebar"] .stRadio label::before {
            content: "";
            display: inline-block;
            margin-left: 10px;
            width: 20px;
            height: 20px;
            background-size: contain;
         }
         
         /* Ajout d'icônes spécifiques selon le contenu */
         [data-testid="stSidebar"] .stRadio label[for*="فضاء التلميذ"]::before {
            content: "🧒";
            font-size: 18px;
         }
         
         [data-testid="stSidebar"] .stRadio label[for*="فضاء المختص"]::before {
            content: "🧠";
            font-size: 18px;
         }
         
         [data-testid="stSidebar"] .stRadio label[for*="فضاء الأستاذ"]::before {
            content: "👨‍🏫";
            font-size: 18px;
         }
         
         /* Animation pour les transitions */
         [data-testid="stSidebar"] * {
            transition: all 0.3s ease !important;
         }
         
         /* Style pour le logo dans la sidebar */
         [data-testid="stSidebarHeader"] {
            padding: 20px !important;
            text-align: center !important;
         }
         
         [data-testid="stSidebarHeader"] img {
            height: 6rem !important;
            border: 3px solid #d32f2f !important;
            border-radius: 15px !important;
            width: 100% !important;
            box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3) !important;
            transition: transform 0.3s ease !important;
         }
         
         [data-testid="stSidebarHeader"] img:hover {
            transform: scale(1.05) !important;
         }
         
         /* Amélioration générale de la sidebar */
         [data-testid="stSidebar"] {
            min-width: 300px !important;
         }
         
         /* Style pour le footer de la sidebar */
         [data-testid="stSidebar"]::after {
            content: "المدرسة الآمنة © 2025";
            display: block;
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 12px;
            border-top: 1px solid #e0e0e0;
            margin-top: 20px;
         }
    </style>
""", unsafe_allow_html=True)

if "data" not in st.session_state:
    st.session_state.data = []

if "reports" not in st.session_state:
    st.session_state.reports = {}

PASSWORD_SPECIALIST = "12345"
PASSWORD_TEACHER = "prof2025"

def analyze_behavior(answers, scenario_answers=None):
    points = 0
    remarks = []
    interventions = []
    activities = []
    communication = []

    if answers["هل تعرضت لسخرية أو إهانة من زميل؟"] == "نعم":
        points += 3
        remarks.append("يتعرض التلميذ لسخرية من طرف الزملاء مما يؤثر على ثقته بنفسه.")
        interventions.append("التوعية داخل القسم حول آثار السخرية وتنظيم حصص تفاعلية حول الاحترام.")
        activities.append("لعبة الأدوار حول احترام الآخر")
        communication.append("تعزيز العلاقة التشاركية مع التلميذ وتشجيعه على التعبير.")

    if answers["هل تعرضت لعنف جسدي داخل المدرسة؟"] == "نعم":
        points += 4
        remarks.append("تعرض التلميذ لعنف جسدي يتطلب تدخل عاجل لضمان سلامته.")
        interventions.append("تحديد مصدر العنف ومتابعة الحالة مع المختص الاجتماعي.")
        activities.append("جلسات دعم نفسي فردية")
        communication.append("التعامل مع التلميذ بهدوء وتطمينه.")

    if answers["هل سبق أن شهدت عنفاً بين زملائك؟"] == "نعم":
        points += 2
        remarks.append("شاهد التلميذ مواقف عنف مما قد يولد لديه توتر وخوف.")
        interventions.append("تحليل الموقف داخل القسم وتوعية جماعية.")
        activities.append("عروض مسرحية حول حل النزاع.")
        communication.append("تشجيع النقاش الجماعي حول العنف المدرسي.")

    if answers["هل تشعر بالخوف من أستاذك؟"] == "نعم":
        points += 2
        remarks.append("التلميذ يخاف من الأستاذ مما يعرقل التعلم.")
        interventions.append("مراجعة أساليب التواصل والتعامل بلين واحترام.")
        activities.append("ورشة عن الثقة المتبادلة.")
        communication.append("فتح حوار فردي مع التلميذ لفهم سبب الخوف.")

    if answers["هل تشعر بأنك ضحية للعنف اللفظي؟"] == "نعم":
        points += 3
        remarks.append("العنف اللفظي يؤثر على نفسية التلميذ ويشوش تركيزه.")
        interventions.append("تنظيم جلسات توعية وتحسيس.")
        activities.append("رسم قصص مصورة حول التسامح.")
        communication.append("الاستماع للتلميذ دون إصدار أحكام.")

    if answers["كيف تحس داخل المؤسسة؟"] in ["غير مرتاح", "محبط"]:
        points += 3
        remarks.append("التلميذ لا يشعر بالارتياح داخل المؤسسة مما يستدعي الانتباه.")
        interventions.append("إشراك التلميذ في أنشطة الحياة المدرسية.")
        activities.append("مجالس التلميذ، أنشطة فنية، رحلات.")
        communication.append("بناء علاقة إنسانية مع التلميذ تشعره بالانتماء.")

    if scenario_answers:
        for scenario, response in scenario_answers.items():
            if "أبقى صامتاً" in response:
                points += 2
                remarks.append(f"في الموقف '{scenario}'، اختار التلميذ الصمت مما يدل على انطواء.")
                interventions.append("تعزيز ثقة التلميذ بنفسه عبر أنشطة جماعية.")
                activities.append("مجموعة الدعم الزمري")
                communication.append("تحديد جلسات فردية لفهم أسباب الصمت.")
            elif "أشتكي" in response:
                points += 1
                remarks.append(f"في الموقف '{scenario}'، التلميذ يلجأ للشكوى وهو سلوك إيجابي.")
                interventions.append("تعزيز ثقافة التبليغ داخل القسم.")
                activities.append("حوار موجه حول حل المشكلات.")
                communication.append("تشجيع التلميذ على التعبير المباشر عند الحاجة.")
            elif "أواجه" in response:
                points += 2
                remarks.append(f"في الموقف '{scenario}'، التلميذ يميل للمواجهة مما قد يسبب صراعات.")
                interventions.append("تعليمه تقنيات ضبط النفس والتعبير المهذب.")
                activities.append("تمثيل أدوار حول الردود الهادئة.")
                communication.append("ضبط القواعد الصفية مع الجميع.")

    return points, remarks, interventions, activities, communication

# --- Header ---
st.markdown("""
    <div style='display: flex; align-items: center; justify-content: center;'>
        <div>
            <h1 style='color: #d32f2f; font-size: 48px;'> المدرسة الآمنة</h1>
            <p style='font-size: 20px;'> خلية إنصات رقمية تسعى إلى دعم التلاميذ نفسيا و تربويا لضمان الأمن داخل المؤسسات التعليمية</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Ajout d'un titre stylisé pour la sidebar
st.sidebar.markdown("""
    <div style='background: linear-gradient(45deg, #d32f2f, #ff6b6b); 
                color: white; 
                padding: 20px; 
                border-radius: 15px; 
                text-align: center; 
                margin-bottom: 30px;
                box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3);'>
        <h2 style='margin: 0; font-size: 24px; font-weight: bold;color:aliceblue'>القائمة الرئيسية</h2>
        <p style='margin: 5px 0 0 0; font-size: 14px; opacity: 0.9;'>اختر الفضاء المناسب</p>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("انتقل إلى:", ["فضاء التلميذ", "فضاء المختص", "فضاء الأستاذ"])

# Ajout d'informations supplémentaires dans la sidebar
st.sidebar.markdown("""
    <div style='background-color: #f8f9fa; 
                border: 2px solid #d32f2f; 
                border-radius: 10px; 
                padding: 15px; 
                margin-top: 30px;
                padding-right: 2rem;'>
        <h2 style='color: #d32f2f; margin-top: 0;'>ℹ️ معلومات مهمة</h2>
        <ul style='font-size: 12px; color: #666;'>
            <li>المنصة آمنة ومحمية</li>
            <li>جميع البيانات سرية</li>
            <li>متاحة 24/7</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

if menu == "فضاء التلميذ":
    st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem;font-size: 25px;">🧒 فضاء التلميذ</strong>
                          </div>
               """, unsafe_allow_html=True)
    #st.subheader("🧒 فضاء التلميذ")
    student_id = st.text_input("أدخل رقمك التعريفي (Code élève)")
    answers = {}
    questions = [
        "هل تعرضت لسخرية أو إهانة من زميل؟",
        "هل تعرضت لعنف جسدي داخل المدرسة؟",
        "هل سبق أن شهدت عنفاً بين زملائك؟",
        "هل تشعر بالخوف من أستاذك؟",
        "هل تشعر بأنك ضحية للعنف اللفظي؟",
        "كيف تحس داخل المؤسسة؟"
    ]

    # Create two columns for the first 5 questions (radio buttons)
    col1, col2 = st.columns(2)

    # Split questions into two groups
    left_questions = questions[:3]  # First 3 questions
    right_questions = questions[3:5]  # Next 2 questions

    with col1:
        for q in left_questions:
            answers[q] = st.radio(f"**{q}**", ["نعم", "لا"], key=q)

    with col2:
        for q in right_questions:
            answers[q] = st.radio(f"**{q}**", ["نعم", "لا"], key=q)

    # Full width for special questions
    answers["كيف تحس داخل المؤسسة؟"] = st.selectbox("**كيف تحس داخل المؤسسة؟**", ["مرتاح", "عادي", "غير مرتاح", "محبط"])

    mood = st.selectbox("**ما هو إحساسك هذه اللحظة؟**", ["😊 سعيد", "😐 عادي", "😢 حزين", "😡 غاضب", "😟 قلق"])
    answers["الإحساس الحالي"] = mood

    st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem;font-size: 25px;">مواقف افتراضية</strong>
                        </div>
            """, unsafe_allow_html=True)

    # Scenarios in columns
    scenario_answers = {}
    scenarios = {
        "قام زميل بأخذ أدواتك بالقوة أمام زملائك": ["أبقى صامتاً", "أواجهه مباشرة", "أشتكي للأستاذ"],
        "أستاذ وبخك أمام القسم بصوت مرتفع": ["أبقى صامتاً", "أشتكي", "أبكي"],
        "تم طردك ظلماً من القسم": ["أواجه الأستاذ", "أشتكي للمدير", "أبقى صامتاً"],
        "زميل أهان أحد أفراد أسرتك أمامك": ["أرد عليه", "أشتكي", "أتجاهل"],
        "تعرضت للسخرية في ساحة المدرسة من أكثر من تلميذ": ["أبكي", "أواجههم", "أخبر أحد الكبار"],
        "رأيت مشاجرة عنيفة بين زملائك": ["أتدخل", "أبتعد", "أخبر الإدارة"],
        "أستاذك تجاهلك رغم رفعك ليدك": ["أبقى صامتاً", "أشعر بالحزن", "أخبره لاحقاً"],
        "لم يتم اختيارك في نشاط جماعي": ["أحزن", "أسأل عن السبب", "لا أبالي"],
        "تم السخرية من لباسك": ["أبقى صامتاً", "أبكي", "أواجههم"],
        "تم نعتك بلقب يزعجك": ["أشتكي", "أغضب", "أتجاهل"]
    }

    # Convert scenarios to list for easier splitting
    scenario_items = list(scenarios.items())

    # Create 2 columns for scenarios
    col1, col2 = st.columns(2)

    # Split scenarios between columns
    left_scenarios = scenario_items[:5]  # First 5 scenarios
    right_scenarios = scenario_items[5:]  # Remaining scenarios

    with col1:
        for scenario, options in left_scenarios:
            scenario_answers[scenario] = st.selectbox(f"**{scenario}**", options, key=scenario)

    with col2:
        for scenario, options in right_scenarios:
            scenario_answers[scenario] = st.selectbox(f"**{scenario}**", options, key=scenario)

    complaint = st.text_area("📨 هل ترغب في تقديم شكاية؟")
   

    if st.button("📤 إرسال"):
        points, remarks, interventions, activities, communication = analyze_behavior(answers, scenario_answers)
        st.session_state.data.append({
            "id": student_id,
            "answers": answers,
            "scenarios": scenario_answers,
            "complaint": complaint,
            "points": points,
            "remarks": remarks,
            "interventions": interventions,
            "activities": activities,
            "communication": communication,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success("تم إرسال البيانات بنجاح.")

elif menu == "فضاء المختص":
    st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">🧠 فضاء المختص النفسي</strong>
                          </div>
               """, unsafe_allow_html=True)
    #st.subheader("🧠 فضاء المختص النفسي")
    password = st.text_input("أدخل كلمة السر", type="password")
    if password == PASSWORD_SPECIALIST:
        st.success("تم الدخول بنجاح.")
        if st.session_state.data:
            selected_id = st.selectbox("اختر رقم التلميذ", [d["id"] for d in st.session_state.data])
            record = next(item for item in st.session_state.data if item["id"] == selected_id)
            st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">✅ شكاية</strong>
                          </div>
               """, unsafe_allow_html=True)
            st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 100%;display:flex;margin-bottom:1rem"> {record['complaint']}</strong>
                          </div>
               """, unsafe_allow_html=True)
           
   
            
            st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">✅ تشخيص الحالة</strong>
                          </div>
               """, unsafe_allow_html=True)
            #st.markdown("### ✅ تشخيص الحالة")

            # Start the HTML string with your custom div
            html = "<div class='custom-box'>"

            # Add each remark as a list item
            for remark in record["remarks"]:
                html += f"<p>👈 {remark}</p>"

            # Close the div
            html += "</div>"

            # Display the HTML in Streamlit
            st.markdown(html, unsafe_allow_html=True)

            


            st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">✍️ تقرير المختص</strong>
                          </div>
               """, unsafe_allow_html=True)
            #st.markdown("### ✍️ تقرير المختص")

            report = st.text_area("اكتب تقريرك هنا")
            if st.button("📨 إرسال التقرير للأستاذ"):
                st.session_state.reports[selected_id] = {
                    "report": report,
                    "interventions": record["interventions"],
                    "activities": record["activities"],
                    "communication": record["communication"]
                }
                st.success("تم إرسال التقرير.")
        else:
            st.info("لا توجد بيانات بعد.")
    elif password:
        st.error("كلمة السر غير صحيحة.")

elif menu == "فضاء الأستاذ":
    st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">👨‍🏫 فضاء الأستاذ</strong>
                          </div>
               """, unsafe_allow_html=True)
    #st.subheader("")
    teacher_password = st.text_input("أدخل رمزك السري", type="password")
    if teacher_password == PASSWORD_TEACHER:
        if st.session_state.reports:
            for student_id, info in st.session_state.reports.items():

               
                
                st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center;margin-bottom:1rem">🧒 تقرير حول التلميذ رقم: {student_id}</strong>
                          </div>
               """, unsafe_allow_html=True)
                st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 100%;display: flex;margin-bottom:1rem">{info["report"]}</strong>
                          </div>
               """, unsafe_allow_html=True)
                st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center">🛠️ اقتراحات للتدخل التربوي:</strong>
                          </div>
               """, unsafe_allow_html=True)
               # st.markdown( list(set(info["interventions"])) )
                st.markdown(f"""
                        <div style="padding: 1.6rem;border-radius: 10px;">
                             <ul style="list-style: circle;">
                                {''.join([f'<li>{a}</li>' for a in list(set(info["interventions"]))])}
                            </ul>
                         </div>""", unsafe_allow_html=True)
                #st.markdown("**🛠️ اقتراحات للتدخل التربوي:**")
               # for i in info["interventions"]:
                #    st.write(f"- {i}")
                
                st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center">🎯 أنشطة مقترحة:</strong>
                </div>
               """, unsafe_allow_html=True)
                #st.markdown("**🎯 أنشطة مقترحة:**")
                st.markdown(f"""
                        <div style="padding: 1.6rem;border-radius: 10px;">
                             <ul style="list-style: circle;">
                                {''.join([f'<li>{a}</li>' for a in list(set(info["activities"])) ])}
                            </ul>
                         </div>""", unsafe_allow_html=True)
                #for a in info["activities"]:
                 #   st.write(f"- {a}")
                
                st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center">🗣️ كيفية التواصل مع التلميذ:</strong>
                </div>
               """, unsafe_allow_html=True)
                #st.markdown( list( set(info["communication"]) ) )
                st.markdown(f"""
                        <div style="padding: 1.6rem;border-radius: 10px;">
                             <ul style="list-style: circle;">
                                {''.join([f'<li>{a}</li>' for a in list( set(info["communication"]) ) ])}
                            </ul>
                         </div>""", unsafe_allow_html=True)
                #st.markdown("**🗣️ كيفية التواصل مع التلميذ:**")
                #for c in info["communication"]:
                 #   st.write(f"- {c}")
            st.markdown("---")
            st.markdown(f"""<div style="">
                                <strong style="padding: 15px;border-radius: 14px 0 14px 0;border: 2px solid #ff4747;width: 25%;display: flex;justify-content: center">🛡️ معلومات قانونية وتربوية:</strong>
                </div>
               """, unsafe_allow_html=True)
            #st.markdown("### 🛡️ معلومات قانونية وتربوية")
            st.markdown(f"""
                        <div style="padding: 1.6rem;border-radius: 10px;">
                             <ul style="list-style: circle;">
                                <li>- يُعد العنف في المؤسسات التعليمية مخالفاً للقانون رقم 07.00 المنظم للتعليم المدرسي.</li>
                                <li>- المادة 19 من القانون الجنائي المغربي تجرّم العنف النفسي والجسدي تجاه القاصرين.</li>
                                <li>- دليل وزارة التربية الوطنية يشير إلى تبني مقاربة وقائية وتربوية لحل النزاعات داخل الوسط المدرسي.</li>
                                <li>- يمكن اللجوء إلى خلية الإنصات بالمؤسسة أو المختص الاجتماعي عند رصد أي حالة عنف.</li>
                            </ul>
                         </div>""", unsafe_allow_html=True)
  # Close the div
            
        else:
            st.info("لم يتم إرسال تقارير بعد.")
    elif teacher_password:
        st.error("رمز الدخول غير صحيح.")