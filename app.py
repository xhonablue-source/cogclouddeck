import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Cognitive Cloud Education | Empowering the Future of Learning",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #005A9C, #4A90E2, #F2A900);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .section-header {
        color: #005A9C;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        border-bottom: 3px solid #F2A900;
        padding-bottom: 0.5rem;
    }
    
    .problem-card {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #dc3545;
        transition: transform 0.3s ease;
    }
    
    .solution-card {
        background: linear-gradient(145deg, #f8f7f4, #ffffff);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #005A9C;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #005A9C, #4A90E2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,90,156,0.3);
        margin-bottom: 1rem;
    }
    
    .team-card {
        background: linear-gradient(145deg, #f8f7f4, #ffffff);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 1px solid #e9ecef;
    }
    
    .feature-highlight {
        background: linear-gradient(135deg, #F2A900, #FFD700);
        color: #333;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(242,169,0,0.3);
    }
    
    .cta-button {
        background: linear-gradient(135deg, #005A9C, #F2A900);
        color: white;
        padding: 1rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        text-align: center;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #005A9C;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🧠 Cognitive Cloud Education")
st.sidebar.markdown("---")

pages = {
    "🏠 Introduction": "intro",
    "❗ The Problem": "problem", 
    "💡 Our Solution": "solution",
    "📈 Market Opportunity": "market",
    "🖥️ Platform & Services": "platform",
    "⚙️ Technology": "technology",
    "📊 Traction": "traction",
    "👥 Our Team": "team",
    "💼 Business Model": "business",
    "🎯 Competitive Edge": "competition",
    "🔮 Vision & Future": "vision",
    "📞 Contact Us": "contact"
}

selected_page = st.sidebar.selectbox("Navigate to:", list(pages.keys()))
current_page = pages[selected_page]

# Introduction Section
if current_page == "intro":
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Cognitive Cloud Education</h1>
        <h2>Empowering the Future of Learning</h2>
        <h3>Reversing the Trend - Bringing Every Student Back to the Classroom</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🌟 Transforming Education Through AI-Powered Personalization
    
    In an era of declining school populations and increasing disengagement, the future of education hinges on our ability to connect with every student. Cognitive Cloud Education offers a revolutionary AI-powered platform that transforms learning by deeply understanding each student.
    
    **Our Mission:** By integrating student names and interests directly into their personalized learning journey, we don't just teach; we inspire, ensuring every student feels seen, valued, and excited to come to school.
    
    **Our Vision:** We're not just preparing students for the future; we're building the future of engaged learning, one personalized experience at a time.
    """)
    
    # Key Stats Overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>$400B+</h3>
            <p>Global K-12 EdTech Market by 2030</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>AI-First</h3>
            <p>Truly Adaptive Learning Platform</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>K-12</h3>
            <p>Complete STEAM Curriculum</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Global</h3>
            <p>Worldwide Classroom Access</p>
        </div>
        """, unsafe_allow_html=True)

# Problem Section
elif current_page == "problem":
    st.markdown('<h2 class="section-header">❗ The Problem: The Evolving Landscape of K-12 Education</h2>', unsafe_allow_html=True)
    
    st.markdown("Traditional K-12 education faces significant challenges in preparing students for a rapidly changing world:")
    
    problems = [
        {
            "icon": "🏭",
            "title": "One-Size-Fits-All Approach",
            "description": "Standardized teaching often fails to cater to diverse learning styles, paces, and individual student needs, leading to disengagement and underperformance."
        },
        {
            "icon": "👤",
            "title": "Lack of Personalized Learning",
            "description": "Educators struggle to provide individualized attention and differentiated instruction to large classes."
        },
        {
            "icon": "🔧",
            "title": "Limited Access to Cutting-Edge Resources",
            "description": "Many schools lack the resources, tools, and training to effectively integrate modern technologies, especially AI, into their curriculum."
        },
        {
            "icon": "😰",
            "title": "Teacher Burden",
            "description": "Teachers are overwhelmed with administrative tasks and the pressure to adapt to new educational demands without adequate support."
        },
        {
            "icon": "❌",
            "title": "Gap in Future-Ready Skills",
            "description": "Students often lack critical 21st-century skills, particularly in STEAM and AI literacy, which are crucial for future success."
        }
    ]
    
    for i, problem in enumerate(problems):
        st.markdown(f"""
        <div class="problem-card">
            <h3>{problem['icon']} {problem['title']}</h3>
            <p>{problem['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Solution Section
elif current_page == "solution":
    st.markdown('<h2 class="section-header">💡 Our Solution: AI-Powered Personalized Learning for K-12</h2>', unsafe_allow_html=True)
    
    st.markdown("Cognitive Cloud Education provides an innovative, AI-powered platform designed to revolutionize K-12 learning by:")
    
    solutions = [
        {
            "icon": "🎯",
            "title": "Personalizing the Learning Journey",
            "description": "Our AI adapts content and pace to each student's unique needs, strengths, and weaknesses, fostering deeper understanding and engagement."
        },
        {
            "icon": "💪",
            "title": "Empowering Educators",
            "description": "We equip teachers with AI-driven tools to automate administrative tasks, provide real-time insights into student progress, and facilitate differentiated instruction."
        },
        {
            "icon": "🌐",
            "title": "Bridging the Technology Gap",
            "description": "Our platform makes advanced AI and educational technologies accessible and easy to integrate for schools and districts, regardless of their current tech infrastructure."
        },
        {
            "icon": "🔬",
            "title": "Fostering STEAM and AI Literacy",
            "description": "We offer engaging, interactive content and projects specifically designed to build critical thinking, problem-solving, and AI-related skills."
        },
        {
            "icon": "🤝",
            "title": "Connecting Classrooms Globally",
            "description": "We provide access to world-class educational resources and foster collaboration with students and educators worldwide."
        }
    ]
    
    for solution in solutions:
        st.markdown(f"""
        <div class="solution-card">
            <h3>{solution['icon']} {solution['title']}</h3>
            <p>{solution['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Market Opportunity Section
elif current_page == "market":
    st.markdown('<h2 class="section-header">📈 Market Opportunity: A Growing Need for EdTech Innovation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Market size chart
        market_data = pd.DataFrame({
            'Year': ['2024', '2026', '2028', '2030'],
            'Market Size (Billions USD)': [280, 325, 370, 404]
        })
        
        fig = px.bar(
            market_data, 
            x='Year', 
            y='Market Size (Billions USD)',
            title='Global K-12 EdTech Market Growth Projection',
            color_discrete_sequence=['#005A9C'],
            text='Market Size (Billions USD)'
        )
        fig.update_traces(texttemplate='$%{text}B', textposition='outside')
        fig.update_layout(
            title_font_size=20,
            xaxis_title="Year",
            yaxis_title="Market Size (Billions USD)",
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="feature-highlight">
            <h4>🚀 Market Drivers</h4>
            <ul>
                <li>Digital transformation acceleration</li>
                <li>AI integration demand</li>
                <li>Personalized learning focus</li>
                <li>STEAM education priority</li>
                <li>Teacher development needs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Market opportunities
    st.markdown("### Key Market Opportunities")
    
    market_points = [
        "**Global K-12 EdTech Market Size:** Estimated to reach over $400 billion by 2030, with significant growth driven by digital transformation and AI integration.",
        "**Increased Adoption of AI in Education:** Schools are increasingly looking for AI solutions to enhance learning, personalize instruction, and improve operational efficiency.",
        "**Focus on STEAM Education:** Governments and educational bodies worldwide are prioritizing STEAM subjects, creating a strong demand for specialized resources.",
        "**Teacher Professional Development:** There's a continuous need for training programs that equip educators with skills for modern teaching environments."
    ]
    
    for point in market_points:
        st.markdown(f"• {point}")

# Platform Section
elif current_page == "platform":
    st.markdown('<h2 class="section-header">🖥️ Product & Service: The Cognitive Cloud Education Platform</h2>', unsafe_allow_html=True)
    
    st.markdown("Our comprehensive platform offers:")
    
    # Platform features with tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧩 AI Learning Modules", 
        "📊 Teacher Dashboard", 
        "🎓 Training Programs", 
        "🌍 Global Resources", 
        "🎮 Interactive Apps"
    ])
    
    with tab1:
        st.markdown("### AI-Powered Adaptive Learning Modules")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Key Features:**
            - Interactive lessons in STEAM subjects (grades 4-12)
            - Dynamic content adjustments based on student performance and learning style
            - Real-time feedback and personalized remediation
            - Adaptive difficulty scaling
            - Multi-modal learning support (visual, auditory, kinesthetic)
            """)
        
        with col2:
            # Sample progress chart
            progress_data = pd.DataFrame({
                'Subject': ['Math', 'Science', 'Technology', 'Engineering', 'Arts'],
                'Engagement': [85, 92, 78, 88, 95],
                'Performance': [82, 89, 75, 85, 91]
            })
            
            fig = px.bar(
                progress_data.melt(id_vars='Subject', var_name='Metric', value_name='Score'),
                x='Subject', y='Score', color='Metric',
                title='Student Engagement & Performance',
                color_discrete_map={'Engagement': '#005A9C', 'Performance': '#F2A900'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### Teacher Dashboard & Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Dashboard Features:**
            - Real-time student progress overview
            - AI-generated insights and recommendations
            - Learning gap identification
            - Engagement analytics
            - Performance predictions
            """)
        
        with col2:
            st.markdown("""
            **Management Tools:**
            - Differentiated assignment creation
            - Automated grading assistance
            - Parent communication tools
            - Classroom management utilities
            - Resource recommendation engine
            """)
    
    with tab3:
        st.markdown("### Teacher Training Programs")
        
        training_options = [
            "🎯 **AI Integration Workshops** - Learn to integrate AI tools into daily teaching",
            "📚 **Personalized Learning Best Practices** - Master individualized instruction techniques",
            "🏆 **Certification Programs** - Become certified in AI-powered teaching",
            "🌐 **Online Course Library** - Self-paced professional development",
            "👥 **Peer Collaboration Networks** - Connect with innovative educators worldwide"
        ]
        
        for option in training_options:
            st.markdown(option)
    
    with tab4:
        st.markdown("### Global Resource Portal")
        
        st.markdown("""
        **Curated Educational Content:**
        - MIT OpenCourseWare integration
        - Stanford Online resources
        - NASA educational materials
        - World-class university partnerships
        - Interactive simulations and virtual labs
        
        **Global Collaboration:**
        - International classroom connections
        - Cross-cultural project opportunities
        - Language exchange programs
        - Global expert guest lectures
        """)
    
    with tab5:
        st.markdown("### Interactive Web Apps (e.g., MathCraft)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **MathCraft Features:**
            - Gamified mathematics learning
            - 3D visualization of abstract concepts
            - Project-based learning experiences
            - Collaborative problem-solving
            - Real-world application scenarios
            """)
        
        with col2:
            # Sample app engagement metrics
            app_data = pd.DataFrame({
                'App Feature': ['3D Visualizations', 'Gamified Lessons', 'Collaborative Projects', 'Real-world Problems'],
                'Student Engagement': [94, 88, 91, 86]
            })
            
            fig = px.pie(
                app_data, 
                values='Student Engagement', 
                names='App Feature',
                title='MathCraft Feature Engagement'
            )
            st.plotly_chart(fig, use_container_width=True)

# Technology Section
elif current_page == "technology":
    st.markdown('<h2 class="section-header">⚙️ Technology & Approach: Intelligent and User-Friendly</h2>', unsafe_allow_html=True)
    
    st.markdown("Our platform is built on a robust and scalable technology stack:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tech_features = [
            {
                "title": "🤖 Advanced AI/ML Algorithms",
                "description": "Utilizes machine learning for adaptive learning paths, content recommendation, and performance analytics."
            },
            {
                "title": "🗣️ Natural Language Processing",
                "description": "For understanding student queries and providing intelligent responses."
            },
            {
                "title": "☁️ Cloud-Native Architecture",
                "description": "Ensures scalability, reliability, and accessibility from any device."
            }
        ]
        
        for feature in tech_features:
            st.markdown(f"""
            <div class="solution-card">
                <h4>{feature['title']}</h4>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        tech_features_2 = [
            {
                "title": "🎨 User-Centric Design",
                "description": "Intuitive interfaces for both students and teachers, minimizing the learning curve."
            },
            {
                "title": "🔒 Data Security & Privacy",
                "description": "Adherence to strict data protection standards (PII is never shared with third-party AI systems)."
            },
            {
                "title": "📱 Cross-Platform Compatibility",
                "description": "Seamless experience across desktop, tablet, and mobile devices."
            }
        ]
        
        for feature in tech_features_2:
            st.markdown(f"""
            <div class="solution-card">
                <h4>{feature['title']}</h4>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Traction Section
elif current_page == "traction":
    st.markdown('<h2 class="section-header">📊 Traction & Milestones: Building Momentum</h2>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Key Achievements")
    
    milestones = [
        {
            "icon": "🏫",
            "title": "Successful Pilot Programs",
            "description": "Implemented in multiple schools, reaching students with positive initial results",
            "status": "Completed"
        },
        {
            "icon": "👨‍🏫",
            "title": "Positive Teacher Feedback",
            "description": "Enthusiastic feedback from educators reporting improved student engagement and reduced workload",
            "status": "Ongoing"
        },
        {
            "icon": "📚",
            "title": "Core Module Deployment",
            "description": "Successfully developed and deployed adaptive learning modules for key STEAM subjects",
            "status": "Completed"
        },
        {
            "icon": "🤝",
            "title": "Strategic Partnerships",
            "description": "Established key collaborations with educational organizations and content providers",
            "status": "Active"
        },
        {
            "icon": "📈",
            "title": "Growing User Base",
            "description": "Continuously expanding reach with increasing student and teacher adoption",
            "status": "Growing"
        }
    ]
    
    for milestone in milestones:
        status_color = {
            "Completed": "#28a745",
            "Ongoing": "#ffc107", 
            "Active": "#007bff",
            "Growing": "#17a2b8"
        }.get(milestone['status'], "#6c757d")
        
        st.markdown(f"""
        <div class="solution-card">
            <h4>{milestone['icon']} {milestone['title']} 
            <span style="background: {status_color}; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8rem;">{milestone['status']}</span></h4>
            <p>{milestone['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Traction metrics visualization
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Schools</h3>
            <p>Pilot Programs Active</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Students</h3>
            <p>Platform Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Teachers</h3>
            <p>Trained Educators</p>
        </div>
        """, unsafe_allow_html=True)

# Team Section
elif current_page == "team":
    st.markdown('<h2 class="section-header">👥 Our Team: Expertise in Education & AI</h2>', unsafe_allow_html=True)
    
    # Placeholder for team members - replace with actual information
    team_members = [
        {
            "name": "Founder/CEO",
            "title": "Visionary Leader",
            "bio": "Years of experience in EdTech, passionate about personalized learning, with background in AI strategy and educational transformation.",
            "expertise": ["EdTech Strategy", "AI Implementation", "Educational Leadership"]
        },
        {
            "name": "Chief Technology Officer",
            "title": "Technical Innovation Leader", 
            "bio": "Expert in AI/ML development with expertise in scalable cloud architectures and former leadership roles at major tech companies.",
            "expertise": ["AI/ML Development", "Cloud Architecture", "Platform Scaling"]
        },
        {
            "name": "Head of Curriculum & Education",
            "title": "Educational Expert",
            "bio": "Experienced educator and curriculum developer with deep understanding of K-12 pedagogy and advocacy for STEAM education.",
            "expertise": ["Curriculum Development", "K-12 Pedagogy", "STEAM Education"]
        },
        {
            "name": "Head of Data Science",
            "title": "Analytics & Insights Leader",
            "bio": "Specialist in educational data analytics, learning analytics, and AI-driven insights for personalized learning optimization.",
            "expertise": ["Learning Analytics", "Data Science", "AI Insights"]
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, member in enumerate(team_members):
        with col1 if i % 2 == 0 else col2:
            expertise_tags = " • ".join(member['expertise'])
            st.markdown(f"""
            <div class="team-card">
                <h3>👤 {member['name']}</h3>
                <p><strong>{member['title']}</strong></p>
                <p>{member['bio']}</p>
                <div style="margin-top: 1rem; padding: 0.5rem; background: #e9ecef; border-radius: 5px;">
                    <small><strong>Expertise:</strong> {expertise_tags}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Seeking Advisors")
    st.markdown("""
    We are actively seeking advisors to join our mission. We are particularly interested in expertise in:
    
    - **AI Ethics & Safety** - Ensuring responsible AI implementation in education
    - **K-12 Administration** - School district leadership and educational policy
    - **EdTech Investment** - Strategic guidance for scaling and funding
    - **Global Education** - International market expansion expertise
    - **Teacher Development** - Professional development and training strategies
    """)

# Business Model Section
elif current_page == "business":
    st.markdown('<h2 class="section-header">💼 Business Model: Sustainable Growth</h2>', unsafe_allow_html=True)
    
    st.markdown("Our revenue streams are designed for sustainable growth and value delivery:")
    
    # Revenue streams visualization
    revenue_data = pd.DataFrame({
        'Revenue Stream': ['School Subscriptions', 'Teacher Training', 'Premium Content', 'Partnerships'],
        'Projected Revenue %': [60, 25, 10, 5],
        'Growth Potential': ['High', 'High', 'Medium', 'Medium']
    })
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.pie(
            revenue_data, 
            values='Projected Revenue %', 
            names='Revenue Stream',
            title='Revenue Stream Distribution',
            color_discrete_sequence=['#005A9C', '#4A90E2', '#F2A900', '#FFD700']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="feature-highlight">
            <h4>💰 Pricing Strategy</h4>
            <ul>
                <li><strong>Freemium Model:</strong> Basic features free</li>
                <li><strong>Tiered Subscriptions:</strong> Scale with school size</li>
                <li><strong>Enterprise Plans:</strong> Custom solutions</li>
                <li><strong>Training Packages:</strong> Professional development</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed revenue streams
    revenue_streams = [
        {
            "title": "🏫 School/District Subscriptions",
            "description": "Tiered subscription plans based on the number of students and features accessed.",
            "details": "Monthly/annual plans with scaling discounts for larger implementations"
        },
        {
            "title": "🎓 Teacher Professional Development Packages",
            "description": "Paid workshops and certification programs for educators.",
            "details": "Live workshops, online courses, and certification programs"
        },
        {
            "title": "⭐ Premium Content & Customization",
            "description": "Optional add-ons for specialized content or tailored curriculum development.",
            "details": "Custom curriculum, advanced analytics, and specialized subject modules"
        },
        {
            "title": "🤝 Partnerships",
            "description": "Collaborations with educational publishers and technology providers.",
            "details": "Revenue sharing with content partners and technology integrations"
        }
    ]
    
    for stream in revenue_streams:
        st.markdown(f"""
        <div class="solution-card">
            <h4>{stream['title']}</h4>
            <p><strong>{stream['description']}</strong></p>
            <p><em>{stream['details']}</em></p>
        </div>
        """, unsafe_allow_html=True)

# Competition Section
elif current_page == "competition":
    st.markdown('<h2 class="section-header">🎯 Competition & Differentiation: Standing Out in the Market</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🏢 Competitive Landscape")
        competitors = [
            "Traditional LMS platforms",
            "Generic EdTech tools", 
            "Content-focused solutions",
            "Single-subject platforms",
            "Enterprise learning systems"
        ]
        
        for comp in competitors:
            st.markdown(f"• {comp}")
    
    with col2:
        st.markdown("### 🚀 Our Differentiation")
        
        differentiators = [
            {
                "title": "🧠 Deep AI Integration",
                "description": "Unlike many platforms that simply digitize content, our core is truly adaptive AI that personalizes learning at a granular level."
            },
            {
                "title": "👥 Dual Focus (Student & Teacher)",
                "description": "We empower both students with personalized learning and teachers with powerful tools and training, creating a symbiotic relationship."
            },
            {
                "title": "🔬 STEAM & Future Skills Emphasis",
                "description": "Our specialized content directly addresses the growing demand for skills crucial for the future workforce."
            },
            {
                "title": "🌍 Global Perspective", 
                "description": "Our curated global resources and collaboration opportunities offer a unique, expansive learning experience."
            },
            {
                "title": "🔒 User-Friendly & Secure",
                "description": "A strong emphasis on intuitive design and robust data privacy sets us apart."
            }
        ]
        
        for diff in differentiators:
            st.markdown(f"**{diff['title']}:** {diff['description']}")
    
    # Competitive advantage matrix
    st.markdown("### 📊 Competitive Advantage Matrix")
    
    comparison_data = pd.DataFrame({
        'Feature': ['AI Personalization', 'Teacher Tools', 'STEAM Focus', 'Global Resources', 'Data Privacy'],
        'Cognitive Cloud': [95, 90, 95, 85, 95],
        'Traditional LMS': [30, 70, 50, 60, 70],
        'Generic EdTech': [60, 60, 40, 50, 60]
    })
    
    fig = px.radar(
        comparison_data.melt(id_vars='Feature', var_name='Platform', value_name='Score'),
        r='Score',
        theta='Feature',
        color='Platform',
        color_discrete_map={
            'Cognitive Cloud': '#005A9C',
            'Traditional LMS': '#dc3545', 
            'Generic EdTech': '#ffc107'
        },
        title='Competitive Advantage Comparison'
    )
    st.plotly_chart(fig, use_container_width=True)

# Vision Section
elif current_page == "vision":
    st.markdown('<h2 class="section-header">🔮 Vision & Future: Shaping the Next Generation of Learners</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-highlight">
            <h3>🌟 Our Vision</h3>
            <p>To create a world where every K-12 student has access to a personalized, engaging, and future-ready education, empowered by intelligent technology.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Core Values")
        values = [
            "**Personalization:** Every student learns differently",
            "**Empowerment:** Technology should enable, not replace teachers", 
            "**Accessibility:** Quality education for all students globally",
            "**Innovation:** Continuous advancement in educational technology",
            "**Privacy:** Student data protection is paramount"
        ]
        
        for value in values:
            st.markdown(f"• {value}")
    
    with col2:
        st.markdown("### 🗺️ Future Roadmap")
        
        roadmap_items = [
            {
                "phase": "Phase 1 (2025)",
                "items": ["Expansion of Content: Introduce new subjects and grade levels", "Advanced AI Features: Implement predictive analytics"]
            },
            {
                "phase": "Phase 2 (2026)", 
                "items": ["Community Building: Foster vibrant teacher communities", "Sentiment Analysis: AI-driven emotional intelligence"]
            },
            {
                "phase": "Phase 3 (2027)",
                "items": ["International Growth: Expand to global markets", "Virtual AI Tutors: 24/7 personalized assistance"]
            },
            {
                "phase": "Phase 4 (2028+)",
                "items": ["Research & Development: Continuous innovation", "Augmented Reality: Immersive learning experiences"]
            }
        ]
        
        for roadmap in roadmap_items:
            st.markdown(f"""
            <div class="solution-card">
                <h4>📅 {roadmap['phase']}</h4>
                <ul>
            """, unsafe_allow_html=True)
            
            for item in roadmap['items']:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            
            st.markdown("</ul></div>", unsafe_allow_html=True)
    
    # Future impact visualization
    st.markdown("### 📈 Projected Impact")
    
    impact_data = pd.DataFrame({
        'Year': [2025, 2026, 2027, 2028, 2030],
        'Students Reached (Thousands)': [50, 150, 400, 800, 2000],
        'Schools Partner': [100, 300, 750, 1500, 4000],
        'Teachers Trained': [500, 1500, 4000, 8000, 20000]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.line(
            impact_data, 
            x='Year', 
            y='Students Reached (Thousands)',
            title='Student Reach Projection',
            markers=True,
            color_discrete_sequence=['#005A9C']
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.bar(
            impact_data,
            x='Year',
            y='Teachers Trained', 
            title='Teacher Training Growth',
            color_discrete_sequence=['#F2A900']
        )
        st.plotly_chart(fig2, use_container_width=True)

# Contact Section
elif current_page == "contact":
    st.markdown('<h2 class="section-header">📞 Call to Action: Contact Us</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-header">
        <h2>🤝 Shape the Next Generation of Learners</h2>
        <p>We are seeking partnerships with forward-thinking educational institutions and investors who share our vision for transforming K-12 education.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🎯 Partnership Opportunities")
        
        partnerships = [
            "🏫 **Educational Institutions** - Pilot our platform in your schools",
            "💰 **Investors** - Join us in revolutionizing education", 
            "🤝 **Content Partners** - Collaborate on curriculum development",
            "🌍 **Global Distributors** - Expand our reach internationally",
            "🎓 **Universities** - Research partnerships and validation studies"
        ]
        
        for partnership in partnerships:
            st.markdown(partnership)
        
        st.markdown("---")
        
        # Contact form
        st.markdown("### 📧 Get In Touch")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            organization = st.text_input("Organization *") 
            email = st.text_input("Email Address *")
            role = st.selectbox("Your Role", [
                "Select your role...",
                "School Administrator", 
                "Teacher/Educator",
                "Investor",
                "Content Partner",
                "Technology Partner",
                "Researcher",
                "Other"
            ])
            interest = st.selectbox("Partnership Interest", [
                "Select your interest...",
                "Pilot Program",
                "Investment Opportunity", 
                "Content Partnership",
                "Distribution Partnership",
                "Research Collaboration",
                "General Inquiry"
            ])
            message = st.text_area("Message", placeholder="Tell us about your interest in Cognitive Cloud Education...")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and organization and email and role != "Select your role..." and interest != "Select your interest...":
                    st.success("✅ Thank you for your interest! We'll get back to you within 24 hours.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")
        
        st.markdown("---")
        
        # Direct contact information
        st.markdown("""
        <div class="solution-card">
            <h4>📞 Direct Contact</h4>
            <p><strong>🌐 Website:</strong> <a href="https://cognitivecloud.ai" target="_blank">cognitivecloud.ai</a></p>
            <p><strong>📧 Partnership Email:</strong> partners@cognitivecloud.ai</p>
            <p><strong>💼 Investment Inquiries:</strong> investors@cognitivecloud.ai</p>
            <p><strong>📚 Education Team:</strong> education@cognitivecloud.ai</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Social proof section
        st.markdown("### 🌟 Join Our Mission")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("""
            <div class="metric-card">
                <h4>🎯</h4>
                <h3>Personalized</h3>
                <p>Learning for Every Student</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_b:
            st.markdown("""
            <div class="metric-card">
                <h4>🚀</h4>
                <h3>AI-Powered</h3>
                <p>Cutting-Edge Technology</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_c:
            st.markdown("""
            <div class="metric-card">
                <h4>🌍</h4>
                <h3>Global</h3>
                <p>Impact & Reach</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #005A9C, #F2A900); color: white; border-radius: 10px; margin-top: 2rem;">
    <h4>🧠 Cognitive Cloud Education</h4>
    <p>Empowering the Future of Learning Through AI-Powered Personalization</p>
    <p>© 2025 Cognitive Cloud Education. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
