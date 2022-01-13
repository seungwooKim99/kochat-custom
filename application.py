from flask import render_template

from kochat.app import KochatApi
from kochat.data import Dataset

from kochat.loss import CRFLoss, CosFace, CenterLoss, COCOLoss, CrossEntropyLoss
from kochat.model import intent, embed, entity
from kochat.proc import DistanceClassifier, GensimEmbedder, EntityRecognizer, SoftmaxClassifier

#from scenario import dust, weather, travel, restaurant
from scenario import edu
# 에러 나면 이걸로 실행해보세요!


# prepare dataset
dataset = Dataset(ood=False)

# 임베딩 프로세서
emb = GensimEmbedder(model=embed.FastText())

# 인텐트 분류기
clf = DistanceClassifier(
    model=intent.CNN(dataset.intent_dict),
    loss=CenterLoss(dataset.intent_dict),
)

# 엔티티 검출기
rcn = EntityRecognizer(
    model=entity.LSTM(dataset.entity_dict),
    loss=CRFLoss(dataset.entity_dict)
)

# train.py 를 실행하여 이미 모델 학습을 마쳤기 때문에 학습여부를 결정하는 두 번째 인자값을 False로 합니다.
# emb, clf, rcn의 학습된 정보들은 saved에서 저절로 불러옵니다.
kochat = KochatApi(
    dataset=dataset,
    embed_processor=(emb, False),
    intent_classifier=(clf, False),
    entity_recognizer=(rcn, False),
    scenarios=[
        edu
    ]
)

@kochat.app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    #kochat.app.template_folder = kochat.root_dir + 'templates'
    #kochat.app.static_folder = kochat.root_dir + 'static'
    kochat.app.run(port=5000, host='0.0.0.0')