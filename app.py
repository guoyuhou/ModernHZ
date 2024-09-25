import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pydeck as pdk
from streamlit_webrtc import webrtc_streamer
import av
import time
import altair as alt
import numpy as np
from streamlit_ace import st_ace
from streamlit_agraph import agraph, Node, Edge, Config
from streamlit_drawable_canvas import st_canvas
import json
from pathlib import Path
import openai

# 设置页面配置
st.set_page_config(page_title="ModernHZ团队", page_icon="🚀", layout="wide")

# 加载Lottie动画
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 自定义CSS样式
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    :root {
        --primary-color: #1E90FF;
        --secondary-color: #4682B4;
        --accent-color: #20B2AA;
        --background-color: #f0f2f6;
        --text-color: #333;
    }
    
    .dark {
        --primary-color: #4DA8DA;
        --secondary-color: #89CFF0;
        --accent-color: #40E0D0;
        --background-color: #2C3E50;
        --text-color: #ECF0F1;
    }
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: var(--background-color);
        color: var(--text-color);
        transition: all 0.3s ease;
    }
    .main-header {
        font-size: 3.5rem;
        color: var(--primary-color);
        text-align: center;
        font-weight: 700;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.8rem;
        color: var(--secondary-color);
        text-align: center;
        font-weight: 300;
        margin-bottom: 3rem;
    }
    .section-header {
        font-size: 2.2rem;
        color: var(--accent-color);
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid var(--accent-color);
        padding-bottom: 0.5rem;
    }   +
    .content {
        font-size: 1.1rem;
        line-height: 1.8;
    }
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: var(--secondary-color);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 1px solid var(--primary-color);
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .stPlotlyChart {
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 1rem;
    }
    #particles-js {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏
