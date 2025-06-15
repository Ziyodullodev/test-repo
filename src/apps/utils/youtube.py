from yt_dlp import YoutubeDL

class YoutubeVideo:
    
    def __init__(self, video_url):
        self.video_url = video_url

    def get_video(self):
        with YoutubeDL() as ydl:
            info = ydl.extract_info(self.video_url, download=False)
            return info
        
    def info_video(self):
        info = self.get_video()
        video_title = info.get('title', 'Noma’lum')
        uploader = info.get('uploader', 'Noma’lum')
        view_count = info.get('view_count', 0)
        thumbnail_url = info.get('thumbnail', 'No Thumbnail')
        thumbnail_medium = info.get('thumbnails', [{}])[1].get('url', thumbnail_url)
        video_duration = info.get('duration', 0)  # Sekundlarda
        file_size = info.get('filesize_approx', 'Noma’lum')  # Baytlarda
        
        hours, remainder = divmod(video_duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
            
        video_duration_info = f"{hours}:{minutes}:{seconds}"
        if hours == 0:
            video_duration_info = f"{minutes}:{seconds}"
        output_data = {
            "title": video_title,
            "uploader": uploader,
            "views": view_count,
            "duration": video_duration,
            "video_duration_info": video_duration_info,
            "thumbnail_high_quality": thumbnail_url,
            "thumbnail_medium_quality": thumbnail_medium,
            "file_size": f"Hajm: {file_size / (1024 * 1024):.2f} MB",
        }
        return output_data
    
    def download_video(self):
        info = self.get_video()
        video_url = info.get('url', False)
        return video_url
        
    

# if __name__ == "__main__":
#     yt = YoutubeVideo(video_url)
#     print(yt.info_video())
#     # print(yt.download_video())
        

