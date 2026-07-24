import streamlit as st
from streamlit_option_menu import option_menu

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
# MENU
# ==============================

selected = option_menu(
    menu_title=None,

    options=[
        "Главная",
        "Обо мне",
        "Портфолио",
        "Python",
        "Видео",
        "Контакты"
    ],

    icons=[
        "house-fill",
        "person-fill",
        "folder-fill",
        "cpu-fill",
        "camera-video-fill",
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

<h1>Hazem Hesham</h1>

<h3>Civil Structural Engineer</h3>

<p>Revit • AutoCAD • Python • BIM • AI</p>

</div>

""",unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
<div class='card'>
<h3>🏗️ ПТО</h3>
Исполнительная документация

АОСР

Журналы работ

ВОР
</div>
""",unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class='card'>
<h3>💻 Python</h3>

Автоматизация

Парсинг PDF

Streamlit

Excel
</div>
""",unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class='card'>
<h3>📐 BIM</h3>

Revit

AutoCAD

ЛИРА

3D модели
</div>
""",unsafe_allow_html=True)

elif selected=="Обо мне":

    st.header("👤 Обо мне")

    st.write("""
Здравствуйте!

Меня зовут Хазем Хешам.

Я инженер ПГС.

Интересуюсь BIM, Python, автоматизацией инженерных процессов и искусственным интеллектом.
""")

elif selected=="Портфолио":

    st.header("📂 Портфолио")

    st.info("Здесь будут мои проекты.")

elif selected=="Python":

    st.header("💻 Python")

    st.success("Программы и автоматизация")

elif selected=="Видео":

    st.header("🎥 Видео")

    st.write("Видео с YouTube.")

elif selected=="Контакты":

    st.header("☎ Контакты")

    st.write("""
📧 Email

💼 Telegram

🌐 LinkedIn

📂 GitHub
""")