# -*- coding: utf-8 -*- #
"""Define pytest fixtures here."""


pytest_plugins = [
    "tests.fixtures.conftest.hooks",
    "tests.fixtures.conftest.transport",
    "tests.fixtures.conftest.ugc_client",
    "tests.fixtures.conftest.json",
    "tests.fixtures.conftest.files",
    "tests.fixtures.conftest.client_type",
    "tests.fixtures.conftest.take",
    "tests.fixtures.conftest.job",
    "tests.fixtures.conftest.commons",
    "tests.fixtures.conftest.webhooks",
]
