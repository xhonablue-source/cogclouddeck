import streamlit as st
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Cognitive Cloud Education | Empowering the Future of Learning",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #005A9C, #F2A900);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #005A9C;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .challenge-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .solution-card {
        background: #F8F7F4;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #005A9C;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #005A9C;
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .team-card {
        background: #F8F7F4;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("🎓 Navigation")
page = st.sidebar.selectbox("Go to section:", [
    "🏠 Hero",
    "❗ Challenge", 
    "💡 Solution",
    "🖥️ Platform",
    "🎯 Why Us",
    "📈 Traction",
    "👥 Team",
    "🔮 Vision",
    "📞 Contact"
])

# Hero Section
if page == "🏠 Hero":
    st.markdown("""
    <div class="main-header">
        <h1>Cognitive Cloud Education</h1>
        <h2>Reversing the Trend of Disengagement</h2>
        <p>In an era of declining school populations, we offer a revolutionary AI-powered platform that transforms learning by deeply understanding each student. By integrating their names and interests into a personalized journey, we ensure every student feels seen, valued, and excited to come to school.</p>
    </div>
    """, unsafe_allow_html=True)

# Challenge Section
elif page == "❗ Challenge":
    st.markdown('<h2 class="section-header">The Evolving Landscape of K-12 Education</h2>', unsafe_allow_html=True)
    st.write("Traditional education faces significant hurdles in preparing students for a rapidly changing world.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="challenge-card">
            <h3>🏭 One-Size-Fits-All Approach</h3>
            <p>Standardized teaching often fails to cater to diverse learning styles and paces, leading to student disengagement.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="challenge-card">
            <h3>😰 Teacher Burden</h3>
            <p>Educators are swamped with administrative tasks, limiting their ability to provide individualized attention.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="challenge-card">
            <h3>❌ Future Skills Gap</h3>
            <p>Students often lack critical 21st-century skills in STEAM and AI literacy, crucial for future success.</p>
        </div>
        """, unsafe_allow_html=True)

# Solution Section
elif page == "💡 Solution":
    st.markdown('<h2 class="section-header">Our AI-Powered Solution</h2>', unsafe_allow_html=True)
    st.write("We revolutionize K-12 learning with an innovative platform designed to engage and empower.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="solution-card">
            <h3>🎯 Personalized Journeys</h3>
            <p>Our AI adapts content and pace to each student's unique needs, strengths, and interests.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="solution-card">
            <h3>💪 Empowered Educators</h3>
            <p>We provide teachers with AI-driven tools to automate tasks and gain real-time insights.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="solution-card">
            <h3>🌐 Bridged Tech Gap</h3>
            <p>Our platform makes advanced AI and educational technologies easy to integrate for any school.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="solution-card">
            <h3>🤝 Global Classrooms</h3>
            <p>We provide access to world-class resources and foster global collaboration.</p>
        </div>
        """, unsafe_allow_html=True)

# Platform Section
elif page == "🖥️ Platform":
    st.markdown('<h2 class="section-header">The Platform in Action</h2>', unsafe_allow_html=True)
    st.write("Explore the core components of our comprehensive educational ecosystem.")
    
    tab1, tab2, tab3 = st.tabs(["🧩 Adaptive Modules", "📊 Teacher Dashboard", "🎓 Teacher Training"])
    
    with tab1:
        st.markdown("### AI-Powered Adaptive Learning Modules")
        st.write("Our modules offer interactive lessons in STEAM subjects for grades 4-12. The AI provides dynamic content adjustments based on student performance and learning style, along with real-time feedback and personalized remediation to ensure mastery.")
    
    with tab2:
        st.markdown("### Insightful Teacher Dashboard")
        st.write("Our dashboard gives educators a holistic overview of student progress and engagement. AI-generated insights help identify learning gaps and inform instruction, while powerful tools simplify differentiated assignment creation and classroom management.")
    
    with tab3:
        st.markdown("### Comprehensive Teacher Training")
        st.write("We offer workshops and online courses on integrating AI into the curriculum. These programs cover best practices for personalized learning and lead to certification, empowering our teachers to become leaders in modern education.")

# Why Us Section
elif page == "🎯 Why Us":
    st.markdown('<h2 class="section-header">Why Cognitive Cloud Education?</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 A Growing Market for Innovation")
        st.write("The Global K-12 EdTech market is experiencing explosive growth, driven by the need for digital transformation and AI integration.")
        
        # Market growth chart
        market_data = pd.DataFrame({
            'Year': ['2024', '2026', '2028', '2030'],
            'Market Size (Billions USD)': [280, 325, 370, 404]
        })
        
        fig = px.bar(market_data, x='Year', y='Market Size (Billions USD)', 
                     title='Global K-12 EdTech Market Growth',
                     color_discrete_sequence=['#005A9C'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Our Differentiating Edge")
        st.markdown("""
        ✅ **Deep AI Integration:** Truly adaptive AI that personalizes learning at a granular level, not just digitized content.
        
        ✅ **Dual Focus:** We empower both students with personalized learning and teachers with powerful tools and training.
        
        ✅ **STEAM & Future Skills:** Our specialized content directly addresses the growing demand for skills crucial for the future workforce.
        """)

# Traction Section
elif page == "📈 Traction":
    st.markdown('<h2 class="section-header">Traction & Milestones</h2>', unsafe_allow_html=True)
    st.write("We are building strong momentum and achieving key milestones on our journey.")
    
    st.markdown("""
    - **Successful Pilot Programs:** We have implemented successful pilot programs in [X] schools, reaching [Y] students with positive initial results.
    - **Positive Teacher Feedback:** We have received enthusiastic feedback from [Z] teachers, reporting improved student engagement and reduced administrative workload.
    - **Core Module Deployment:** We have successfully developed and deployed core adaptive learning modules for key STEAM subjects.
    - **Strategic Partnerships:** The firm has established key collaborations with educational organizations and content providers.
    - **Growing User Base:** We are continuously expanding our user base, now serving [X] students and [Y] teachers.
    """)

# Team Section
elif page == "👥 Team":
    st.markdown('<h2 class="section-header">Our Team: Expertise in Education & AI</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <h3>Xavier Honablue M.Ed</h3>
            <p><strong>Founder</strong></p>
            <p>A visionary leader with a deep understanding of educational pedagogy and a passion for leveraging technology to create equitable and engaging learning experiences.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <h3>CTO & Head of Curriculum</h3>
            <p><strong>MADS UMICH</strong></p>
            <p>Leading our technological innovation and curriculum development for mathematics, ensuring our platform is cutting-edge and pedagogically sound.</p>
        </div>
        """, unsafe_allow_html=True)

# Vision Section
elif page == "🔮 Vision":
    st.markdown('<h2 class="section-header">Vision & Future</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Our Vision")
        st.write("Our vision is to create a world where every K-12 student has access to a personalized, engaging, and future-ready education, empowered by intelligent technology.")
    
    with col2:
        st.markdown("### Future Roadmap")
        st.markdown("""
        - **Expansion of Content:** New subjects and grade levels
        - **Advanced AI Features:** Predictive analytics, sentiment analysis, AI tutors
        - **Community Building:** Online community for teachers
        - **International Growth:** Global expansion
        - **Research & Development:** Continuous innovation
        """)

# Contact Section
elif page == "📞 Contact":
    st.markdown('<h2 class="section-header">Shape the Next Generation of Learners</h2>', unsafe_allow_html=True)
    st.write("We are seeking partnerships with forward-thinking educational institutions and investors who share our vision for transforming K-12 education.")
    
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <a href="mailto:partners@cognitivecloud.ai" style="background: #005A9C; color: white; padding: 1rem 2rem; border-radius: 25px; text-decoration: none; font-weight: bold;">
            📧 Contact Us
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2025 Cognitive Cloud Education. All rights reserved.", unsafe_allow_html=True)
