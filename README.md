# Part - 1

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


---
