# WhatsApp Cloud API Webhooks Sample Coded using Flask

These are sample clients for Facebook's [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks/) product, powered by [Flask on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).


1. [Heroku](heroku) - A sample client that receives Webhook events for WhatsApp Cloud API.

## Setup

### WhatsApp Cloud API Webhooks
1. Deploy the sample app on Heroku with this button:

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://github.com/JAXPARROW/whatsapi-flask-webhook)


1. Set up your client's [subscription] using your `https://<your-subdomain>.herokuapp.com/whatsapi` as the callback URL. It is recommended that you set a `TOKEN` and `APP_SECRET` [config var](https://devcenter.heroku.com/articles/config-vars) as part of the set up of your Heroku app to secure requests. If you choose not to set a config var, then you will need to set a verify token of 'token' when configuring the callback URL.
