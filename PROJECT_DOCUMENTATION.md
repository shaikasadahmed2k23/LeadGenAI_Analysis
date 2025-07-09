# LEADGen AI — Project Documentation

## Overview
LEADGen AI is a professional lead generation and analysis tool designed for venture capital firms and business analysts. It provides a modern, interactive web interface for analyzing company data, investment potential, and growth signals using advanced web scraping and AI analysis.

---

## Architecture

### Main Components
- **Streamlit UI (`leadgen_ui.py`):** The main user interface, handling all user interactions, data visualization, and export features.
- **AI Logic (`leadGENAI.py`):** (Expected) Handles data extraction, analysis, and report generation. Not included in this folder, but referenced in the UI.

### Data Flow
1. **User Input:**
   - Users enter a company name or upload a batch file via the sidebar.
2. **Analysis Trigger:**
   - On clicking "Analyze Company", the UI calls `LeadGenAI.extract_company_profile()` to fetch and analyze data.
3. **Progress Feedback:**
   - The UI shows a progress bar and status updates during analysis.
4. **Results Display:**
   - Results are displayed in a tabbed interface: Overview, Financial, Growth, Team & Contact, and Raw Data.
5. **Export:**
   - Users can export results in JSON, Markdown, or plain text formats.

---

## UI Structure

- **Header:**
  - Project title and subtitle with custom CSS styling.
- **Sidebar:**
  - Analysis type selection (Single/Batch)
  - Company input or file upload
  - Analysis settings (retries, delay)
  - Export options
- **Main Area:**
  - Welcome message or analysis results
  - Metric cards for key company data
  - Investment score gauge (Plotly)
  - Growth signals and funding timeline (Plotly)
  - Tabbed layout for detailed sections
- **Footer:**
  - Project credits and copyright

---

## Key Functions (from `leadgen_ui.py`)

- `create_header()`: Renders the main header.
- `create_metric_card(title, value, description, color)`: Displays a styled metric card.
- `create_investment_score_gauge(score)`: Shows a Plotly gauge for investment score.
- `create_growth_signals_chart(growth_signals)`: Visualizes growth signals as a bar chart.
- `create_funding_timeline(funding_rounds)`: Visualizes funding rounds as a timeline.
- `display_company_profile(profile)`: Main function to display all company data in tabs.
- `main()`: Application entry point, handles UI logic and user interaction.

---

## Extensibility

- **Batch Analysis:**
  - The UI is ready for batch uploads; logic can be implemented in `LeadGenAI`.
- **Data Sources:**
  - The AI logic can be extended to include more data sources or APIs.
- **Custom Visualizations:**
  - Add new Plotly charts or Streamlit components for deeper insights.
- **Authentication:**
  - Add user authentication for multi-user or SaaS deployments.

---

## Requirements
- Python 3.8+
- Streamlit, pandas, plotly, and other dependencies in `requirements_ui.txt`
- `leadGENAI.py` (not included) for core AI logic

---

## Known Limitations
- The core AI/data extraction logic (`leadGENAI.py`) is not included in this folder.
- Batch analysis is a placeholder and not yet implemented.
- Some visualizations use placeholder data if real data is missing.

---

## Contact
For questions, support, or contributions, please contact the project maintainer. 