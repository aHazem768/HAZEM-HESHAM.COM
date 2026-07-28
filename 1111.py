import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64

st.set_page_config(
    page_title="Hazem Hesham",
    page_icon="🏗️",
    layout="wide"
)

# ==============================
# CSS
# ==============================

st.markdown("""
<style>

.stApp{
    background:#0f172a;
}

/* القائمة */

ul{
    background:rgba(20,30,48,.85)!important;
    backdrop-filter:blur(18px);
    border-radius:18px;
    padding:12px!important;
    box-shadow:0 10px 35px rgba(0,0,0,.35);
}

/* كل زر */

.nav-link{

    color:#dce3ef!important;

    font-size:18px!important;

    font-weight:600!important;

    border-radius:14px!important;

    margin:0 5px!important;

    transition:.35s ease!important;

}

/* Hover */

.nav-link:hover{

    background:linear-gradient(90deg,#2563EB,#06B6D4)!important;

    color:white!important;

    transform:translateY(-4px) scale(1.05);

    box-shadow:0 10px 22px rgba(37,99,235,.4);

}

/* Active */

.nav-link.active{

    background:linear-gradient(90deg,#2563EB,#3B82F6)!important;

    color:white!important;

}

/* عنوان الصفحة */

.hero{

text-align:center;

padding:70px 0;

}

.hero h1{

font-size:60px;

color:white;

margin-bottom:10px;

}

.hero h3{

color:#38bdf8;

font-size:28px;

}

.hero p{

color:#cbd5e1;

font-size:20px;

}

/* Cards */

.card{

background:#1e293b;

padding:25px;

border-radius:20px;

color:white;

box-shadow:0 10px 25px rgba(0,0,0,.3);

transition:.3s;

}

.card:hover{

transform:translateY(-8px);

}

</style>
""", unsafe_allow_html=True)





# ==============================
# menu
# ==============================

selected = option_menu(
    menu_title=None,

    options=[
        "Главная",
        "Обо мне",
        "Портфолио",
        "Сертификат",
        "Python",
        "Видео",
        "Языки",
        "Контакты"
    ],

    icons=[
        "house-fill",
        "person-fill",
        "folder-fill",
        "patch-check-fill",
        "cpu-fill",
        "camera-video-fill",
        "translate",
        "telephone-fill"
    ],

    default_index=0,

    orientation="horizontal"
)





# ==============================
# HOME
# ==============================

