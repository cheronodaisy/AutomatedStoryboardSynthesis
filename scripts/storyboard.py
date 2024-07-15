from PIL import Image
import os

def create_storyboard(output_dir, storyboard_path):
    frame_names = ['preview.png', 'landing_frame.png', 'endframe.png']
    frames = []

    for frame_name in frame_names:
        frame_path = os.path.join(output_dir, frame_name)
        if os.path.exists(frame_path):
            frames.append(Image.open(frame_path))
        else:
            print(f"Frame {frame_name} not found in {output_dir}")

    if len(frames) != len(frame_names):
        print("Not all frames could be loaded. Exiting.")
        return

    total_width = sum(frame.width for frame in frames) + (len(frames) - 1) * 40  # Adding padding space
    max_height = max(frame.height for frame in frames)

    storyboard = Image.new('RGBA', (total_width, max_height), color=(255, 255, 255, 255))

    # Paste each frame with padding space
    x_offset = 0
    for frame in frames:
        storyboard.paste(frame, (x_offset, 0))
        x_offset += frame.width + 40

    storyboard.save(storyboard_path)
    print(f"Storyboard saved to {storyboard_path}")

output_dir = 'output'
storyboard_path = 'output/storyboard.png'

create_storyboard(output_dir, storyboard_path)
