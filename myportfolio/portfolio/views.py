from django.shortcuts import render


def get_portfolio_context():
    return {
        'name': 'M Rohitha Reddy',
        'title': 'CSE Undergraduate | AI, IoT & Sustainability Enthusiast',
        'tagline': 'Seeking internship opportunities to apply technical skills, design thinking, and problem-solving in AI, IoT, and agriculture projects.',
        'summary': 'A highly motivated innovation-driven student passionate about building impactful solutions for agriculture, sustainability, and intelligent systems.',
        'location': 'Hyderabad, India',
        'email': 'rohithareddy1277@gmail.com',
        'phone': '+91 90304 41491',
        'linkedin': 'https://www.linkedin.com/in/rohitha-reddy-b53689326/',
        'github': 'https://github.com/Roh110',
        'profile_image': 'portfolio/images/profile-photo.jpg',
        'resume_file': 'portfolio/resume.pdf',
        'objective': 'A highly motivated and innovation-driven undergraduate student seeking internship opportunities to apply technical knowledge, design thinking, and problem-solving skills in real-world projects. Passionate about technology, sustainability, and building impactful solutions in domains such as AI, IoT, and agriculture.',
        'skills': [
            'Python',
            'C',
            'Java',
            'HTML',
            'CSS',
            'Data Structures & Algorithms',
            'Web Development',
            'Design Thinking',
        ],
        'outcomes': [
            {'value': 'Patent Published', 'label': 'Sustainable Soil Regeneration'},
            {'value': 'First Prize', 'label': 'She-Solve Ideathon'},
            {'value': 'National Showcase', 'label': 'Vaisheshika Science Fair'},
        ],
        'highlights': [
            'AI, IoT and agriculture-focused innovation projects',
            'Patent published for sustainable soil regeneration',
            'National-level awards and science fair showcases',
        ],
        'projects': [
            {
                'name': 'AI Agentic Chatbot for Farmers',
                'description': 'Building an AI-powered agentic chatbot to assist farmers with crop guidance, agricultural decision-making, and sustainability support.',
                'status': 'Ongoing',
                'tags': ['AI', 'Chatbot', 'Agri-tech'],
            },
            {
                'name': 'IoT-Based Water Quality Tester',
                'description': 'Designed an IoT system to monitor water quality parameters, showcased at a national level science fair.',
                'status': 'Showcased',
                'tags': ['IoT', 'Sensors', 'Water Quality'],
            },
            {
                'name': 'Piezo Electricity Generation Project',
                'description': 'Developed a sustainable energy prototype using piezoelectric principles during an IoT value-added course.',
                'status': 'Completed',
                'tags': ['Sustainability', 'Energy', 'IoT'],
            },
        ],
        'experience': [
            {
                'role': 'Innovation Associate',
                'company': 'Geenovate – Incubation Centre, Geetanjali College of Engineering and Technology',
                'duration': 'Currently Working',
                'details': 'Contributing to innovation and startup incubation initiatives by supporting ideation, problem analysis, and solution development with mentors and student teams.',
            },
        ],
        'education': [
            {
                'degree': 'B.Tech in Computer Science and Engineering',
                'institution': 'Geetanjali College Of Engineering and Technology',
                'year': '2028',
                'details': 'CGPA: 7.8 • Relevant coursework: DSA, DBMS, Web Development, Digital Design, OOP',
            },
        ],
        'certifications': [
            {
                'title': 'Deloitte Internship / Certification',
                'issuer': 'Deloitte',
                'detail': 'Hands-on exposure to corporate software project workflows and business process understanding.',
                'image': 'portfolio/images/cert-deloitte.png',
            },
            {
                'title': 'Python Programming',
                'issuer': 'NPTEL',
                'detail': 'Certificate in Python fundamentals, scripting, and practical programming exercises.',
                'image': 'portfolio/images/cert-nptel-python.png',
            },
            {
                'title': 'Design Thinking',
                'issuer': 'NPTEL',
                'detail': 'Certificate in human-centered design, ideation frameworks, and product innovation.',
                'image': 'portfolio/images/cert-nptel-design.png',
            },
        ],
        'achievements': [
            'First Prize – She-Solve Ideathon for an initiative uplifting tribal women.',
            'Consolation Prize – National Level Science Fair “Vaisheshika” for IoT-Based Water Quality Tester.',
            'Participant – ACIC CBIT Srushti Sangamam Ideathon: Online Health Consultancy Application.',
            'Participant – 36-Hour Hackathon: Blockchain-based organic food sourcing platform.',
        ],
        'memberships': ['Student Member – ISTE (Indian Society for Technical Education)'],
        'patents': [
            {
                'title': 'Sustainable Soil Regeneration and Nutrient Recycling',
                'number': '202541107793 A',
            },
        ],
        'soft_skills': [
            'Problem Solving',
            'Design Thinking',
            'Teamwork & Collaboration',
            'Communication Skills',
            'Adaptability & Continuous Learning',
        ],
    }


def home(request):
    context = get_portfolio_context()
    context['active_page'] = 'home'
    return render(request, 'portfolio/home.html', context)


def about(request):
    context = get_portfolio_context()
    context['active_page'] = 'about'
    return render(request, 'portfolio/about.html', context)


def skills(request):
    context = get_portfolio_context()
    context['active_page'] = 'skills'
    return render(request, 'portfolio/skills.html', context)


def projects(request):
    context = get_portfolio_context()
    context['active_page'] = 'projects'
    return render(request, 'portfolio/projects.html', context)


def education(request):
    context = get_portfolio_context()
    context['active_page'] = 'education'
    return render(request, 'portfolio/education.html', context)


def certifications(request):
    context = get_portfolio_context()
    context['active_page'] = 'certifications'
    return render(request, 'portfolio/certifications.html', context)


def experience(request):
    context = get_portfolio_context()
    context['active_page'] = 'experience'
    return render(request, 'portfolio/experience.html', context)


def contact(request):
    context = get_portfolio_context()
    context['active_page'] = 'contact'
    context['form_name'] = ''
    context['form_email'] = ''
    context['form_phone'] = ''
    context['form_message'] = ''

    if request.method == 'POST':
        context['form_name'] = request.POST.get('name', '').strip()
        context['form_email'] = request.POST.get('email', '').strip()
        context['form_phone'] = request.POST.get('phone', '').strip()
        context['form_message'] = request.POST.get('message', '').strip()

        if context['form_name'] and context['form_email'] and context['form_message']:
            context['success_message'] = 'Thank you! Your message has been submitted successfully. I will connect with you soon.'
        else:
            context['error_message'] = 'Please fill in your name, email, and message before submitting.'

    return render(request, 'portfolio/contact.html', context)
