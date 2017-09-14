import config

class ImgUrls:
    def __init__(self):
        self.girlNum = config.START_GIRL;
        self.catNum = config.START_CAT;

    def getImgUrl(self, type):
        if (type == 'girls'):
            url = config.girlsUrl + str(self.girlNum) + '.jpg'
            self.girlNum = config.START_GIRL if self.girlNum > config.MAX_GIRL else self.girlNum + 1
        elif (type == 'cats'):
            url = config.catsUrl + str(self.catNum) + '.jpg'
            self.catNum = config.START_CAT if self.catNum > config.MAX_CAT else self.catNum + 1
        return url