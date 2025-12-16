# The Correlation Between Housing Value and the Unemployment Rates in the United States

## Project Overview
This project analyzes the economic relationship between the housing market and labor market stability in the United States. Specifically, it explores the correlation between the **Housing Price Index (HPI)** and the **Unemployment Rate** across various Core-Based Statistical Areas (CBSAs). By integrating data from the Federal Housing Finance Agency (FHFA) and the Bureau of Labor Statistics (BLS), this analysis determines there is a relationship between the housing market and the labor rates.

## Main Questions & Findings

### Questions
1. **National Trend:** Is there a significant correlation between the unemployment rate and housing value index on a national scale?
2. **Local Variations:** Does the correlation become stronger or exhibit different behaviors when isolated to specific metropolitan areas?

### Findings & Observations
* **National Correlation:** Intuition suggests that as unemployment rises, housing value drops, but the analysis suggests a relatively weak correlation between the national unemployment rate and housing value index.
* **Metro-Specific Trends:** The project investigates specific metro areas (e.g., Fresno, CA; Des Moines, IA; Tulsa, OK; Louisville, KY). These were selected to observe because the correlation was exceptionally strong (Fresno, CA), middling (Tulsa, OK), and low (Louisville, KY; Des Moines, IA). The time series analysis suggests that factors other than unemployment tend to drive housing value. 
* **Data Coverage:** The analysis covers a timeframe of thirty-five years (1990–2025) and joins data between sixty-seven geographic regions. However, of the 393 geographical codes (CBSAs) only 67 were found to be in common between the two datasets. A larger commonality between datasets may yield differing results. 

---

## Data Sources
Credit is given to the following federal agencies for the raw data used in this analysis:

1. **Housing Price Index (HPI)**
    * **Source:** [Federal Housing Finance Agency (FHFA)](https://www.fhfa.gov/data/hpi)
    * **Dataset:** `hpi_po_metro.csv`
    * **Description:** Seasonally adjusted and non-seasonally adjusted housing price index values for metropolitan areas.

2. **Local Area Unemployment Statistics (LAUS)**
    * **Source:** [U.S. Bureau of Labor Statistics (BLS)](https://www.bls.gov/lau/)
    * **Dataset:** `ssamatab1.csv`
    * **Description:** Monthly estimates of employment, unemployment, and labor force data by metropolitan area.

---

## Setup & Installation

Follow these instructions to set up the project environment on your local machine.

### 1. Clone or Download the Repository
Download the files to a local directory.

### 2. Create a Python Virtual Environment
Create a virtual environment to download all library dependencies.

Run `python -m venv venv`:
This calls the built-in `venv` module to create a Python virtual environment.
* **`venv` (the second one)**: This is the name of the folder created. Standard convention is `venv` or `.venv`.

### 3. How to Activate the Environment
Creating the environment is only half the battle; you must **activate** it to use it.

**For Windows (Command Prompt):**
```
.\venv\Scripts\activate
```

**For Windows (Git Bash / PowerShell):**
```
source venv/Scripts/activate
```

**For macOS / Linux:**
```
source venv/bin/activate
```

 **Note:** Once activated, your terminal prompt should change to show `(venv)` at the beginning.

**Deactivation** To exit the virtual environment enter `deactivate` into your terminal.

### 4. Install 'requirements.txt'

Run ```pip install -r requirements.txt``` This will install all the required dependencies.

### 5. Using Jupyter Notebooks
This project uses Jupyter notebooks instead of the traditional Python file. The advantages of using this file type are the ability to run code blocks independently of one another in python cells. Markdown cells are also able to be inserted into the document, making for presentable code. 

In order to use the notebook:
1. Select the Kernel of Python installed from requirements.txt.
2. Run the file using the 'run' button found in your IDE. This will generate all the code and visualizations within the notebook itself, and not in your terminal.

# Author
David English

# Acknowledgements
Gemini, ChatGPT, and Claude were consulted during the making of this project.

# License
MIT License