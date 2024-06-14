# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat, Inc.
# Apache License 2.0 (see LICENSE or http://www.apache.org/licenses/LICENSE-2.0)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.kubevirt.core.plugins.inventory.kubevirt import (
    InventoryOptions,
)


def test_inventory_options_defaults():
    opts = InventoryOptions()
    assert opts.api_version == "kubevirt.io/v1"
    assert opts.kube_secondary_dns is False
    assert opts.use_service is True
    assert opts.create_groups is False
    assert opts.append_base_domain is False
    assert opts.host_format == "{namespace}-{name}"


def test_inventory_options_override_defaults():
    api_version = "test/v1"
    kube_secondary_dns = True
    use_service = False
    create_groups = True
    append_base_domain = True
    host_format = "{name}-testhost"

    opts = InventoryOptions(
        api_version=api_version,
        kube_secondary_dns=kube_secondary_dns,
        use_service=use_service,
        create_groups=create_groups,
        append_base_domain=append_base_domain,
        host_format=host_format,
    )
    assert opts.api_version == api_version
    assert opts.kube_secondary_dns == kube_secondary_dns
    assert opts.use_service == use_service
    assert opts.create_groups == create_groups
    assert opts.append_base_domain == append_base_domain
    assert opts.host_format == host_format
