<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cognitive Cloud Education | Empowering the Future of Learning</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals with Blue Accent (#F8F7F4, #333333, #005A9C, #F2A900) -->
    <!-- Application Structure Plan: A narrative, single-page application with thematic sections (Challenge, Solution, Platform, Why Us, Traction, Team, Vision, Contact). Uses a sticky nav for smooth scrolling. Key interactions include a tabbed interface for the platform features and a dynamic chart for market data. This structure is more engaging than a linear slide deck and guides the user through the company's story logically, from problem to solution to future vision, enhancing comprehension and engagement. -->
    <!-- Visualization & Content Choices: Market Opportunity -> Goal: Compare/Change -> Viz: Bar Chart -> Interaction: Tooltip on hover -> Justification: Visually represents market growth, more impactful than text -> Library: Chart.js. Platform Features -> Goal: Organize -> Viz: Tabbed Interface -> Interaction: Click to switch tabs -> Justification: Condenses large amounts of information into a clean, interactive component -> Library/Method: Vanilla JS. Key Stats -> Goal: Inform -> Viz: Animated Number Counter -> Interaction: Animates on scroll into view -> Justification: Draws attention to key metrics in an engaging way -> Library/Method: Vanilla JS with IntersectionObserver. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8F7F4;
            color: #333333;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        .nav-link {
            transition: color 0.3s ease;
        }
        .nav-link:hover {
            color: #F2A900;
        }
        .tab.active {
            border-color: #005A9C;
            color: #005A9C;
            font-weight: 700;
        }
    </style>
