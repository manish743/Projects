from django.shortcuts import render, redirect
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

# Create your views here.
# def youtube(request):
#     if request.method == "POST":
#         url = request.POST["url"]
#         video = YouTube(url)
#         stream = video.streams.get_lowest_resolution()
#         stream.download()
#         print("Download complete!")
#         return render(request, template_name="youtube/index.html")
#     return render(request, template_name="youtube/index.html")

def youtube(request):
    if request.method == "POST":
        url = request.POST.get("url")
        try:
            video = YouTube(url)
            stream = video.streams.get_lowest_resolution()
            stream.download()  # You can specify a download location here if needed
            message = "Download complete!"
        except RegexMatchError:
            message = "There was an issue with processing the URL. Please try again."
        except VideoUnavailable:
            message = "The video is unavailable. Please check the URL."
        except Exception as e:
            message = f"An error occurred: {str(e)}"

        return render(request, template_name="youtube/index.html", context={"message": message})

    return render(request, template_name="youtube/index.html")