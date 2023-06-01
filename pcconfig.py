import pynecone as pc

class MytestConfig(pc.Config):
    pass

config = MytestConfig(
    app_name="myBlog",
    db_url="sqlite:///pynecone.db",
    api_url="http://20.73.12.202:8000",
    bun_path="$HOME/.bun/bin/bun",
    frontend_packages=[
        "antd",
    ],
    #env=pc.Env.DEV,
)