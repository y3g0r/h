# -*- coding: utf-8 -*-

import json

from pyramid.httpexceptions import HTTPFound
import pytest

from h.views import client
from h import __version__


@pytest.mark.usefixtures("routes", "pyramid_settings")
class TestSidebarApp:
    def test_it_includes_client_config(self, pyramid_request):
        ctx = client.sidebar_app(pyramid_request)
        expected_config = {
            "apiUrl": "http://example.com/api",
            "websocketUrl": "wss://example.com/ws",
            "release": __version__,
            "sentry": {"dsn": "test-sentry-dsn", "environment": "dev"},
            "authDomain": "example.com",
            "googleAnalytics": "UA-4567",
            "oauthClientId": "test-client-id",
            "rpcAllowedOrigins": "https://lti.hypothes.is",
        }

        actual_config = json.loads(ctx["app_config"])

        assert actual_config == expected_config

    def test_it_sets_embed_url(self, pyramid_request):
        ctx = client.sidebar_app(pyramid_request)

        assert ctx["embed_url"] == "/embed.js"

    def test_it_sets_custom_content_security_policy_header(self, pyramid_request):
        client.sidebar_app(pyramid_request)
        csp_header = pyramid_request.response.headers["Content-Security-Policy"]

        assert (
            csp_header
            == "script-src 'self' https://cdn.hypothes.is https://www.google-analytics.com; style-src https://cdn.hypothes.is 'unsafe-inline'"
        )


@pytest.mark.usefixtures("routes", "pyramid_settings")
class TestEmbedRedirect:
    def test_redirects_to_client_boot_script(self, pyramid_request):
        pyramid_request.feature.flags["embed_cachebuster"] = False

        rsp = client.embed_redirect(pyramid_request)

        assert isinstance(rsp, HTTPFound)
        assert rsp.location == "https://cdn.hypothes.is/hypothesis"

    def test_adds_cachebuster(self, pyramid_request):
        pyramid_request.feature.flags["embed_cachebuster"] = True

        rsp = client.embed_redirect(pyramid_request)

        assert isinstance(rsp, HTTPFound)
        assert "?cachebuster=" in rsp.location


@pytest.fixture
def pyramid_settings(pyramid_settings):

    pyramid_settings.update(
        {
            "ga_client_tracking_id": "UA-4567",
            "h.client_oauth_id": "test-client-id",
            "h.sentry_dsn_client": "test-sentry-dsn",
            "h.sentry_environment": "dev",
            "h.websocket_url": "wss://example.com/ws",
            "h.client_rpc_allowed_origins": "https://lti.hypothes.is",
            "authority": "example.com",
        }
    )

    return pyramid_settings


@pytest.fixture
def routes(pyramid_config):
    pyramid_config.add_route("api.index", "/api")
    pyramid_config.add_route("embed", "/embed.js")
    pyramid_config.add_route("index", "/")
    pyramid_config.add_route("sidebar_app", "/app.html")
    pyramid_config.add_route("oauth_authorize", "/oauth/authorize")
    pyramid_config.add_route("oauth_revoke", "/oauth/revoke")
