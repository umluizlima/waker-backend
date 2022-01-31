# wake-up-caller
A project to wake you up like in a hotel.

## Development

### Requirements
- [Python 3.10.0](https://realpython.com/intro-to-pyenv/)

### Installing
Setup Python and virtualenv
```bash
make environment
```

Install dependencies
```bash
make install
```

### Running
Get your Twilio account sid, auth token, and trial number. Then create a `.env` file at the root of this folder and fill it with Twilio's info and your verified number that will receive calls.

```bash
TWILIO_ACCOUNT_SID=L1joief...
TWILIO_AUTH_TOKEN=jo24Mfa...
TWILIO_FROM_NUMBER=+1222333444
TWILIO_TO_NUMBER=+1333444555
```

After that you should be good to go:

```bash
make run
```

Access the API docs on http://localhost:8001/docs


### Migrating
Generate migration files automatically for changes to models. Make sure all models are imported on `models/__init__.py`

```bash
make db_generate_migration description="your description"
```
