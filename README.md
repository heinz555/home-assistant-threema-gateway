# home-assistant-threema-gateway
Home-Assistant Threema Gateway (by Chatgpt...)

I'm trying to set up a home assistant Threema gateway because I haven't found anything useful. Due to lack of knowledge, I'm trying this with the help of ChatGP.

Your help is greatly appreciated to bring this to life. It's also my first Github project.

Example Configuration in configuration.yaml

threema_gateway:
  gateway_id: "YOUR_GATEWAY_ID"
  secret: "YOUR_SECRET"
  private_key_path: "/config/threema/private_key.pem"


# Home Assistant Threema Gateway Integration

This custom integration allows you to send and receive messages using Threema Gateway (E2E encryption) in Home Assistant.

## Installation

### Using [HACS](https://hacs.xyz/)
1. Go to **HACS > Integrations**.
2. Click the three dots in the top-right corner, then select **Custom repositories**.
3. Add this repository URL: `https://github.com/your-username/home-assistant-threema-gateway` and set the category to **Integration**.
4. Search for "Threema Gateway" in HACS and install it.

### Manual Installation
1. Download this repository as a ZIP file and extract it.
2. Copy the `custom_components/threema_gateway/` folder to your Home Assistant `custom_components` directory.

## Configuration

Add the following to your `configuration.yaml` file:

```yaml
threema_gateway:
  gateway_id: "YOUR_GATEWAY_ID"
  secret: "YOUR_SECRET"
  private_key_path: "/config/threema/private_key.pem"
