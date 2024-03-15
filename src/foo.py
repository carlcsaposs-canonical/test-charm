import ops

class Foo(ops.Object):
    def __init__(self, charm):
        super().__init__(charm, key="foobar")
        self.framework.observe(charm.on.install, self._on_install)

    def _on_install(self, event: ops.InstallEvent):
        event.defer()