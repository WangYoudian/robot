*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
case01
    Create Session    api    http://81.68.211.21:8090
    #${data}    Post Request    http://81.68.211.21:8090/api/admin/login    {"username":"light-chaser","password":"wyd12345","authcode":null}
