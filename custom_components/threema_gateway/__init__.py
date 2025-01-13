from homeassistant.core import HomeAssistant

DOMAIN = "threema_gateway"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Threema Gateway integration."""
    hass.data[DOMAIN] = {}

    # Register services
    async def send_message_service(call):
        """Send a Threema message."""
        from .threema_gateway import send_message

        gateway_id = call.data["gateway_id"]
        secret = call.data["secret"]
        private_key_path = call.data["private_key_path"]
        recipient_id = call.data["recipient_id"]
        message = call.data["message"]

        result = send_message(gateway_id, secret, private_key_path, recipient_id, message)
        hass.states.set(f"{DOMAIN}.last_message_status", result)

    hass.services.async_register(DOMAIN, "send_message", send_message_service)

    return True
