from IPython.display import display, HTML
import filecmp
import yaml
from smolder.summary.report_fhir_counts import AVAILABLE_STUDIES



PROD_loc = 'output/summary/PROD'
QA_loc = 'output/summary/QA'

#run diff on QA and PROD
def folder_diff(folder1, folder2):
    """Compares two folders and generates HTML output for the differences or "All good!" if identical."""
    result = filecmp.dircmp(folder1, folder2)

    # Check if folders are identical
    if not result.left_only and not result.right_only and not result.diff_files:
        return f"<h3>Comparing '{folder1}' and '{folder2}'</h3><h2>✅ All good!</h2>" 

    # If not identical, generate the diff output
    diff_output = f"<h1>‼️ 🔴 🆘</h1><h3>'{folder1}' and '{folder2}' are not synced!</h3><ul>"

    if result.left_only:
        diff_output += f"<li><b>Files only in {folder1}:</b><ul>"
        for item in result.left_only:
            diff_output += f"<li>{item}</li>"
        diff_output += "</ul></li>"

    if result.right_only:
        diff_output += f"<li><b>Files only in {folder2}:</b><ul>"
        for item in result.right_only:
            diff_output += f"<li>{item}</li>"
        diff_output += "</ul></li>"

    if result.diff_files:
        diff_output += "<li><b>Different files:</b><ul>"
        for item in result.diff_files:
            diff_output += f"<li>{item}</li>"
        diff_output += "</ul></li>"

    # Recursively compare subdirectories
    for common_dir in result.common_dirs:
        diff_output += folder_diff(os.path.join(folder1, common_dir), os.path.join(folder2, common_dir))

    diff_output += "</ul>"
    return diff_output

def diplay_summaries():
        #display summaries
    all_html=""

    for study in AVAILABLE_STUDIES:
        with open(f"output/summary/PROD/fhir_summary_{study}.yaml", 'r') as file:
            yaml_content = yaml.safe_load(file)
        cards_html = ""
        for section, values in yaml_content.items():
            card_content = f"<h3>{section}</h3><ul>"
            if isinstance(values, dict):  # Check if 'values' is a dictionary
                for key, value in values.items():
                    card_content += f"<li><span>{key}:</span> <span>{value}</span></li>"
            else:
                card_content += f"<li class='values'>{values}</li>"  # Handle single values
            card_content += "</ul>"
            cards_html += f'<div class="card">{card_content}</div>'

            style = """<style>
                        .container {
                    display: grid;
                    grid-template-columns: repeat(4, minmax(7.5rem, 1fr)); /* Responsive grid */
                    gap: .5rem;
                    max-width:1000px;
                }
                .card {
                    border: 1px solid #00000069;
                    border-radius: 3px;
                    /* box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); */
                }
                .card ul {
                    list-style: none;
                    padding: 0!important;
                    margin: 0;
                    margin-top:.5rem;
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(3rem,120px));
                }
                .card h3 {
                    margin: 0!important;
                    background:rgb(254,254,254);
                }
            </style>"""
        all_html += style + f"<h2>{study}</h2>" +"<div class='container'>" + cards_html +"</div>"
    return all_html