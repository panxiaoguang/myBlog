import pynecone as pc

class Pagination(pc.Component):
    library = "antd"
    tag="Pagination"
    current: pc.Var[int]
    total:pc.Var[int]
    pageSize:pc.Var[int]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_change": pc.EVENT_ARG}
