import pynecone as pc

class AskhalConfig(pc.Config):
    pass

config = AskhalConfig(
    app_name="askhal",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
