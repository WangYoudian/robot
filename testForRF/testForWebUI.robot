*** Settings ***
Library           Selenium2Library

*** Test Cases ***
case01
    Open Browser    http://www.baidu.com    chrome
    Input Text    id=kw    斗罗大陆
    Click Element    id=su
    Close Browser
