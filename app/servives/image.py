from .common import CommonService
from app.functions import down_file, update_to_qiniu, thumbnail
import os


class ImageService(CommonService):

    def save(self, **kwargs):
        data = self.get_first({'img_id': kwargs.get('img_id')})

        if not data:
            if kwargs.get('bookmarked') == "ture":
                kwargs['bookmarked'] = 1
            else:
                kwargs['bookmarked'] = 0

            file_name = kwargs.get('url').split('/')[-1]

            image_dir = os.getenv(key='IMAGE_PATH')
            path = down_file('https:' + kwargs.get('url'), file_name, image_dir)
            update_to_qiniu(path, file_name)
            thumbnail_name = "thumbnail_" + file_name
            thumbnail_path = thumbnail(path, 3, image_dir, thumbnail_name, 'jpeg')
            update_to_qiniu(thumbnail_path, thumbnail_name)

            return super(ImageService, self).save(file_name=file_name, **kwargs)
        return data.id
