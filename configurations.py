import os


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pymssql://MUD/E1009817:@csEHPAf*@Gv3rj@PF2WGETC/SQLEXPRESS/database_name"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