def sidebar():
    with st.sidebar:
        st.markdown("""
        <style>
        .sidebar .sidebar-content {
            width: 250px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.image("images/SpaceX-2.jpg", width=150)
        selected = option_menu(
            menu_title="ModernHZ导航",
            options=["主页", "团队介绍", "项目展示", "知识库", "加入我们", "实时协作", "AI助手", "数据仪表板", "创新挑战"],
            icons=["house", "people", "kanban", "book", "envelope", "camera-video", "robot", "bar-chart", "trophy"],
            menu_icon="rocket",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "14px"}, 
                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
        
        # 深色模式切换
        if st.checkbox("深色模式", key="dark_mode"):
            st.markdown("""
            <script>
                document.body.classList.add('dark');
            </script>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <script>
                document.body.classList.remove('dark');
            </script>
            """, unsafe_allow_html=True)
        
    return selected

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_home():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap');
    
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 700;
        color: #00BFFF;
        text-align: center;
        text-shadow: 0 0 10px rgba(0,191,255,0.5);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 10px rgba(0,191,255,0.5);
        }
        to {
            text-shadow: 0 0 20px rgba(0,191,255,0.8), 0 0 30px rgba(0,191,255,0.6), 0 0 40px rgba(0,191,255,0.4);
        }
    }
    
    .sub-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        color: #B0E0E6;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .innovation-card {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    .innovation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,191,255,0.2);
    }
    
    .innovation-icon {
        font-size: 3rem;
        margin-bottom: 10px;
        text-align: center;
    }
    
    .innovation-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        color: #00BFFF;
        margin-bottom: 10px;
        text-align: center;
    }
    
    .innovation-description {
        color: #B0E0E6;
        text-align: center;
    }
    
    .quote-container {
        background: rgba(0,191,255,0.1);
        border-radius: 15px;
        padding: 20px;
        margin-top: 2rem;
        text-align: center;
        font-style: italic;
        color: #B0E0E6;
    }
    
    .interactive-globe {
        width: 100%;
        height: 400px;
    }
    
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>ModernHZ 创新实验室</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>突破界限，创造未来</p>", unsafe_allow_html=True)

    # 创新领域展示
    col1, col2, col3 = st.columns(3)
    innovation_areas = [
        {"icon": "🧠", "title": "人工智能", "description": "探索AI的无限可能，重塑世界的运作方式。"},
        {"icon": "🌐", "title": "物联网", "description": "连接万物，智能化改变生活的每个角落。"},
        {"icon": "🚀", "title": "太空技术", "description": "突破地球的束缚，开启人类文明的新篇章。"}
    ]
    
    for col, area in zip([col1, col2, col3], innovation_areas):
        with col:
            st.markdown(f"""
            <div class='innovation-card'>
                <div class='innovation-icon'>{area['icon']}</div>
                <div class='innovation-title'>{area['title']}</div>
                <div class='innovation-description'>{area['description']}</div>
            </div>
            """, unsafe_allow_html=True)

    # 交互式地球仪
    st.markdown("<h2 class='innovation-title'>全球创新网络</h2>", unsafe_allow_html=True)
    fig = go.Figure(data=go.Scattergeo(
        lon = [116.4, -74, 37.8, 151.2, 55.7],
        lat = [39.9, 40.7, -37.8, -33.9, -37.8],
        text = ['北京', '纽约', '墨尔本', '悉尼', '开普敦'],
        mode = 'markers',
        marker = dict(
            size = 10,
            color = 'rgb(0, 191, 255)',
            line = dict(
                width = 3,
                color = 'rgba(0, 191, 255, 0.8)'
            )
        )
    ))

    fig.update_layout(
        geo = dict(
            projection_type = 'orthographic',
            showland = True,
            landcolor = 'rgb(30, 30, 30)',
            countrycolor = 'rgb(50, 50, 50)',
            showocean = True,
            oceancolor = 'rgb(10, 10, 40)'
        ),
        height=500,
        margin={"r":0,"t":0,"l":0,"b":0},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)

    # 创新指数动画
    st.markdown("<h2 class='innovation-title'>ModernHZ 创新指数</h2>", unsafe_allow_html=True)
    innovation_index = random.randint(80, 100)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = innovation_index,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "创新指数", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "rgba(0,191,255,0.8)"},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "white",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(255,255,255,0.1)'},
                {'range': [50, 80], 'color': 'rgba(0,191,255,0.3)'},
                {'range': [80, 100], 'color': 'rgba(0,191,255,0.6)'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90}}))

    fig.update_layout(paper_bgcolor = "rgba(0,0,0,0)", font = {'color': "white", 'family': "Arial"})
    st.plotly_chart(fig, use_container_width=True)

    # 创新项目展示
    st.markdown("<h2 class='innovation-title'>突破性项目</h2>", unsafe_allow_html=True)
    projects = [
        {"name": "量子计算突破", "progress": 75},
        {"name": "脑机接口研发", "progress": 60},
        {"name": "可持续能源革命", "progress": 80},
        {"name": "纳米医疗技术", "progress": 70}
    ]
    
    for project in projects:
        st.markdown(f"""
        <div class='innovation-card'>
            <div class='innovation-title'>{project['name']}</div>
            <div class='progress-bar' style='background: linear-gradient(to right, rgba(0,191,255,0.8) {project['progress']}%, rgba(255,255,255,0.1) {project['progress']}%); height: 10px; border-radius: 5px;'></div>
            <div style='text-align: right; color: #B0E0E6;'>{project['progress']}%</div>
        </div>
        """, unsafe_allow_html=True)

    # 动画展示
    st_lottie(load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ystsffqy.json"), height=300)

    # 激励性名言
    quotes = [
        "创新是将想象力转化为现实的能力。 - 威廉·波拉德",
        "创新区分领导者和跟随者。 - 史蒂夫·乔布斯",
        "创新是一种生活方式，而不仅仅是一种思维方式。 - 迪恩·卡门",
        "最大的风险是不承担任何风险。在一个飞速变化的世界里，唯一保证失败的策略就是不承担风险。 - 马克·扎克伯格"
    ]
    st.markdown(f"""
    <div class='quote-container'>
        "{random.choice(quotes)}"
    </div>
    """, unsafe_allow_html=True)

    # 互动部分
    st.markdown("<h2 class='innovation-title'>你的创新想法</h2>", unsafe_allow_html=True)
    user_idea = st.text_area("分享你的创新想法，成为改变世界的一部分！")
    if st.button("提交想法"):
        st.success("感谢您的分享！您的想法已经被记录，并将成为我们创新的灵感来源。")
        # 这里可以添加将用户想法保存到数据库的逻辑

    # 实时创新数据流
    st.markdown("<h2 class='innovation-title'>实时创新数据流</h2>", unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['创意生成', '专利申请', '技术突破'])

    st.line_chart(chart_data)

# 团队介绍
def show_team():
    st.markdown("<h1 class='main-header'>团队介绍</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content card'>
    我们是一群充满激情的创新者，专注于AI+领域的产品创造。
    我们的团队文化鼓励创造力、前沿思维和与众不同的观点。
    </div>
    """, unsafe_allow_html=True)
    
    team_members = [
        {"name": "张三", "role": "创始人 & CEO", "image": "member1.jpg", "bio": "AI领域专家，拥有10年产品开发经验"},
        {"name": "李四", "role": "CTO", "image": "member2.jpg", "bio": "全栈开发工程师，热衷于新技术探索"},
        {"name": "王五", "role": "产品经理", "image": "member3.jpg", "bio": "用户体验设计专家，擅长产品创新"},
    ]
    
    cols = st.columns(3)
    for idx, member in enumerate(team_members):
        with cols[idx]:
            st.markdown(f"""
            <div class='card'>
                <img src='{member["image"]}' style='width:100%; border-radius:10px;'>
                <h3>{member["name"]}</h3>
                <h4>{member["role"]}</h4>
                <p>{member["bio"]}</p>
            </div>
            """, unsafe_allow_html=True)

    # 添加团队技能雷达图
    skills = ['AI', '产品开发', 'UI/UX', '数据分析', '项目管理']
    values = [9, 8, 7, 8, 9]

    fig = go.Figure(data=go.Scatterpolar(
      r=values,
      theta=skills,
      fill='toself'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 10]
        )),
      showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<h3 class='section-header'>团队协作网络</h3>", unsafe_allow_html=True)
    
    nodes = [
        Node(id="1", label="张三", size=25),
        Node(id="2", label="李四", size=25),
        Node(id="3", label="王五", size=25),
        Node(id="4", label="AI项目", size=20, shape="diamond"),
        Node(id="5", label="IoT项目", size=20, shape="diamond"),
    ]
    
    edges = [
        Edge(source="1", target="4", type="CURVE_SMOOTH"),
        Edge(source="2", target="4", type="CURVE_SMOOTH"),
        Edge(source="2", target="5", type="CURVE_SMOOTH"),
        Edge(source="3", target="5", type="CURVE_SMOOTH"),
    ]
    
    config = Config(width=700, 
                    height=500, 
                    directed=True,
                    physics=True, 
                    hierarchical=False)
    
    return_value = agraph(nodes=nodes, 
                          edges=edges, 
                          config=config)

