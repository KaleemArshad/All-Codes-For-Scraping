import json
import facebook

def facebook_scraping(token, obj):
    graph = facebook.GraphAPI(access_token=token)
    profile = graph.get_object(obj, fields='name')
    print(json.dumps(profile, indent=3))
# , location, email, link'


my_token = "EAADY0kIjdrgBAC2O133w6DO0U8pTJGPoNfC2Gfdk0pOl5C4jetTnMVUAqHGZADZBqGt1nhcsUrLhvuFQwBJ1pO5tYcuca" \
           "ZBpHPWZArk5u1n5ZAUeVEp7skguE2Bgum2cz7h6F5uiKwB33llKEWiRHeSeH8lu36CUHoYEutwZA2bAZDZD"

facebook_scraping(my_token, '425710818151147')
