# Install gcloud
See details in the [documentation](https://cloud.google.com/sdk/docs/install#deb).

```
sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get install google-cloud-cli
```

Once this is done, initialize `gcloud`.

```
gcloud init
gcloud auth application-default login
```

You may have to set the current project.

```
gcloud config set project sha1digest
```

# Install virtual environment
First create a virtual environment with `venv` and activate it.

```
python3 -m venv venv
source venv/bin/activate
```

Then install the requirements with `pip`.

```
pip install -r requirements.txt
```

# Test the app.
Activate the virtual environment and launch the application with Python.

```
source venv/bin/activate
python main.py
```

The app is then available at [http://localhost:8080](http://localhost:8080).

# Deploy
Use `gcloud` to deploy the app (billing must be enabled).

```
gcloud app deploy --quiet
```

You can monitor the versions of the app on the
[console](https://console.cloud.google.com/appengine/versions?project=sha1digest&serviceId=default).