if selected=="Главная":
    
    st.markdown("""

<div class='hero'>
<h1>Бадри Хазем Хешам</h1>
<h4>Выпускник ПГС 2026</h4>



""",unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)

    with c2:
        st.markdown("""
<div class='card'>
<h3>🏗️ Инженер ПТО</h3>
<p>
Подготавливаю исполнительную документацию, оформляю АОСР, журналы работ и ведомости объёмов работ. Быстро осваиваю внутренние стандарты компании и уделяю большое внимание точности документации.
</p>

<p>
- 📄 Исполнительная документация<br>
- 📄 АОСР<br>
- 📄 Журналы работ<br>
- 📄 ВОР
</p>

</div>
""",unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class='card'>
<h3>💻 Python</h3>
<br>
Создаю инженерные программы для автоматизации рутинных задач, работаю с Excel, Word, PDF и Streamlit. Постоянно совершенствую навыки программирования для повышения эффективности инженерной работы.
</p>
<br>
- 🖥️ Автоматизация<br>
- 🖥️ Excel<br>
- 🖥️ Word
</p>
</div>
""",unsafe_allow_html=True)

    with c1:

        st.markdown("""
<div class='card'>

<h3>🏢 Инженер-конструктор</h3>

<p>
Разрабатываю проектную и рабочую документацию, создаю чертежи в AutoCAD и Revit, выполняю инженерные расчёты и стремлюсь постоянно развивать профессиональные навыки.
</p>

<p>
-📐 Проектирование конструкций<br>
-📄 Разработка рабочей документации<br>
-🧮 Расчёты (ЛИРА 10)<br>
-🖥️ AutoCAD • Revit
</p>

</div>
""", unsafe_allow_html=True)




#=========================================
#=========================================

elif selected=="Обо мне":

    st.header("👤 Обо мне")


    # ====== Фото профиля ======

    image_path = "Фото.jpg"

    if os.path.exists(image_path):

        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()


        col_img, col_info = st.columns([1, 3])


        with col_img:

            st.markdown(f"""
            <img src="data:image/jpeg;base64,{img_base64}"
            style="
            width:180px;
            height:180px;
            object-fit:cover;
            border-radius:50%;
            border:4px solid #38bdf8;
            box-shadow:0 0 20px rgba(56,189,248,0.5);
            ">
            """, unsafe_allow_html=True)



        with col_info:

            st.markdown("""
            <div class="card">

            <h2>👷 Хазем Хешам</h2>

            <h3>Инженер-конструктор ПГС</h3>

            <p>
            Выпускник Уральского федерального университета (УрФУ)
            по направлению «Промышленное и гражданское строительство».
            </p>

            <p>
            Специализируюсь на проектировании строительных конструкций,
            разработке проектной и рабочей документации, а также автоматизации
            инженерных процессов.
            </p>

            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("Фото.jpg не найдено")



    col1, col2 = st.columns(2)



    with col1:

        st.markdown("""
        <div class="card">

        <h3>🏗 Профессиональные навыки</h3>

        <ul>
        <li>Разработка строительных чертежей</li>
        <li>Работа с проектной и рабочей документацией</li>
        <li>Расчёт строительных конструкций</li>
        <li>Подготовка технических решений</li>
        <li>Анализ строительных процессов</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)



    with col2:

        st.markdown("""
        <div class="card">

        <h3>💻 Программное обеспечение</h3>

        <ul>
        <li>AutoCAD</li>
        <li>Revit (BIM-моделирование)</li>
        <li>LIRA 10 (расчёт конструкций)</li>
        <li>Renga</li>
        <li>Python (автоматизация расчётов)</li>
        <li>Excel (инженерные расчёты)</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)



    st.markdown("""
    <div class="card">

    <h3>🚀 Мои интересы</h3>

    <p>
    Развитие в области BIM-технологий, цифровизации строительства,
    автоматизации инженерных задач и применения искусственного интеллекта
    в строительной отрасли.
    </p>

    <p>
    Цель — создавать эффективные инструменты, которые помогают инженерам
    быстрее выполнять расчёты, анализировать данные и повышать качество
    проектирования.
    </p>

    </div>
    """, unsafe_allow_html=True)



    st.info("""
    📍 Готов к профессиональному развитию,
    участию в строительных проектах и работе в команде инженеров.
    """)






#=========================================
#=========================================





elif selected=="Портфолио":

    st.header("📂 Портфолио")

    st.info("Здесь будут мои проекты.")


#=========================================
#=========================================



elif selected=="Python":

    st.header("💻 Python")

    st.success("Программы и автоматизация")



#=========================================
#=========================================



elif selected=="Видео":

    st.header("🎥 Видео")

    st.write("Видео с YouTube.")


#=========================================
#=========================================



elif selected=="Контакты":

    st.header("☎ Контакты")

    st.write("""
📧 Email

💼 Telegram

🌐 LinkedIn

📂 GitHub
""")



#=========================================
#=========================================
elif selected == "Сертификат":

    st.header("📜 Сертификат")

    st.write("Здесь будут размещены мои сертификаты.")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🏅 Revit")

    with col2:
        st.info("🏅 Python")





#=========================================
#=========================================



elif selected == "Языки":

    st.header("🌍 Языки")

    st.markdown("""
### 🇪🇬 Арабский
Родной язык

---

### 🇬🇧 Английский
Средний уровень (B1)

---

### 🇷🇺 Русский
Средний уровень (B1)
Продолжаю активно совершенствовать язык в профессиональной сфере.
""")
