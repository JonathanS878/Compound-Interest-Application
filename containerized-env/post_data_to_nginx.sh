#!/bin/bash


curl -i http://localhost:80/register/ > get_session_token.txt

http_cookie=$(cat get_session_token.txt | grep -oP 'session=\K[^;]+')

echo "session: $http_cookie"


curl -i -v http://localhost:80/register/ \
-H "Cookie: $http_cookie" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=testuser&email=test@example.com&password1=123456&password2=123456"