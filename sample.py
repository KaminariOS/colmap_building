import cv2
import os

def sample_frames_from_video(video_path, output_folder, num_frames=200):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_interval = max(1, total_frames // num_frames)

    frame_count = 0
    sampled_count = 0

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        if frame_count % frame_interval == 0 and sampled_count < num_frames:
            frame_filename = os.path.join(output_folder, f"frame_{sampled_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            sampled_count += 1

        frame_count += 1

        if sampled_count >= num_frames:
            break

    video_capture.release()
    print(f"Sampled {sampled_count} frames from the video.")

video_path = 'PXL_20241127_212357340.mp4'  
output_folder = 'sampled_frames'       
sample_frames_from_video(video_path, output_folder)
