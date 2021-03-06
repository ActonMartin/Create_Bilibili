import subprocess,json
import os


class MakeVideo:
	def __init__(self, mp23_path):
		self.mp3_path = mp23_path

	def get_files(self):
		files_name = []
		files_path = []
		for file in os.listdir(mp3_path):
			file_name = file.split(".")[0]
			files_name.append(file_name)
			file_path = os.path.join(mp3_path,file)
			files_path.append(file_path)
		images_path = "E:\\PR\\04\\image"
		for each_file_path in files_path:
			command = ["D:\\Software\\ffmpeg\\bin\\ffprobe.exe", "-loglevel", "quiet", "-print_format", "json",
			           "-show_format", "-show_streams", "-i", each_file_path]
			result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			out = result.stdout.read()
			# print(str(out))
			temp = str(out.decode('utf-8'))
			data = json.loads(temp)["format"]['duration']
			print(data, each_file_path)
			image_name = os.path.join(os.path.basename(each_file_path).split(".")[0], ".jpg")
			image_path = os.path.join(images_path, image_name)
			vframes = data * 30
			video_name = os.path.join(os.path.basename(each_file_path).split(".")[0], ".mp4")
			videos_dir = "E:\\PR\\04\\here"
			video_path = os.path.join(videos_dir, video_name)
			command2 = ["D:\\Software\\ffmpeg\\bin\\ffmpeg.exe", "-y", "-loop", "1", "-i", image_path, "-i", each_file_path, "-r", "30", "-b:v",
			            "2500k", "-vframes", vframes, "-acodec", "libvo_aacenc", "-ab", "160k", video_path]
			subprocess.Popen(command2)

if __name__ == "__main__":
	mp3_path = "E:\\PR\\04\\mp3"
	files_path1 = MakeVideo.get_files(mp3_path)



