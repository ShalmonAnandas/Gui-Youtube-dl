from yt_dlp import YoutubeDL
import json

from models.info_model import InfoModel


class TestDownload:
    def __init__(self):
        result = YoutubeDL().extract_info(
            "https://www.youtube.com/watch?v=cgfx2mLSI-A&pp=ygUPbGludXMgdGVjaCB0aXBz",
            download=False,
        )

        model: InfoModel = InfoModel.from_json(
            json.dumps(YoutubeDL.sanitize_info(result))
        )

        for format in model.formats:
            if format.format_note != "storyboard" and format.protocol == "m3u8_native":
                print(
                    f"{format.resolution} :: {format.video_ext} :: {format.vcodec} :: {format.protocol} :: {format.dynamic_range} :: {format.format_id}"
                )

        ytdlp_opts = {
            "format": "bestaudio+602",
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
