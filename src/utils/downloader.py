from yt_dlp import YoutubeDL
import json

from src.models.media_model import MediaModel


class Downloader:
    def __init__(self, dlFormat: str):
        result = YoutubeDL().extract_info(
            "https://www.youtube.com/watch?v=cgfx2mLSI-A&pp=ygUPbGludXMgdGVjaCB0aXBz",
            download=False,
        )


        model: MediaModel = MediaModel(**YoutubeDL.sanitize_info(result))

        for format in model.formats:
            if format.format_note != "storyboard" and format.protocol == "m3u8_native":
                print(
                    f"{format.resolution} :: {format.video_ext} :: {format.vcodec} :: {format.protocol} :: {format.dynamic_range} :: {format.format_id}"
                )

        ytdlp_opts = {
            "format": dlFormat,
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "EmbedThumbnail",
                    "already_have_thumbnail": False,
                },
            ],
        }

        YoutubeDL(ytdlp_opts).download(
            "https://www.youtube.com/watch?v=cgfx2mLSI-A&pp=ygUPbGludXMgdGVjaCB0aXBz"
        )
