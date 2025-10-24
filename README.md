# Meeting Summarizer (Transcript Collector)

This project processes meeting audio files and generates text transcripts. **Note:** It currently only handles transcripts and does **not** provide summaries.

## Features

- Convert meeting audio into text transcripts
- Store transcripts for later review

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Install required libraries:

```bash
pip install -r requirements.txt
Usage
Place your meeting audio file (e.g., final_test_audio.mp3) in the project folder.

Run the main script:

bash
Copy code
python main.py
The transcript will be generated and saved.

Project Structure
bash
Copy code
Summarizer/
├── main.py              # Main script for processing transcripts
├── final_test_audio.mp3 # Example meeting audio
├── .gitignore           # Ignored files/folders
└── README.md            # Project description
Notes
The project only generates transcripts, not summaries.

Keep your virtual environment (venv) out of the repository or ignored in .gitignore.
