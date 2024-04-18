"""pytest fixtures."""

import pytest

from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component


# This fixture enables loading custom integrations in all tests.
# Remove to enable selective use of this fixture
@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Automatically enable loading custom integrations in all tests."""
    yield


@pytest.fixture(autouse=True)
@pytest.mark.asyncio
async def auto_setup_homeassistant(hass: HomeAssistant):
    """Automatically load homeassistant component."""
    assert await async_setup_component(hass, "homeassistant", {})
    await hass.async_block_till_done()
    yield
