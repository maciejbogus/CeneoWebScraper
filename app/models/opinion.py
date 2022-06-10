from app.utils import get_item
from app.parameters import selectors
class Opinion:
    def __init__(self, score_, recommendation_, author_, stars_, useful_, useless_, content_, pros_, cons_, purchase_, publish_, opinion_id_):
        self.score = score_
        self.recommendation = recommendation_
        self.author = author_
        self.stars = stars_
        self.useful = useful_
        self.useless = useless_
        self.content = content_
        self.pros = pros_
        self.cons = cons_
        self.purchase = purchase_
        self.publish = publish_
        self.opinion_id = opinion_id_
        return self
    
    
    def __str__(self):
        pass
    
    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
             
        return self
        single_opinion["opinion_id"] = opinion["data-entry-id"]