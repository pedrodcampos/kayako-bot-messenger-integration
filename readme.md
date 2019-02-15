# DialogFlow Chatbot - Kayako Messenger Integration 
## Instructions
Start by cloning this repo: 
```> git clone https://github.com/trilogy-group/kayako-messenger-bot.git```

### Dialogflow Chatbot
If you have not created your bot yet, proceed to [DialogFlow](https://dialogflow.com/) and create a new one. You can follow this [get started guide]().

### Create Google Service Account key
1. Go to Dialogflow Console, have your bot selected and click settings(gear icon) ;
2. Under _GOOGLE PROJECT_ section click **_Service Account_** link. You are going to be redirected to _Google Platform Service accounts for your project;
3. Click **_+ CREATE SERVICE ACCOUNT_** and fill in the details about the service account, then click **_CONTINUE_**;
4. Click **_Select a role_** and scroll down to DialogFlow, on the right panel select **_Dialogflow API Client_**, then click **_CONTINUE_**;
5. Under **_Create key (optional)_** click **_+ CREATE KEY_**, on the right panel select **_JSON_**, then **_CREATE_**
6. Finally, click **_DONE_**
7. Move the downloaded file to your working directory.
>**SECURITY NOTE**
> The credentials you have just downloaded give access to your bot through API. Make sure to store it securely and add it to `.gitignore` file.

### Deploy the integration service
_For this guide we use Heroku to deploy the service. Feel free to use any option of your own choice_.
1. Login to your Heroku Console or [create a new account](https://www.heroku.com/home);
2. Click **_New_**, then **_Create new app_**. Give it a name and click **_Create app_**;
3. Now click **_Settings_** and add the following _Config vars_:

    | KEY | Value Description |
    | ------ | ------ |
    |API_USER| User credentials to access the service API. e.g. `api_user` 
    |API_TOKEN|A strong password. e.g. `cBlB*rOKu27PDinzO&HT!UHi2D81iK`
    |KAYAKO_USER|A real admin user from your kayako instance. e.g. `your_name@your_domain.com`
    |KAYAKO_PASSWORD| Account passowrd
    |KAYAKO_API_ENDPOINT|Kayako API enpoint e.g `https://domian.kayako.com/api/v1`
    |GOOGLE_APPLICATION_CREDENTIALS| Account service credentials path. e.g. `./credentials.json`
4. Take note of your application  **_Domain_** under the same section. You will need it for the next step.
5. Click **_Deploy_** and follow instructions on how to push the cloned repo to heroku. Once you have pushed your project, it will be up and running. You can get more instructions [here](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app).

### Create a Kayko Integration Endpoint
1. Go to your Kayako Instance Admin Portal;
2. Click **_Endpoints_** link under _INTEGRATIONS_ category;
3. Click **_New endpoint_** button and choose option **_Webhook (HTTP request)_**
4. Give it a reasonable name (Kayako Chatbot)
5. Provide your app domain for **_Request URL_**
6. Select POST for **_Request Method_**
7. Check option **_Send authentication headers with this request_** and use the same credentials you set up previously for _Config vars_.
### Create a Kayko Trigger
1. Go to your Kayako Instance Admin Portal;
2. Click **_Triggers_** link under _AUTOMATIONS_ category;
3. Click **_New trigger_** button and give it a reasonable name (chat income messages);
5. Select **_Messenger_** for _Rule settings_;
6. Under _When these conditions are met_ select **_Conversation: Update type_**, **_equal to_**, **_Any type of update_** for each option.
7. Choose your endpoint name in the list for _Perform the following actions_.
8. Check option **_Custom (specify your own payload format)_** and copy paste the following template:
    ```json
    {"id": "{{case.id}}",
    "assignee":{ "id":"{{case.assignee.id}}", "full_name":"{{case.assignee.name}}", "email":"{{case.assignee.email}}"}, 
    "requester": {"id":"{{case.requester.id}}", "name":"{{case.requester.name}}", "email":"{{case.requester.email}}"},
    "message":"{{case.latest_public_post.contents_text}}"}
    ```
Your integration is setup. Go to Kayako Help Center and try your Chatbot.


