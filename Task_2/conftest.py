import pytest
from playwright.sync_api import Page
from components import Announcement, Listings


@pytest.fixture
def announcement(page: Page):
    return Announcement(page)

@pytest.fixture
def listings(page: Page):
    return Listings(page)