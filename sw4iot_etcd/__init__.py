# Copyright 2018 SOFTWAY4IoT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import etcd3

ETCD_PREFIX = '/sw4iot.io'


def decode_utf8(text):
    if type(text) is bytes:
        return text.decode('utf-8')
    return text


class Sw4iotEtcd:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.etcd = None
        self.__connect()

    def __connect(self):
        """
        Connect with etcd server
        """
        self.etcd = etcd3.client(host=self.host, port=self.port)

    ###
    # Slice
    ###
    def add_slice(self, slice, network):
        self.etcd.put('{}/slice/list/{}'.format(ETCD_PREFIX, slice), slice)
        self.etcd.put('{}/slice/{}/network'.format(ETCD_PREFIX, slice), json.dumps(network))

    def get_slice(self, slice):
        slice = self.etcd.get('{}/slice/{}/network'.format(ETCD_PREFIX, slice))[0]
        return json.loads(decode_utf8(slice)) if slice else None

    def delete_slice(self, slice):
        self.etcd.delete('{}/slice/list/{}'.format(ETCD_PREFIX, slice))
        return self.etcd.delete_prefix('{}/slice/{}'.format(ETCD_PREFIX, slice))

    ###
    # Slice list
    ###
    def get_slice_list(self):
        return [decode_utf8(slice[0]) for slice in self.etcd.get_prefix('{}/slice/list'.format(ETCD_PREFIX))]

    ###
    # Slice info
    ###
    def get_slice_info(self, slice):
        return self.etcd.get('{}/slice/{}/info'.format(ETCD_PREFIX, slice))[0]

    ###
    # Slice device
    ###
    def add_slice_device(self, slice, device, data):
        self.etcd.put('{}/slice/{}/device/list/{}'.format(ETCD_PREFIX, slice, device), device)
        self.etcd.put('{}/slice/{}/device/{}'.format(ETCD_PREFIX, slice, device), json.dumps(data))

    def get_slice_device(self, slice, device):
        dev = self.etcd.get('{}/slice/{}/device/{}'.format(ETCD_PREFIX, slice, device))[0]
        return json.loads(decode_utf8(dev)) if dev else None

    def delete_slice_device(self, slice, device):
        self.etcd.delete('{}/slice/{}/device/list/{}'.format(ETCD_PREFIX, slice, device))
        return self.etcd.delete('{}/slice/{}/device/{}'.format(ETCD_PREFIX, slice, device))

    def get_slice_devices(self, slice):
        return [decode_utf8(device[0]) for device in self.etcd.get_prefix('{}/slice/{}/device/list'.format(ETCD_PREFIX, slice))]

    ###
    # Slice gateway
    ###
    def add_slice_gw(self, slice, gateway, data):
        self.etcd.put('{}/slice/{}/gateway/list/{}'.format(ETCD_PREFIX, slice, gateway), gateway)
        self.etcd.put('{}/slice/{}/gateway/{}'.format(ETCD_PREFIX, slice, gateway), json.dumps(data))

    def get_slice_gw(self, slice, gateway):
        gw = self.etcd.get('{}/slice/{}/gateway/{}'.format(ETCD_PREFIX, slice, gateway))[0]
        return json.loads(decode_utf8(gw)) if gw else None

    def delete_slice_gw(self, slice, gateway):
        self.etcd.delete('{}/slice/{}/gateway/list/{}'.format(ETCD_PREFIX, slice, gateway))
        return self.etcd.delete_prefix('{}/slice/{}/gateway/{}'.format(ETCD_PREFIX, slice, gateway))

    def get_slice_gws(self, slice):
        return [decode_utf8(gw[0]) for gw in self.etcd.get_prefix('{}/slice/{}/gateway/list'.format(ETCD_PREFIX, slice))]

    def add_slice_gw_driver(self, slice, gateway, driver):
        self.etcd.put('{}/slice/{}/gateway/driver/{}'.format(ETCD_PREFIX, slice, gateway), driver)

    def del_slice_gw_driver(self, slice, gateway, driver):
        self.etcd.delete('{}/slice/{}/gateway/driver/{}'.format(ETCD_PREFIX, slice, gateway))

    ###
    # Gateway
    ###
    def enable_gw(self, gateway):
        self.etcd.put('{}/gateway/{}/enable'.format(ETCD_PREFIX, gateway), json.dumps({'enable': True}))

    def disable_gw(self, gateway):
        self.etcd.put('{}/gateway/{}/enable'.format(ETCD_PREFIX, gateway), json.dumps({'enable': False}))

    def get_gw_status(self, gateway):
        status = self.etcd.get('{}/gateway/{}/enable'.format(ETCD_PREFIX, gateway))[0]
        status = json.loads(decode_utf8(status))['enable'] if status else None
        return status

    def set_gw(self, gateway, data):
        self.etcd.put('{}/gateway/list/{}'.format(ETCD_PREFIX, gateway), gateway)
        self.etcd.put('{}/gateway/{}/info'.format(ETCD_PREFIX, gateway), json.dumps(data))

    def get_gw(self, gateway):
        gw_data = self.etcd.get('{}/gateway/{}/info'.format(ETCD_PREFIX, gateway))[0]
        return json.loads(decode_utf8(gw_data)) if gw_data else None

    def delete_gw(self, gateway):
        self.etcd.delete('{}/gateway/list/{}'.format(ETCD_PREFIX, gateway), gateway)
        return self.etcd.delete_prefix('{}/gateway/{}'.format(ETCD_PREFIX, gateway))

    def get_gw_list(self):
        return [decode_utf8(gw[0]) for gw in self.etcd.get_prefix('{}/gateway/list'.format(ETCD_PREFIX))]

    ###
    # Gateway slice
    ###
    def add_gw_slice(self, gateway, slice):
        self.etcd.put('{}/gateway/{}/slice/{}'.format(ETCD_PREFIX, gateway, slice), slice)

    def get_gw_slice(self, gateway, slice):
        sl = self.etcd.get('{}/gateway/{}/slice/{}'.format(ETCD_PREFIX, gateway, slice))[0]
        return json.loads(sl) if sl else None

    def delete_gw_slice(self, gateway, slice):
        return self.etcd.delete_prefix('{}/gateway/{}/slice/{}'.format(ETCD_PREFIX, gateway, slice))

    def get_gw_slices(self, gateway):
        return [decode_utf8(slice[0]) for slice in self.etcd.get_prefix('{}/gateway/{}/slice'.format(ETCD_PREFIX, gateway))]
