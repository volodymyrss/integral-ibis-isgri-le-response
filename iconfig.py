from dynaconf import Dynaconf, Validator
import os

settings = Dynaconf(
    envvar_prefix="INTEGRAL",
    settings_files=[
        os.path.join(os.getenv("HOME"), '.integral-settings.toml'), 
        ],
)

settings.validators.register(
    Validator("REP_BASE_PROD", must_exist=True, eq="/isdc/arc/rev_3")
)

settings.validators.validate()