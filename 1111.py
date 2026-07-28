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

# ==============================
# CSS
# ==============================
# ==============================
# TOP CONTACT BAR
# ==============================

st.markdown("""
<style>

.contact-bar{

    display:flex;

    justify-content:flex-end;

    gap:30px;

    align-items:center;

    padding:10px 25px;

    margin-bottom:10px;

    color:#cbd5e1;

    font-size:14px;

}


.contact-item{

    display:flex;

    align-items:center;

    gap:8px;

}


.contact-item:hover{

    color:#38bdf8;

    transition:.3s;

}


</style>


<div class="contact-bar">


<div class="contact-item">
📞 +7 955 565 71 27
</div>


<div class="contact-item">
✉️ hazim20001@icloud.com
</div>


</div>

""", unsafe_allow_html=True)
# ==============================
# CSS
# ==============================

st.markdown("""
<style>

/* ==============================
   MAIN BACKGROUND
============================== */

.stApp{

    background:
    radial-gradient(
        circle at top,
        #1e3a8a 0%,
        #0f172a 45%
    );

}


/* ==============================
   NAVBAR
============================== */

ul{

    background:
    rgba(15,23,42,0.65)!important;

    backdrop-filter:
    blur(25px);

    border-radius:
    30px;

    padding:
    8px 15px!important;

    box-shadow:
    0 15px 40px rgba(0,0,0,.35);

    border:
    1px solid rgba(255,255,255,.08);

}



/* ==============================
   MENU BUTTONS
============================== */

.nav-link{

    color:
    #94a3b8!important;

    font-size:
    15px!important;

    font-weight:
    600!important;

    border-radius:
    20px!important;

    padding:
    11px 18px!important;

    margin:
    0 4px!important;

    transition:
    all .35s ease!important;

}



/* ==============================
   HOVER
============================== */

.nav-link:hover{

    color:
    #38bdf8!important;

    background:
    rgba(56,189,248,.12)!important;


    transform:
    translateY(-3px);


    box-shadow:
    0 8px 20px rgba(56,189,248,.2);

}



/* ==============================
   ACTIVE
============================== */

.nav-link.active{


    color:
    white!important;


    background:
    linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    )!important;


    box-shadow:

    0 10px 30px
    rgba(37,99,235,.45);


}



/* ==============================
   ICONS
============================== */

.nav-link i{

    font-size:
    16px!important;

}



/* ==============================
   CARDS
============================== */

.card{

    background:
    rgba(30,41,59,.85);

    backdrop-filter:
    blur(15px);

    padding:
    25px;

    border-radius:
    22px;

    color:white;

    box-shadow:

    0 15px 35px
    rgba(0,0,0,.35);

    border:

    1px solid rgba(255,255,255,.05);

    transition:
    .3s;

}


.card:hover{

    transform:
    translateY(-8px);

    box-shadow:

    0 20px 45px
    rgba(0,0,0,.45);

}



/* ==============================
   HERO
============================== */

.hero{

    text-align:center;

    padding:
    80px 0;

}



.hero h1{

    font-size:
    60px;

    font-weight:
    800;

    color:white;

}



.hero h4{

    color:
    #38bdf8;

    font-size:
    25px;

}



.hero p{

    color:
    #cbd5e1;

    font-size:
    20px;

}


</style>

""", unsafe_allow_html=True)



# ==============================
# PROFESSIONAL MENU
# ==============================


selected = option_menu(

    menu_title="🏗️ Hazem Hesham",


    options=[

        "Главная",

        "Обо мне",

        "Проекты",

        "Навыки",

        "Python",

        "Медиа",

        "Языки",

        "Контакты"

    ],


    icons=[

        "house-fill",

        "person-fill",

        "folder-fill",

        "tools",

        "code-slash",

        "camera-video-fill",

        "translate",

        "envelope-fill"

    ],


    default_index=0,


    orientation="horizontal",



    styles={


        "container":{

            "background-color":
            "rgba(15,23,42,.65)",

            "border-radius":
            "30px",

            "padding":
            "8px",

            "box-shadow":
            "0 15px 40px rgba(0,0,0,.35)"

        },


        "icon":{

            "color":
            "#f838a8",

            "font-size":
            "16px"

        },


        "nav-link":{

            "font-size":
            "15px",

            "margin":
            "0 4px",

            "padding":
            "10px 16px"

        },


        "nav-link-selected":{

            "background":
            "linear-gradient(90deg,#2563eb,#06b6d4)"

        }

    }

)




















# ==============================
# HOME
# ==============================


# ==============================
# HOME
# ==============================

# ==============================
# HOME
# ==============================

