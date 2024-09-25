import streamlit as st
from PIL import Image
import os
def main():
    st.set_page_config(page_title="ModernHZ团队", page_icon="🚀", layout="wide")
    
    # 侧边栏
    st.sidebar.title("导航")
    page = st.sidebar.radio("选择页面", ["主页", "团队介绍", "项目展示", "加入我们"])
    
    if page == "主页":
        show_home()
    elif page == "团队介绍":
        show_team()
    elif page == "项目展示":
        show_projects()
    elif page == "加入我们":
        show_join()

def show_home():
    st.title("欢迎来到ModernHZ")
    st.subheader("Be creative, be at the frontier, and be different.")
    
    st.write("""
    ModernHZ是一个致力于创新和独特产品开发的团队。我们的目标是:
    1. 做有意义的事情   
    2. 创造创新性和与众不同的产品
    3. 吸引有同样梦想的人
    """)
    
    st.image("images/SpaceX-2.jpg", caption="ModernHZ团队", use_column_width=True)

def show_team():
    st.title("团队介绍")
    st.write("""
    我们是一群充满激情的创新者,专注于AI+领域的产品创造。
    我们的团队文化鼓励创造力、前沿思维和与众不同的观点。
    """)
    
    # 这里可以添加团队成员介绍

def show_projects():
    st.title("项目展示")
    st.write("以下是我们团队的一些代表性项目:")
    
    # 项目1
    st.subheader("快速APP搭建工作流")
    st.write("我们自主开发了一套高效的APP开发流程和范式,大大提高了产品迭代速度。")
    
    # 项目2
    st.subheader("AI+产品创新")
    st.write("我们积极探索AI技术与现有产品的结合,不断创造新的可能性。")
    
    # 可以继续添加更多项目

def show_join():
    st.title("加入我们")
    st.write("""
    如果你也热爱创新,渴望做有意义的事情,欢迎加入ModernHZ团队!
    我们期待与志同道合的伙伴一起,共同创造更多令人兴奋的产品。
    """)
    
    # 这里可以添加联系方式或申请表单

if __name__ == "__main__":
    main()
