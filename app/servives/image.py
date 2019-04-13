from .common import CommonService


class ImageService(CommonService):

    def save(self, **kwargs):
        data = self.get_first({'img_id': kwargs.get('img_id')})
        if not data:
            if kwargs.get('bookmarked') == "ture":
                kwargs['bookmarked'] = 1
            else:
                kwargs['bookmarked'] = 0

            return super(ImageService, self).save(**kwargs)
        return data.id
