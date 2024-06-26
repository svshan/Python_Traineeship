from flask import Flask, jsonify, request, g
import json
from jose import jwt
from jose import ExpiredSignatureError
from jose import JWTError
from six.moves.urllib.request import urlopen
from functools import wraps
import ssl

app = Flask(__name__)

AUTH0_DOMAIN = 'dev-0f7unnw50nl6p226.eu.auth0.com'
API_IDENTIFIER = 'https://flask-api-trainin g'
ALGORITHMS = ["RS256"]


# Errors handler if authentication fails.
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# Retrieving the JWT token from the HTTP headers.
def get_token_auth_header():
    """
    Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                         "description":
                             "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must start with"
                             " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                         "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Authorization header must be"
                             " Bearer token"}, 401)

    token = parts[1]
    return token


# Token validation
def requires_auth(f):
    """
    Determines if the Access Token is valid
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        context = ssl._create_unverified_context()  # Disable SSL verification
        jsonurl = urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json", context=context)
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_IDENTIFIER,
                    issuer="https://" + AUTH0_DOMAIN + "/"
                )
            except ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                 "description": "token is expired"}, 401)
            except JWTError:
                raise AuthError({"code": "invalid_claims",
                                 "description":
                                     "incorrect claims,"
                                     "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                 "description":
                                     "Unable to parse authentication"
                                     " token."}, 401)

            g.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                         "description": "Unable to find appropriate key"}, 401)

    return decorated


def requires_scope(required_scope):
    """
    Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
        token_scopes = unverified_claims["scope"].split()
        for token_scope in token_scopes:
            if token_scope == required_scope:
                return True
    return False


@app.route("/")
def index_view():
    """
    Default endpoint, it is public and can be accessed by anyone
    """
    return jsonify(msg="Hello world!")


@app.route("/user")
@requires_auth
def user_view():
    """
    User endpoint, can only be accessed by an authorized user
    """
    return jsonify(msg="Hello user!")


@app.route("/admin")
@requires_auth
def admin_view():
    """
    Admin endpoint, can only be accessed by an admin
    """
    if requires_scope("read:admin"):
        return jsonify(msg="Hello admin!")

    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
