import os

import dotenv
from vk_api import VkApi
from vk_api.vk_api import VkApiMethod

dotenv.load_dotenv()


class Vk:
    _user_session: VkApi
    _user_api: VkApiMethod

    def __init__(self):
        self._user_session = VkApi(token=os.environ["USER_API_KEY"])
        self._user_api = self._user_session.get_api()

    def get_comments(self, video: str):
        owner_id = video[5:].split("_")[0]
        video_id = video[5:].split("_")[1]
        count = self._user_api.video.getComments(video_id=video_id, owner_id=owner_id, count=int(1))["count"]
        return self._user_api.video.getComments(video_id=video_id, owner_id=owner_id, count=int(count))['items']
