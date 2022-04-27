# Auth REST API

## Root, show all available paths
request

    GET /

response

    {
        "success": true,
        "res": {
            "get_user": {
                "methods": ["GET"],
                "path": ".../user/{username}"
            },
            "modify_user": {
                "methods": ["POST", "PATCH", "DELETE"],
                "path": ".../user"
            }
        }
    }

## Authenticate user
request

    POST /auth
    {
        "email": "john.doe@example.com",
        "plaintext": "qwerty1234"
    }

response

    {
        "success": true,
        "res": {
            "uid": "ivan"
        }
    }

or

    {
        "success": false,
        "res": {
            "reason": "provided user data incomplete or incorrect"
        }
    }

## Add user account
request

    POST /user
    {
        "username": "ivan",
        "plaintext": "qwerty1234"
        "email": "john.doe@example.com",
        "roles": ["admin", "mod", "reg"]
    }

response

    {
        "success": true,
        "res": {
            "uid": "ivan",
            "hpw": "983d0b14294b49be93f637c084fd02e8"
        }
    }

or

    {
        "success": false,
        "res": {
            "reason": "user already exists"
        }
    }

## Retrieve user account information
request

    GET /user/ivan

response

    {
        "success": true,
        "res": {
            "uid": "ivan",
            "email": "john.doe@example.com",
            "roles": ["admin", "mod", "pawn"]
        }
    }

or

    {
        "success": false,
        "res": {
            "reason": "user not found"
        }
    }

## Change user account information
request

    PATCH /user
    {
        "username": "ivan",
        "roles": ["mod"]
    }

response

    {
        "success": true,
        "res": {
            "uid": "ivan"
        }
    }

or

    {
        "success": false,
        "res": {
            "reason": "user not found"
        }
    }

## Delete user account information
request

    DELETE /user
    {
        "username": "ivan"
    }

response

    {
        "success": true,
        "res": {
            "uid": "ivan"
        }
    }

or

    {
        "success": false,
        "res": {
            "reason": "user not found"
        }
    }

# TODO List

1. Block requests that don't originate inside the network.
2. Add OAuth2 support.
