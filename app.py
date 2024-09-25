import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json

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
            options=["主页", "团队介绍", "项目展示", "知识库", "加入我们"],
            icons=["house", "people", "kanban", "book", "envelope"],
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

# 主页
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

# 项目展示
def show_projects():
    st.markdown("<h1 class='main-header'>项目展示</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>以下是我们团队的一些代表性项目:</div>", unsafe_allow_html=True)
    
    projects = [
        {"name": "快速APP搭建工作流", "description": "自主开发的高效APP开发流程和范式，大大提高了产品迭代速度。", "image": "project1.jpg"},
        {"name": "AI+产品创新", "description": "积极探索AI技术与现有产品的结合，不断创造新的可能性。", "image": "project2.jpg"},
        {"name": "智能数据分析平台", "description": "利用机器学习算法，为企业提供深度数据洞察。", "image": "project3.jpg"},
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
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    text = "AI 机器学习 深度学习 神经网络 自然语言处理 计算机视觉 强化学习 数据挖掘 ���数据 云计算"
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

# 主函数
def main():
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

if __name__ == "__main__":
    main()
