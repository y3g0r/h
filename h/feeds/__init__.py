# -*- coding: utf-8 -*-

"""Code for generating feeds (e.g. Atom and RSS feeds)."""

from h.feeds.render import render_atom
from h.feeds.render import render_rss

__all__ = ("render_atom", "render_rss")
