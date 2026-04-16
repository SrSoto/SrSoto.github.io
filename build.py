import os

def build():
    # Define the components in order
    components = [
        'src/components/head.html',
        'src/components/header.html',
        'src/components/milestones_intro.html',
        'devs/01_data_cleaning_performance/card.html',
        'devs/02_multitenant/card.html',
        'devs/03_wls_service_test/card.html',
        'devs/04_wls_model_refactor/card.html',
        'devs/05_tm_team/card.html',
        'src/components/milestones_outro.html',
        'src/components/experience.html',
        'src/components/about.html',
        'src/components/skills.html',
        'src/components/education.html',
        'src/components/scripts.html'
    ]

    html_content = ""
    for component in components:
        if os.path.exists(component):
            with open(component, 'r', encoding='utf-8') as f:
                html_content += f.read() + "\n"
        else:
            print(f"Warning: Component {component} not found.")

    # Write the final index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content.strip())
    
    print("Successfully built index.html from components.")

if __name__ == "__main__":
    build()
