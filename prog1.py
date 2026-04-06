def mask_password(log):
    return log.replace("password=", "password=****")

log = "login success - username=admin password=12345"
print(mask_password(log))