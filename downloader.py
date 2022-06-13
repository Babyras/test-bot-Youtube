from pytube import YouTube

def on_complete(stream, file_path):
	print(stream)
	print(file_path)

def on_progress(stream, chunk, bytes_remaining):
	print(100 - (bytes_remaining / stream.filesize * 100))

def download_by_url(url):
	video_object = YouTube(
	url, 
	on_complete_callback = on_complete,
	on_progress_callback = on_progress)

	print(video_object.title)

	# download
	video_object.streams.get_highest_resolution().download()


