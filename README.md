How to Detect and Display Unique Speakers
--

This is an example of how you can use AssemblyAI's [Speaker Labels](https://www.assemblyai.com/docs/core-transcription#speaker-labels-speaker-diarization) model to automatically detect unique speakers and display a turn-by-turn dialogue of the conversation. 

## Quick Setup

* Download project files by running `git clone https://github.com/AssemblyAI/speaker-diarization.git`
* Navigate to the project folder
* Create a new [virtual environment](https://docs.python.org/3/library/venv.html)
* Activate the new virtual environment and run `pip install -r requirements.txt` to install project dependencies
* Add your AssemblyAI API key to the `configure.py` file
* Run the application using the `streamlit run app.py`

## How it Works

The file you upload is submitted to AssemblyAI for transcription with `speaker_labels` set to `true`. When the transcript is complete you will receive a JSON response that contains a top-level key names `utterances`. Data from the `utterance` key is iterated upon to Streamlit is used display a turn-by-turn transcript of "who spoke when" in the browser.

## Main Dependencies

* [Streamlit](https://pypi.org/project/streamlit/) The fastest way to build data apps in Python
* [Pandas](https://pypi.org/project/pandas/) Powerful data structures for data analysis, time series, and statistics

Contact Us
--
If you have any questions, please feel free to reach out to our Support team - support@assemblyai.com!
