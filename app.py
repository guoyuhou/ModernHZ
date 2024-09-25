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

def show_home():
    st.markdown("<h1 class='main-header'>欢迎来到ModernHZ</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Be creative, be at the frontier, and be different.</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='content card'>
        <h3>我们的使命</h3>
        ModernHZ是一个致力于创新和独特产品开发的团队。我们的目标是:
        <ol>
            <li>做有意义的事情</li>
            <li>创造创新性和与众不同的产品</li>
            <li>吸引有同样梦想的人</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        st_lottie(lottie_coding, height=300, key="coding")
    
    st.markdown("<h3 class='section-header'>我们的愿景</h3>", unsafe_allow_html=True)
    st.video("video/elon_mask.mp4")
    
    st.markdown("<h3 class='section-header'>实时公司指标</h3>", unsafe_allow_html=True)
    
    # 模拟实时数据
    df = pd.DataFrame({
        'time': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'users': np.random.randint(100, 1000, 100),
        'revenue': np.random.randint(1000, 10000, 100)
    })
    
    chart = alt.Chart(df).transform_fold(
        ['users', 'revenue'],
        as_=['metric', 'value']
    ).mark_line().encode(
        x='time:T',
        y='value:Q',
        color='metric:N'
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)

    st.markdown("<h3 class='section-header'>我们的创新过程</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    try:
        animations = [
            {"key": "idea", "title": "创意孵化", "file": "Lottie/idea_animation.json"},
            {"key": "development", "title": "快速开发", "file": "Lottie/dev_animation.json"},
            {"key": "launch", "title": "产品发布", "file": "Lottie/launch_animation.json"}
        ]
        
        for col, anim in zip([col1, col2, col3], animations):
            with col:
                lottie_anim = load_lottiefile(anim["file"])
                if lottie_anim:
                    st_lottie(lottie_anim, key=anim["key"], height=200, quality="low", speed=1)
                    st.markdown(f"<h4 style='text-align: center;'>{anim['title']}</h4>", unsafe_allow_html=True)
                else:
                    st.warning(f"无法加载 {anim['title']} 动画")
    except Exception as e:
        st.error(f"加载动画时出错: {str(e)}")
        st.info("我们正在努力修复这个问题。请稍后再试。")

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
    st.markdown("<h1 class='main-header'>AI助手</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content card'>有任何问题？问问我们的AI助手吧！</div>", unsafe_allow_html=True)
    
    user_input = st.text_input("输入你的问题：")
    if user_input:
        st.write("AI助手：抱歉，AI助手功能暂时不可用。我们正在努力修复这个问题。请稍后再试。")

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
    st.write("欢迎参与ModernHZ的创新挑战！这个游戏将测试你的直觉和创新思维。")

    # 初始化会话状态
    if 'challenge_number' not in st.session_state:
        st.session_state.challenge_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.hints = []
        st.session_state.game_over = False

    if not st.session_state.game_over:
        guess = st.number_input("你的创新指数（1-100）：", min_value=1, max_value=100)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("提交猜测"):
                st.session_state.attempts += 1
                if guess == st.session_state.challenge_number:
                    st.success(f"恭喜你找到了最佳创新指数！你用了{st.session_state.attempts}次尝试。")
                    st.session_state.game_over = True
                elif guess < st.session_state.challenge_number:
                    st.warning("创新度不够，再大胆一些！")
                    st.session_state.hints.append(f"第{st.session_state.attempts}次：{guess} - 创新度不够")
                else:
                    st.warning("创新过头了，需要更务实一些！")
                    st.session_state.hints.append(f"第{st.session_state.attempts}次：{guess} - 创新过头了")
        
        with col2:
            if st.button("获取灵感"):
                inspiration = random.choice([
                    "想想未来科技可能带来的改变。",
                    "考虑如何将不同领域的知识结合起来。",
                    "关注用户的痛点，寻找创新的机会。",
                    "大胆假设，小心求证。",
                    "有时候，减法比加法更能带来创新。"
                ])
                st.info(f"灵感：{inspiration}")
        
        with col3:
            if st.button("重新挑战"):
                st.session_state.challenge_number = random.randint(1, 100)
                st.session_state.attempts = 0
                st.session_state.hints = []
                st.session_state.game_over = False
                st.experimental_rerun()

    # 显示历史记录
    if st.session_state.hints:
        st.markdown("### 创新历程")
        for hint in st.session_state.hints:
            st.write(hint)

    # 显示创新排行榜
    st.markdown("### 创新排行榜")
    leaderboard = {
        "爱因斯坦": 3,
        "特斯拉": 4,
        "乔布斯": 5,
        "马斯克": 6
    }
    for name, score in leaderboard.items():
        st.write(f"{name}: {score}次尝试")

    # 提供一些创新建议
    st.markdown("### 创新小贴士")
    st.write("1. 保持好奇心，不断学习新知识。")
    st.write("2. 勇于挑战常规，尝试不同的思路。")
    st.write("3. 与团队合作，集思广益。")
    st.write("4. 关注用户需求，以解决问题为导向。")
    st.write("5. 拥抱失败，从错误中学习。")

    # 添加创新项目展示
    st.markdown("<h2 class='section-header'>创新项目展示</h2>", unsafe_allow_html=True)
    projects = [
        {"name": "AI助手", "description": "基于最新NLP技术的智能助手", "progress": 75},
        {"name": "智能家居系统", "description": "整合IoT设备的智能家居解决方案", "progress": 60},
        {"name": "AR教育平台", "description": "利用增强现实技术的互动教育平台", "progress": 40}
    ]
    
    for project in projects:
        st.markdown(f"""
        <div class='card'>
        <h3>{project['name']}</h3>
        <p>{project['description']}</p>
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: {project['progress']}%;" aria-valuenow="{project['progress']}" aria-valuemin="0" aria-valuemax="100">{project['progress']}%</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>创意涂鸦板</h3>", unsafe_allow_html=True)
    st.write("在这里画出你的创新想法！")
    
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=3,
        stroke_color="#e00",
        background_color="#eee",
        height=300,
        drawing_mode="freedraw",
        key="canvas",
    )
    
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)

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

def welcome_screen():
    if 'name' not in st.session_state:
        st.session_state.name = ''
    
    if not st.session_state.name:
        st.markdown("<h1 class='main-header'>欢迎来到ModernHZ</h1>", unsafe_allow_html=True)
        name = st.text_input("请输入你的名字：")
        if st.button("开始探索"):
            st.session_state.name = name
            st.experimental_rerun()
    else:
        st.markdown(f"<h1 class='main-header'>欢迎回来，{st.session_state.name}！</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header'>准备好开始今天的创新之旅了吗？</p>", unsafe_allow_html=True)
        if st.button("开始探索"):
            st.experimental_rerun()

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
        
        # 在每个页面底部添加猜数字游戏
        guess_number_game()

if __name__ == "__main__":
    main()
