DELETE FROM auth_user
WHERE id > 3

DELETE From authtoken_token
WHERE user_id > 3

DELETE FROM spotterapi_profile
WHERE id > 3