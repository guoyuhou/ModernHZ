import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import os

# 设置页面配置
st.set_page_config(page_title="ModernHZ团队", page_icon="🚀", layout="wide")

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E90FF;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4682B4;
        text-align: center;
    }
    .section-header {
        font-size: 2rem;
        color: #20B2AA;
    }
    .content {
        font-size: 1.1rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏
def sidebar():
    with st.sidebar:
        st.image("images/SpaceX-2.jpg", width=200)
        st.title("ModernHZ导航")
        return st.radio("选择页面", ["主页", "团队介绍", "项目展示", "知识库", "加入我们"])

# 主页
def show_home():
    st.markdown("<h1 class='main-header'>欢迎来到ModernHZ</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Be creative, be at the frontier, and be different.</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='content'>
        ModernHZ是一个致力于创新和独特产品开发的团队。我们的目标是:
        <ol>
            <li>做有意义的事情</li>
            <li>创造创新性和与众不同的产品</li>
            <li>吸引有同样梦想的人</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("images/SpaceX-2.jpg", caption="ModernHZ团队", use_column_width=True)
    
    st.markdown("<h3 class='section-header'>我们的愿景</h3>", unsafe_allow_html=True)
    st.video("vision_video.mp4")

# 团队介绍
def show_team():
    st.markdown("<h1 class='main-header'>团队介绍</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content'>
    我们是一群充满激情的创新者,专注于AI+领域的产品创造。
    我们的团队文化鼓励创造力、前沿思维和与众不同的观点。
    </div>
    """, unsafe_allow_html=True)
    
    team_members = [
        {"name": "张三", "role": "创始人 & CEO", "image": "member1.jpg", "bio": "AI领域专家,拥有10年产品开发经验"},
        {"name": "李四", "role": "CTO", "image": "member2.jpg", "bio": "全栈开发工程师,热衷于新技术探索"},
        {"name": "王五", "role": "产品经理", "image": "member3.jpg", "bio": "用户体验设计专家,擅长产品创新"},
    ]
    
    cols = st.columns(3)
    for idx, member in enumerate(team_members):
        with cols[idx]:
            st.image(member["image"], width=200)
            st.subheader(member["name"])
            st.write(member["role"])
            st.write(member["bio"])

# 项目展示
def show_projects():
    st.markdown("<h1 class='main-header'>项目展示</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>以下是我们团队的一些代表性项目:</div>", unsafe_allow_html=True)
    
    projects = [
        {"name": "快速APP搭建工作流", "description": "自主开发的高效APP开发流程和范式,大大提高了产品迭代速度。", "image": "project1.jpg"},
        {"name": "AI+产品创新", "description": "积极探索AI技术与现有产品的结合,不断创造新的可能性。", "image": "project2.jpg"},
        {"name": "智能数据分析平台", "description": "利用机器学习算法,为企业提供深度数据洞察。", "image": "project3.jpg"},
    ]
    
    for project in projects:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(project["image"], use_column_width=True)
        with col2:
            st.subheader(project["name"])
            st.write(project["description"])
        st.markdown("---")

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

# 加入我们
def show_join():
    st.markdown("<h1 class='main-header'>加入我们</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class='content'>
    如果你也热爱创新,渴望做有意义的事情,欢迎加入ModernHZ团队!
    我们期待与志同道合的伙伴一起,共同创造更多令人兴奋的产品。
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
            st.success("感谢您的留言,我们会尽快与您联系!")

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
