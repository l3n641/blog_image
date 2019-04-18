import requests, os
from qiniu import Auth, put_file
from PIL import Image
from requests_html import HTMLSession
from app.extensions import db


def down_file(resource, file_name, save_path):
    """
    下载文件 到本地
    :param resource:  目标文件地址
    :param file_name:  文件名
    :param save_path: 保存路径,没有的话就自动创建
    :return:
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = os.path.join(save_path, file_name)
    with open(path, 'wb') as file:
        file.write(requests.get(resource).content)
        return path


def update_to_qiniu(file, file_name=None):
    """
    上传文件到七牛
    :param file:  文件路径
    :param file_name:  自定义文件名
    :return:
    """
    access_key = os.getenv('QINIU_ACCESS_KEY')
    secret_key = os.getenv("QINIU_SECRET_KEY")
    bucket = os.getenv("QINIU_BUCKET")

    try:
        qiniu = Auth(access_key, secret_key)
        token = qiniu.upload_token(bucket)
        ret, detail_info = put_file(token, file_name, file)
        return ret.get('key')

    except:
        update_to_qiniu(file, file_name)


def thumbnail(file_path, multiple, save_dir, save_name, save_ext=None):
    """
    生成缩略图
    :param file_path: 源文件
    :param multiple: 缩放倍速
    :param save_dir: 保存路径
    :param save_name: 保存的文件名
    :param save_ext: 文件类型
    :return: 文件路径
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    path = os.path.join(save_dir, save_name)
    img = Image.open(file_path)
    w, h = img.size
    img.thumbnail((w // multiple, h // multiple))
    img.save(path, save_ext)
    return path


def spider_image():
    """
    爬取网页内容
    :return:
    """
    from app.servives import image_srv

    session = HTMLSession()
    page = 1
    while True:
        url = 'https://www.apptu.cn/wp-admin/admin-ajax.php?action=getpost&paged=' + str(page)
        response = session.get(url)
        datas = response.json()

        if not datas:
            return True
        for data in datas:
            image_srv.save(url=data.get('message'), img_id=data.get('id'), bookmarked=data.get('bookmarked'))
            db.session.commit()

        page = page + 1
        print(url)
