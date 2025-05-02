import cv2
import numpy as np

# Parameters
video_path = "full_clip.mp4"
threshold_percentile = 95  # Sensitivity of detection (higher = fewer events)
min_gap_seconds = 3        # Minimum time between events

# Load video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"FPS: {fps}, Total Frames: {frame_count}")

# Initialize
prev_gray = None
diff_scores = []
frame_indices = []

# Compute difference scores
for i in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev_gray is not None:
        diff = cv2.absdiff(gray, prev_gray)
        score = np.mean(diff)
        diff_scores.append(score)
        frame_indices.append(i)
    prev_gray = gray

cap.release()

# Find frame indices with high visual change
threshold = np.percentile(diff_scores, threshold_percentile)
min_gap_frames = int(fps * min_gap_seconds)

events = []
last_event = -min_gap_frames

for i, score in zip(frame_indices, diff_scores):
    if score > threshold and (i - last_event) >= min_gap_frames:
        events.append(i)
        last_event = i

# Convert to timestamps
timestamps = [round(i / fps, 2) for i in events]

print("\n🎯 Detected Event Change Timestamps:")
for i, t in enumerate(timestamps, 1):
    print(f"Event {i}: {t} seconds")
