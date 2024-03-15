#!/usr/bin/env python3
# Copyright 2024 Ubuntu
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following tutorial that will help you
develop a new k8s charm using the Operator Framework:

https://juju.is/docs/sdk/create-a-minimal-kubernetes-charm
"""

import logging

import ops

logger = logging.getLogger(__name__)

class FooEvent(ops.EventBase):
    pass


class FooCharm(ops.CharmBase):
    """Charm the service."""

    foo_event = ops.EventSource(FooEvent)

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.update_status, self._on_update_status)
        self.framework.observe(self.foo_event, self._on_foo)

    def _on_install(self, event: ops.InstallEvent):
        logger.warning("A")
        event.defer()
        self.foo_event.emit()
        return

    def _on_foo(self, _):
        pass

    def _on_update_status(self, event: ops.UpdateStatusEvent):
        logger.warning(f"{list(self.framework._storage.notices())=}")

if __name__ == "__main__":  # pragma: nocover
    ops.main(FooCharm)  # type: ignore
