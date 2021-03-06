import os
import virustotal3

API_KEY = os.environ['VT_API']
Livehunt = virustotal3.Livehunt(API_KEY)

data = {
        "data": {
        "type": "hunting_ruleset",
        "attributes": {
        "name": "foobar",
        "enabled": True,
        "limit": 100,
        "rules": "rule foobar { strings: $ = \"loops fruit loops\" condition: all of them }",
        "notification_emails": ["wcoyte@acme.com", "rrunner@acme.com"]
        }
    }
}

Livehunt.create_rulset(data)