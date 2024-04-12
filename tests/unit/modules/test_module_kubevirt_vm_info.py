# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kubernetes.core.plugins.module_utils.k8s.service import (
    K8sService,
)
from ansible_collections.kubevirt.core.plugins.modules import (
    kubevirt_vm_info,
)
from ansible_collections.kubevirt.core.tests.unit.utils.ansible_module_mock import (
    AnsibleExitJson,
    exit_json,
    set_module_args,
)

FIND_ARGS_DEFAULT = {
    "kind": "VirtualMachine",
    "api_version": "kubevirt.io/v1",
    "name": None,
    "namespace": None,
    "label_selectors": [],
    "field_selectors": [],
    "wait": False,
    "wait_sleep": 5,
    "wait_timeout": 120,
    "condition": {"type": "Ready", "status": True},
}

FIND_ARGS_NAME_NAMESPACE = {
    "kind": "VirtualMachine",
    "api_version": "kubevirt.io/v1",
    "name": "testvm",
    "namespace": "default",
    "label_selectors": [],
    "field_selectors": [],
    "wait": False,
    "wait_sleep": 5,
    "wait_timeout": 120,
    "condition": {"type": "Ready", "status": True},
}


@pytest.mark.parametrize(
    "module_args,find_args",
    [
        ({}, FIND_ARGS_DEFAULT),
        ({"name": "testvm", "namespace": "default"}, FIND_ARGS_NAME_NAMESPACE),
    ],
)
def test_module(monkeypatch, mocker, module_args, find_args):
    monkeypatch.setattr(AnsibleModule, "exit_json", exit_json)
    monkeypatch.setattr(kubevirt_vm_info, "get_api_client", lambda _: None)

    set_module_args(module_args)

    find = mocker.patch.object(K8sService, "find")
    find.return_value = {
        "api_found": True,
        "failed": False,
        "resources": [],
    }

    with pytest.raises(AnsibleExitJson):
        kubevirt_vm_info.main()
    find.assert_called_once_with(**find_args)
