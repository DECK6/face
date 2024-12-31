import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random

# 감정과 이모지 매핑
target_emotions = {
    "happy": ":)",
    "sad": ":(",
    "angry": "-_-+",
    "surprised": "o_o",
    "neutral": "-_-"
}

def assign_random_emotion():
    return random.choice(list(target_emotions.keys()))

def overlay_emoji(image, emotion):
    emoji = target_emotions[emotion]
    
    # Convert emoji to image overlay
    overlay_image = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay_image)

    # Adjust font size based on image dimensions
    font_size = int(min(image.size) * 0.1)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Position the emoji near the forehead
    position = (image.width // 2 - font_size // 2, image.height // 4 - font_size // 2)

    draw.text(position, emoji, font=font, fill=(255, 255, 255, 255))
    return Image.alpha_composite(image.convert("RGBA"), overlay_image)

def main():
    st.title("Emotion Overlay App")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.write("Analyzing the image...")
        # Assign a random emotion for now
        assigned_emotion = assign_random_emotion()
        st.write(f"Detected Emotion: {assigned_emotion.capitalize()}")

        # Overlay emoji based on emotion
        result_image = overlay_emoji(image, assigned_emotion)

        st.image(result_image, caption="Image with Emotion Overlay", use_column_width=True)

if __name__ == "__main__":
    main()
