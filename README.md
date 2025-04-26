# Part - 1

## Event Detection model

The Python script `sceneDetect.py` processes a cricket highlights video to automatically detect key event transitions, such as wickets, boundaries, or major action scenes. It uses a lightweight and efficient method based on frame-to-frame pixel difference.

### Approach

1.	Loads the video using OpenCV and retrieves its frame rate and total number of frames.
2.	Converts each frame to grayscale for efficient processing.
3.	Computes frame difference scores between consecutive frames to detect visual changes.
4.	Identifies timestamps where a significant scene change (event) occurs, based on:
* Top 5% visual difference (threshold_percentile)
* Minimum 3 seconds gap between events to avoid duplicates (min_gap_seconds)
5.	Prints timestamps of detected events in seconds.

### How to use

1.	Place your cricket video in the same directory as the script and update the video_path.
2.	Run the script:
   `python detect_events.py`


# Part - 2

## Commentary Generation with GPT-4o

This component of the project focuses on generating cricket commentary using OpenAI's GPT-4o vision model. By providing selected video frames from highlight clips, the model generates human-like, event-specific cricket voiceovers that mimic real-time commentators.


### Notebooks Overview

| Notebook                             | Purpose                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------|
| `gpt_model_single_event.ipynb`       | Generates commentary for a short clip featuring a **single cricket event** (e.g., one delivery). Every 30th frame is sampled and passed to `gpt-4o-mini` to generate concise commentary. |
| `gpt_model_multiple_events.ipynb`    | Tests commentary generation for **multiple deliveries** in one video. It uses the stronger `gpt-4o` model and prompts it to identify and generate **separate commentaries per ball** from the continuous frame stream. |
| `ablation_test_single_event.ipynb`   | Performs an **ablation study** to test how many frames are actually needed to generate meaningful commentary for a single event. It compares performance when sampling every 25th, 30th, 40th, up to 100th frame. |



### Approach

1. **Frame Extraction**: Videos are read using OpenCV and converted to base64-encoded frames.
2. **Sampling**: Depending on the use case, every Nth frame is sampled (e.g., 30th frame for single event, or varying intervals for ablation).
3. **Prompt Engineering**: Carefully crafted prompts instruct GPT-4o to:
   - Narrate each delivery like a commentator.
   - Avoid visual or player descriptions.
   - Number responses for multiple events.
4. **Model Inference**: Frames are sent to the `gpt-4o` or `gpt-4o-mini` model with a `max_tokens` cap, and the generated commentary is printed.



### Key Features and Experiments

- **Event Differentiation**: Multiple-events prompt tells the model to segment input into separate deliveries and respond accordingly.
- **Frame Sampling Tradeoff**: The ablation test helps optimize the number of frames to send, balancing quality vs. API cost.
- **Prompt Variants Tested**:
  - `"These are frames of a video. Create a voiceover commentary..."` (Single event)
  - `"This video contains multiple cricket deliveries. Number the responses..."` (Multiple events)



### How to use

1. Upload a `.mov` cricket video to your working directory.
2. Update the `VideoCapture("your_video.mov")` path in the notebook.
3. Run the notebook to:
   - Extract frames
   - Sample frames
   - Generate commentary using GPT-4o
4. Adjust frame sampling intervals or prompt text as needed.



### API Setup

To run the GPT-based commentary generation notebooks, you'll need access to the OpenAI GPT-4o (or GPT-4o-mini) Vision API. Follow the steps below to get started:

#### 1. Get an OpenAI API Key

- Go to [https://platform.openai.com/signup](https://platform.openai.com/signup) and create an account (or log in if you already have one).
- Navigate to your [API Keys page](https://platform.openai.com/account/api-keys).
- Click **Create new secret key** and copy the key (starts with `sk-...`).

#### 2. Add Payment Method

To use GPT-4o with vision (image) inputs, you need to upgrade from the free-tier trial:

- Visit [Billing → Overview](https://platform.openai.com/account/usage) on your OpenAI account.
- Add a **payment method**.
- Choose one of the following:
  - **Pay-as-you-go**: You're billed based on how many tokens and image inputs you use.
  - **Prepaid credits**: You can buy credits in advance (e.g., \$5, \$10, \$20) and your usage is deducted from that balance.

> **Note:** GPT-4o vision usage can be token-heavy when many frames are sent. Start with small clips and increase as needed.

#### 3. Use the API Key in Code

Once you have your API key, insert it in your notebook like this:

```python

client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")
```` 


# Part - 3

## Text-to-Speech Conversion with gTTS

The Python script `tts_gtts_generate.py` processes the generated cricket commentary text and automatically converts it into spoken audio files. It uses the lightweight and efficient Google Text-to-Speech (gTTS) library to synthesize human-like speech, producing .mp3 audio clips ready to be merged with highlight videos.

### Approach

1. **Commentary Text Input:** The text commentary generated by the GPT-4o model is collected and used as input.
2. **Speech Synthesis with gTTS:** Utilize the `gTTS` library to send the input text to Google's cloud-based TTS API. Specify the target language (e.g., English) for the speech output.
3. **MP3 Audio File Generation:** Generate and save the synthesized audio as `.mp3` files. Each event commentary is saved as a separate audio file for modularity and easy mapping.
4. **Playback and Export:** Play the generated audio files for quick evaluation. Files are ready to be stitched back with the corresponding video highlight clips during post-processing.

### Key Features

- **Lightweight Integration:** No need for GPU or large local models — speech synthesis happens via simple API calls.
- **Fast Prototyping:** Enables quick testing of commentary audibility and fluency.
- **Language Support:** gTTS supports multiple languages; English was used for this project.
- Limitations
   - Static Voice: gTTS provides a default static voice (typically female for English) with no emotional modulation.
   - Limited Expressiveness: The generated audio lacks pitch variations and excitement, which are often desirable in sports commentary.

### How to use 

1. Install the gTTS library if not already installed:
   ```python
   pip install gTTS
   ````
2. Prepare the commentary text output generated from the GPT-4o model.
3. Use the provided `tts_gtts_generate.py` script (or a Jupyter notebook) to:
   - Input the commentary text.
   - Generate corresponding `.mp3` audio files using gTTS.
   - Save the files in the desired output directory.
4. Optionally, batch-process multiple commentary lines to generate a complete set of event audio files.
      
