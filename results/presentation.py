import pandas as pd
from IPython.display import display
# Read in the JSON file
S=['DIETClassifier_report','intent_report','story_report']
for s in S:
    df = pd.read_json('results\{}.json'.format(s))

    # Convert the DataFrame to an HTML table
    html_table = df.to_html()
    #display(html_table)
    with open(r'results\{}.html'.format(s), 'w') as f:
        f.write(html_table)

# Open the file in a web browser
