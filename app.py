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
import streamlit.components.v1 as components

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

def show_home():
    st.markdown("<h1 class='main-header'>欢迎来到ModernHZ</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>创新无界，梦想无限</h2>", unsafe_allow_html=True)

    # 添加粒子效果背景
    st.markdown("""
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
    particlesJS('particles-js', {
      particles: {
        number: { value: 80, density: { enable: true, value_area: 800 } },
        color: { value: '#ffffff' },
        shape: { type: 'circle' },
        opacity: { value: 0.5, random: false },
        size: { value: 3, random: true },
        line_linked: { enable: true, distance: 150, color: '#ffffff', opacity: 0.4, width: 1 },
        move: { enable: true, speed: 6, direction: 'none', random: false, straight: false, out_mode: 'out', bounce: false }
      },
      interactivity: {
        detect_on: 'canvas',
        events: { onhover: { enable: true, mode: 'repulse' }, onclick: { enable: true, mode: 'push' }, resize: true },
        modes: { repulse: { distance: 100, duration: 0.4 }, push: { particles_nb: 4 } }
      },
      retina_detect: true
    });
    </script>
    <style>
    #particles-js {
      position: absolute;
      width: 100%;
      height: 100%;
      background-color: #000000;
      background-image: url('');
      background-repeat: no-repeat;
      background-size: cover;
      background-position: 50% 50%;
      z-index: -1;
    }
    </style>
    """, unsafe_allow_html=True)

    # 添加3D全息投影效果
    st.markdown("""
    <div class="hologram-container">
      <div class="hologram">
        <div class="hologram-text">ModernHZ</div>
      </div>
    </div>
    <style>
    @keyframes hologram {
      0% { transform: rotateX(0deg) rotateY(0deg); }
      100% { transform: rotateX(360deg) rotateY(360deg); }
    }
    .hologram-container {
      perspective: 1000px;
      height: 200px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .hologram {
      width: 200px;
      height: 200px;
      position: relative;
      transform-style: preserve-3d;
      animation: hologram 20s infinite linear;
    }
    .hologram-text {
      position: absolute;
      font-size: 24px;
      color: #00ffff;
      text-shadow: 0 0 10px #00ffff;
      opacity: 0.7;
    }
    .hologram-text:nth-child(1) { transform: translateZ(100px); }
    .hologram-text:nth-child(2) { transform: rotateY(90deg) translateZ(100px); }
    .hologram-text:nth-child(3) { transform: rotateY(180deg) translateZ(100px); }
    .hologram-text:nth-child(4) { transform: rotateY(-90deg) translateZ(100px); }
    </style>
    """, unsafe_allow_html=True)


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
    
    vision_col1, vision_col2, vision_col3 = st.columns(3)
    
    vision_animations = [
        {"key": "breakthrough", "title": "突破界限", "url": "https://assets5.lottiefiles.com/packages/lf20_rnnlxazi.json"},
        {"key": "change_world", "title": "改变世界", "url": "https://assets3.lottiefiles.com/private_files/lf30_bb9bkg1h.json"},
        {"key": "potential", "title": "激发潜能", "url": "https://assets2.lottiefiles.com/packages/lf20_inuxiflu.json"}
    ]
    for col, anim in zip([vision_col1, vision_col2, vision_col3], vision_animations):
        with col:
            lottie_anim = load_lottieurl(anim["url"])
            if lottie_anim:
                st_lottie(lottie_anim, key=anim["key"], height=150, quality="low", speed=1)
                st.markdown(f"""
                <div class='vision-card'>
                    <h4>{'🚀' if anim['title'] == '突破界限' else '🌍' if anim['title'] == '改变世界' else '🌟'} {anim['title']}</h4>
                    <p>{
                        "我们致力于打破传统思维的束缚，探索未知领域，创造前所未有的可能性。" if anim['title'] == '突破界限' else
                        "我们的目标是通过创新科技，解决人类面临的重大挑战，让世界变得更美好。" if anim['title'] == '改变世界' else
                        "我们相信每个人都有无限潜力，我们的产品将帮助人们释放创造力，实现自我价值。"
                    }</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning(f"无法加载 {anim['title']} 动画")
    
    st.markdown("""
    <div class='vision-quote'>
        "想象力比知识更重要。知识是有限的，而想象力概括着世界的一切，推动着进步，并且是知识进化的源泉。" —— 阿尔伯特·爱因斯坦
    </div>
    """, unsafe_allow_html=True)

    # 添加创新故事展示
    st.markdown("<h3 class='section-header'>创新故事</h3>", unsafe_allow_html=True)
    stories = [
        {"title": "从0到1：我们如何颠覆传统行业", "content": "这是一个关于我们如何在传统行业中引入创新解决方案的故事..."},
        {"title": "当AI遇上艺术：跨界创新的奇妙火花", "content": "探索人工智能如何为艺术创作带来新的可能性..."},
        {"title": "绿色科技：我们为地球做的那些事", "content": "了解我们如何利用技术创新来应对环境挑战..."}
    ]
    
    for i, story in enumerate(stories):
        with st.expander(f"故事 {i+1}: {story['title']}"):
            st.write(story['content'])
            if st.button(f"了解更多 {i+1}", key=f"story_{i}"):
                st.write("更多详细内容即将推出...")
    
    st.markdown("""
    <style>
    .streamlit-expanderHeader {
        background-color: var(--primary-color);
        color: white;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .streamlit-expanderContent {
        background-color: rgba(255,255,255,0.1);
        border-radius: 5px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # 添加互动式创新挑战
    st.markdown("<h3 class='section-header'>今日创新挑战</h3>", unsafe_allow_html=True)
    challenge = random.choice([
        "设计一个可以在5分钟内学会任何技能的AI助手",
        "发明一种可以清洁海洋的环保材料",
        "创造一个能够实现跨语言即时交流的设备"
    ])
    st.markdown(f"""
    <div class="challenge-card">
        <h4>🧠 {challenge}</h4>
        <p>接受挑战，展示你的创新思维！</p>
    </div>
    """, unsafe_allow_html=True)
    user_solution = st.text_area("你的创新方案是：")
    if st.button("提交方案"):
        st.success("太棒了！你的创新方案已经提交。我们的团队会认真审阅每一个想法！")

    # 添加实时创新指数
    st.markdown("<h3 class='section-header'>ModernHZ创新指数</h3>", unsafe_allow_html=True)
    innovation_index = random.randint(80, 100)
    st.markdown(f"""
    <div class="innovation-index">
        <div class="index-value" style="width: {innovation_index}%;">{innovation_index}</div>
    </div>
    <p class="index-description">我们的创新指数反映了团队的创新活力和项目进展。</p>
    <style>
    .innovation-index {{
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        height: 40px;
        position: relative;
        overflow: hidden;
    }}
    .index-value {{
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 10px;
        color: white;
        font-weight: bold;
        transition: width 1s ease-in-out;
    }}
    .index-description {{
        text-align: center;
        font-style: italic;
        margin-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # 添加团队成员见解
    st.markdown("<h3 class='section-header'>团队洞察</h3>", unsafe_allow_html=True)
    insights = [
        {"name": "刘曜畅", "role": "AI研究员", "insight": "未来的AI将不仅仅是工具，而是创新的伙伴。"},
        {"name": "王鸣乐", "role": "产品设计师", "insight": "最好的设计是让复杂变简单，让困难变轻松。"},
        {"name": "王一帆", "role": "创新战略师", "insight": "创新不是一蹴而就的，而是日积月累的结果。"}
    ]
    for insight in insights:
        st.markdown(f"""
        <div class="insight-card">
            <img src="https://api.dicebear.com/6.x/initials/svg?seed={insight['name']}" alt="{insight['name']}" class="avatar">
            <div class="insight-content">
                <h4>{insight['name']} - {insight['role']}</h4>
                <p>"{insight['insight']}"</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .insight-card {
        display: flex;
        align-items: center;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 15px;
    }
    .insight-content h4 {
        margin: 0;
        color: var(--primary-color);
    }
    .insight-content p {
        margin: 5px 0 0;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

    # 添加互动式创新工具箱
    st.markdown("<h3 class='section-header'>创新工具箱</h3>", unsafe_allow_html=True)
    tool = st.selectbox("选择一个创新工具", ["头脑风暴生成器", "创意评估矩阵", "未来趋势预测器"])
    if tool == "头脑风暴生成器":
        keywords = st.text_input("输入几个关键词，用逗号分隔")
        if st.button("生成创意"):
            ideas = [f"基于{keywords}的{random.choice(['智能家居', '可穿戴设备', '教育平台', '健康监测系统'])}" for _ in range(3)]
            for idea in ideas:
                st.markdown(f"- {idea}")
    elif tool == "创意评估矩阵":
        st.image("https://via.placeholder.com/500x300.png?text=创意评估矩阵示例", caption="创意评估矩阵示例")
    elif tool == "未来趋势预测器":
        st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=['AI', '可持续发展', '太空技术']))

    # 添加全球创新网络地图
    st.markdown("<h3 class='section-header'>全球创新网络</h3>", unsafe_allow_html=True)
    world_map = px.scatter_geo(
        pd.DataFrame({
            'lat': [40.7128, 51.5074, 35.6762, -33.8688, 1.3521],
            'lon': [-74.0060, -0.1278, 139.6503, 151.2093, 103.8198],
            'city': ['纽约', '伦敦', '东京', '悉尼', '新加坡'],
            'size': [20, 18, 15, 12, 10]
        }),
        lat='lat',
        lon='lon',
        hover_name='city',
        size='size',
        projection='natural earth',
        title='ModernHZ全球创新中心'
    )
    world_map.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(world_map, use_container_width=True)

    # 添加加入我们的号召
    st.markdown("""
    <div class="join-us">
        <h3>加入我们，共创未来！</h3>
        <p>我们正在寻找充满激情、富有创造力的人才。如果你对创新充满热情，欢迎加入我们的团队！</p>
        <a href="#" class="join-button">立即申请</a>
    </div>
    <style>
    .join-us {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        color: white;
    }
    .join-button {
        display: inline-block;
        background: white;
        color: var(--primary-color);
        padding: 10px 20px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .join-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

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
