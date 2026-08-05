import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64
from streamlit_carousel import carousel

st.set_page_config(
    page_title="Hazem Hesham",
    page_icon="🏗️",
    layout="wide"
)


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

    menu_title="🏗️ Hazem Hesham - Civil & Structural Engineer",


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
Промышленное и гражданское строительство
</h2>


Добро пожаловать на мой профессиональный сайт.

Цель данного сайта — показать мои реальные знания и практический опыт через выполненные проекты, инженерные расчёты, видео и примеры моей работы.

Здесь я буду постепенно публиковать новые проекты, полезные материалы, инженерные решения и информацию, связанную со строительством, BIM-технологиями и автоматизацией инженерных процессов.

Этот сайт является площадкой для обмена опытом, развития профессиональных навыков и демонстрации моего подхода к работе инженера.




Сайт находится в процессе разработки. Первая версия будет официально опубликована .
<h4>
10.08.2026
</h4>

В следующих обновлениях планируется добавить новые проекты, дополнительные разделы и больше инженерных материалов.



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


    c1,c2,c3 = st.columns(3)



    with c1:

        st.markdown("""

<div class="card">

<h2>🏢</h2>

<h3>Инженер-конструктор</h3>

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

""",unsafe_allow_html=True)



    with c2:

        st.markdown("""

<div class="card">

<h2>🏗️ </h2>

<h3> Инженер ПТО</h3>

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

<div class="card">

<h2>💻</h2>

<h3>Python</h3>

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











#=========================================
#=========================================



elif selected=="Обо мне":

    st.header("👤 Обо мне")


    # ====== Фото профиля ======

    image_path = "Фото.jpg"

    if os.path.exists(image_path):

        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()


        col_img, col_info = st.columns([1, 7])


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



elif selected=="Проекты":


    st.markdown("""
    <style>


    /* عنوان المشاريع */

    .project-title{

        font-size:45px;
        font-weight:900;
        color:white;

    }


    .project-sub{

        color:#94a3b8;
        font-size:18px;
        margin-bottom:30px;

    }



    /* كارت المشروع */

    .project-card{

        background:
        rgba(30,41,59,.85);

        backdrop-filter:
        blur(20px);

        padding:35px;

        border-radius:30px;

        color:white;

        box-shadow:
        0 20px 45px rgba(0,0,0,.4);

        border:
        1px solid rgba(255,255,255,.08);

    }


    .project-card h2{

        font-size:32px;

    }



    .tag{

        display:inline-block;

        padding:8px 18px;

        margin:5px;

        border-radius:30px;

        background:
        linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
        );

        color:white;

        font-size:14px;

        font-weight:bold;

    }



    /* تعديل السايدبار */

    section[data-testid="stSidebar"]{

        background:
        transparent;

    }



    section[data-testid="stSidebar"] > div{

        background:
        rgba(15,23,42,.85);

        backdrop-filter:
        blur(20px);

        border-radius:25px;

        margin-top:80px;

        padding:20px;

        box-shadow:
        0 20px 40px rgba(0,0,0,.4);

    }



    </style>

    """, unsafe_allow_html=True)




    # ==========================
    # Sidebar المشاريع
    # ==========================


    st.sidebar.markdown(
        """
        <h2 style='color:white;text-align:center'>
        🏗 Projects
        </h2>
        """,
        unsafe_allow_html=True
    )


    project = st.sidebar.radio(

        "",

        [

            "Project 1",
            "Project 2",
            "Project 3",
            "Project 4",
            "Project 5",
            "Project 6",
            "Project 7",
            "Project 8",
            "Project 9",
            "Project 10"

        ]

    )



    st.markdown(
        f"""
        <div class="project-title">
        📂 {project}
        </div>

        <div class="project-sub">
        Учебные и инженерные проекты
        </div>

        """,
        unsafe_allow_html=True
    )




    # ==========================
    # PROJECT 1
    # ==========================


    if project=="Project 1":


        col1,col2 = st.columns([1,1.5])



        with col1:


            if os.path.exists("122.png"):

                st.image(
                    "122.png",
                    use_container_width=True
                )

            else:

                st.info(
                "Добавьте изображение проекта"
                )




        with col2:


            st.markdown("""
            
            <div class="project-card">


            <h2>
            🏢 11-этажный жилой дом
            </h2>


            <p>

            Выпускной инженерный проект по направлению
            «Промышленное и гражданское строительство».

            Проект включает разработку конструктивной схемы,
            рабочей документации и инженерных расчётов.

            </p>



            <br>

            <b>
            Выполнено:
            </b>


            <ul>

            <li>Проектирование конструкций</li>

            <li>Чертежи AutoCAD</li>

            <li>BIM модель Revit</li>

            <li>Расчёт ЛИРА 10</li>

            <li>Календарный план строительства</li>

            </ul>


            <br>


            <span class="tag">
            AutoCAD
            </span>


            <span class="tag">
            Revit
            </span>


            <span class="tag">
            LIRA 10
            </span>


            <span class="tag">
            Excel
            </span>


            </div>

            """,
            unsafe_allow_html=True)



        st.write("")



        # تحميل المشروع


        if os.path.exists(
        "2026.СТ-420004.Бадри Х.Х. ГЧ.pdf"
        ):


            with open(
            "2026.СТ-420004.Бадри Х.Х. ГЧ.pdf",
            "rb"
            ) as file:


                st.download_button(

                    label="📄 Скачать полный проект",

                    data=file,

                    file_name=
                    "Project_11_floor.pdf",

                    mime=
                    "application/pdf",

                    use_container_width=True

                )


        else:


            st.warning(
            "Файл проекта не найден"
            )











    # ==========================
    # باقي المشاريع
    # ==========================

    if project=="Project 2":


        col1,col2 = st.columns([1,1.5])



        with col1:


            if os.path.exists("144.png"):

                st.image(
                    "144.png",
                    use_container_width=True
                )

            else:

                st.info(
                "Добавьте изображение проекта"
                )




        with col2:


            st.markdown("""
            
            <div class="project-card">


            <h2>
            🏢 Расчет и конструирование основных несущих конструкций одноэтажного промышленного здания
            </h2>


            <p>

            
            «Промышленное и гражданское строительство».

            Проект включает разработку конструктивной схемы,
            рабочей документации и инженерных расчётов.

            </p>



            <br>

            <b>
            Выполнено:
            </b>


            <ul>

            <li>Проектирование конструкций</li>

            <li>Чертежи AutoCAD</li>

            <li>BIM модель Revit</li>

            <li>Расчёт ЛИРА 10</li>

            

            </ul>


            <br>


            <span class="tag">
            AutoCAD
            </span>


            <span class="tag">
            Revit
            </span>


            <span class="tag">
            LIRA 10
            </span>


            <span class="tag">
            Excel
            </span>


            </div>

            """,
            unsafe_allow_html=True)



        st.write("")



        # تحميل المشروع


        if os.path.exists(
        "ГЧ_ПП(4)_Бадри Х.Х..pdf"
        ):


            with open(
            "ГЧ_ПП(4)_Бадри Х.Х..pdf",
            "rb"
            ) as file:


                st.download_button(

                    label="📄 Скачать полный проект",

                    data=file,

                    file_name=
                    "Project_ПП(4).pdf",

                    mime=
                    "application/pdf",

                    use_container_width=True

                )


        else:


            st.warning(
            "Файл проекта не найден"
            )



    # else:


    #     st.info(
    #     f"🚧 {project} скоро будет добавлен"
    #     )







    # ==========================
    # باقي المشاريع
    # ==========================

    if project=="Project 3":


        col1,col2 = st.columns([1,1.5])



        with col1:


            if os.path.exists("166.png"):

                st.image(
                    "166.png",
                    use_container_width=True
                )

            else:

                st.info(
                "Добавьте изображение проекта"
                )




        with col2:


            st.markdown("""
            
            <div class="project-card">


            <h2>
            🏢 Многоэтажное промышленное здание с железобетонным каркасом
            </h2>


            <p>

            
            «Промышленное и гражданское строительство».

            Проект включает разработку конструктивной схемы,
            рабочей документации и инженерных расчётов.

            </p>



            <br>

            <b>
            Выполнено:
            </b>


            <ul>

            <li>Проектирование конструкций</li>

            <li>Чертежи AutoCAD</li>

            <li>BIM модель Revit</li>

            <li>Расчёт ЛИРА 10</li>

            

            </ul>


            <br>


            <span class="tag">
            AutoCAD
            </span>


            <span class="tag">
            Revit
            </span>


            <span class="tag">
            LIRA 10
            </span>


            <span class="tag">
            Excel
            </span>


            </div>

            """,
            unsafe_allow_html=True)



        st.write("")



        # تحميل المشروع


        if os.path.exists(
        "ГЧ_Бадри Х.Х._СТ-320004(ЖБК).pdf"
        ):


            with open(
            "ГЧ_Бадри Х.Х._СТ-320004(ЖБК).pdf",
            "rb"
            ) as file:


                st.download_button(

                    label="📄 Скачать полный проект",

                    data=file,

                    file_name=
                    "Project_ГЧ.pdf",

                    mime=
                    "application/pdf",

                    use_container_width=True

                )


        else:


            st.warning(
            "Файл проекта не найден"
            )









    # ==========================
    # باقي المشاريع
    # ==========================

    if project=="Project 4":


        col1,col2 = st.columns([1,1.5])



        with col1:


            if os.path.exists("177.png"):

                st.image(
                    "177.png",
                    use_container_width=True
                )

            else:

                st.info(
                "Добавьте изображение проекта"
                )




        with col2:


            st.markdown("""
            
            <div class="project-card">


            <h2>
            🏢 Расчет и конструирование железобетонных конструкций одноэтажного промышленного здания в г. Магнитогорск
            </h2>


            <p>

            
            «Промышленное и гражданское строительство».

            Проект включает разработку конструктивной схемы,
            рабочей документации и инженерных расчётов.

            </p>



            <br>

            <b>
            Выполнено:
            </b>


            <ul>

            <li>Проектирование конструкций</li>

            <li>Чертежи AutoCAD</li>

            <li>BIM модель Revit</li>

            <li>Расчёт ЛИРА 10</li>

            

            </ul>


            <br>


            <span class="tag">
            AutoCAD
            </span>


            <span class="tag">
            Revit
            </span>


            <span class="tag">
            LIRA 10
            </span>


            <span class="tag">
            Excel
            </span>


            </div>

            """,
            unsafe_allow_html=True)



        st.write("")



        # تحميل المشروع


        if os.path.exists(
        "ГЧ.pdf"
        ):


            with open(
            "ГЧ.pdf",
            "rb"
            ) as file:


                st.download_button(

                    label="📄 Скачать полный проект",

                    data=file,

                    file_name=
                    "Project_ГЧ.pdf",

                    mime=
                    "application/pdf",

                    use_container_width=True

                )


        else:


            st.warning(
            "Файл проекта не найден"
            )








#=========================================
#=========================================



elif selected=="Python":

    st.header("💻 Python")

    st.success("Программы и автоматизация")



#=========================================
#=========================================


# ```python
elif selected == "Медиа":

    st.markdown("""
    <style>

    /* =========================
       MEDIA HEADER
       ========================= */

    .media-header{

        background:
        linear-gradient(
            135deg,
            rgba(30,41,59,.95),
            rgba(15,23,42,.95)
        );

        padding:35px;

        border-radius:30px;

        color:white;

        text-align:center;

        box-shadow:
        0 20px 45px rgba(0,0,0,.4);

        margin-bottom:40px;
    }


    .media-title{

        font-size:45px;

        font-weight:900;

        color:white;

        margin-bottom:8px;

    }


    .media-sub{

        color:#94a3b8;

        font-size:19px;

    }


    /* =========================
       VIDEO CARD
       ========================= */

    .video-card{

        background:
        rgba(30,41,59,.85);

        backdrop-filter:blur(15px);

        border-radius:25px;

        padding:25px;

        margin-bottom:15px;

        box-shadow:
        0 15px 40px rgba(0,0,0,.35);

        border:
        1px solid rgba(255,255,255,.05);

        transition:.3s ease;

    }


    .video-card:hover{

        transform:translateY(-5px);

        box-shadow:
        0 25px 50px rgba(0,0,0,.45);

    }


    .video-title{

        color:white;

        font-size:28px;

        font-weight:800;

        margin-bottom:10px;

        text-align:center;

    }


    .video-description{

        color:#cbd5e1;

        font-size:16px;

        line-height:1.7;

        text-align:center;

        margin-bottom:20px;

    }


    /* =========================
       TAGS
       ========================= */

    .video-tag{

        display:inline-block;

        padding:7px 15px;

        margin:4px;

        border-radius:20px;

        background:#2563eb;

        color:white;

        font-size:13px;

        font-weight:700;

    }


    .tags-container{

        text-align:center;

        margin-top:15px;

        margin-bottom:45px;

    }


    </style>
    """, unsafe_allow_html=True)


    # =====================================================
    # HEADER
    # =====================================================

    st.markdown("""
    <div class="media-header">

        <div class="media-title">
            🎥 Медиа
        </div>

        <div class="media-sub">
            Инженерные проекты, расчёты и автоматизация
        </div>

    </div>
    """, unsafe_allow_html=True)


    # =====================================================
    # VIDEOS
    # =====================================================

    videos = [

        # =================================================
        # VIDEO 1
        # =================================================

        {
            "title":
            "📐 Расчёт металлической фермы | LIRA 10",

            "description":
            """
            Демонстрация инженерного расчёта металлической фермы.
            В видео показан процесс создания расчётной схемы,
            задания нагрузок и анализа результатов.
            """,

            "url":
            "https://youtu.be/FUQH9DWbkg4",

            "tags":
            [
                "LIRA 10",
                "Structural Design",
                "Расчёты"
            ]
        },


        # =================================================
        # VIDEO 2
        # =================================================

        {
            "title":
            "📄 Автоматизация АОСР | Excel + Word",

            "description":
            """
            Демонстрация автоматизации заполнения АОСР
            с использованием Excel и Word.
            Данные из Excel автоматически используются
            для заполнения исполнительной документации.
            """,

            "url":
            "https://www.youtube.com/watch?v=CkulkAB6OdU",

            "tags":
            [
                "ПТО",
                "АОСР",
                "Excel",
                "Word",
                "Автоматизация"
            ]
        },


    



        # =================================================
        # VIDEO 3
        # =================================================

        {
            "title":
            "📄 Автоматизация АОСР | Excel + Word",

            "description":
            """
            Демонстрация автоматизации заполнения АОСР
            с использованием Excel и Word.
            Данные из Excel автоматически используются
            для заполнения исполнительной документации.
            """,

            "url":
            "https://www.youtube.com/watch?v=qkhwPi5slX0",

            "tags":
            [
                "ПТО",
                "АОСР",
                "Excel",
                "Word",
                "Автоматизация"
            ]
        }

    ]



    # =====================================================
    # DISPLAY VIDEOS
    # =====================================================

    for video in videos:

        # -----------------------------------------
        # CARD HEADER
        # -----------------------------------------

        st.markdown(
            f"""
            <div class="video-card">

                <div class="video-title">
                    {video["title"]}
                </div>

                <div class="video-description">
                    {video["description"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        # -----------------------------------------
        # SMALL VIDEO
        # -----------------------------------------

        left, center, right = st.columns([1, 2, 1])

        with center:

            st.video(
                video["url"]
            )


        # -----------------------------------------
        # TAGS
        # -----------------------------------------

        tags_html = ""

        for tag in video["tags"]:

            tags_html += f"""
            <span class="video-tag">
                {tag}
            </span>
            """


        st.markdown(
            f"""
            <div class="tags-container">
                {tags_html}
            </div>
            """,
            unsafe_allow_html=True
        )
# ```



#=========================================
#=========================================







# elif selected=="Контакты":

#     st.header("☎ Контакты")

#     st.write("""
# 📧 Email

# 💼 Telegram

# 🌐 LinkedIn

# 📂 GitHub
# """)








#=========================================
#=========================================
# elif selected == "Сертификат":

#     st.header("📜 Сертификат")

#     st.write("Здесь будут размещены мои сертификаты.")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.info("🏅 Revit")

#     with col2:
#         st.info("🏅 Python")







#=========================================
#=========================================



# elif selected == "Языки":

#     st.header("🌍 Языки")

#     st.markdown("""
# ### 🇪🇬 Арабский
# Родной язык

# ---

# ### 🇬🇧 Английский
# Средний уровень (B1)

# ---

# ### 🇷🇺 Русский
# Средний уровень (B1)
# Продолжаю активно совершенствовать язык в профессиональной сфере.
# """)