# 项目展示
def show_projects():
    st.markdown("<h1 class='main-header'>项目展示</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>以下是我们团队的一些代表性项目:</div>", unsafe_allow_html=True)
    
    projects = [
        {"name": "快速APP搭建工作流", "description": "自主开发的高效APP开发流程和范式，大大提高了产品迭代速度。", "image": "images/SpaceX-2.jpg"},
        {"name": "AI+产品创新", "description": "积极探索AI技术与现有产品的结合，不断创造新的可能性。", "image": "images/SpaceX-2.jpg"},
        {"name": "智能数据分析平台", "description": "利用机器学习算法，为企业提供深度数据洞察。", "image": "images/SpaceX-2.jpg"},
    ]
    
    for project in projects:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(project["image"], use_column_width=True)
        with col2:
            st.subheader(project["name"])
            st.write(project["description"])
        st.markdown("---")
    
    # 添加项目进度甘特图
    df = pd.DataFrame([
        dict(Task="项目A", Start='2023-01-01', Finish='2023-05-15', Resource="团队1"),
        dict(Task="项目B", Start='2023-02-15', Finish='2023-08-30', Resource="团队2"),
        dict(Task="项目C", Start='2023-04-01', Finish='2023-12-31', Resource="团队3")
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

    # 在项目展示页面添加3D地图
    st.subheader("全球项目分布")
    
    chart_data = pd.DataFrame({
        'lat': [40.7128, 37.7749, 51.5074],
        'lon': [-74.0060, -122.4194, -0.1278],
        'project': ['纽约项目', '旧金山项目', '伦敦项目'],
        'size': [100, 150, 80]
    })

    view_state = pdk.ViewState(
        latitude=chart_data["lat"].mean(),
        longitude=chart_data["lon"].mean(),
        zoom=3,
        pitch=50,
    )

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=chart_data,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius='size',
        pickable=True
    )

    tool_tip = {"html": "项目: {project}", "style": {"backgroundColor": "steelblue", "color": "white"}}

    deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=view_state,
        layers=[layer],
        tooltip=tool_tip
    )

    st.pydeck_chart(deck)

    st.markdown("<h3 class='section-header'>实时代码编辑</h3>", unsafe_allow_html=True)
    code = st_ace(language="python", theme="monokai", value="# 在这里编写你的Python代码")
    if code:
        st.code(code)

