# Copyright 2014 - Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.api.ec2 import ec2utils
from nova import context
from nova import objects
from nova import test


class EC2UtilsTestCase(test.TestCase):
    def setUp(self):
        self.ctxt = context.get_admin_context()
        ec2utils.reset_cache()
        super(EC2UtilsTestCase, self).setUp()

    def test_get_int_id_from_snapshot_uuid(self):
        smap = objects.EC2SnapshotMapping(self.ctxt, uuid='fake-uuid')
        smap.create()
        smap_id = ec2utils.get_int_id_from_snapshot_uuid(self.ctxt,
                                                         'fake-uuid')
        self.assertEqual(smap.id, smap_id)

    def test_get_int_id_from_snapshot_uuid_creates_mapping(self):
        smap_id = ec2utils.get_int_id_from_snapshot_uuid(self.ctxt,
                                                         'fake-uuid')
        smap = objects.EC2SnapshotMapping.get_by_id(self.ctxt, smap_id)
        self.assertEqual('fake-uuid', smap.uuid)