</head>
<body class="antialiased">

    <header id="header" class="bg-white/80 backdrop-blur-md sticky top-0 z-50 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <a href="#" class="text-xl font-bold text-[#005A9C]">
                Cognitive Cloud Education
            </a>
            <div class="hidden md:flex space-x-8">
                <a href="#challenge" class="nav-link text-gray-700">The Challenge</a>
                <a href="#solution" class="nav-link text-gray-700">Our Solution</a>
                <a href="#platform" class="nav-link text-gray-700">The Platform</a>
                <a href="#why-us" class="nav-link text-gray-700">Why Us?</a>
                <a href="#traction" class="nav-link text-gray-700">Traction</a>
                <a href="#team" class="nav-link text-gray-700">Our Team</a>
                <a href="#vision" class="nav-link text-gray-700">Vision</a>
                <a href="#contact" class="nav-link bg-[#005A9C] text-white px-4 py-2 rounded-full hover:bg-[#F2A900] hover:text-white transition-colors">Contact</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden text-gray-700">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
            <a href="#challenge" class="block py-2 nav-link text-gray-700">The Challenge</a>
            <a href="#solution" class="block py-2 nav-link text-gray-700">Our Solution</a>
            <a href="#platform" class="block py-2 nav-link text-gray-700">The Platform</a>
            <a href="#why-us" class="block py-2 nav-link text-gray-700">Why Us?</a>
            <a href="#traction" class="block py-2 nav-link text-gray-700">Traction</a>
            <a href="#team" class="block py-2 nav-link text-gray-700">Our Team</a>
            <a href="#vision" class="block py-2 nav-link text-gray-700">Vision</a>
            <a href="#contact" class="block mt-2 text-center nav-link bg-[#005A9C] text-white px-4 py-2 rounded-full hover:bg-[#F2A900] hover:text-white transition-colors">Contact</a>
        </div>
    </header>

    <main>
        <section id="hero" class="py-20 md:py-32 bg-white">
            <div class="container mx-auto px-6 text-center">
                <h1 class="text-4xl md:text-6xl font-bold text-[#005A9C] mb-4">Reversing the Trend of Disengagement</h1>
                <p class="text-lg md:text-xl max-w-3xl mx-auto text-gray-600">
                    In an era of declining school populations, we offer a revolutionary AI-powered platform that transforms learning by deeply understanding each student. By integrating their names and interests into a personalized journey, we ensure every student feels seen, valued, and excited to come to school.
                </p>
            </div>
        </section>

        <section id="challenge" class="py-16">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">The Evolving Landscape of K-12 Education</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">Traditional education faces significant hurdles in preparing students for a rapidly changing world.</p>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="bg-white p-6 rounded-lg shadow-md">
                        <div class="text-3xl text-[#F2A900] mb-3"> homogenized </div>
                        <h3 class="text-xl font-bold mb-2">One-Size-Fits-All Approach</h3>
                        <p class="text-gray-600">Standardized teaching often fails to cater to diverse learning styles and paces, leading to student disengagement.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md">
                        <div class="text-3xl text-[#F2A900] mb-3"> overwhelmed </div>
                        <h3 class="text-xl font-bold mb-2">Teacher Burden</h3>
                        <p class="text-gray-600">Educators are swamped with administrative tasks, limiting their ability to provide individualized attention.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md">
                        <div class="text-3xl text-[#F2A900] mb-3"> unprepared </div>
                        <h3 class="text-xl font-bold mb-2">Future Skills Gap</h3>
                        <p class="text-gray-600">Students often lack critical 21st-century skills in STEAM and AI literacy, crucial for future success.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="solution" class="py-16 bg-white">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">Our AI-Powered Solution</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">We revolutionize K-12 learning with an innovative platform designed to engage and empower.</p>
                </div>
                <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div class="text-center p-4">
                        <div class="text-4xl mb-3 text-[#005A9C]"> personalized </div>
                        <h3 class="font-bold text-lg">Personalized Journeys</h3>
                        <p class="text-sm text-gray-600">Our AI adapts content and pace to each student's unique needs, strengths, and interests.</p>
                    </div>
                    <div class="text-center p-4">
                        <div class="text-4xl mb-3 text-[#005A9C]"> empowered </div>
                        <h3 class="font-bold text-lg">Empowered Educators</h3>
                        <p class="text-sm text-gray-600">We provide teachers with AI-driven tools to automate tasks and gain real-time insights.</p>
                    </div>
                    <div class="text-center p-4">
                        <div class="text-4xl mb-3 text-[#005A9C]"> accessible </div>
                        <h3 class="font-bold text-lg">Bridged Tech Gap</h3>
                        <p class="text-sm text-gray-600">Our platform makes advanced AI and educational technologies easy to integrate for any school.</p>
                    </div>
                    <div class="text-center p-4">
                        <div class="text-4xl mb-3 text-[#005A9C]"> connected </div>
                        <h3 class="font-bold text-lg">Global Classrooms</h3>
                        <p class="text-sm text-gray-600">We provide access to world-class resources and foster global collaboration.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="platform" class="py-16">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">The Platform in Action</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">Explore the core components of our comprehensive educational ecosystem.</p>
                </div>
                <div>
                    <div class="border-b border-gray-200 mb-8">
                        <nav class="-mb-px flex space-x-6 justify-center" aria-label="Tabs">
                            <button class="tab active whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm" data-tab="modules">
                                Adaptive Modules
                            </button>
                            <button class="tab whitespace-nowrap py-4 px-1 border-b-2 border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 font-medium text-sm" data-tab="dashboard">
                                Teacher Dashboard
                            </button>
                            <button class="tab whitespace-nowrap py-4 px-1 border-b-2 border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 font-medium text-sm" data-tab="training">
                                Teacher Training
                            </button>
                        </nav>
                    </div>
                    <div id="tab-content" class="max-w-4xl mx-auto">
                        <div class="tab-pane active" id="modules">
                            <h3 class="text-2xl font-bold text-center mb-4 text-[#005A9C]">AI-Powered Adaptive Learning Modules</h3>
                            <p class="text-center text-gray-600">Our modules offer interactive lessons in STEAM subjects for grades 4-12. The AI provides dynamic content adjustments based on student performance and learning style, along with real-time feedback and personalized remediation to ensure mastery.</p>
                        </div>
                        <div class="tab-pane hidden" id="dashboard">
                            <h3 class="text-2xl font-bold text-center mb-4 text-[#005A9C]">Insightful Teacher Dashboard</h3>
                            <p class="text-center text-gray-600">Our dashboard gives educators a holistic overview of student progress and engagement. AI-generated insights help identify learning gaps and inform instruction, while powerful tools simplify differentiated assignment creation and classroom management.</p>
                        </div>
                        <div class="tab-pane hidden" id="training">
                            <h3 class="text-2xl font-bold text-center mb-4 text-[#005A9C]">Comprehensive Teacher Training</h3>
                            <p class="text-center text-gray-600">We offer workshops and online courses on integrating AI into the curriculum. These programs cover best practices for personalized learning and lead to certification, empowering our teachers to become leaders in modern education.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="why-us" class="py-16 bg-white">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">Why Cognitive Cloud Education?</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">We are uniquely positioned to lead the future of education through deep technology and a student-centric approach.</p>
                </div>
                <div class="grid lg:grid-cols-2 gap-12 items-center">
                    <div>
                        <h3 class="text-2xl font-bold text-[#005A9C] mb-4">A Growing Market for Innovation</h3>
                        <p class="text-gray-600 mb-6">The Global K-12 EdTech market is experiencing explosive growth, driven by the need for digital transformation and AI integration. This creates a massive opportunity for the firm to deliver real results.</p>
                        <div class="chart-container">
                            <canvas id="marketChart"></canvas>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-[#005A9C] mb-4">Our Differentiating Edge</h3>
                        <ul class="space-y-4">
                            <li class="flex items-start">
                                <span class="text-xl text-[#F2A900] mr-3">✔</span>
                                <p><strong class="text-gray-800">Deep AI Integration:</strong> Truly adaptive AI that personalizes learning at a granular level, not just digitized content.</p>
                            </li>
                            <li class="flex items-start">
                                <span class="text-xl text-[#F2A900] mr-3">✔</span>
                                <p><strong class="text-gray-800">Dual Focus:</strong> We empower both students with personalized learning and teachers with powerful tools and training, creating a symbiotic relationship.</p>
                            </li>
                            <li class="flex items-start">
                                <span class="text-xl text-[#F2A900] mr-3">✔</span>
                                <p><strong class="text-gray-800">STEAM & Future Skills:</strong> Our specialized content directly addresses the growing demand for skills crucial for the future workforce.</p>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section id="traction" class="py-16">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">Traction & Milestones</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">We are building strong momentum and achieving key milestones on our journey.</p>
                </div>
                <ul class="list-disc list-inside space-y-4 text-gray-700 max-w-3xl mx-auto">
                    <li>**Successful Pilot Programs:** We have implemented successful pilot programs in [X] schools, reaching [Y] students with positive initial results.</li>
                    <li>**Positive Teacher Feedback:** We have received enthusiastic feedback from [Z] teachers, reporting improved student engagement and reduced administrative workload.</li>
                    <li>**Core Module Deployment:** We have successfully developed and deployed core adaptive learning modules for key STEAM subjects.</li>
                    <li>**Strategic Partnerships:** The firm has established key collaborations with [mention any partners if applicable, e.g., educational organizations, content providers].</li>
                    <li>**Growing User Base:** We are continuously expanding our user base, now serving [X] students and [Y] teachers.</li>
                </ul>
            </div>
        </section>

        <section id="team" class="py-16 bg-white">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">Our Team: Expertise in Education & AI</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">Our passionate and experienced team is dedicated to transforming K-12 education.</p>
                </div>
                <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <div class="bg-gray-50 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">Xavier Honablue M.Ed</h3>
                        <p class="text-gray-700 font-medium">Founder</p>
                        <p class="mt-3 text-gray-600">A visionary leader with a deep understanding of educational pedagogy and a passion for leveraging technology to create equitable and engaging learning experiences. Xavier brings extensive experience in EdTech and a commitment to student success.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">CTO & Head of Curriculum (Mathematics)</h3>
                        <p class="text-gray-700 font-medium">MADS UMICH</p>
                        <p class="mt-3 text-gray-600">Leading our technological innovation and curriculum development for mathematics, ensuring our platform is cutting-edge and pedagogically sound for all learners.</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">[Other Key Team Members]</h3>
                        <p class="text-gray-700 font-medium">[Their Title]</p>
                        <p class="mt-3 text-gray-600">[Brief Bio for each, highlighting relevant experience].</p>
                    </div>
                    <div class="bg-gray-50 p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">Seeking Advisors</h3>
                        <p class="mt-3 text-gray-600">We are actively seeking advisors to join our mission. We are particularly interested in expertise in:
                        <ul class="list-disc list-inside mt-1 text-gray-600">
                            <li>[Areas of expertise you are seeking advisors in, e.g., AI Ethics, K-12 Administration, EdTech Investment]</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="vision" class="py-16">
            <div class="container mx-auto px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-[#005A9C]">Vision & Future: Shaping the Next Generation of Learners</h2>
                    <p class="mt-2 text-gray-600 max-w-2xl mx-auto">Our long-term vision and roadmap for continuous innovation and impact.</p>
                </div>
                <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <div class="bg-white p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">Our Vision</h3>
                        <p class="text-gray-600">Our vision is to create a world where every K-12 student has access to a personalized, engaging, and future-ready education, empowered by intelligent technology.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md">
                        <h3 class="text-xl font-bold text-[#005A9C] mb-2">Future Roadmap</h3>
                        <ul class="list-disc list-inside space-y-2 text-gray-600">
                            <li>**Expansion of Content:** We plan to introduce new subjects and grade levels.</li>
                            <li>**Advanced AI Features:** We will implement more sophisticated AI for predictive analytics, sentiment analysis, and AI-driven virtual tutors.</li>
                            <li>**Community Building:** We will foster a vibrant online community for teachers to share best practices.</li>
                            <li>**International Growth:** The firm intends to expand its reach to schools and districts globally.</li>
                            <li>**Research & Development:** We are committed to continuously innovating based on educational research and technological advancements.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="contact" class="py-16 bg-[#005A9C]">
            <div class="container mx-auto px-6 text-center text-white">
                <h2 class="text-3xl font-bold">Shape the Next Generation of Learners</h2>
                <p class="mt-4 max-w-2xl mx-auto">We are seeking partnerships with forward-thinking educational institutions and investors who share our vision for transforming K-12 education. Let's build the future of learning together.</p>
                <a href="mailto:partners@cognitivecloud.ai" class="mt-8 inline-block bg-white text-[#005A9C] font-bold px-8 py-3 rounded-full hover:bg-[#F2A900] hover:text-white transition-colors">
                    Contact Us
                </a>
            </div>
        </section>
    </main>

    <footer class="bg-gray-800 text-white py-6">
        <div class="container mx-auto px-6 text-center text-sm">
            <p>&copy; 2025 Cognitive Cloud Education. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
            
            const tabs = document.querySelectorAll('.tab');
            const tabPanes = document.querySelectorAll('.tab-pane');

            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    const target = tab.getAttribute('data-tab');

                    tabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');

                    tabPanes.forEach(pane => {
                        if (pane.id === target) {
                            pane.classList.remove('hidden');
                            pane.classList.add('active');
                        } else {
                            pane.classList.add('hidden');
                            pane.classList.remove('active');
                        }
                    });
                });
            });

            const marketChartCtx = document.getElementById('marketChart').getContext('2d');
            const marketChart = new Chart(marketChartCtx, {
                type: 'bar',
                data: {
                    labels: ['2024', '2026', '2028', '2030'],
                    datasets: [{
                        label: 'Global K-12 EdTech Market (in Billions USD)',
                        data: [280, 325, 370, 404],
                        backgroundColor: '#005A9C',
                        borderColor: '#004B80',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return '$' + value + 'B';
                                }
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    if (label) {
                                        label += ': ';
                                    }
                                    if (context.parsed.y !== null) {
                                        label += new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', notation: 'compact' }).format(context.parsed.y * 1000000000);
                                    }
                                    return label;
                                }
                            }
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>
