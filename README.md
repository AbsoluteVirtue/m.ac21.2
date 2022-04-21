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

## Add user account
request

    POST /user
    {
        "username": "ivan",
        "plaintext": "qwerty1234"
        "email": "john.doe@example.com",
        "roles": ["admin", "mod"]
    }

response

    {
        "success": true,
        "res": {
            "code": 0,
            "hpw": "983d0b14294b49be93f637c084fd02e8"
        }
    }

or

    {
        "success": false,
        "res": {
            "code": 1,
            "reason" "user already exists"
        }
    }

## Retrieve user account information
request

    GET /user/ivan

response

    {
        "success": true,
        "res": {
            "username": "ivan",
            "email": "john.doe@example.com",
            "roles": ["admin", "mod", "pawn"]
        }
    }

or

    {
        "success": false,
        "res": {}
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
        "res": {}
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
        "res": {}
    }

# TODO List

1. Block requests that don't originate inside the network.
2. Add OAuth2 support.
