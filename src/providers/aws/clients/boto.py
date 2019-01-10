# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import boto3
import botocore
import src.utils as utils

# Default values
botocore_client_read_timeout = 360

class BotoClient(object):
    
    def __init__(self, **kwargs):
        self.session_args = kwargs['session']
        self.client_args = kwargs['client']
        
    @utils.lazy_property
    def client(self):
        session = boto3.Session(**self.session_args)
        self.client_args['config'] = botocore.config.Config(read_timeout=botocore_client_read_timeout)
        return session.client(self.boto_client_name, **self.client_args)
    
    def get_access_key(self):
        session = boto3.Session(**self.session_args)
        credentials = session.get_credentials()
        return credentials.access_key