# 知识库
def show_knowledge_base():
    st.markdown("<h1 class='main-header'>知识库</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>这里是我们团队积累的知识和经验分享:</div>", unsafe_allow_html=True)
    
    categories = ["AI技术", "产品开发", "团队管理", "创新思维"]
    selected_category = st.selectbox("选择分类", categories)
    
    # 这里可以根据选择的分类显示相应的文章列表
    st.markdown(f"### {selected_category}相关文章")
    st.markdown("1. [文章标题1](#)")
    st.markdown("2. [文章标题2](#)")
    st.markdown("3. [文章标题3](#)")
    
    # 添加一个简单的统计图表
    data = pd.DataFrame({
        "类别": categories,
        "文章数量": [15, 20, 10, 18]
    })
    fig = px.bar(data, x="类别", y="文章数量", title="各分类文章数量")
    st.plotly_chart(fig)

    # 添加词云图
    text = "AI Machine_Learning Deep_Learning Neural_Networks Natural_Language_Processing Computer_Vision Reinforcement_Learning Data_Mining Big_Data Cloud_Computing Innovation Product_Development Team_Management Agile Scrum DevOps Blockchain IoT Artificial_Intelligence"
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

# 加入我们
def show_join():
    st.markdown("<h1 class='main-header'>加入我们</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content card'>
    如果你也热爱创新，渴望做有意义的事情，欢迎加入ModernHZ团队!
    我们期待与志同道合的伙伴一起，共同创造更多令人兴奋的产品。
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("开放职位")
        st.markdown("- AI研究员")
        st.markdown("- 全栈开发工程师")
        st.markdown("- 产品经理")
        st.markdown("- UI/UX设计师")
    
    with col2:
        st.subheader("联系我们")
        name = st.text_input("姓名")
        email = st.text_input("邮箱")
        message = st.text_area("留言")
        if st.button("提交"):
            st.success("感谢您的留言，我们会尽快与您联系!")

    # 添加位置地图
    st.subheader("我们的位置")
    df = pd.DataFrame({
        'lat': [31.2304],
        'lon': [121.4737]
    })
    st.map(df)

def guess_number_game():
    st.markdown("<h3 class='section-header'>猜数字游戏</h3>", unsafe_allow_html=True)
    st.write("猜一个1到100之间的数字！")
    
    number = random.randint(1, 100)

def show_collaboration():
    st.markdown("<h1 class='main-header'>团队协作工具</h1>", unsafe_allow_html=True)
    
    tools = {
        "视频会议": {"icon": "🎥", "description": "高清视频会议，支持屏幕共享"},
        "实时文档": {"icon": "📄", "description": "多人同时编辑文档，实时同步"},
        "项目管理": {"icon": "📊", "description": "任务分配、进度跟踪、里程碑管理"},
        "头脑风暴": {"icon": "💡", "description": "虚拟白板，支持实时协作绘图"},
        "代码仓库": {"icon": "💻", "description": "代码版本控制，支持代码审查"}
    }
    
    cols = st.columns(3)
    for idx, (tool, info) in enumerate(tools.items()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='card'>
            <h3>{info['icon']} {tool}</h3>
            <p>{info['description']}</p>
            <button class='stButton'>开始使用</button>
            </div>
            """, unsafe_allow_html=True)
    
    # 保留原有的视频会议功能
    st.markdown("### 视频会议")
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

def show_ai_assistant():
    st.markdown("<h1 class='main-header'>AI创新助手</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content card'>有任何创新想法或问题？让AI助手帮你梳理思路！</div>", unsafe_allow_html=True)
    
    # 初始化对话历史
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # 显示对话历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 用户输入
    if prompt := st.chat_input("你的问题是？"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是ModernHZ团队的AI创新助手，专门帮助用户激发创意、解决创新难题。"},
                    {"role": "user", "content": prompt},
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 添加思维导图生成功能
    if st.button("生成思维导图"):
        # 这里可以集成一个思维导图生成API
        st.image("path_to_generated_mindmap.png", caption="基于对话生成的思维导图")

    # 添加创意评分系统
    if st.button("评估我的创意"):
        # 这里可以使用NLP模型来评估创意的新颖性、可行性等
        st.markdown("""
        <div class="idea-score">
            <h3>创意评分</h3>
            <div class="score-item">
                <span>新颖性</span>
                <div class="progress-bar" style="width: 85%;"></div>
                <span>85%</span>
            </div>
            <div class="score-item">
                <span>可行性</span>
                <div class="progress-bar" style="width: 70%;"></div>
                <span>70%</span>
            </div>
            <div class="score-item">
                <span>市场潜力</span>
                <div class="progress-bar" style="width: 90%;"></div>
                <span>90%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 添加新的CSS样式
st.markdown("""
<style>
.idea-score {
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 10px;
}
.score-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.progress-bar {
    height: 20px;
    background-color: #4CAF50;
    margin: 0 10px;
}
</style>
""", unsafe_allow_html=True)

def show_dashboard():
    st.markdown("<h1 class='main-header'>实时数据仪表板</h1>", unsafe_allow_html=True)
    
    # 由于streamlit_extras.stqdm不可用，我们将使用st.progress来模拟进度条
    progress_bars = []
    for i in range(5):
        progress_bars.append(st.progress(0))
    
    for _ in range(100):
        for bar in progress_bars:
            bar.progress(random.randint(1, 100))
        time.sleep(0.1)

def innovation_challenge():
    st.markdown("<h2 class='section-header'>创新挑战</h2>", unsafe_allow_html=True)
    st.write("欢迎来到ModernHZ的创新实验室！")

    # 初始化游戏状态
    if 'game_state' not in st.session_state:
        st.session_state.game_state = {
            'level': 1,
            'score': 0,
            'challenges_completed': 0,
            'current_challenge': generate_challenge()
        }

    # 显示当前等级和分数
    st.markdown(f"""
    <div class='game-stats'>
        <span>等级: {st.session_state.game_state['level']}</span>
        <span>分数: {st.session_state.game_state['score']}</span>
    </div>
    """, unsafe_allow_html=True)

    # 显示当前挑战
    st.markdown(f"""
    <div class='challenge-card'>
        <h3>当前挑战：{st.session_state.game_state['current_challenge']['title']}</h3>
        <p>{st.session_state.game_state['current_challenge']['description']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 用户输入
    user_solution = st.text_area("你的创新方案：")

    if st.button("提交方案"):
        score = evaluate_solution(user_solution, st.session_state.game_state['current_challenge'])
        st.session_state.game_state['score'] += score
        st.session_state.game_state['challenges_completed'] += 1

        if st.session_state.game_state['challenges_completed'] % 3 == 0:
            st.session_state.game_state['level'] += 1
            st.success(f"恭喜你晋级到 {st.session_state.game_state['level']} 级创新大师！")

        st.session_state.game_state['current_challenge'] = generate_challenge()
        st.experimental_rerun()

    # 创新排行榜
    show_leaderboard()

def generate_challenge():
    challenges = [
        {"title": "未来城市", "description": "设计一个解决未来城市交通拥堵问题的创新方案。"},
        {"title": "环保科技", "description": "提出一个能够显著减少塑料污染的创新技术或产品。"},
        {"title": "教育革新", "description": "构思一种利用VR/AR技术提升学习体验的创新教育方法。"},
        # 添加更多挑战...
    ]
    return random.choice(challenges)

def evaluate_solution(solution, challenge):
    # 这里可以集成更复杂的评分系统，如NLP分析等
    keywords = ["创新", "可行", "影响力", "可持续"]
    score = sum(10 for keyword in keywords if keyword in solution.lower())
    return min(score, 100)  # 最高100分

def show_leaderboard():
    st.markdown("<h3>创新英雄榜</h3>", unsafe_allow_html=True)
    leaderboard = [
        {"name": "爱因斯坦", "score": 1000},
        {"name": "达芬奇", "score": 950},
        {"name": "特斯拉", "score": 900},
        {"name": st.session_state.name, "score": st.session_state.game_state['score']}
    ]
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    for i, player in enumerate(leaderboard[:5], 1):
        st.markdown(f"{i}. {player['name']} - {player['score']}分")

# 在CSS中添加新的样式
st.markdown("""
<style>
.game-stats {
    display: flex;
    justify-content: space-around;
    padding: 10px;
    background-color: rgba(255,255,255,0.1);
    border-radius: 10px;
    margin-bottom: 20px;
}
.game-stats span {
    font-size: 18px;
    font-weight: bold;
}
.challenge-card {
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

def change_theme():
    themes = {
        "默认": {"primary": "#1E90FF", "secondary": "#4682B4", "background": "#f0f2f6"},
        "深邃夜空": {"primary": "#4DA8DA", "secondary": "#89CFF0", "background": "#2C3E50"},
        "森林绿意": {"primary": "#2ecc71", "secondary": "#27ae60", "background": "#f1f8e9"},
        "温暖阳光": {"primary": "#f39c12", "secondary": "#f1c40f", "background": "#fff5e6"}
    }
    
    selected_theme = st.sidebar.selectbox("选择主题", list(themes.keys()))
    
    theme = themes[selected_theme]
    st.markdown(f"""
    <style>
        :root {{
            --primary-color: {theme['primary']};
            --secondary-color: {theme['secondary']};
            --background-color: {theme['background']};
        }}
    </style>
    """, unsafe_allow_html=True)
import streamlit as st
import random

import streamlit as st
import random

import streamlit as st
import random

def welcome_screen():
    if 'name' not in st.session_state:
        st.session_state.name = ''
    
    # 生成随机的数据点和连接线
    nodes = ''.join([f'<div class="node" style="left: {random.randint(0, 100)}vw; top: {random.randint(0, 100)}vh;"></div>' for _ in range(20)])
    lines = ''.join([f'<div class="line" style="left: {random.randint(0, 100)}vw; top: {random.randint(0, 100)}vh; width: {random.randint(50, 200)}px; transform: rotate({random.randint(0, 360)}deg);"></div>' for _ in range(30)])
    
    st.markdown(f"""
    <style>
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); opacity: 0.5; }}
        50% {{ transform: scale(1.2); opacity: 1; }}
    }}
    @keyframes flow {{
        0% {{ background-position: 0% 50%; }}
        100% {{ background-position: 100% 50%; }}
    }}
    .node {{
        position: fixed;
        width: 8px;
        height: 8px;
        background-color: #4169E1;
        border-radius: 50%;
        animation: pulse 3s infinite;
    }}
    .line {{
        position: fixed;
        height: 2px;
        background: linear-gradient(90deg, rgba(65,105,225,0) 0%, rgba(65,105,225,1) 50%, rgba(65,105,225,0) 100%);
        opacity: 0.5;
        animation: flow 3s linear infinite;
    }}
    .innovation-background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: linear-gradient(135deg, #001F3F 0%, #003366 100%);
        z-index: -1;
    }}
    .welcome-header {{
        font-size: 4em;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-weight: bold;
    }}
    .welcome-subheader {{
        font-size: 1.8em;
        color: #B0E0E6;
        text-align: center;
        margin-bottom: 40px;
        position: relative;
        z-index: 1;
    }}
    .stApp {{
        background: transparent;
    }}
    .stButton>button {{
        background-color: #00BFFF;
        color: white;
        border-radius: 30px;
        padding: 10px 25px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: #1E90FF;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 191, 255, 0.4);
    }}
    .stTextInput>div>div>input {{
        border-radius: 15px;
        border: 2px solid #00BFFF;
        padding: 10px 15px;
        font-size: 16px;
        background-color: rgba(255, 255, 255, 0.1);
        color: #FFFFFF;
    }}
    .inspiration-quote {{
        font-style: italic;
        color: #B0E0E6;
        text-align: center;
        margin-top: 30px;
    }}
    .innovation-icon {{
        font-size: 3em;
        text-align: center;
        margin-bottom: 20px;
    }}
    </style>
    <div class="innovation-background"></div>
    <div class="node-container">{nodes}</div>
    <div class="line-container">{lines}</div>
    """, unsafe_allow_html=True)
    
    # 其余的函数内容保持不变
    if not st.session_state.name:
        st.markdown("<h1 class='welcome-header'>创新无界</h1>", unsafe_allow_html=True)
        st.markdown("<p class='welcome-subheader'>在ModernHZ，每个想法都是新世界的起点</p>", unsafe_allow_html=True)
        st.markdown("<div class='innovation-icon'>🚀💡🌟</div>", unsafe_allow_html=True)
        
        name = st.text_input("请输入你的名字", key="welcome_input", max_chars=50)
        if st.button("开启你的创新之旅", key="welcome_button"):
            if name:
                st.session_state.name = name
            else:
                st.warning("请输入你的名字")
        
        st.markdown("<p class='inspiration-quote'>\"创新是将想象力转化为现实的能力。\" —— 威廉·波拉德</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 class='welcome-header'>欢迎回来，{st.session_state.name}</h1>", unsafe_allow_html=True)
        st.markdown("<p class='welcome-subheader'>你的下一个突破性想法，就在眼前</p>", unsafe_allow_html=True)
        st.markdown("<div class='innovation-icon'>🌈🔬🎨</div>", unsafe_allow_html=True)
        
        
        daily_inspirations = [
            "今天，让我们挑战不可能！",
            "创新始于问题，成于解决。",
            "在平凡中发现非凡，在已知中探索未知。",
            "每一次失败都是成功的铺垫。",
            "创新不是目的地，而是一段永无止境的旅程。"
        ]
        st.markdown(f"<p class='inspiration-quote'>{random.choice(daily_inspirations)}</p>", unsafe_allow_html=True)

    # 添加一个隐藏的按钮，用于重置用户名（仅用于测试目的）
    if st.button("重置", key="reset_button", help="重置用户名（仅用于测试）"):
        st.session_state.name = ''
# 主函数
def main():
    if 'name' not in st.session_state or not st.session_state.name:
        welcome_screen()
    else:
        change_theme()  # 在侧边栏添加主题选择
        page = sidebar()
        
        if page == "主页":
            show_home()
        elif page == "团队介绍":
            show_team()
        elif page == "项目展示":
            show_projects()
        elif page == "知识库":
            show_knowledge_base()
        elif page == "加入我们":
            show_join()
        elif page == "实时协作":
            show_collaboration()
        elif page == "AI助手":
            show_ai_assistant()
        elif page == "数据仪表板":
            show_dashboard()
        elif page == "创新挑战":
            innovation_challenge()

if __name__ == "__main__":
    main()
