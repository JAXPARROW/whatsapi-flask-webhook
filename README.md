# WhatsApp Cloud API Webhooks Sample Coded using Flask

These is the sample Webhook Flask app for WhatsApp Cloud API. You can read more from [Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/set-up-webhooks) product, powered by [Flask on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).


1. [Heroku](heroku) - A sample client that receives Webhook events for WhatsApp Cloud API.

## Setup

### WhatsApp Cloud API Webhooks
1. Deploy the sample app on Heroku with this button:

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/JAXPARROW/whatsapi-flask-webhook)


1. Set up your client's [subscription] using your `https://<your-subdomain>.herokuapp.com/whatsapi` as the callback URL. It is recommended that you set a `TOKEN` and `APP_SECRET` [config var](https://devcenter.heroku.com/articles/config-vars) as part of the set up of your Heroku app to secure requests. If you choose not to set a config var, then you will need to set a verify token of 'token' when configuring the callback URL.


## References 
1. [WhatsApp Cloud API official documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/)
2. [Heyoo WhatsApp API Python Wrapper](https://github.com/Neurotech-HQ/heyoo)


## Related WhatsApp Cloud API Wrappers
1. [Heyoo Python](https://github.com/Neurotech-HQ/heyoo)
2. [WhatsApp Cloud API PHP Wrapper ](https://github.com/pro-cms/whatsappcloud-php)
3. [Heyoo Javascript](https://github.com/JS-Hub-ZW/heyooh)


## All the credit
1. [Jaxparrow](https://github.com/JAXPARROW/)
2. [kalebu](https://github.com/Kalebu)
3. Other Contributors
