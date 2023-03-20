from moviepy.editor import *
import moviepy.audio.fx.all as afx

# Load the video file
video_path = "your_video_path"
video = VideoFileClip(video_path)

# Fade-out duration in seconds
fade_out_duration = 5

# Apply the fade-out effect to the audio
audio_fade_out = video.audio.fx(afx.audio_fadeout, fade_out_duration)
video_with_fade_out_audio = video.set_audio(audio_fade_out)

# Save the video with the fade-out audio effect
output_path = "your_output_path"
video_with_fade_out_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Close the video clips to release resources
video.close()
video_with_fade_out_audio.close()


