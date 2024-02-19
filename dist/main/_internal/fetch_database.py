import firebase_admin
from firebase_admin import credentials, firestore, auth
import os

basedir = os.path.dirname(__file__)

class FirebaseConnector:
    def __init__(self):
        self.cred = credentials.Certificate(basedir+'/cognitive-training-6c8ff-firebase-adminsdk-hrd1k-1b51412a4f.json')

        self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()

        self.global_info = self.db.collection("global_info")
        self.basic_info = self.db.collection("user_basic_info")
        self.checkin_info = self.db.collection("user_checkin_info")
        self.game_info = self.db.collection("user_game_info")

        self.user_id = None

        self.user = None

    def get_user_by_email(self, user_id:str):
        userEmail = user_id + '@gmail.com'
        try:
            self.user = auth.get_user_by_email(userEmail)
            return self.user
        except:
            self.user = None
            return None
        
    def get_game_info(self, game_name:str):
        # if(self.user_id != user_id):
        #     self.get_user_by_email(user_id)
        if(self.user != None):
            users_ref = self.game_info.document(self.user.uid)
            docs = users_ref.collection(game_name).get()
            return docs if docs != [] else None
        return None