import cv2
from moviepy.editor import VideoFileClip

video_input_path = input("(Ia| Mary Janne):Onde tá o video, Lindinho? ")


def orientation_adjust(video_input, video_output):
    try:
        clip = VideoFileClip(video_input)
        largura, altura = clip.size
        out = cv2.VideoWriter(
            video_output, cv2.VideoWriter_fourcc(*"XVID"), clip.fps, (altura, largura)
        )
        for frame in clip.iter_frames():
            frame_rotaded = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            out.write(frame_rotaded)
        out.release()
        print("clip_copy save")
    except KeyboardInterrupt:
        print("Esqueceu o Path, né! Até logo!")
    except:
        print("not found")


# /home/ednei/Vídeos/istockphoto-1469018003-640_adpp_is.mp4
video_output_path = "copia.mp4"


orientation_adjust(video_input_path, video_output_path)