if selected=="Главная":


    st.markdown("""

<style>


.hero-container{

    height:520px;

    background:

    linear-gradient(
    rgba(15,23,42,.75),
    rgba(15,23,42,.95)
    ),

    url("https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1600&q=80");


    background-size:cover;

    background-position:center;

    border-radius:30px;

    display:flex;

    justify-content:center;

    align-items:center;

    text-align:center;

    box-shadow:
    0 20px 50px rgba(0,0,0,.5);

    animation:
    fadeIn 1.5s ease;

}



.hero-content{

    color:white;

    animation:
    float 4s ease-in-out infinite;

}



.hero-content h1{

    font-size:65px;

    font-weight:900;

    margin-bottom:10px;

}



.hero-content h2{

    color:#38bdf8;

    font-size:32px;

}



.hero-content p{

    font-size:22px;

    color:#cbd5e1;

}



.stDownloadButton button{


    background:
    linear-gradient(
    90deg,
    #2563eb,
    #06b6d4
    );


    color:white;


    border:none;


    border-radius:30px;


    padding:12px 30px;


    font-weight:700;


    transition:.3s;

}



.stDownloadButton button:hover{


    transform:
    translateY(-4px);


    box-shadow:
    0 10px 25px rgba(6,182,212,.4);


}



.project-btn button{


    background:
    linear-gradient(
    90deg,
    #0ea5e9,
    #2563eb
    );


    color:white;


    border:none;


    border-radius:30px;


    padding:12px 30px;


    font-weight:700;

}



@keyframes float{


0%{

transform:translateY(0px);

}


50%{

transform:translateY(-15px);

}


100%{

transform:translateY(0px);

}


}



@keyframes fadeIn{


from{

opacity:0;

transform:
translateY(40px);

}


to{

opacity:1;

transform:
translateY(0);

}


}


</style>



<div class="hero-container">


<div class="hero-content">


<h1>
Бадри Хазем Хешам
</h1>

<h3>
Выпускник 2026
</h3>

<h3>
Промышленное и гражданское строительство
</h2>


</div>


""", unsafe_allow_html=True)



    st.write("")



    # ==============================
    # Buttons
    # ==============================


    col1, col2 = st.columns([1,1])


    with col1:

        try:

            with open("CV.pdf","rb") as file:

                st.download_button(

                    label="📄 Скачать CV",

                    data=file,

                    file_name="Hazem_Hesham_CV.pdf",

                    mime="application/pdf"

                )

        except FileNotFoundError:

            st.warning("CV.pdf не найден")






    st.write("")



    # ==============================
    # Statistics
    # ==============================


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.markdown("""

<div class="card">

<h2>🏢</h2>

<h3>ПГС</h3>

<p>
Промышленное и гражданское строительство
</p>

</div>

""",unsafe_allow_html=True)



    with c2:

        st.markdown("""

<div class="card">

<h2>📐</h2>

<h3>BIM</h3>

<p>
Revit моделирование
</p>

</div>

""",unsafe_allow_html=True)



    with c3:

        st.markdown("""

<div class="card">

<h2>🐍</h2>

<h3>Python</h3>

<p>
Автоматизация инженерных задач
</p>

</div>

""",unsafe_allow_html=True)



    with c4:

        st.markdown("""

<div class="card">

<h2>🧮</h2>

<h3>LIRA</h3>

<p>
Расчёт строительных конструкций
</p>

</div>

""",unsafe_allow_html=True)






















# if selected=="Главная":
    
#     st.markdown("""

# <div class='hero'>
# <h1>Бадри Хазем Хешам</h1>
# <h4>Выпускник ПГС 2026</h4>



# """,unsafe_allow_html=True)

#     c1,c2,c3 = st.columns(3)

#     with c2:
#         st.markdown("""
# <div class='card'>
# <h3>🏗️ Инженер ПТО</h3>
# <p>
# Подготавливаю исполнительную документацию, оформляю АОСР, журналы работ и ведомости объёмов работ. Быстро осваиваю внутренние стандарты компании и уделяю большое внимание точности документации.
# </p>

# <p>
# - 📄 Исполнительная документация<br>
# - 📄 АОСР<br>
# - 📄 Журналы работ<br>
# - 📄 ВОР
# </p>

# </div>
# """,unsafe_allow_html=True)

#     with c3:
#         st.markdown("""
# <div class='card'>
# <h3>💻 Python</h3>
# <br>
# Создаю инженерные программы для автоматизации рутинных задач, работаю с Excel, Word, PDF и Streamlit. Постоянно совершенствую навыки программирования для повышения эффективности инженерной работы.
# </p>
# <br>
# - 🖥️ Автоматизация<br>
# - 🖥️ Excel<br>
# - 🖥️ Word
# </p>
# </div>
# """,unsafe_allow_html=True)

#     with c1:

#         st.markdown("""
# <div class='card'>

# <h3>🏢 Инженер-конструктор</h3>

# <p>
# Разрабатываю проектную и рабочую документацию, создаю чертежи в AutoCAD и Revit, выполняю инженерные расчёты и стремлюсь постоянно развивать профессиональные навыки.
# </p>

# <p>
# -📐 Проектирование конструкций<br>
# -📄 Разработка рабочей документации<br>
# -🧮 Расчёты (ЛИРА 10)<br>
# -🖥️ AutoCAD • Revit
# </p>

# </div>
# """, unsafe_allow_html=True)
























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
