class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "c8X_p5-.nSsh2X_YU8vlkYPe.pDjE7b_mX" 

    #AUTHORITY = "https://login.microsoftonline.com/organizations"  # For multi-tenant app
    AUTHORITY = "https://login.microsoftonline.com/agrossigmxde.onmicrosoft.com"#Enter_the_Tenant_Name_Here"

    # TODO: Enter your application client ID here
    CLIENT_ID = "dccda654-452f-477d-ba38-21fcfd609081"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session