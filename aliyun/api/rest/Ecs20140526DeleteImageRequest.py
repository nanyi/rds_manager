'''
Created by auto_sdk on 2015.06.23
'''
from aliyun.api.base import RestApi
class Ecs20140526DeleteImageRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ImageId = None
		self.RegionId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DeleteImage.2014-05-26'
