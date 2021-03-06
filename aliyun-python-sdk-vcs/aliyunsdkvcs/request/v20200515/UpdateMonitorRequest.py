# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvcs.endpoint import endpoint_data

class UpdateMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'UpdateMonitor','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_RuleName(self):
		return self.get_body_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_body_params('RuleName', RuleName)

	def get_PicOperateType(self):
		return self.get_body_params().get('PicOperateType')

	def set_PicOperateType(self,PicOperateType):
		self.add_body_params('PicOperateType', PicOperateType)

	def get_AttributeName(self):
		return self.get_body_params().get('AttributeName')

	def set_AttributeName(self,AttributeName):
		self.add_body_params('AttributeName', AttributeName)

	def get_AttributeOperateType(self):
		return self.get_body_params().get('AttributeOperateType')

	def set_AttributeOperateType(self,AttributeOperateType):
		self.add_body_params('AttributeOperateType', AttributeOperateType)

	def get_RuleExpression(self):
		return self.get_body_params().get('RuleExpression')

	def set_RuleExpression(self,RuleExpression):
		self.add_body_params('RuleExpression', RuleExpression)

	def get_TaskId(self):
		return self.get_body_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_body_params('TaskId', TaskId)

	def get_DeviceOperateType(self):
		return self.get_body_params().get('DeviceOperateType')

	def set_DeviceOperateType(self,DeviceOperateType):
		self.add_body_params('DeviceOperateType', DeviceOperateType)

	def get_PicList(self):
		return self.get_body_params().get('PicList')

	def set_PicList(self,PicList):
		self.add_body_params('PicList', PicList)

	def get_AttributeValueList(self):
		return self.get_body_params().get('AttributeValueList')

	def set_AttributeValueList(self,AttributeValueList):
		self.add_body_params('AttributeValueList', AttributeValueList)

	def get_DeviceList(self):
		return self.get_body_params().get('DeviceList')

	def set_DeviceList(self,DeviceList):
		self.add_body_params('DeviceList', DeviceList)