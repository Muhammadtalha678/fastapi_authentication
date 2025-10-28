from sqlmodel import Session, create_engine,SQLModel
class ConnectDB:
    def __init__(self,url):
        self.url = url
        self.engine = None
    def connection(self):
        self.engine = create_engine(self.url,echo=True)
        try:
            self.engine.connect()
            print("Connection created successfully")
        except Exception as e:

            print(f"error {e}")
    def close_connection(self):
        if self.engine:
            self.engine.dispose()
            print("Connection closed successfully")

    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

    # def get_session(self):
        # return Session(self.engine)