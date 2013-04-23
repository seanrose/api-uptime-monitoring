from requests_oauthlib import OAuth2Session

box_session = OAuth2Session(
    client_id='lyk5wlgetcan0ur7x15pzg9ekvh9p02k',
    token={
        'access_token': 'access_token',
        'refresh_token': 'refresh_token'
    },
    auto_refresh_url='https://www.box.com/api/oauth2/token',
    auto_refresh_kwargs={
        'client_secret': 'client_secret'
    }
)
